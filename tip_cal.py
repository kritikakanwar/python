#tip calculator

print("Welcome to tip calculator\n")
total_bill=float(input("what was the total bill ?"))
total_persons=int(input("Split bill into how many persons ?"))
tip=int(input("what percentile of Tip persons would like to give on Total amount. 10,12 or 15"))
if tip in (10,12,15):
    print("choosen correct option")
    a=(total_bill*(tip/100))/total_persons
    print(a)
    Per_person_amount=(total_bill/total_persons)+a
else:
    print("Select Standard Tip percentage 10,12 or 15")
    
print("Each person should pay :",Per_person_amount)

print("Welcome to tip calculator\n")
total_bill=float(input("what was the total bill ?"))
total_persons=int(input("Split bill into how many persons ?"))
tip=int(input("what percentile of Tip persons would like to give on Total amount. 10,12 or 15"))
if tip in (10,12,15):
    print("choosen correct option")
    tip_calculation=total_bill*(tip/100)
    total_amt=total_bill+tip_calculation
    per_Person_Amt=total_amt/total_persons
    
else:
    print("Select Standard Tip percentage 10,12 or 15")
print("Each person should pay :",per_Person_Amt)


