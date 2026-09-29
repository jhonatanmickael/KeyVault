"""
@file crypto.py
@brief Motor Criptográfico do KeyVault CLI para a Cifra Afim.
@details Este módulo implementa todas as operações matemáticas da Cifra Afim em módulo 256 (ASCII estendido),
incluindo validação de chaves coprimas via Algoritmo de Euclides, cálculo de inverso modular via Algoritmo 
Extendido de Euclides, e uma interface CLI interativa em terminal com tratamento seguro de sequências de escape.

@author KeyVault Dev Team
@date 2026
"""

import ast
import os


def clear_screen() -> None:
    """
    @brief Limpa a tela do terminal de forma agnóstica ao sistema operacional.
    @details Verifica a variável os.name do ambiente Python: executa 'cls' se for Windows ('nt')
    ou 'clear' se for sistemas baseados em Unix/Linux/macOS ('posix').
    """
    os.system("cls" if os.name == "nt" else "clear")


def gcd(a: int, b: int) -> int:
    """
    @brief Calcula o Máximo Divisor Comum (MDC) entre dois inteiros.
    @details Utiliza o Algoritmo de Euclides clássico através do operador de resto mod (%).
    Usado principalmente para verificar se a chave multiplicativa 'a' e o módulo 'm' são coprimos.

    @param a Primeiro número inteiro.
    @param b Segundo número inteiro (módulo ou divisor).
    @return O Máximo Divisor Comum (MDC) entre a e b.
    """
    while b != 0:
        a, b = b, a % b
    return a


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """
    @brief Algoritmo Extendido de Euclides.
    @details Encontra os coeficientes inteiros de Bézout (x, y) que satisfazem a Identidade de Bézout:
    a*x + b*y = MDC(a, b). Essa função é essencial para computar o inverso multiplicativo modular.

    @param a Primeiro número inteiro.
    @param b Segundo número inteiro.
    @return Tupla (g, x, y) onde:
            - g: MDC(a, b)
            - x: Coeficiente associado a 'a'
            - y: Coeficiente associado a 'b'
    """
    if a == 0:
        return b, 0, 1

    g, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return g, x, y


def mod_inverse(a: int, m: int = 256) -> int:
    """
    @brief Calcula o inverso multiplicativo modular de 'a' em módulo 'm' (a^-1 mod m).
    @details Encontra um valor x tal que (a * x) ≡ 1 (mod m). Utiliza o Algoritmo Extendido
    de Euclides para derivar o resultado de forma eficiente em tempo O(log m).

    @param a A chave multiplicativa cuja inversa é buscada.
    @param m O tamanho do espaço de estados/módulo (Padrão: 256 para tabela ASCII).
    @return O menor inteiro positivo x correspondente ao inverso modular a^-1 mod m.
    @exception ValueError Disparada caso MDC(a, m) != 1 (inverso modular não existe).
    """
    g, x, _ = extended_gcd(a, m)
    if g != 1:
        raise ValueError(
            f"A chave 'a' ({a}) não tem inverso modular em mod {m}. MDC({a}, {m}) = {g} != 1."
        )
    return x % m


def validate_keys(a: int, b: int, m: int = 256) -> tuple[bool, str]:
    """
    @brief Valida as chaves criptográficas 'a' e 'b' da Cifra Afim.
    @details Garante a reversibilidade matemática da cifragem exigindo que MDC(a, m) == 1.
    Se 'a' for par em mod 256, a função de cifragem não será bijetora (causará colisões).

    @param a Chave multiplicativa.
    @param b Chave de deslocamento (aditiva).
    @param m Módulo da cifra (Padrão: 256).
    @return Tupla (status, mensagem):
            - status (bool): True se as chaves forem válidas, False caso contrário.
            - mensagem (str): Detalhes do resultado da validação.
    """
    if gcd(a, m) != 1:
        return (
            False,
            f"Chave 'a' ({a}) inválida! MDC({a}, {m}) = {gcd(a, m)}. Escolha um 'a' coprimo com {m} (ex: 1, 3, 5, 7, 9, 11, 15, etc.).",
        )
    return True, "Chaves válidas!"


def encrypt_affine(plaintext: str, a: int, b: int, m: int = 256) -> str:
    """
    @brief Cifra uma mensagem em texto claro utilizando a Cifra Afim.
    @details Para cada caractere da mensagem, obtém seu valor ordinal ASCII P = ord(char)
    e aplica a fórmula matemática: C = (a * P + b) mod m.

    @param plaintext Texto em claro/senha a ser cifrada.
    @param a Chave multiplicativa (deve ser coprima com m).
    @param b Chave de deslocamento aditivo.
    @param m Tamanho da tabela de caracteres (Padrão: 256).
    @return String contendo o texto cifrado resultante.
    @exception ValueError Se as chaves fornecidas forem matematicamente inválidas.
    """
    valid, msg = validate_keys(a, b, m)
    if not valid:
        raise ValueError(msg)

    encrypted_chars = []
    for char in plaintext:
        p = ord(char)
        c = (a * p + b) % m
        encrypted_chars.append(chr(c))

    return "".join(encrypted_chars)


def decrypt_affine(ciphertext: str, a: int, b: int, m: int = 256) -> str:
    """
    @brief Decifram uma mensagem cifrada revertendo a Cifra Afim.
    @details Calcula primeiramente o inverso modular a^-1 mod m. Em seguida, para cada caractere
    cifrado de valor C = ord(char), aplica a fórmula de reversão: P = a^-1 * (C - b) mod m.

    @param ciphertext A mensagem cifrada obtida anteriormente.
    @param a Chave multiplicativa utilizada na cifragem.
    @param b Chave de deslocamento utilizada na cifragem.
    @param m Tamanho do alfabeto/módulo (Padrão: 256).
    @return String com o texto original decifrado.
    @exception ValueError Se a chave 'a' não possuir inverso modular em mod m.
    """
    valid, msg = validate_keys(a, b, m)
    if not valid:
        raise ValueError(msg)

    a_inv = mod_inverse(a, m)
    decrypted_chars = []

    for char in ciphertext:
        c = ord(char)
        p = (a_inv * (c - b)) % m
        decrypted_chars.append(chr(p))

    return "".join(decrypted_chars)


def demonstrate_affine(text: str, a: int, b: int, m: int = 256) -> None:
    """
    @brief Exibe uma demonstração passo a passo e didática do processo da Cifra Afim.
    @details Formata uma tabela no terminal com os valores oridinários ASCII (P), a aplicação da fórmula 
    (a*P + b) mod m, o código ASCII resultante (C) e a representação imprimível usando repr() para 
    evitar quebrar a saída do terminal com caracteres não-imprimíveis.

    @param text Texto ou palavra de teste.
    @param a Chave multiplicativa.
    @param b Chave de deslocamento.
    @param m Módulo (Padrão: 256).
    """
    valid, msg = validate_keys(a, b, m)
    if not valid:
        print(f"\n[ERRO] {msg}")
        return

    a_inv = mod_inverse(a, m)

    print("\n" + "=" * 60)
    print("        DEMONSTRAÇÃO MATEMÁTICA - CIFRA AFIM")
    print("=" * 60)
    print(f"Parâmetros: a = {a}, b = {b}, m = {m}")
    print(f"Propriedade: MDC({a}, {m}) = {gcd(a, m)} (Coprimos)")
    print(
        f"Inverso Modular: a^-1 mod {m} = {a_inv} (pois {a} * {a_inv} ≡ 1 mod {m})"
    )
    print("-" * 60)

    print(
        f"{'Char':<6} | {'P (ASCII)':<10} | {'Cifra: (a*P + b) mod m':<24} | {'C (ASCII)':<10} | {'Cifr.'}"
    )
    print("-" * 60)

    cipher_chars = []
    for char in text:
        p = ord(char)
        c = (a * p + b) % m
        cipher_char = chr(c)
        cipher_chars.append(cipher_char)
        c_disp = repr(cipher_char) if c < 32 or c > 126 else cipher_char
        p_disp = repr(char) if p < 32 or p > 126 else char
        print(
            f"{p_disp:<6} | {p:<10} | ({a}*{p} + {b}) mod {m} = {c:<6} | {c:<10} | {c_disp}"
        )

    ciphertext = "".join(cipher_chars)
    print("-" * 60)
    print(f"Texto Cifrado Final: {ciphertext!r}")
    print("=" * 60 + "\n")


def main() -> None:
    """
    @brief Ponto de entrada do KeyVault CLI (Menu Interativo).
    @details Controla o loop principal de navegação do usuário, solicita entradas de teclado, 
    trata strings literais provenientes de repr() via ast.literal_eval() para suportar caracteres 
    de escape (como \\x89 ou \\n) e gerencia chamadas de limpeza de tela.
    """
    clear_screen()
    while True:
        print("==========================================")
        print("              KEYVAULT CLI                ")
        print("    Motor Criptográfico - Cifra Afim      ")
        print("==========================================")
        print("[1] Cifrar Mensagem")
        print("[2] Decifrar Mensagem")
        print("[3] Demonstração Passo a Passo (Didático)")
        print("[4] Testar Chave (MDC e Inverso Modular)")
        print("[0] Sair")
        print("==========================================")

        option = input("Escolha uma opção: ").strip()

        if option == "0":
            clear_screen()
            print("\nEncerrando o KeyVault CLI. Até logo!\n")
            break

        elif option in ("1", "2", "3"):
            clear_screen()
            raw_text = input("Digite o texto/senha: ").strip()

            text = raw_text
            if option == "2":
                try:
                    # Converte a representação literal copiada do repr() ex: '\x89' nos bytes reais
                    if (raw_text.startswith("'") and raw_text.endswith("'")) or (
                        raw_text.startswith('"') and raw_text.endswith('"')
                    ):
                        text = ast.literal_eval(raw_text)
                    else:
                        text = ast.literal_eval(f"'{raw_text}'")
                except Exception:
                    text = raw_text

            try:
                a = int(
                    input(
                        "Digite a chave 'a' (multiplicativa, coprima com 256): "
                    )
                )
                b = int(input("Digite a chave 'b' (deslocamento): "))

                clear_screen()
                if option == "1":
                    result = encrypt_affine(text, a, b)
                    print(f"\n[+] Texto Cifrado: {result!r}\n")
                elif option == "2":
                    result = decrypt_affine(text, a, b)
                    print(f"\n[+] Texto Decifrado: {result}\n")
                elif option == "3":
                    demonstrate_affine(text, a, b)

            except ValueError as e:
                clear_screen()
                print(f"\n[ERRO DE ENTRADA] {e}\n")

            input("Pressione ENTER para voltar ao menu...")
            clear_screen()

        elif option == "4":
            clear_screen()
            try:
                a = int(input("Digite a chave 'a' para testar: "))
                clear_screen()
                g = gcd(a, 256)
                print(f"-> MDC({a}, 256) = {g}")
                if g == 1:
                    inv = mod_inverse(a, 256)
                    print(
                        f"-> VÁLIDA! O inverso modular a^-1 mod 256 é: {inv}\n"
                    )
                else:
                    print(
                        f"-> INVÁLIDA! Como MDC({a}, 256) != 1, não existe inverso modular.\n"
                    )
            except ValueError as e:
                clear_screen()
                print(f"\n[ERRO DE ENTRADA] {e}\n")

            input("Pressione ENTER para voltar ao menu...")
            clear_screen()

        else:
            clear_screen()
            print("\nOpção inválida! Tente novamente.\n")


if __name__ == "__main__":
    main()