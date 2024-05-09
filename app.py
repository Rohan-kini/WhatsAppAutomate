import pywhatkit
import pyautogui
import time

##customizable inputs 
recipient_number = 'ENTER_PHONE_NUMBER'
message = 'ENTER_MSG'
hours='ENTER_HOUR' #in 24 hour format not need of preceeding zero 
minutes='ENTER_MINUTES' #at what minute 


pywhatkit.sendwhatmsg(recipient_number, message, hours,minutes)


time.sleep(20)


pyautogui.press('enter')
