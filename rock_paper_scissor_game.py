#Rock Paper scissor Game using python if else statement
#and random module
import random

rock='''

 ______
| | | |/\   
|_|_|_|\ \       
|        /
\_______/            
 \______\
'''

paper='''
           ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   
'''

scissor='''
   _       ,/'
   (_).  ,/'
   __  ::
  (__)'  `\.
            `\.
'''
game=[rock,paper,scissor]

option=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer_choose=random.randint(0,2)

if option in (0,1,2):
    if option==0:
        
        print(f"\nYou choose : {option}")
        print(game[option])
        if computer_choose==0:
            print(f"\nComputer choose: {computer_choose}")
            print(game[computer_choose])
        if computer_choose==1:
            print(f"\nComputer choose: {computer_choose}")
            print(game[computer_choose])   
        if computer_choose==2:
            print(f"\nComputer choose: {computer_choose}")
            print(game[computer_choose])
        
            
    elif option==2:
        print(f"\nYou Choose: {option} for scissors")
        print(game[option])

        if computer_choose==0:
           print(f"\nComputer choose: {computer_choose}")
           print(game[computer_choose])
        if computer_choose==1:
            print(f"\nComputer choose: {computer_choose}")
            print(game[computer_choose])
        if computer_choose==2:
            print(f"\nComputer choose: {computer_choose}")
            print(game[computer_choose])
        
    elif option==1:
        print(f"\nYou choose {option}")
        print(game[option])
        if computer_choose==0:
               print(f"\nComputer choose: {computer_choose}")
               print(game[computer_choose])
        if computer_choose==1:
            print(f"\nComputer choose: {computer_choose}")
            print(game[computer_choose])
        if computer_choose==2:
            print(f"\nComputer choose: {computer_choose}")
            print(game[computer_choose])
        
    
    if option==computer_choose:
        print("It's a tie ")
    elif option==0 and computer_choose==2:
        print("you won!Rock beats scissor")
    elif option==2 and computer_choose==1:
        print("you won! Scissors cut paper")
    elif option==1 and computer_choose==0:
        print("you won! Paper covers Rock")
    elif option==2 and computer_choose==0:
        print("you lose!Rock beats scissor")
    elif option==1 and computer_choose==2:
        print("you lose! Scissors cut paper")
    elif option==0 and computer_choose==1:
        print("you Lose! Paper covers Rock")    
else:
    print("Choose from 0 ,1 or 2 ")
        
