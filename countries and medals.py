import numpy as np
import matplotlib.pyplot as plt
countries=["Usa","China","Russia","Germany"]
golds=[46,26,19,17]
silvers=[34,18,18,10]
bronzes=[38,26,19,19]
ind=list(range(4))
x=zip(silvers,bronzes)
mylist=list(x)
print(mylist)
list1=[]
for item in mylist:
    list1.append(int(item[0])+int(item[1]))
plt.bar(ind,bronzes,width=0.3,color="brown")
plt.bar(ind,silvers,width=0.3,color="silver",bottom=bronzes)
plt.bar(ind,golds,width=0.3,color="gold",bottom=list1)
plt.xticks(ind,countries)
plt.legend(loc="upper right")
plt.show()