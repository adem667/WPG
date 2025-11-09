# Wolf Pass Generator v3.2

![Screenshot](https://github.com/adem667/WPG/blob/main/Screenshot_20251109_144802_com_termux_TermuxActivity_edit_44332026366719.jpg)

## Advanced Multi-Mode Password Generation Tool
Developed by Wolf Security Team

---

## Overview

Wolf Pass Generator is a Python tool that generates password lists for penetration testing, cybersecurity research, and security analysis.
It offers multiple generation algorithms including random, victim-based, hybrid, and combinator patterns and supports custom wordlists.

---

## Features

- Random password generation using multiple formats (alpha, numeric, special, etc.)
- Victim-based generation using user-defined info (name, year, keywords, etc.)
- Six algorithms: `basic`, `leet`, `advanced`, `combinator`, `massive`, `hybrid`
- Supports loading `rockyou.txt` and custom wordlists
- Custom format parsing (e.g., "word"numbspecial)
- Interactive mode and command-line mode
- Colorful terminal output and banner

---

## Installation

Requirements
Make sure you have Python 3.7+ installed:

```bash
python --version
```

Clone the repository:

```bash
git clone https://github.com/adem667/WPG.git
cd WPG
```

Run the tool:

```bash
python3 generator.py
```

---

## Linux installation (Debian/Ubuntu example)

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y git python3 python3-pip
git clone https://github.com/adem667/WPG.git
cd WPG
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
python3 generator.py
```

---

## Termux installation (Android)

```bash
pkg update && pkg upgrade -y
pkg install  python3
git clone https://github.com/adem667/WPG.git
cd WPG
pip install -r requirements.txt
python3 generator.py
```

Note: Termux uses `pkg`. If dependencies require compilation, install build tools (for example `pkg install clang make`).

---

## Usage

Command-line examples:

Random password generation:

```bash
python3 generator.py -g -f all -l 12 -c 100
```

Victim-based generation:

```bash
python3 generator.py -v -a massive,hybrid -c 50000 -n victim_list.txt
```

Load RockYou list:

```bash
python3 generator.py -r -c 100000 -n rockyou_filtered.txt
```

Use custom wordlist:

```bash
python3 generator.py -w /path/to/wordlist.txt -c 50000 -n my_passwords.txt
```

Interactive mode:

```bash
python3 generator.py
```

---

## Command-line options

- `-g`, `--generate`        Generate random password list
- `-n`, `--filename`        Output filename
- `-f`, `--format`          Password format type (bigalpha, smallalpha, alpha, numeric, special, alphanumeric, all, custom)
- `-l`, `--length`          Password length (default: 12)
- `-c`, `--count`           Number of passwords (default: 10)
- `-v`, `--victim`          Use victim information (interactive prompt)
- `-r`, `--rockyou`         Load passwords from rockyou.txt in current directory
- `-w`, `--wordlist`        Path to a custom wordlist file
- `-a`, `--algorithm`       Algorithms for victim-based generation (comma separated)
- `-h`, `--help`            Show help

---

## Format types

- `bigalpha`    Uppercase letters (A-Z)
- `smallalpha`  Lowercase letters (a-z)
- `alpha`       Upper and lower case
- `numeric`     Numbers (0-9)
- `special`     Special characters
- `alphanumeric` Letters + numbers
- `all`         All character types combined
- `custom`      User-defined patterns (see examples below)

Custom format examples:

```bash
"word"numb
bigalphasmallalphanumb
alpha"123"special
```

---

## Algorithms overview

- `basic`      Basic combinations with special characters and years
- `leet`       Leet substitutions (a->4, e->3, ...)
- `advanced`   Adds suffixes and complex combinations
- `combinator` Merge multiple victim keywords
- `massive`    Extensive variations and numeric sequences
- `hybrid`     Combination of transformations and leet

---

## Output

Save generated passwords to a file:

```bash
python3 generator.py -g -f alpha -l 10 -c 50 -n output.txt
```

Example content of `output.txt`:

```
Alpha2025!
aLph@123
ALPHA!2024
...
```

---

## Where files (.txt) are located

- If you run the script from the repository folder (`cd WPG-main`) any created files (for example `output.txt`, `wrong.txt`) will be saved in that same folder.
- If you run the script from another path, look for files in the current working directory where you ran `python3 generator.py`.
- To find `.txt` files recursively:

```bash
find . -type f -name "*.txt"
```

- On Android Termux, to access files from file manager or ZArchiver you can copy to `/sdcard`:

```bash
cp output.txt /sdcard/
```

---

## Legal disclaimer

This project is for educational and authorized security testing only. Do not use it for unauthorized attacks or illegal activities. The author is not responsible for misuse.

---

## Credits

Developer: Wolf Security Team  
Version: 3.2  
Language: Python 3

---

## License

MIT License
