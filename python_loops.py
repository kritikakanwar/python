##for i in range(5):
##    print(i)
##    if(i==3):
##        continue
##        print('hello')
##else:
##    print('loop is complete')
##print()
##print('second for loop ')
##for i in range(5):
##    if i==3:
##        continue
##        print(i)  
##        print('hello')
##    else:
##        print('loop is complete')
        
for outer in range(1,6):
    for inner in range(1,6):
        print('*',end=' ')
    print()#this print is of outer for loop
print()#for space after next code
##* * * * * 
##* * * * * 
##* * * * * 
##* * * * * 
##* * * * * 

for outer in range(1,6):
    for inner in range(1,6):
        print('+',end=' ')
    print()#this print is of outer for loop
print()
##+ + + + + 
##+ + + + + 
##+ + + + + 
##+ + + + + 
##+ + + + + 
for outer in range(1,6):
    for inner in range(1,outer+1):
        print('*',end=' ')
    print()#this print is of outer for loop
print()#for space after next code
##* 
##* * 
##* * * 
##* * * * 
##* * * * * 

for outer in range(1,6):
    for inner in range(1,outer+1):
        print('A',end=' ')
    print()#this print is of outer for loop
print()
##A 
##A A 
##A A A 
##A A A A 
##A A A A A 

for outer in range(1,6):
    for inner in range(0,outer):
        print(inner,end=' ')
    print()
print() 
##0 
##0 1 
##0 1 2 
##0 1 2 3 
##0 1 2 3 4 
for outer in range(1,6):
    for inner in range(1,outer+1):
        print(inner,end=' ')
    print()
print() 
##1 
##1 2 
##1 2 3 
##1 2 3 4 
##1 2 3 4 5     
for outer in range(1,6):
    for inner in range(1,6):
        print(outer,end=' ')
    print()
print() 
##1 1 1 1 1 
##2 2 2 2 2 
##3 3 3 3 3 
##4 4 4 4 4 
##5 5 5 5 5 
   
for outer in range(1,6):
    for inner in range(1,outer+1):
        print(outer,end=' ')
    print()
print() 
##1 
##2 2 
##3 3 3 
##4 4 4 4 
##5 5 5 5 5 
char =65
for outer in range(1,6):
    for inner in range(1,outer+1):
        print(char,end=' ')
        char=char+1
    print()
print() #for space after next code
##65 
##66 67 
##68 69 70 
##71 72 73 74 
##75 76 77 78 79 

char=65
for outer in range(1,6):
    for inner in range(1,outer+1):
        print(chr(char),end=' ')
        char=char+1
    print()
print()
##A 
##B C 
##D E F 
##G H I J 
##K L M N O 
char=97
for outer in range(1,6):
    for inner in range(1,outer+1):
        print(chr(char),end=' ')
        char=char+1
    print()
print()
##a 
##b c 
##d e f 
##g h i j 
##k l m n o 
for outer in range(1,6):
    char=65
    for inner in range(1,outer+1):
        print(chr(char),end=' ')
        char=char+1
    print()
print()
##A 
##A B 
##A B C 
##A B C D 
##A B C D E 
for outer in range(1,6):
    char=97
    for inner in range(1,outer+1):
        print(chr(char),end=' ')
        char=char+1
    print()
print()
##a 
##a b 
##a b c 
##a b c d 
##a b c d e 
for outer in range(6,1,-1):
    for inner in range(outer-1):
        print('*',end=' ')
    print()
print()
##* * * * * 
##* * * * 
##* * * 
##* * 
##* 
char=97
for outer in range(6,1,-1):
    
    for inner in range(outer-1):
        print(chr(char),end=' ')
        
    print()
print()
##a a a a a 
##a a a a 
##a a a 
##a a 
##a 

for outer in range(6,1,-1):
    for inner in range(outer-1):
        print('a',end=' ')
    print()
print()
##a a a a a 
##a a a a 
##a a a 
##a a 
##a 
for outer in range(6,0,-1):
    
    for inner in range(outer-1,-1,-1):
        print(outer,end=' ')
        
    print()
print()
##6 6 6 6 6 6 
##5 5 5 5 5 
##4 4 4 4 
##3 3 3 
##2 2 
##1 
for outer in range(1,6):
    
    for inner in range(1,outer+1):
        print('*',end=' ')
        
    print()
print()
##* 
##* * 
##* * * 
##* * * * 
##* * * * * 
for outer in range(1,6):
    num=1
    for inner in range(1,6):
        print(num,end=' ')
        num=num+1
    print()
print()
##1 2 3 4 5 
##1 2 3 4 5 
##1 2 3 4 5 
##1 2 3 4 5 
##1 2 3 4 5 
num=1
for outer in range(1,6):
    
    for inner in range(1,6):
        print(num,end=' ')
        num=num+1
    print()
print()
##1 2 3 4 5 
##6 7 8 9 10 
##11 12 13 14 15 
##16 17 18 19 20 
##21 22 23 24 25 
for outer in range(1,6):
    num=1
    for inner in range(1,6):
        print(num,end=' ')
    print()    
print()
##1 1 1 1 1 
##1 1 1 1 1 
##1 1 1 1 1 
##1 1 1 1 1 
##1 1 1 1 1 

for outer in range(1,6):
    num=1
    for inner in range(1,outer+1):
        print(num,end=' ')
    print()    
print()
##1 
##1 1 
##1 1 1 
##1 1 1 1 
##1 1 1 1 1 
for outer in range(6,0,-1):
    
    for inner in range(1,6):
        print(outer,end=' ')
    print()    
print()
##6 6 6 6 6 
##5 5 5 5 5 
##4 4 4 4 4 
##3 3 3 3 3 
##2 2 2 2 2 
##1 1 1 1 1 
for outer in range(6,0,-1):
    n=5
    for inner in range(1,6):
        print(n,end=' ')
        n=n-1
    print()    
print()

##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1 

for outer in range(1,6):
    for inner in range(1,outer):
        print(inner,end=' ')
    print()    
print()

##1 
##1 2 
##1 2 3 
##1 2 3 4 

for outer in range(1,6):
    for inner in range(1,outer+1):
        print(outer,end=' ')
    print()    
print()

##1 
##2 2 
##3 3 3 
##4 4 4 4 
##5 5 5 5 5 

#to check whether a char entered by a user is vowel or consonant
char=input('enter any alphabet :')
str='aeiouAEIOU'
if char not in str:
    print(f"{char} is a consonant")
else:
    print(f"{char} is a vowel")
print()
##enter any alphabet :r
##r is a consonant

n=1
for outer in range(1,6):
    for inner in range(1,outer+1):
        print(n,end=' ')
        n=n+1
    print()
print()
##1 
##2 3 
##4 5 6 
##7 8 9 10 
##11 12 13 14 15 

