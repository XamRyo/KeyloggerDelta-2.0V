<p align="center">
  <img width="500" height="500" src="https://i.ibb.co/kmwkqvg/Key-Logg-PNG.png" alt="KeyLoggPNG" border="0">
</p>

# **KeyloggerDelta v2.0** - **An Open-Source Keylogger**
A simple yet powerful Python-based keylogger with an ethical focus. Open Source - MIT License. Contributions and suggestions are always welcome! - **XamRyo**

---

## **Ethical and Open-Source**
This repository contains a simple keylogger implemented in Python for **educational purposes only**. It is designed to demonstrate how keylogging works and should be used **responsibly**. Unauthorized use of this software may violate privacy laws and is strictly prohibited.

---

## **✨ Features**

- **Captures and logs keypresses with Keyboard Event Handling:**
  - The `OnKeyboardEvent` function processes keyboard events, logs the key presses to a specified file, and provides additional information such as the window name and window handle.
  
- **Destination Folder Definition:**
  - The keylogger stores data in a user-defined destination folder, specified by the `destination_folder` variable.
  
- **Timeout Mechanism:**
  - The script waits a set time (in seconds) before sending an email. The `TimeOut` function checks whether the timeout has been reached and triggers the sending of captured data.

- **Email Notification:**
  - The `SendEmail` function reads captured data from the log file, formats it, and sends it via email using the SMTP protocol. The `createEmail` function handles email creation and transmission.

- **Hook Manager Setup:**
  - The code uses the **pyHook** library to capture keyboard events through a hook manager.

- **Main Loop:**
  - The main loop checks for timeout and sends the captured data via email. It continuously processes any waiting messages.

---

## **⚙️ Requirements**
- **Python**: Version 3.13.1 or higher
- **Required Libraries**:
  - [pyHook](https://sourceforge.net/projects/pyhook/files/pyhook/1.5.1/)
  - [auto-py-to-exe](https://pypi.org/project/auto-py-to-exe/) ([GitHub](https://github.com/brentvollebregt/auto-py-to-exe?tab=readme-ov-file))
  - [pywin32](https://pypi.org/project/pywin32/)
  - [pynput](https://pypi.org/project/pynput/)
  - [pyinstaller](https://pypi.org/project/pyinstaller/)
  - [time](https://docs.python.org/es/3.10/library/time.html)
  - [logging](https://docs.python.org/es/3.9/library/logging.html)

---

## **📥 Installation**
### 1. Clone this repository:
```bash
git clone https://github.com/XamRyo/KeyloggerDelta-2.0V
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
**Convert the script into an executable file:**
```bash
pyinstaller --clean --onefile --windowed .\KeyloggerDelta-2.0V.py
```
**With auto-py-to-exe:**
```bash
python -m auto_py_to_exe
```

## **⚠️ DISCLAIMER AND LICENCE**
This project is for ethical use only. The Dev-XamRyo are not responsible for any misuse. Ensure you have explicit permission to log keystrokes on any system where this tool is used ^-^)/

## **📜Licence**
This project is licensed under the MIT License. Feel free to ask questions, contribute, or support the repository! 👍
