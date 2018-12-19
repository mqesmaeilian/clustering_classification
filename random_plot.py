import random as r
import matplotlib as mpl
lst = []
z = 0
x = int(input("Please insert how many number do you want to generate?"))
for i in range(0, x):
    y = r.random()
    z += 1
    data = [z,y]
    lst.append(data)

X = [lst[:,0]]
Y = [lst[:,1]]
print(X)
print(Y)


