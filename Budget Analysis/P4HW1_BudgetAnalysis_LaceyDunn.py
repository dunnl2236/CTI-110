
# Buget Analysis
# 11/24/2018
# CTI-110 P4HW1-Buget Analysis
# Lacey Dunn


# input the budget
usersBudget=float(input('Please enter your budget: $ '))
moreExpenses='y'

totalExpenses=0

while moreExpenses=='y':    
    userExpense=float(input('Enter next expense: $ '))
    totalExpenses+=userExpense
    moreExpenses=input('More expenses? Type y for yes, Press any key for no: ' )
overUnder=usersBudget-totalExpenses                     

if overUnder < 0:
    print('You went over budget')
elif overUnder > 0:
    print('You are under budget, Great Job!')
else:
    print('You are within budget, Great Job!')
    
