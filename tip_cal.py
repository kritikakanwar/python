#tip calculator
#Using f string 
#1
print("Welcome to tip calculator\n")
bill=float(input("what was the total bill ?"))
total_persons=int(input("Split bill into how many persons ?"))
tip=int(input("what percentile of Tip persons would like to give on Total amount. 10,12 or 15"))
if tip in (10,12,15):
    print("choosen correct option")
    a=(bill*(tip/100))/total_persons
    print(a)
    per_person_amount=(bill/total_persons)+a
    print(f"Each person should pay :{per_person_amount}")
else:
    print("Select Standard Tip percentage 10,12 or 15")
    


#2
print("Welcome to tip calculator\n")
bill=float(input("what was the total bill ?"))
total_persons=int(input("Split bill into how many persons ?"))
tip=int(input("what percentile of Tip persons would like to give on Total amount. 10,12 or 15"))
if tip in (10,12,15):
    print("choosen correct option")
    tip_calculation=float(bill*(tip/100))
    total_bill=bill+tip_calculation
    per_Person_Amt=total_bill/total_persons
    print(f"Each person should pay :{per_Person_Amt}")
else:
    print("Select Standard Tip percentage 10,12 or 15")




