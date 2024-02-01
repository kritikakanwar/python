#######################class and objects########################

#constructor use for memory initialization /allocate for objects
#destructor
#1) is member method of class
#2) it deletes the memory of object
#3) it can be called with object
#4)name is (doubleUnderscore)__del__ which works as garbage collector

#a program to delete referencses
# it runs automatically
#it does memory management

##class a:
##    def __init__(self):
##        print('THis is constructor method')
##    def show(self):
##        print('This is normal show method')
##    def __del__(self):
##        print('destructor method called')
##        print('object deleted')
##ob=a()
##ob.show()
##
##del ob
##ob.show()  #name 'ob' is not defined

##class student:
##    name='kritika'#static variable/class varibale/constant variable
##    address='vashi'
##    roll_no=115
##    def show():
##        pass
##a=student()
##print(a.name)#accessing kritika using object
##print(a.roll_no)
##print(a.address)
####
##print(student.name)#kritika (accesing through class name)
##print(student.address)
##print(student.roll_no)

#how to call method using object
##class student:
##    name='kritika'#static variable/class varibale/constant variable
##    address='vashi'
##    roll_no=115
##    def __init__(self):
##        print('init method called')
##    def show(self):
##        print('python developer')
##a=student()#a is object of class student
###a.show()#gives error(student.show() takes 0 positional arguments but 1 was given)
###beacuse object is passing its inbuilt argument when calling the method (show)
###if we dont specify the self paramter then this error occurs
##a.show()
##student.show('arg')#python developer
###calling the show method withthe student class with an argument because we are treating it as a
###class method

##class student:
##    name='kritika'#static variable/class varibale/constant variable
##    address='vashi'
##    roll_no=115
##    def show(self):#self is a default parameter that represent the instance of class
##        print('python developer')
##        print(self)
##        print(a)
##a=student()#a is object of class student
##a.show()#python developer
##print(a)

##class student:
##    name='kritika'#static variable/class varibale/constant variable
##    address='vashi'
##    roll_no=115
##    def show(self):#self is a default parameter that represent the instance of class
##        print('python developer')
##        print(self)#kritika
##        print(a)
##a=student()#a is object of class student
##student.show('kritika')#here we are passing explicitly an argument 'kritika'
####when calling from
####class name and the method in class having an parameter self
##a.show()#python developer
##print(a)

##class A:
##        def show(self):#self is a default parameter that represent the instance of class
##            print('hii')
##            print(self)
##a=A()#a is object of class student
##A.show('bye')#here we are passing explicitly an argument 'bye'
######when calling from
#######class name and the method in class having an parameter self
##a.show()
##print(a)#<__main__.A object at 0x104c3d890>

##hii
##bye
##hii
##<__main__.A object at 0x100fb96d0>
##<__main__.A object at 0x100fb96d0>


##class A:
##    def show(self):
##        name='kriti'
##        age=20
##        print(f'my name is {name} and my age is {age}')
##a=A()
##a.show()

##class A:
##    def show(self,name):
##        print(name)#name local varoable hai
##        name='kritika'
##        age=20
##        print(f'my name is {name} and my age is {age}')
##        print('name overwrites after assigning kritika :',name)
##a=A()
##a.show('sourav')#a ka object show ke self mai jayega and sourav name parameter mai jayega

##class A:
##    def show(self,name,age,gender):
##        print(name)#name local variable hai
##        print(age)
##        print(gender)
##        name='kritika'
##        age=22
##        print(f'my name is {name} and my age is {age}')
##        print('name overwrites after assigning kritika :',name)
##a=A()
##a.show('sourav',20,'male')#a ka object show ke self mai jayega and sourav name parameter mai jayega

##class A:
##    def getdata(s):#Both methods take a parameter s, which refers to the instance of the class
##        #(a in this case). 
##        print('python developer')
##    def demo(s):
##        print('java developer')
##        a.getdata()#pyhton developer
##a=A()
##a.getdata()
##a.demo()
##
##class A:
##    def getdata(s):
##        print('python developer')
##    def demo(s):
##        print('java developer')
##        s.getdata()#pyhton developer because s is instance of a
##a=A()
##a.getdata()
##a.demo()

##class A:
##    def getdata(s):
##        print('python developer')
##    def demo(s):
##        print('java developer')
##        k.getdata()#NameError: name 'k' is not defined
##a=A()
##a.getdata()
##a.demo()

##class A:
##    def getdata(s):
##        print('python developer')
##    def demo(k):
##        print('java developer')
##        k.getdata()#pyhton developer
##a=A()
##a.getdata()
##a.demo()

#instance variable
#an instance variable is a variable that is associated with the particular instance(object)
#each instance of  a class can have its own set of instance varaibles and these variables are defined and used within
#instance methods of the class

##class Person:
##    def __init__(self, name, age):
##        self.name = name  # Instance variable for name
##        self.age = age    # Instance variable for age
##
##    def introduce(self):
##        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating two instances with different values for instance variables
##person1 = Person("Alice", 30)
##person1 = Person("Bob", 25)#when we have twoobjects of same name the ouput will be overwritten
#the output will be displayed from last obje

##class Person:
##    def __init__(self, name, age):
##        self.name = name  # Instance variable for name
##        self.age = age    # Instance variable for age
##
##    def introduce(self):
##        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating two instances with different values for instance variables
##person1 = Person("Alice", 30)
##person2 = Person("Bob", 25)
##
# Accessing and using instance variables
##person1.introduce()  # Output: My name is Alice and I am 30 years old.
##person2.introduce()  # Output: My name is Bob and I am 25 years old.


#a variable which is present inside the method is called as local variable
#scope of local var inside the mmethod only
##class A:
##    def show(s):
##        name='kritika'
##        address='vashi'
##        print(name,address)
##    def display(s):
##        print('pyhton developer')
##        s.show()
##        print(s.name,s.address)
##a=A()
##a.show()
##a.display()

#a var which is present as an argument in function header part is called
#as local varible
##class A:
##    def show(s,age,rollno):#all these are local variable
##        name='kritika'
##        address='vashi'
##        print(name,address,age,rollno)
##    def display(s):
##        print('pyhton developer')
##        s.show()#if we dont pass additional arguments then below error arises
##        #A.show() missing 2 required positional arguments: 'age' and 'rollno'
##
##        #print(name,address,age,rollno)#gives error (NameError: name 'name' is not defined)
##a=A()
##a.show('31','115')
##a.display()

##class A:
##    def show(s,age,rollno):#all these are localvar
##        name='kritika'
##        address='vashi'
##        print(name,address,age,rollno)
##    def display(s):
##        print('pyhton developer')
##        s.show(23,112)#yahan 2 arguments required
##        #print(name,address,age,rollno)#gives error (NameError: name 'name' is not defined)
##a=A()
##a.show('31','115')
##a.display()

#instance variable example
##class A:
##   def show(s):
##        s.name='kritika'
##        s.address='vashi'
##        s.roll_no=115
##        s.contact=9876543210
##        print(s.name,s.address,s.roll_no,s.contact)
##   def display(s):
##        print(s.name,s.address,s.roll_no,s.contact)#agar var ko instance var banoge toh woh
##       #kisi or method mai bhi call ho jayega
####        #means available in iside and outside the method
##        print('pyhton developer')
##        #s.show(23,112)#yahan 2 arguments required
####        #print(name,address,age,rollno)#gives error (NameError: name 'name' is not defined)
##a=A()
##a.show()
##a.display()

##class A:
##    def show(s):
##        s.name='kritika'
##        s.address='vashi'#k.address='vashi' will give error because
##        #instance is s
##        s.roll_no=115
##        s.contact=9876543210
##        print(s.name,s.address,s.roll_no,s.contact)
##    def display(k):
##       print(k.name,a.address,k.roll_no,s.contact)#error :'s' is not defined
##       #because s is not the instance of display method
##a=A()
##a.show()
##a.display()

##class A:
##    def show(s):
##        s.name='kritika'
##        s.address='vashi'#k.address='vashi' will give error because instance is s
##        s.roll_no=115
##        s.contact=9876543210
##        print(s.name,s.address,s.roll_no,s.contact)
##    def display(k):
##        print(k.name,a.address,k.roll_no,s.contact)#error :'s' is not defined
##a=A()
##a.show()
##a.display()
##print(s.name,s.address,s.roll_no,s.contact)#error:'s' is not defined

##class A:
##    def show(s):
##        s.name='kritika'
##        s.address='vashi'#k.address='vashi' will give error because instance is s
##        s.roll_no=115
##        s.contact=9876543210
##        print(s.name,s.address,s.roll_no,s.contact)
##    def display(k):
##        print(k.name,a.address,k.roll_no,k.contact)
##a=A()
##a.show()
##a.display()
##print(a.name,a.address,a.roll_no,a.contact)#class ke bhar class ke local var ko class
#####ke object ke through call kar sakhtein hain
##print(A.name,A.address,A.roll_no,A.contact)#AttributeError: type object 'A' has no attribute 'name'
##

##class A:
##    name='kritika'
##    address='vashi'#k.address='vashi' will give error because instance is s
##    roll_no=115
##    contact=9876543210
##    print(name,address,roll_no,contact)
##    def display(k):
##        print(k.name,a.address,k.roll_no,k.contact)#error :'s' is not defined
##a=A()
##a.display()
##print(a.name,a.address,a.roll_no,a.contact)#static var and local var ko hum class ke bhar class ke objko call
###kar sakhtein hain 
##print(A.name,A.address,A.roll_no,A.contact)

###############Difference between static var and instance var################

##class A:
##    a=10
##    b=20
##    def display(s):
##        s.a=s.a+1# 11 11 11
##        #s.a inside the display() method refers to the instance variable a for each instance (x, y, and z),
##        #so it starts at 10 and increments by 1 for each instance.
##        A.b=A.b+1#21 22 23
##        print(s.a,A.b)
##x=A()
##x.display()
##y=A()
##y.display()
##z=A()
##z.display()

##class A:
##    a=10
##    b=20
##    def display(s):
##        s.a=s.a+1
##        x.b=x.b+1#
##        print(s.a,A.b)#11 20 11 20 11 20
##x=A()
##x.display()
##y=A()
##y.display()
##z=A()
##z.display()

##class A:
##    a=10
##    b=20
##    def display(s):
##        s.a=s.a+1
##        x.b=x.b+1#
##        print(s.a,x.b)#11 21 11 22 11 23
##x=A()
##x.display()
##y=A()
##y.display()
##z=A()
##z.display()


##class A:
##    a=10
##    b=20
##    def display(s):
##        s.a=s.a+1
##        x.b=x.b+1
##        print(s.a,x.b)#11 21 11 22 11 23
##        print(s)
##x=A()
##x.display()
##y=A()
##y.display()
##z=A()
##z.display()

#constructor runs automatically when object of class is created
##class A:
##    def __init__(s):#In Python, the constructor method should be
##        #named __init__ with double underscores on both sides. 
##        print('welcome to constructor')
##    def show(s,name,email,contact,address):
##        s.name=name
##        s.email=email
##        s.contact=contact
##        s.address=address
##    def display(s):
##        print(s.name,s.email,s.contact,s.address)
##a=A()
##a.show('kritika','kk@gmil.com','9876543210','vashi')
##a.display()        

#__init__ runs automatically when object of class is created
##class A:
##    def __init__(s,name,email,contact,address):
##        s.name=name
##        s.email=email
##        s.contact=contact
##        s.address=address
##    def display(s):
##        print(s.name,s.email,s.contact,s.address)
##a=A('kritika','kk@gmil.com','9876543210','vashi')#initi ke liye yahan arguments pass
#####karne hoge because object create hote hi init apne aap call ho jata hai
##a.display()  

##class A:
##
##    def __init__(self):
##        print('pyhton developer')
##    def __str__(self):
##       return 'java developer'
##a=A()
##print(a)#str function tab call hoga jab object print hoga

##class A:
##
##    def __init__(self,name,age,address):
##        print('pyhton developer')
##        self.name=name
##        self.age=age
##        self.address=address
##    def __str__(self):#str function 
##        return self.name +' '+ str(self.age)+' '+ self.address
##a=A('kritika',30,'vashi')
##print(a)#str function tab call hoga jab object print hoga
##

#inheritance/virasat
#one class can inherit the properties and methods of another class


##class father:
##    name='ravi'
##    age=55
##    college='jmit'
##    def show(s):
##        print('method of father class')
##class child():#parenthesis mai parent class ka name dal do
##    #usse parent class inherit ho jayegi
##    name='kriti'
##    age=27
##    college='kuk'
##    def display(s):
##        print('method of child class')
##a=child()
##print(a.name)#kriti
##a.display()#method of child class
##a.show()##AttributeError: 'child' object has no attribute 'show' because we dont
#inherits the father class in child class and show is the father class method

##
##class father:
##    name='ravi'
##    age=55
##    college='jmit'
##    def show(s):
##        print('method of father class')
##class child(father):#parenthesis mai parent class ka name dal do
##    #usse parent class inherit ho jayegi
##    name='kriti'
##    age=27
##    college='kuk'
##    def display(s):
##        print('method of child class')
##a=child()
##print(a.name)#kriti
##a.display()#method of child class
##a.show()#method of father class


##class A:
##    a=50
##    def get(s):
##        return 50+30
##    
##class b(A):
##    b=60
##    def display(s):
##        print(s.a+s.b)#b ke instance s se call hua 110(50+60)
##        print(s.get()) #80 because return statement hai ilsiye hum print use kar rahe hain
##        print(s.get()+40) #120
##a=b()
##a.display()
##a.get()

##class A:
##    a=50
##    def get(s):
##        return 50+30
##class B(A):
##    b=60
##    def display(s):
##        print(B.a+B.b)#class name se static var/class var call hoga 110
##        print(s.get())#80 #parent class ke method ko child class mai call kiya
##        print(s.get()+40)#120
##a=B()
##a.display()
##a.get()
##print(B.b)#60

#types of inheritance

# single level inheritance
#multilevel
#hierarchical
#multiple
#hybrid

#multilevel inheritance   A==>B(A)==>C(B)
#That means the derived/subclass class inherits the features of the base class/parent class,
#and the new derived class inherits the features of the derived class.

##class A:
##    a=30
##    def show(s):
##        print('grandparent method')
##class B(A):
##    b=40
##    def display(s):
##        print('parent method')
##class C(B):
##    c=50
##    def data(s):
##        print('child method')
##a=C()
##a.data()
##a.display()
##a.show()

##class A:
##    a=30
##    def show(s):
##        print('grandparent method')
##class B(A):
##    b=40
##    def display(s):
##        print('parent method')
##        print(s.a+s.b)#70
##        #print(s.show())
##class C(B):
##    c=50
##    def data(s):
##        print('child method')
##        print('addition',s.c+s.b+s.a)#120
##c=C()#child class ka object 
##c.data()
##c.display()
##c.show()
##b=B()# parent class ka object
##b.display()
##b.show()
###b.data()#AttributeError: 'B' object has no attribute 'data'

##class A:
##    a=30
##    def show(s):
##       print('grandparent method')
##class B(A):
##    b=40
##    def display(s):
##        print('parent method')
##        print(s.a+s.c)#80
##        
##class C(B):
##    c=50
##    def data(s):
##        print('child method')
##        print('addition',s.c+s.b+s.a)#120
##c=C()
##c.data()
##c.display()
##c.show()

##class A:
##    a=20
##    def show(s):
##        print(s.a,s.c)#20 40 here we are trying to acess the static var
##        #of child class in to the parent class
##class B(A):
##    c=40
##    def dis(s):
##        print('hii')
##
##x=B()
##x.dis()
##x.show()


##c=40
##class A:
##    a=20
##    def show(s):
##        print(s.a,s.c)#AttributeError: 'B' object has no attribute 'c'
##class B(A):
##    #c=40
##    def dis(s):
##        print('hii')
##x=B()
##x.dis()
##x.show()

##class A:
##    a=20
##    def show(s):
##        print(s.a,s.c)#20 40 yahan c child class ka static var hai jo instance s
##        #ke through access ho rha hai
##class B(A):
##    c=40
##    def dis(k):
##        print('hii')
##x=B()
##x.dis()
##x.show()

#hierarchical inheritance 
#one parent have more than one child

##class A:
##    a=30
##    def show(s):
##        print(s.c)#40
##        print('grandparent method')
##class B(A):
##    b=40
##    def display(s):
##        print('parent method')
##        print(s.a)#30
##        
##class C(A):
##    c=50
##    def data(s):
##        print('child method')
##        print('addition',s.c+s.a)#80
##b=B()
##b.display()
###b.data() ko call nhi kar sakhte
##b.show()
##c=C()
##c.data()
####c.display() ko call nhi kar sakhtein hain
##c.show()

#multiple inheritance
##class A:
##    a=10
##    def show(s):
##        print('first parent called')
##        print(s.a+s.b)#30
##        print(s.b)#20 because b parent hai c ka isliye call ho rha hai
##class B:
##    b=20
##    def display(k):
##        print('second parent called')
##        print(k.b+k.c)#50
##        print(k.c)#30 child ke static var ko parent mai call kar sakhtein
##        #hain using parent instance k 
##        print(k.a)#10
##class C(A,B):
##    c=30
##    def demo(s):
##        print('child method called')
##c=C()
##c.demo()
##print(c.a)#10
##c.show()#first parent called
##print(c.b)#20
##c.display()#second parent called
##


##class eng:
##    def study(s):
##        print('engineer study method')
##    def show(s):
##        print('pyhton devloper')
##
##class Doc():
##    def study(s):
##        print('doc study method')
##    def display(s):
##        print('java develpoer')
##class son(eng,Doc):
##    def demo(s):
##        print('son method called')
##s=son()
##s.demo()
##s.show()
##s.display()
##s.study()#engineer study method
###aayega because isne first parent ko select karega        

##class eng:
##    def study(s):
##        print('engineer study method')
##    def show(s):
##        print('pyhton devloper')
##
##class Doc():
##    def study(s):
##        print('doc study method')
##    def display(s):
##        print('java develpoer')
##class son(Doc,eng):#isme first parent ka output aayega
##    def demo(s):
##        print('son method called')
##s=son()
##s.demo()
##s.show()
##s.display()
##s.study()#doc study method
###aayega because isne first parent ko select karega        

#constructor use for memory initialization /allocate for objects
#destructor
#1) is member method of class
#2) it deletes the memory of object
#3) it can be called with object
#4)name is (doubleUnderscore)__del__ which works as garbage collector

#a program to delete referencses
# it runs automatically
#it does memory management

##class a:
##    def __init__(self):
##        print('THis is constructor method')
##    def show(self):
##        print('This is normal show method')
##    def __del__(self):
##        print('destructor method called')
##        print('object deleted')
##ob=a()
##ob.show()
##
##del ob
##ob.show()  #name 'ob' is not defined

##try:
##    a=int(input('enter first no'))
##    b=int(input('enter second no'))
##    print(a/b)
##except:
##    print('exception occured')#fun+f4 for undo
##else:
##    print('when exception not occured')
##    
##try:
##    a=int(input('enter first no'))
##    b=int(input('enter second no'))
##    print(a/b)
##except:
##    print('exception occured')#fun+f4 for undo
##else:
##    print('when exception not occured')
##finally:
##    print('it is always exceuted')

##try:
##
##    print(2/0)#division by zero
##    #print(a/b)
##    #print(abc)
##    #print(int('demo'))
##    
##except ZeroDivisionError as e :
##    print(e)
##except NameError as e :
##    print(e)
##except ValueError as e :
##    print(e)


##try:
##
##    #print(2/0)#division by zero
##    #print(a/b)#name 'a' is not defined
##    #print(abc)#name 'abc' is not defined
##    print(int('demo'))#invalid literal for int() with base 10: 'demo'
##
##except(ZeroDivisionError,NameError,ValueError) as e:
##    print(e)
    
#Raise keyword
#python raise keyword is used to raise exception or errors
#the raise keyword raise an error and stop the control flow of the program

##print('pyhton developer')
##try:
##    raise NameError
##except:
##    print('exception handled')
##print('java developer')
##    

##print('pyhton developer')
###try:
##raise InvalidError #NameError: name 'InvalidError' is not defined
###except:
## #   print('exception handled')
##print('java developer')
    
##print('pyhton developer')
##try:
##    raise InvalidError 
##except:
##    print('exception handled')
##print('java developer')
    
##class InvalidError():
##    pass
##print('pyhton developer')
###try:
##raise InvalidError #TypeError: exceptions must derive from BaseException
###except:
## #   print('exception handled')
##print('java developer')

#a=InvalidError()

##class InvalidError(Exception):
##    pass
##print('pyhton developer')
##try:
##    raise InvalidError 
##except InvalidError as e:
##    print(e)
##print('java developer')

##class InvalidError(Exception):
##    def __str__(self):
##        return 'InvalidError' #this will print our own created error messages
##print('pyhton developer')
##try:
##    raise InvalidError 
##except InvalidError as e:
##    print(e)
##print('java developer')

