import numpy as np
import json
#import sys
import time
start_time = time.time()
def prodmv(c, B, tam):
    a = list()
    for i in range(tam):
        sum = 0
        for j in range(tam):
            sum += B[i][j] * c[j]
        a.append(sum)
    return np.array(a)

 
mat = np.loadtxt('mat.txt',dtype=np.int)
vec=np.loadtxt('vec.txt',dtype=np.int)
final=prodmv(vec, mat, len(vec))
end_time = time.time()
timeFinal=end_time - start_time

#print('Resulado: ',final)
print("Tiempo Secuencial={:,.2f}".format(timeFinal))
