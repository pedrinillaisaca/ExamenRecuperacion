import numpy as np
import random
import os
#Genera una matris cuadrada aleatoria y un vector 
#de una dimension determinada

from random import randrange, choice
a=[]
dimension=10
for i in range(dimension): 
    b=[]        
    for j in range(dimension):       
        b.append(random.randint(1,9))
    a.append(b)            
vec=[]
for i in range(dimension):       
        vec.append(i+1)
data =np.asarray(a,dtype=np.int)
data1 =np.asarray(vec,dtype=np.int)
os.remove("mat.txt")
os.remove("vec.txt")
np.savetxt("mat.txt",data)
np.savetxt("vec.txt",data1)