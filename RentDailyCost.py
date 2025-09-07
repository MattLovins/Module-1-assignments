#initialization

FLOAT_DAYS_IN_MONTH = 30
floatCostOfRent = 0.00
floatGroceryCost = 0.00
floatRentCost = 0.00
floatUtilitiesCost = 0.00
floatMonthlyIncome = 0.00
floatTotalCost = 0.00
floatDiscretionarySpending = 0.00
floatDailyIncome = 0.00
floatDailyCost = 0.00

#get data
floatMonthlyIncome = float(input("Please enter user's monthly income: $"))
floatCostOfRent = float(input("Please enter cost of rent/mortgage: $"))
floatGroceryCost = float(input("Please enter cost of grocerey bill: $"))
floatUtilitiesCost = float(input("Please enter cost of utilities bill: $"))


#process data
floatDailyIncome = floatMonthlyIncome / FLOAT_DAYS_IN_MONTH
floatCostOfRent = floatCostOfRent / FLOAT_DAYS_IN_MONTH
floatGroceryCost = floatGroceryCost / FLOAT_DAYS_IN_MONTH
floatUtilitiesCost = floatUtilitiesCost / FLOAT_DAYS_IN_MONTH
floatTotalCost = floatCostOfRent + floatGroceryCost + floatUtilitiesCost
floatDiscretionarySpending = floatDailyIncome - floatTotalCost

#output information
print(f"user's daily income is: ${floatDailyIncome}")
print(f"user's daily rent is: ${floatTotalCost}")
print(f"user's daily discretionary spending is: ${floatDiscretionarySpending}")