import pywhatkit
import pyautogui
import time

# Define the recipient's phone number and message
recipient_number = '+918424849827'
message = 'All the Best !!'

# Schedule the message to be sent at 10:47
pywhatkit.sendwhatmsg(recipient_number, message, 11,1)

# Delay for a few seconds to ensure the message sending dialog appears
time.sleep(20)


pyautogui.press('enter')
