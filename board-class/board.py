"""

chess.com-move-scraper formatted into a class
creates a chess board option

"""
import sys
import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from math import floor

class Board:

    def __init__(self):
        self.player_black_key = [[x for x in range(i, i - 8, -1)] for i in range(88, 8, -10)]
        self.comp_key = [[x for x in range(i, i + 71, 10)] for i in range(18, 10, -1)]
        self.path = 'C:/Users/12158/Documents/chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--ignore-certificate-errors')
        self.options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(executable_path=self.path)
        self.new_pos = '-600, -600'
        self.old_pos = '-600, -600'
        self.move_number = 1
        self.start_game()
        # self.home()  # Move to (-600, 600)

    def start_game(self):
        self.driver.get('https://chess.com')
        while self.set():
            print(f'move {str(self.move_number)}: {self.old_pos} ---> {self.new_pos}')
            self.move_number += 1
        self.driver.quit()
        keyboard.wait('esc')

    def set(self):
        # Gets new position of piece against computer or if self is white against real player
        lets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        nums = ['1', '2', '3', '4', '5', '6', '7', '8']
        new_note = WebDriverWait(self.driver, sys.maxsize) \
            .until(
            EC.presence_of_element_located((By.XPATH, f"//div[@data-ply=" + str(self.move_number) + "]"))).text
        if len(new_note) == 2:
            self.new_pos = str(lets.index(new_note[0]) + 1) + new_note[1]
        elif new_note == 'o-o':
            return 'King-Side-Castle'
        elif new_note == 'o-o-o':
            return 'Queen-Side-Castle'
        else:
            checker = [num in nums for num in new_note]
            index = checker.index(True)
            new_note = new_note[index - 1:index + 1]
            self.new_pos = str(lets.index(new_note[0]) + 1) + new_note[1]

        # Gets old position of piece
        test = WebDriverWait(self.driver, sys.maxsize).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body"))).get_attribute('class')
        if 'max' not in test:
            # If playing against real player
            divs = self.driver.find_elements_by_xpath(
                "/html/body/div[2]/div[2]/chess-board/div")
        else:
            # If playing against the computer
            divs = self.driver.find_elements_by_css_selector("#board-vs-personalities div")
        options = ''
        for element in divs:
            if element.get_attribute('class')[:4] == 'high':
                options = options + element.get_attribute('class') + ' '
        options = options.split()
        old_note = options[1][-2:]
        for x in range(8):
            for y in range(8):
                if str(self.comp_key[x][y]) == old_note:
                    self.old_pos = self.comp_key[x][y]
        self.old_pos = old_note

        if self.driver.find_element_by_tag_name('chess-board').get_attribute('class') == 'board flipped':
            xo = floor(int(self.old_pos) / 10) - 1
            yo = (int(self.old_pos) % 10) - 1
            xn = floor(int(self.new_pos) / 10) - 1
            yn = (int(self.new_pos) % 10) - 1

            rotated_key = self.player_black_key
            self.old_pos = str(rotated_key[xo][yo])
            self.new_pos = str(rotated_key[xn][yn])
        return True
