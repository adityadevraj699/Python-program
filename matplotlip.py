import numpy as np 
import matplotlib.pyplot as plt 
d=np.array([2,3,4,1,6,7])
b=np.array([4,2,5,1,3,4])
c=np.array([5,3,2,4,5,3])
a=np.array(["a","b","c","d","e","f"])
plt.title("graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.plot(a,b,c,d,marker="*")
plt.grid()
plt.show()
