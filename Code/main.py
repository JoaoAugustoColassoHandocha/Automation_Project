'''
Automation Logic:

1 - Access the company system
2 - Log in
3 - Open the database
4 - Register the products

pip install pyautogui
pip install pandas
pip install pandas openpyxl

Link used in the project: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pandas.read_excel(sheet_name = 'Tab Name') - Select the Excel tab into which the information needs to be imported.

scroll() - Scroll down or up(Positive numbers upwards | Negative numbers downwards.).

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

# Register the products

for line in table.index:
    
    # Collecting product information
    code_table = table.loc[line, 'código']
    mark_table = table.loc[line, 'marca']
    type_table = table.loc[line, 'tipo']
    category_table = table.loc[line, 'categoria']
    price_table = table.loc[line, 'preco_unitario']
    cost_table = table.loc[line, 'custo']
    note_table = table.loc[line, 'obs']

    click(x=864, y=271)
    write(code_table) # Code
    press('tab')
    write(mark_table) # Mark
    press('tab')
    write(type_table) # Type
    press('tab')
    write(category_table) # Category
    press('tab')
    write(price_table) # Price
    press('tab')
    write('Custo') # Cost
    press('tab')
    write('Obs') # Note
    write('tab')
    press('enter')