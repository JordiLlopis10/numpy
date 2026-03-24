import numpy as np
import timeit
#Ejercicio 1 Comparacion de rendimiento 

# arr = np.random.random(500_000)
# t1 = timeit.timeit(lambda: sum(arr), number=10)
# t2 = timeit.timeit(lambda: np.sum(arr), number=10)

# print("sum() tarda:", t1)
# print("np.sum() tarda:", t2)

#Ejercicio 2 Minimo, máximo y suma con método

notas = np.array([6.5, 8.0, 4.3, 9.1, 7.7, 5.5,10.0, 3.2])
# print("Nota minima:", np.min(notas))
# print("Nota maxima:", np.max(notas))
# print("Suma de notas:", np.sum(notas))

#Ejercicio 3 usando el array del ejercicio 2
print("Nota media:",np.mean(notas))
print("Desviacion estandar poblacional:",np.std(notas))
print("Nota mediana:",np.median(notas))