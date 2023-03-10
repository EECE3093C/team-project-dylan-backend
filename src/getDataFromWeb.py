###############################################################################
#                         EECE 3093C, Spring 2023
#                            Project Cache Cab
#                               Team Dylan
#                        University of Cincinnati
###############################################################################
#
# Description: Selenium class to find data points required for calculations
# Income tax rates per state, Monthly Rent
# 

import os
import time
from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class WebScraper():

    # Temporary until webpage dropdowns are complete
    ct = input("\nEnter the state that you live in: ")
    def medianRentFinder(ct):

        Path = os.getcwd()
        driver = webdriver.Chrome(Path + "/Documents/chromedriver.exe")

        # Load median rental rates website
        driver.get("https://www.experian.com/blogs/ask-experian/research/median-rental-rates-for-an-apartment-by-state/")
        webload = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located)

        x = 1
        for i in range(51):
            
            # Search for the state we are looking for
            stateFind = driver.find_element(By.XPATH, "//*[@id='postBlk']/div/div/div/div/table/tbody/tr[" + f'{x}' + "]/td[1]")
            stateName = stateFind.get_attribute('innerHTML')

            if (stateName == ct):

                # Find monthly rent for selected state
                findMonthlyRent = driver.find_element(By.XPATH, "//*[@id='postBlk']/div/div/div/div/table/tbody/tr[" + f'{x}' + "]/td[2]")
                monthlyRent = findMonthlyRent.get_attribute('innerHTML')
                monthlyRentString = f'{monthlyRent}'.replace(',', '').replace('$', '')

                # Use monthlyRentString for floating value
                driver.quit()
                return float(monthlyRentString)

            x = x+1

    def incomeTaxFinder(ct):

        Path = os.getcwd()
        driver = webdriver.Chrome(Path + "/Documents/chromedriver.exe")

        # Load state income tax site
        driver.get("https://www.thebalancemoney.com/state-income-tax-rates-3193320")
        webload = WebDriverWait(driver, 10).until(EC.visibility_of_any_elements_located)

        x = 1
        for i in range(51):

            # Search for state we are looking for
            stateFind = driver.find_element(By.XPATH, "//*[@id='mntl-sc-block_1-0-31']/div/table/tbody/tr[" + f'{x}' + "]/td[1]")
            stateName = stateFind.get_attribute('innerHTML')
            stateNameStrip = stateName.split("&")

            if (stateNameStrip[0] == ct):

                # Find income tax for state
                findIncomeTax = driver.find_element(By.XPATH, "//*[@id='mntl-sc-block_1-0-31']/div/table/tbody/tr[" + f'{x}' + "]/td[2]")
                incomeTax = findIncomeTax.get_attribute('innerHTML')
                incomeTaxString = f'{incomeTax}'.split('%')

                # Use incomeTaxString for percentage income tax for lowest quartile as float
                driver.quit()
                return float(incomeTaxString[0])

            x = x+1





