# Math Hearts – CLI Math Quiz

> A tiny, punchy command-line math game. You get **5 hearts** to solve a randomly generated problem before you bust.

[![Python 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#license)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)
[![Made with Love](https://img.shields.io/badge/made%20with-%E2%9D%A4%EF%B8%8F-ff69b4.svg)](#)

---

## Table of Contents
- [Overview](#overview)
- [Gameplay](#gameplay)
- [Why This Exists](#why-this-exists)
- [Quick Start](#quick-start)
- [Usage](#usage)
- [Configuration](#configuration)
- [Build a Windows EXE](#build-a-windows-exe)
- [Project Structure](#project-structure)
- [Notes on Division](#notes-on-division)
- [Roadmap](#roadmap)
- [FAQ](#faq)
- [Contributing](#contributing)
- [License](#license)

---

## Overview
**Math Hearts** is a no-frills terminal game to practice quick arithmetic.  
Each round:
- Two integers in the range **1…9999**
- One operator from **`+ - * / %`**
- **5 hearts** (lives) to guess the correct answer

It keeps running round after round so you can warm up your brain before coding sessions.

---

## Gameplay
- If the operator is `/`, enter an **integer** (the program truncates decimals).
- Correct answer → round ends, your remaining hearts are shown.
- Wrong answer → lose one heart. At **0**, the correct answer is revealed and a new round begins.

**Example session**
```bash
please enter without decimals
3478 / 23: = 151
your answer is correct
you had 5 more

128 * 77: = 9850
your answer is incorrect, try again
Hearts: 4
128 * 77: = 9856
your answer is correct
you had 4 more
```

---

## Why This Exists
- Tiny footprint (single file, no deps)
- Perfect for short focus sprints or teaching kids basic ops
- Extensible: tweak number ranges, hearts, operators in a minute

---

## Quick Start
Requirements:
- **Python 3.8+**
- No external dependencies (uses the standard library `random`)

Run:
```bash
python main.py
```
Windows (double-click):
If “Open with Python” is configured, you can double-click main.py, but running in a terminal is recommended to see all messages.

## Usage
The game reads from standard input:
- Enter integers only (no commas, symbols, or decimals).
- On invalid input (e.g., letters), you’ll get a helpful retry message.

## Configuration
Edit these values directly in main.py to customize:
- hearts per round
  ```python
  hearts = 5
  ```
- number range
  ```python
  firstNumber = random.randint(1, 9999)
  secondNumber = random.randint(1, 9999)
  ```
- operations in play
  ```python
  operations = ['+', '-', '*', '/', '%']
  ```
  
~ Tip: To avoid decimals entirely for division, switch to integer division (```//```) or constrain ```secondNumber``` to divisors of ```firstNumber```.

### you can build windows exe by pyinstall, exeutable, protable
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
```

## License
This project is released under the MIT License. See LICENSE
 for details.
