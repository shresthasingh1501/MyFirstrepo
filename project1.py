'''
Major project 1. spammer.
'''
import pyautogui as pista
import time
while True:
    limit=input("enter limit:")
    message=input("enter message:")
    time.sleep(10)
    i=-1
    time.sleep(0.01)
    while i<int (limit):
        pista.typewrite(message)
        pista.press("enter")
        i=i+1
    
