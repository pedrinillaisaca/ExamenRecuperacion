import multiprocessing
import time
import numpy as np
mat = np.loadtxt('mat.txt',dtype=np.int)#Cargamos la Matris desde un archivo extermo
vecAux=np.loadtxt('vec.txt',dtype=np.int)#Cargamos el vectorAuxiliar desde un archivo extermo
#Variable Global donde se sumaran los vectores el resultado final de la multiplicaion matris por vector 
#se encontrara en la ultima posicion
final=np.zeros(len(vecAux)) 

def producto(vec): 
    global final
    index= np.where(vecAux==vec)#indice que hayudara a encontrar la columna correcta de la matris
    matAux=mat[:,index[0][0]]#extraccion de la columna de la matrix           
    """ """
    sum = 0  
    tam=len(mat[0])
    a = list()      
    for i in range(tam):
        sum = matAux[i]*vec #Multiplicacion de la Columna por determinada posicion del vector
        a.append(sum)

    f=final+np.array(a)#suma de vectores actual mas anterior
    final=f
    return f
           
if __name__=='__main__':   
    start_time = time.time()
    vec=np.loadtxt('vec.txt',dtype=np.int)#Cargamos el vector desde un archivo extermo    
    pool=multiprocessing.Pool(processes=4)#Establecemos los procesos  
    pool_outputs_A=pool.map(producto,vec)#Map subdivide los datos almacenados en         
    pool.close()
    pool.join()    
    end_time = time.time()
    timeFinal=end_time - start_time
    #print("Resultado: ",pool_outputs_A[-1])#Como mensione anteriormente el resultado se encuentra en la ultima posicion
    print(" Tiempo Procesos={:,.2f}".format(timeFinal))