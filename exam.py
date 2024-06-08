import numpy as np 
import matplotlib.pyplot as plt 
a=np.array(["Meat","Banana","Avocados","Sweet Potatoes","Spinach","Watermelon","Coconut water","Beans","Legumes","Tomato"])
b=np.array([250,130,140,120,20,20,10,50,40,19])
c=np.array([40,55,20,30,40,32,10,26,25,20])
d=np.array([8,5,3,6,1,1.5,0,2,1.5,2.5])
plt.title("graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(a,b,c,d,marker="*")
plt.show()

#plt.bar(c,a)
#plt.show()
#plt.pie(b,labels=[1,2,3,4,5,6,7,8,9,10])
#plt.show()
