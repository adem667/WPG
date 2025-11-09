# ðŸº Wolf Pass Generator v3.1  
### Advanced Multi-Mode Password Generation Tool  
**Developed by Wolf Security Team**

---

## ðŸ§© Overview

**Wolf Pass Generator** is a powerful and flexible Python tool that generates password lists for penetration testing, cybersecurity research, and advanced security analysis.  
It offers multiple generation algorithms â€” including random, victim-based, hybrid, and combinator patterns â€” capable of producing up to **30 million passwords**.

---

## âš¡ Features

- ðŸ”¢ **Random password generation** using multiple formats (alpha, numeric, special, etc.)
- ðŸ‘¤ **Victim-based generation** using user-defined info (name, year, keywords, etc.)
- ðŸ’¡ **6 smart algorithms** (`basic`, `leet`, `advanced`, `combinator`, `massive`, `hybrid`)
- ðŸ’¾ **Supports loading `rockyou.txt`** for common password analysis
- ðŸ§  **Custom format parsing** (`"word"numbspecial`)
- ðŸ§® **High performance** â€” handles millions of passwords efficiently
- ðŸŒˆ **Beautiful terminal colors & banners**
- ðŸ§° **Interactive mode + Command-line mode**

---

## ðŸ› ï¸ Installation

### Requirements
Make sure you have **Python 3.7+** installed.

```bash
python --version
```

### Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Wolf-Pass-Generator.git
cd Wolf-Pass-Generator
```

### Run the Tool
```bash
python wolf_pass_generator.py
```

---

## ðŸ§  Usage

### Command-Line Examples

#### ðŸ”¹ Random Password Generation
```bash
python wolf_pass_generator.py -g -f all -l 12 -c 100
```

#### ðŸ”¹ Victim-Based Generation
```bash
python wolf_pass_generator.py -v -a massive,hybrid -c 50000 -n victim_list.txt
```

#### ðŸ”¹ Load RockYou List
```bash
python wolf_pass_generator.py -r -c 100000 -n rockyou_filtered.txt
```

#### ðŸ”¹ Interactive Mode
```bash
python wolf_pass_generator.py
```

---

## ðŸ§© Format Types

| Type | Description |
|------|--------------|
| `bigalpha` | Uppercase letters (Aâ€“Z) |
| `smallalpha` | Lowercase letters (aâ€“z) |
| `alpha` | Both upper and lower case |
| `numeric` | Numbers (0â€“9) |
| `special` | Special characters |
| `alphanumeric` | Letters + numbers |
| `all` | All character types combined |
| `custom` | User-defined patterns |

**Custom format examples:**
```bash
"word"numb
bigalphasmallalphanumb
alpha"123"special
```

---

## ðŸ§  Algorithms Overview

| Algorithm | Description |
|------------|-------------|
| `basic` | Basic combinations with special chars and years |
| `leet` | Converts letters into leet-style numbers |
| `advanced` | Adds suffixes and complex combinations |
| `combinator` | Merges multiple victim keywords |
| `massive` | Generates extensive variations |
| `hybrid` | Combines multiple transformation techniques |

---

## ðŸ’¾ Output

All generated passwords can be automatically saved to a file:
```bash
python wolf_pass_generator.py -g -f alpha -l 10 -c 50 -n output.txt
```

Example output file (`output.txt`):
```
Alpha2025!
aLph@123
ALPHA!2024
...
```

---

## âš ï¸ Legal Disclaimer

This project is created **strictly for educational and cybersecurity research purposes**.  
Do **not** use this tool for unauthorized attacks or any illegal activities.  
The author(s) are **not responsible** for any misuse or damage caused by this software.

---

## ðŸº Credits

- **Developer:** Wolf Security Team  
- **Version:** 3.1  
- **Languages:** Python 3  
- **Banner:** Custom ANSI Art  

---

## ðŸ“œ License

This project is released under the **MIT License** â€” free to modify and distribute with attribution.

---

> ðŸ§  *"Strong passwords protect weak systems. Weak passwords destroy strong systems."*  
> â€” Wolf Security Team


---

## ðŸ› ï¸ Installation

### Requirements
Make sure you have **Python 3.7+** installed.

```bash
python --version
```

### Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/Wolf-Pass-Generator.git
cd Wolf-Pass-Generator
```

### Run the Tool
```bash
python wolf_pass_generator.py
```

---

### Install on **Linux** (Debian/Ubuntu example)
```bash
# Update package lists and upgrade packages
sudo apt update && sudo apt upgrade -y

# Install git and Python 3 + pip
sudo apt install -y git python3 python3-pip

# Clone the repository and navigate into it
git clone https://github.com/YOUR_USERNAME/Wolf-Pass-Generator.git
cd Wolf-Pass-Generator

# (Optional) If your script filename is different, replace wolf_pass_generator.py below with your filename (e.g., generator.py)
# Install Python dependencies if you have a requirements.txt
if [ -f requirements.txt ]; then
    python3 -m pip install --upgrade pip
    python3 -m pip install -r requirements.txt
fi

# Run the generator (use python3 explicitly)
python3 wolf_pass_generator.py
```

### Install on **Termux** (Android)
```bash
# Update and upgrade Termux packages
pkg update && pkg upgrade -y

# Install git and python (provides Python 3)
pkg install -y git python

# Clone the repository and navigate into it
git clone https://github.com/YOUR_USERNAME/Wolf-Pass-Generator.git
cd Wolf-Pass-Generator

# Install Python dependencies (if present)
if [ -f requirements.txt ]; then
    pip install --upgrade pip
    pip install -r requirements.txt
fi

# Run the generator
# If the script name is wolf_pass_generator.py:
python wolf_pass_generator.py

# Or if you've renamed it to generator.py:
# python generator.py
```

> Note: Termux runs on Android and uses `pkg` to manage packages. Some packages or dependencies (native extensions) may require additional build tools (`clang`, `make`, etc.). If you run into missing build tools, install them via `pkg install clang make`.

---
