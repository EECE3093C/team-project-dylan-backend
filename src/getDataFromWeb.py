###############################################################################
#                         EECE 3093C, Spring 2023
#                            Project Cache Cab
#                               Team Dylan
#                        University of Cincinnati
###############################################################################
#
# Description: 
#
# 

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

time.sleep(5)
ct = input("\nEnter the state that you live in: ")
time.sleep(5)
driver.get("https://www.google.com")
searchbox = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")))
inputsearch = driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input").send_keys("Average Living Costs in " + ct + "\n")
time.sleep(20)