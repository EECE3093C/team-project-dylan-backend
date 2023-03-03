###############################################################################
#                         EECE 3093C, Spring 2023
#                            Project Cache Cab
#                               Team Dylan
#                        University of Cincinnati
###############################################################################
#
# Description: 
#
# Main file to execute financial tool backend code

from selenium import webdriver
from webbrowser import Chrome
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
import os

Path = os.getcwd()
driver = webdriver.Chrome(Path + "/Documents/chromedriver.exe")

ct = input("\nEnter the state that you live in: ")
driver.get("https://www.experian.com/blogs/ask-experian/research/median-rental-rates-for-an-apartment-by-state/")
time.sleep(2)
x = 1
for i in range(51):
    stateFind = driver.find_element(By.XPATH, "//*[@id='postBlk']/div/div/div/div/table/tbody/tr[" + f'{x}' + "]/td[1]")
    stateName = stateFind.get_attribute('innerHTML')
    if (stateName == ct):
        findMonthlyRent = driver.find_element(By.XPATH, "//*[@id='postBlk']/div/div/div/div/table/tbody/tr[" + f'{x}' + "]/td[2]")
        monthlyRent = findMonthlyRent.get_attribute('innerHTML')
        print('The monthly rent in ' + ct + ' is ' + monthlyRent + '.')
    x = x+1
time.sleep(5)
