'''
Scrapes chess.com for moves in current game.
Prints moves to console as they are made.

PrinceZ27, May 15th, 2021

'''

import keyboard
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = 'chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get('https://chess.com')

moveNumber = 1

def getMove():
    moveElement = WebDriverWait(driver, sys.maxsize)\
           .until(EC.presence_of_element_located\
                  ((By.XPATH, "//div[@data-ply=" + str(moveNumber) + "]")))
    print(" move #" + str((moveNumber)) + ": " + moveElement.text)
    return moveElement.text

while(not keyboard.is_pressed('q')):
    nextMove = getMove()
    print(nextMove)
    moveNumber +=1

print('\nPress esc key to exit.')
keyboard.wait('esc')
