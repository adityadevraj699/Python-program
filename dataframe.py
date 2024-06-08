import pandas as pd 
a={"Roll No.":[1,2,3,4,5],"Name":["Aditya KUmar","Rishu Gupta","Iqra Mudussira","MIstu","Piku"],"Course":["CSE","CSE","AIML","B.COM","BFF"],"Marks":[99,89,90,87,92]}
b=pd.DataFrame(a)
print(b)
print(b.head(2))
print(b.tail(2))