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

import getDataFromWeb
import time

class Student():
    def __init__(self, rate, hoursPerWeek, weeks):
        self.rate = rate
        self.hoursPerWeek = hoursPerWeek
        self.weeks = weeks
    
    def getData(self):
        # Get data from user input
        return getDataFromWeb.getData()
    
    def getSemesterIncome(self):
        # Semester income calculator
        x = self.rate
        y = self.hoursPerWeek
        z = self.weeks
        return (x*y)*z
    
    def getSemesterEarnings(self):
        x = self.getSemesterIncome() #gets income without cost of living or taxes taken out
        y = getDataFromWeb.getTaxPercent() #PLACEHOLDER FUNCTION. gets percent of income is taxes
        xy = x-(x*y) #calculates earnings with taxes taken out
        z = getDataFromWeb.getSemesterRent() #PLACEHOLDER FUNCTION. gets total rent for the semester
        return xy-z
    
    def getYearlyIncome(self):
        # Calculate yearly income
        return
    
    def getBudgetBreakdown(self):
        # 50/30/20 calculator
        return

#Interface with web, send data