#tresure island mini game for beginners
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island\n")
print("Your Mission is to find the Treasure.\n")
direction=input("You are at cross road.Where to you want to go?TYpe 'left' or 'right': ")
path=direction.casefold()
#print(path)
if path=='left':
    wait_swim=input("\nYou come to a lake.There is an island in the middle of the lake.Type 'wait' to wait for the boat.Type 'swim to swim across.: ")
    waitSwim=wait_swim.casefold()
    if waitSwim=="wait":
        print(f"You have selected to {waitSwim}\n")
        colour=input("You arrived at the island unharmed.There is a house with 3 doors.one Red,one Yellow , one Blue.Which colour do you  want to choose? ")
        color=colour.casefold()
        if color=='blue' or color=='red':
            print("\nYou enter the room of beast.Game over")
        else:
            print("\nYou got the treasure.You Win!")
    else:
        print("Game Over")
else:
    print("\nYou were defeated by the Monster.Game Over")
