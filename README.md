# → KeyVault CLI 

## Academic Context

* **Institution:** Federal University of Alagoas (UFAL)
* **Campus:** Arapiraca Campus (Penedo Unit)
* **Degree Program:** Bachelor’s Degree in Information Systems
* **Course:** Discrete Mathematics
* **Authors:** Jhonatan Mickael and Cauet Remigio

> ⚠️ **Project Status & Notice**
> KeyVault CLI is currently in its early active development phase (Phase 1). System architecture, features, module implementations, and mathematical demonstrations are subject to change as development progresses.

## 2. About the Project

**KeyVault CLI** is a command-line password manager and educational cryptographic engine developed as an academic project for the Discrete Mathematics course at UFAL. The main objective is to showcase the practical application of fundamental mathematical concepts within real-world software architecture.

The core system is built without relying on third-party cryptographic libraries, manually implementing the **Affine Cipher** to highlight the underlying mathematical theory.

### 2.1 Core Concepts Applied
* **Modular Arithmetic ($\pmod n$):** Mapping and transforming characters across the extended ASCII table ($m = 256$).
* **Greatest Common Divisor (GCD) & Coprime Numbers:** Key validation using the Euclidean Algorithm ($\text{GCD}(a, m) = 1$) to guarantee encryption reversibility.
* **Modular Multiplicative Inverse ($a^{-1} \pmod m$):** Decryption key calculation via the Extended Euclidean Algorithm.
* **Step-by-Step Demonstration:** Detailed terminal outputs displaying the exact mathematical transformations for each character.
* **Automated Cross-Platform Management:** Platform-agnostic shell (`.sh`) and batch (`.bat`) scripts for virtual environment (`venv`) setup across Linux, macOS, and Windows.
* **Isolated File Persistence:** Local storage management ensuring raw secrets are never written to disk in plaintext.

## Directory Structure

The repository is organized following industry standards for Python projects, keeping source code, root configurations, and environment automation scripts cleanly isolated:

```text
KeyVault/
├── .gitignore          # Specifies untracked files to ignore in Git (e.g., venv/)
├── LICENSE             # Proprietary commercial license terms
├── README.md           # Official project documentation
├── setup.sh            # Automated installer for Linux and macOS
├── setup.bat           # Automated installer for Windows
├── clean.sh            # Environment cleaner and cache purger for Linux/macOS
├── clean.bat           # Environment cleaner and cache purger for Windows
│
└── src/                # Core application source code
    ├── __init__.py     # Package initialization marker
    └── crypto.py       # Cryptographic engine (Affine Cipher, GCD & Modular Inverse)
```

## How to Install and Run

The repository features platform-agnostic automation scripts designed to detect the local environment, create isolated virtual environments (`venv`), and manage dependencies seamlessly.

### →  Linux / macOS Environment (Arch Linux, Ubuntu, Fedora, etc.)

**Prerequisites:** Python 3.11+ and `git`. On Arch Linux, verify or install using:
```bash
sudo pacman -S python git
```
#### 1. Clone the repository:

```bash
git clone 'link' # Replace with your actual repository URL
cd KeyVault
```
#### 2. Run the automated installer:

```bash
chmod +x setup.sh
./setup.sh
```
#### 3. Activate the virtual environment and execute:

```bash
source venv/bin/activate
python -m src.crypto
```
#### 4. Clean the environment (Optional):
To deactivate the virtual environment and purge temporary files and venv/:

```bash
source clean.sh
```

### → Windows Environment

**Prerequisites:** Python 3.11+ (added to PATH) and Git for Windows.

#### 1. Clone the repository:
```bash
git clone 'link' # Replace with your actual repository URL
cd KeyVault
```
#### 2. Run the automated installer:

```bash
setup.bat
```
#### 3. Activate the virtual environment and execute:

 **Command Prompt (CMD):**

```bash
venv\Scripts\activate
python -m src.crypto
```

**PowerShell:**

```bash
.\venv\Scripts\Activate.ps1
python -m src.crypto
```
#### 4. Clean the environment (Optional):
Double-click clean.bat or run in terminal:

```bash
clean.bat
```

## Security and Commercial Licensing

KeyVault CLI is protected under a proprietary commercial license:

* **Commercial Protection:** Unauthorized copying, distribution, or commercial exploitation is strictly prohibited without explicit written consent from the copyright holders.
* **Academic Evaluation:** Developed specifically for academic demonstration in the Discrete Mathematics course at Universidade Federal de Alagoas (UFAL - Penedo).
* **Disclaimer:** The software is provided "as is", without warranty of any kind. See the [`LICENSE`](./LICENSE) file for full legal terms.

## Authors & Contribution

Developed as part of the Information Systems curriculum at **Universidade Federal de Alagoas (UFAL - Unidade Penedo)**.

* **Jhonatan Mickael** — [*jhonatanmickael*](https://github.com/jhonatanmickael)
* **Cauet Remigio** — [*cauergss*](https://github.com/cauergss)

---
*KeyVault CLI — Proprietary Academic & Commercial Prototype (2026).*