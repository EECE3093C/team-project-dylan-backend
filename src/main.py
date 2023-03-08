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
    def __init__(self):
        self.job = self.Job()

    def getData(self):
        # Get data from user input
        return getDataFromWeb.getData()
    
    def getYearlyIncome(self):
        # Calculate yearly income
        return
    
    def getBudgetBreakdown(self):
        # 50/30/20 calculator
        return
    
    class Job():
        def __init__(self, numWeeks, hoursPerWeek, rate, avgRent, taxRate):
            self.numWeeks = numWeeks
            self.hoursPerWeek = hoursPerWeek
            self.rate = rate
            self.avgRent = avgRent
            self.taxRate = taxRate
        
        def getRent(self):
            self.avgRent = 0 # Placeholder, replace with function to get rent from website
            return self.avgRent
        
        def getJobIncome(self):
            # Semester income calculator
            x = self.rate
            y = self.hoursPerWeek
            z = self.numWeeks
            return (x*y)*z

n = 1 # Number of jobs input by the user for the year
user = Student(n)
print(user.jobs[0].numWeeks)

#Interface with web, send data