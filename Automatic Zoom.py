import pyautogui
import os


def min():
    pyautogui.hotkey('win','d')
    pyautogui.sleep(5)
    zoom()
    
def zoom():
    cords = pyautogui.locateOnScreen('your zoom logo')
    pyautogui.click(cords)
    pyautogui.click(cords)
    join()

def join():
    pyautogui.sleep(7)
    cords1 = pyautogui.locateOnScreen("your join logo")
    pyautogui.click(cords1)
    id()

def id():
    pyautogui.sleep(3)
    no = " your meeting id "
    pyautogui.typewrite(no)
    pyautogui.sleep(2)
    pyautogui.moveTo(550,416)
    pyautogui.click(550,416)
    pyautogui.hotkey('ctrl','a')
    pyautogui.press('delete')
    pyautogui.typewrite('your name in the meeting')
    pyautogui.sleep(2)
    
    pyautogui.press('enter')
    pyautogui.sleep(4)
    Pass = "your meeting password"
    pyautogui.typewrite(Pass)
    pyautogui.press('enter')

min()

