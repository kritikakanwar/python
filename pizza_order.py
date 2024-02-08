
#pizza order project

print("Thankyou for choosing Python Pizza Deliveries")
size=input("what size pizza do you want?S,M,L")
if size=='S':
    cost=15
    print("small pizza")
elif size=="M":
    cost=20
    print("Medium Pizza")
else:
    cost=25
    print("large Pizza")
if size in ("S","M","L"):
    want_pepproni=input("Do you want peperoni?Y or N")
    if want_pepproni in ("Y","y"):
        if size=='S':
            pcost=2
            print(f"you have to pay extra Rs {pcost} for pepproni topping ")
        if size in("L","M"):
            pcost=3
            print(f"you have to pay extra Rs {pcost} for pepproni topping ")
    else:
        pcost=0
            
    extra_cheeze=input("do you want extra cheese?Y or N")
    if extra_cheeze in ("Y","y"):
        c_cost=1
        print(f"your final bill is :Rs{cost+pcost+c_cost} ")

        
        
            
