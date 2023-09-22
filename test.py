import pyautogui
import time

print(pyautogui.size())
print(pyautogui.position())

pyautogui.moveTo(100, 200)
pyautogui.click()

time.sleep(1)
pyautogui.write('hello world!')
pyautogui.write('hello world!', interval=0.1)

time.sleep(1)
pyautogui.press('enter')

for x in ['machine1', 'machine2', 'machine3']:
    if x == 'machine1':
        pyautogui.write('command1', interval=0.1)
    elif x == 'machine2':
        pyautogui.write('command2', interval=0.1)
    elif x == 'machine3':
        pyautogui.write('command3', interval=0.1)
    time.sleep(1)
    pyautogui.press('enter')
