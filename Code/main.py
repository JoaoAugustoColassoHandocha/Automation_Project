'''
Automation Logic:

1 - Access the company system
2 - Log in
3 - Open the database
4 - Register a product
5 - Repeat step 4 until the product list is finished

'''

import pyautogui

pyautogui.PAUSE = 1

pyautogui.press('win')
pyautogui.write('edge')
pyautogui.press('enter')
pyautogui.write('https://dlp.hashtagtreinamentos.com/python/intensivao/login')
pyautogui.press('enter')