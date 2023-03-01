# Header
import getDataFromWeb
import time

class Student():
    def __init__(self, rate, weeks):
        self.rate = rate
        self.weeks = weeks
    
    def getData(self):
        # Get data from user input
        return getDataFromWeb.getData()
    
    def getSemesterIncome(self):
        # Semester income calculator
        return
    
    def getYearlyIncome(self):
        # Calculate yearly income
        return
    
    def getBudgetBreakdown(self):
        # 50/30/20 calculator
        return

s = Student(20, 15)

print(s.getSemesterIncome())

#Interface with web, send data