# This file will be the main file for all our Python code. 


# get user input
value = float(input("Please enter your total amount of income: "))

# calculate percentages
fifty_percent = value * 0.5
thirty_percent = value * 0.3
twenty_percent = value * 0.2

# print results with labels
print("Total Income:", value)
print("It is reccommended to only spend this amount on needs:", fifty_percent)
print("It is reccommended to only spend this amount on wants:", thirty_percent)
print("It is reccommended that you save atleast this much money:", twenty_percent)
