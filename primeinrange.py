# write a prime number in range

def prime(n):
    p=0
    for i in range(2,n):
        if (n%i==0):
            p=p+1
    if(p==0):
        print("the number is prime :-",n)
    
n=int(input("enter a term of number :-"))
for i in range(2,n):
    prime(i)
