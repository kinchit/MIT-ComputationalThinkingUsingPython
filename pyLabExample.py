import matplotlib.pylab as plt
#import pyplot as plt

listx=[]
listy=[]
for i in range (30):
    listx.append(i)
    listy.append(i*3)

plt.figure("x-y graph")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.title("Graph")
plt.plot(listx, listy)
#plt.clf()  #Clear Frame
#plt.show()
print(listx)