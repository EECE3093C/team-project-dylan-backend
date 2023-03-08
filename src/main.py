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
    
    def getYearlyIncome(self):
        # Calculate yearly income
        return
    
    def getBudgetBreakdown(self):
        # 50/30/20 calculator
        return

s = Student(20, 15)

print(s.getSemesterIncome())

#Interface with web, send data