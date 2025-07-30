# Kvanta
# code from kvanta camp 2025 in summer

The project and exsesize is in this presentation:
[click here](https://docs.google.com/presentation/d/1y2nVD5pIWoul3HU0f28udZoJGliT0383ZjXMg_Hnc-I/edit?slide=id.g362ff9ae707_1_23#slide=id.g362ff9ae707_1_23)

This is my version of code.

**If you not work with `python` look here**
- [Do you have python and pip?](#start)
- [🐧 Linux](#-linux-and--ubuntu)
- [💻 Ubuntu](#-linux-and--ubuntu)
- [🪟 Windows](#-windows-python)
- [🍎 Macos](#-macos-python)


To start the "Tetris game" look down:
Chose Os and where you gone run game:
- [🐧 Linux](#-linux)
    - [🐟 fish shell](#-fish-shell)
    - [🐚 bash shell](#-bash-shell)
- [💻 Ubuntu](#-ubuntu)
    - [🐟 fish-shell](#-fish-shell)
    - [🐚 bash shell](#-bash-shell)
- [🪟 Windows](#-windows)
    - [Cmd](#cmd)
    - [PowerShell](#powershell)
- [🍎 Macos](#-macos)
    - [🐟 fish-shell](#-fish-shell)
    - [🐚 bash shell](#-bash-shell)

## 🐧 Linux, 💻 Ubuntu, 🍎 macOS

1. Press 
    - 🐧 Linux and 💻 Ubuntu
        - <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>T</kbd>
    - 🍎 macOS
        - <kbd>Cmd</kbd> + <kbd>Space</kbd> → wright `Terminal` → <kbd>Enter</kbd>


### 🐟 Fish shell
2. Clone the repository:
    ```bash
    git clone https://github.com/N1k78/Kvanta.git
    ```
3. go to the folder Kvanta:
    ```bash
    cd Kvanta
    ```
4. Create a virtual environment:
    ```bash
    python3 -m venv .Kvanta
    ```
5. Activate environment:
    ```bash
    source .Kvanta/bin/activate.fish
    ```
6. Install packages:
    ```bash
    pip3 install -r requirements.txt
    ```
7. Enter the Tetris directory:
    ```bash
    cd Tetris
    ```
8. Run the game:
    ```bash
    python3 paint.py
    ```

[Go to the start](#kvanta)

### 🐚 Bash shell

2. Clone the repository:
    ```bash
    git clone https://github.com/N1k78/Kvanta.git
    ```
3. Go to the Kvanta folder:
    ```bash
    cd Kvanta
    ```
4. Create a virtual environment:
    ```bash
    python3 -m venv .Kvanta
    ```
5. Activate environment:
    ```bash
    source .Kvanta/bin/activate
    ```
6. Install packages:
    ```bash
    pip3 install -r requirements.txt
    ```
7. Enter the Tetris directory:
    ```bash
    cd Tetris
    ```
8. Run the game:
    ```bash
    python3 paint.py
    ```

[Go to the start](#kvanta)

## 🪟 Windows

1. Open Command Prompt (CMD) or PowerShell

### Cmd
2. Clone the repository:
    ```cmd
    git clone https://github.com/N1k78/Kvanta.git
    ```
3. Go to the Kvanta folder:
    ```cmd
    cd Kvanta
    ```
4. Create a virtual environment:
    ```cmd
    python -m venv .Kvanta
    ```
5. Activate environment:
    ```cmd
    .Kvanta\Scripts\activate.bat
    ```
6. Install packages:
    ```cmd
    pip install -r requirements.txt
    ```
7. Enter the Tetris directory:
    ```cmd
    cd Tetris
    ```
8. Run the game:
    ```cmd
    python paint.py
    ```

[Go to the start](#kvanta)

### Powershell

2. Clone the repository:
    ```powershell
    git clone https://github.com/N1k78/Kvanta.git
    ```
3. Go to the Kvanta folder:
    ```powershell
    cd Kvanta
    ```
4. Create a virtual environment:
    ```powershell
    python -m venv .Kvanta
    ```
5. Activate environment:
    ```powershell
    .\.Kvanta\Scripts\Activate.ps1
    ```
6. Install packages:
    ```powershell
    pip install -r requirements.txt
    ```
7. Enter the Tetris directory:
    ```powershell
    cd Tetris
    ```
8. Run the game:
    ```powershell
    python paint.py
    ```

[Go to the start](#kvanta)



## ***`python`* installation**
### start

at first you have to:
- [ ] python version
```bash
python --version
```

- [ ] pip3 version
```bash
pip3 --version
```

- [ ] pip version
```bash
pip --version
```

If you dont have pip or python look down

### python instaletion:
### 🐧 Linux and 💻 Ubuntu
- ```bash
sudo apt update
```
- ```bash
sudo apt install python3 python3-pip -y
