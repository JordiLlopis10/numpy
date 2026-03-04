######################################################1

import numpy as np

#np.random.seed(42)

#arr = np.random.randint(50, size=12)

#print(arr.ndim,arr.shape,arr.size,arr.dtype,arr.itemsize,arr.nbytes)
#print(arr.nbytes == arr.size * arr.itemsize)

###Tiene un int32, creo que NumPy elige el tipo de dato más pequeño que pueda contener los datos, en este caso, el int32 es suficiente para contener los números aleatorios generados.


######################################################2
# datos = np.array([10,20,30,40,50,60,70,80,90,100])
# print(datos[-1],datos[-2])

###datos[10] 
###Da un indexError porque el índice 10 está fuera del rango del array, que tiene índices de 0 a 9.



######################################################3
#enteros = np.array([1, 2, 3, 4, 5])
#enteros[0] = 3.99
### El 3.99 se convierte en 3 porque los arrays de Numpy tiene un tipo de dato fijo y en este caso es un array de enteros
###int64 es el tipo que tienen las arrays de enteros por defecto en Numpy



######################################################4
#x = np.arange(20)
#print(x[:5])
#print(x[10:])
#print(x[5:15])
#print(x[::3])
#print(x[-4:])


######################################################5
#x = np.arange(10)
#print(x[::-1])
#print(x[8:0:-2])
#print(x[7:1:-2])
### Devolvera [5,3,1]
#print(x[5::-2])


#######################################################6
#original = np.arange(10)

#vista = original[2:7]

#vista[0] = 999
#print(original)
### Si, se a cambiado el 2 por el 99, ya que el 2 era el primer numero de la array vista, y al modificarlo, se modifica el mismo numero en la array original, ya que vista es una vista del array original, no una copia independiente.


#original2 = original.copy()
#original2[0] = 999
#print(original)

###Aqui ya no se modifica la original ya que hemos usado el copy() que crea una copia independiente del array original

#######################################################7
#a = np.array([1,2,3])
#b = np.array([4,5,6])
#c = np.array([7,8,9])
#d = np.concatenate((a,b,c))
#print(d)


#######################################################8
x = np.arange(1,13)



