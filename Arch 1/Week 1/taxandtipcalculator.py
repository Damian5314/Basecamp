cost=float(input("Cost of the meal: "))

tip= cost*0.15
tax= cost*0.21

total= tip+tax+cost

print("Tax:", format(tax, '.3f'), ", Tip:", format(tip, '.3f'), ", Total:", format(total, '.3f'))