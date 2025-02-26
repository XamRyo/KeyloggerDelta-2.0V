<p align="center">
<img width="500" height="500" src="https://i.ibb.co/kmwkqvg/Key-Logg-PNG.png" alt="KeyLoggPNG" border="0">
</p>

# KeyloggerDelta-2.0V
This is KeyloggerDelta-2.0V. By Python Code with proper comments and an ethical focus. Open Source - MIT License - Contributions and Ask are welcome to improve its functionality or add new features. (^^) / ♡ -XamRyo-

# Ethical and Open-Source:
This repository contains a simple keylogger implemented in Python for **educational purposes** only. It is intended to demonstrate how keylogging works and should be used responsibly. Unauthorized use of this software may violate privacy laws and is strictly prohibited.

## Features
- Captures and logs keypresses with Keyboard Event Handling:
  - The OnKeyboardEvent function handles keyboard events, logs the key presses to the specified file, and       prints additional information such as the window name and window handle..
- Destination Folder Definition
  - The code defines a destination folder where the keylogger data will be stored. This is specified by the     destination_folder variable.
- Timeout Mechanism.
  - The code sets a wait time in seconds (seconds_wait) before sending the email. It calculates the timeout     based on the current time and the wait time.
  - The TimeOut function checks if the timeout has been reached.
- Email Notification:
  - The SendEmail function reads the captured keylogger data from the specified file, formats it, and sends     it via email...
  - The createEmail function creates and sends an email using the SMTP protocol. 
- Hook Manager Setup:
  - The code sets up a hook manager to capture keyboard events using pyHook.
- Main Loop:
  - The main loop continuously checks for the timeout and sends an email if the timeout has been reached.       It also processes any waiting messages.

## Requirements
- Python 3.13.1 or any V.py>
- Libraries:
  - [pyHook](https://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/)
  - [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) [GitHub](https://github.com/brentvollebregt/auto-py-to-exe?tab=readme-ov-file)
  - [pywin32](https://pypi.org/project/pywin32/)
  - [pynput](https://pypi.org/project/pynput/)
  - [pyinstaller](https://pypi.org/project/pyinstaller/)
  - [time](https://docs.python.org/es/3.10/library/time.html)
  - [logging](https://docs.python.org/es/3.9/library/logging.html)

## Installation
1. Clone this repository:
    ```bash
    git clone XamRyo/KeyloggerDelta-2.0V
    cd KeyloggerDelta-2.0V
    ```
<p align="center">
<img src="https://i.ibb.co/vvxmqHV5/Py-Code-snippet.png" alt="Py-Code-snippet" border="0">
</p>

2. Install the required Python packages:
    ```bash
    python -m pip install –upgrade pip.
    pip install pyHook
    pip install auto-py-to-exe 
    pip install pywin32
    pip install pynput
    pip install pyinstaller (optional)
    pip install time (general library)
    pip install logging
    ```

3. Run the script:
    ```bash
    cd python KeyloggerDelta-2.0V.py
    ```

## Create Executable
#Convert the script into an executable file:
```bash
pyinstaller --clean --onefile --windowed .\KeyloggerDelta-2.0V.py
```
#With auto-py-to-exe:
```bash
python -m auto_py_to_exe
```

## DISCLAIMER AND LICENCE
This project is for ethical use only. The Dev-XamRyo are not responsible for any misuse. Ensure you have explicit permission to log keystrokes on any system where this tool is used ^-^

## Licence
This project is licensed under the MIT License. Ask and support repository :)
