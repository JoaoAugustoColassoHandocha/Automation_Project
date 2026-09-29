'''
Automation Logic:

1 - Access the company system
2 - Log in
3 - Open the database
4 - Register the product
5 - Repeat step 4 until the product list is finished

pip install pyautogui
pip install pandas
pip install pandas openpyxl

Link used in the project: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pandas.read_excel(sheet_name = 'Tab Name') - Select the Excel tab into which the information needs to be imported.

'''

import pyautogui, os, time, pandas

# Pause time between each execution
pyautogui.PAUSE = 1

# Executions
press = pyautogui.press
write = pyautogui.write
click = pyautogui.click
sleep = time.sleep

# Open the database
table = pandas.read_csv('Code\\produtos.csv')

# Browser request and link
os.system('cls' if os.name == 'nt' else 'clear')
browser = input('\nNavegador: ')
os.system('cls' if os.name == 'nt' else 'clear')
link = input('\nLink: ')
os.system('cls' if os.name == 'nt' else 'clear')

# Access the company system
press('win')
write(browser)
press('enter')
write(link)
press('enter')
sleep(5)

# Log in
click(x=717, y=371)
write('pythonimpressinador@gmail.com') # Login
press('tab')
write('teste') # Password
press('tab')
press('enter')
sleep(5)

# Register the product
click(x=864, y=271)
press('tab')