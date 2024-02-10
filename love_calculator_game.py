
#love calculator-without using  

name1=input("What is your name?")
name2=input("What is their name?")
fullname=(name1+name2).casefold()
print(fullname)
str1="true"
str2='love'
if 't'or 'r' or'u' or'e'  in fullname:
    t=fullname.count('t')
    r=fullname.count('r')
    u=fullname.count('u')
    e=fullname.count('e')
    true=t+r+u+e
    #print(true)
if 'l'or 'o' or'v' or'e'  in fullname:
    l=fullname.count('l')
    o=fullname.count('o')
    v=fullname.count('v')
    e=fullname.count('e')
    love=l+o+v+e
    
   # print(love)
loveScore=str(true)+str(love)
#print(loveScore)


if int(loveScore)>40 and int(loveScore)<50:
    print(f"Your Score is {loveScore}, you are alright together")
elif int(loveScore)<10 or int(loveScore)>90:
    print(f"Your Score is {loveScore}, you go together like coke and mentos.")
else:
    print(f"Your Score is {loveScore}.")



