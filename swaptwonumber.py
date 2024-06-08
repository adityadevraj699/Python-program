#swap two number without third variable

a=int(input("enter a first number :-"))
b=int(input("enter a second number :-"))
print("Number before swaping :-")
print( "a = ",a,"b = ",b)
a=a+b 
b=a-b 
a=a-b 
print("Number after swaping :-")
print("a = ",a,"b = ",b)