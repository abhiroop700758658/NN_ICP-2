x = int(input("Enter number of values to be converted\n"))
inches=[]
cm=[]
print("Enter inches values")
for i in range(x):
    val=float(input())
    inches.append(val)
    cm.append(val*2.54)
    
print("inches: ",inches)
print("CM: ",cm)