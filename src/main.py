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
    def __init__(self, numJobs):
        self.numJobs = numJobs

        self.jobs = []
        for i in range(self.numJobs):
            self.jobs.append(self.Job())

    def getData(self):
        # Get data from user input
        return getDataFromWeb.getData()
    
    def getYearlyIncome(self):
        # Calculate yearly income
        sum = 0
        for i in range(self.numJobs):
            sum += self.jobs[i].getJobIncome()
        return sum
    
    def getBudgetBreakdown(self):
        # 50/30/20 calculator
        return
    
    class Job():
        def __init__(self):
            # From User
            self.numWeeks = 3
            self.hoursPerWeek = 10
            self.rate = 20
            self.state = "Ohio"

            # From web scraper
            self.avgRent = 0
            self.taxRate = 0
            
            # Get values for data
            self.getUserInput()
            self.webScraper(self.rate, self.numWeeks, self.hoursPerWeek, self.state)
        
        # Not sure if this is the way to do it with web interface. Is data passed per-job or all at once?
        def getUserInput(self):
            numWkFromWeb = 15
            self.numWeeks = numWkFromWeb
            return


        # Parameters are data from user (web interface)
        def webScraper(self, rate, weeks, hrPerWk, state):
            # Run selenium, pass parameters

            # rent = getDataFromWeb.getRent(state)

            stateTax = 0.1
            self.taxRate = stateTax

            return
        
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
print(user.getYearlyIncome())

# Interface with web, send data