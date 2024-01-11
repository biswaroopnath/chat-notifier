from selenium import webdriver
from selenium.webdriver.common.by import By
from win10toast import ToastNotifier
# import pygame
import time
import re
import os
import sys
MAX=150


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
# def send_notification(message):
#     print("Queue : " + message)
#     pygame.mixer.init()
#     pygame.mixer.music.load(resource_path("click-button.mp3"))  # Replace 'chime.wav' with the path to your audio file
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(2)
# def send_notification2(message):
#     print("Queue : " + message)
#     pygame.mixer.init()
#     pygame.mixer.music.load(resource_path("cat.mp3"))  # Replace 'chime.wav' with the path to your audio file
#     pygame.mixer.music.play()
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(1)

def send_notification(message):
    toaster = ToastNotifier()
    toaster.show_toast("Queue Status Update", message, duration=10,icon_path=resource_path('spicy_icon.ico'))



pattern = r'\d+'

print("...........................WELCOME TO SPICYCHAT BOT NOTIFIER[dev:@reafall].......................................")
bot_link=input("PRESS 0 for DEFAULT or else CUSTOM link .... : ")
if bot_link=='0':
    bot_link = "https://spicychat.ai/chat/d89788ca-c851-4f0c-af36-ae0985f28363"

else:
    bot_link = input("Enter spicychat-bot link : ")

driver = webdriver.Chrome()
driver.get(bot_link)

time.sleep(10)
i = MAX
element_xpath = "(//*[contains(text(),'position')])[2]"

try:
    element = driver.find_element(By.XPATH, element_xpath)
except:
    print("Element not found")
    send_notification("Ready")

text_content = element.text
matches = re.findall(pattern, text_content)
out =int(matches[0])
send_notification(str(out))

while(True):
    time.sleep(i)
    try:
        element = driver.find_element(By.XPATH, element_xpath)
    except :
        print("Element not found")
        send_notification("Ready")
        break


    text_content = element.text
    matches = re.findall(pattern, text_content)
    out =int(matches[0])

    if out<500:
        i=60
        send_notification(str(out))

    elif out<1000:
        i=120
        send_notification(str(out))
    else:
        # send_notification(str(out))
        continue


while(True):
    time.sleep(5000)




# driver.quit()
