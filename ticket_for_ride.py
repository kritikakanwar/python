#Ticket for Ride

height=int(input("Enter your Height\n"))
if height>=120:
    print("You can ride")
    age=int(input("Enter your age:\n"))
    if age>18:
        if age>45 and age <=55:
            money=0
            print("You ticket is free ")
        else:
            money=12
            print(f"Adult Ticket price is Rs {money}")
    elif age>12 and age<=18:
        money=7
        print(f"Youth Ticket price is Rs {money}")
    else:
        money=5
        print(f"Child Ticket PRice is Rs {money}")
    photo=input("Do you want photo ? Yes or No")
    if photo in ('yes',"YES","Yes"):
        photo_Price=3
        print(f"You have to pay extra Rs {photo_Price} for the photo")
        print(f"Total Ticket Price to pay is : Rs {photo_Price+money} ")
    else:
        print(f"You have to pay Rs {money} ")
else:
    print("Sorry! you have to be alleast 120cm in height to take the ride")
