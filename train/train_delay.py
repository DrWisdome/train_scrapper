from encodings import utf_8

from numpy import array, size
import train.list_trains as const
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TrainDelay(webdriver.Chrome):
    def __init__(self,teardown=False):
        self.teardown = teardown
        super().__init__()
        self.implicitly_wait(0.5)
        self.array = []
        #self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def find_train(self, train):
        train_search = self.find_element(
            By.ID, 'MainContentPlaceHolder_txtTrain'
            )
        train_search.clear()
        train_search.send_keys(const.trains[train]) #const.trains[train]
        search_btn = self.find_element(
            By.ID, 'MainContentPlaceHolder_SearchButton'
        )
        search_btn.click()    

    def find_delay_time(self):
        try:
            delay_time_element = self.find_element(
                By.XPATH, '//*[@id="MainContentPlaceHolder"]/table/tbody/tr[1]/td[2]/b/font')
            self.array.append(delay_time_element.text) 
        except:
            self.array.append('Čakam na informacie vlaku') 
        
    def print_array(self):
        print("Čas: \t", end='')
        print("Meškanie: ")
        for i in range(len(self.array)):
            print(const.times_of_trains[i]+ '\t', end='')
            print(self.array[i])