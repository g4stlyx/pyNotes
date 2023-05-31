# Profit and Lost Calculator by g4 :d

income = int(input("please input your income: "))
cost = int(input("please input your cost: "))

profit = 0
lost = 0

if income >= cost:
    profit = income - cost
    print("Your profit is: ",profit)
else:
    lost = cost - income
    print("Your lost is: ",lost)





















