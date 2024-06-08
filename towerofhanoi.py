def TOH(n ,big,mid,end):
	if n>=1:
            TOH(n-1,big,end,mid)
            print(big,"to",end)
            TOH(n-1,mid,big,end)

n = int(input(print("Enter the no. of plate :-  ")))

TOH(n,'1','2','3') 




