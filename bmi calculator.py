#BMI Calculator without using control statements
#1
weight=int(input("Enter your weight\n"))
height=float(input("Enter your height\n"))
heightSquare=height*height
bmi=int(weight/heightSquare)
print("Your body mass index is: ",bmi)

#2
import math
weight=float(input("Enter your weight\n"))
height=float(input("Enter your height\n"))
heightSquare=math.pow(height,2)
bmi=int(weight/heightSquare)
print("Your body mass index is: ",bmi)


