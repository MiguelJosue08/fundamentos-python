
import random
import matplotlib.pyplot as plt
print(random.randrange(10,100,2))

lista=[1,2,3,4,5,6,7,8,9,10]
print ('Lisya Original ' ,lista )
random.shuffle(lista)
print (lista)

campana=[random.gauss(1,0.5) for i in range(1000)]
plt.hist(campana,bins=14)
plt.show()