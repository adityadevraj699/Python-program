s=input("enter ant string")
v=0
u=0
for i in s :
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'): #to che
        v=v+1
    elif(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        v=v+1
    else :
        u=u+1
        
print("total vowel is :- ",v) 
print("total consonent :-",u)
