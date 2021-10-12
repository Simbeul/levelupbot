import AppKit
import mouseinfo
import time
import platform
import random2
import pyautogui
from random import randint
from time import sleep
list = ['WAGMI', 'Lets get this Level 10 boys', 'Love this project', 'LFG!!', 'Up all night for this LVL10', 'I love this project','Great community', 'Love this chat', 'This is sick', 'Cant wait to be level 10', 'Lots of people grinfing... respect', 'were all in this together','LETS GOOO', 'This is taking a while','moon time', 'LFG Guys', 'Yoooo', 'To the mooooon', 'Bears are lit', 'We love this project', 'So many messages lol']
print('Bot launched. Click on desktop.')
time.sleep(5)
a = 1
while a == 1:
    pyautogui.typewrite(random2.choice(list))
    time.sleep(randint(31,40))
    pyautogui.press('enter')  