import numpy as np
#1
a = np.array([1, 2, 3, 4, 5])
print(a.dtype)

#2 Aqui todos pasaran a flotante, porque el 3.14 es un flotante, y el resto enteros, entonces se pasan todo a flotante
b = np.array([3.14, 4, 2, 3])
print(b.dtype)

#3
c = np.zeros(15, dtype=np.int32)
print(c.dtype)

#4
d = np.full((4,6), 7.5)
print(d)

#5
e = np.arange(0,29,2)
print(e)

#6
f = np.linspace(0,10,8)
print(f)

#7 
g = np.random.rand(10)
print("\n7",g)
print(g.mean())

#8

np.random.seed(42)
h = np.random.normal(0, 1, (5, 5))
print("\n8",h)

#9
i = np.random.randint(5, 15, (20))
print("\n9",i)

#10Crea un array desde una lista Python [1, 2, 3] y luego crea un segundo array del mismo tamaño pero con tipo float64. Compara ambos usando dtype
j = np.arange(1, 4)
k = np.array([1.0, 2.0, 3.0], dtype=np.float64)
print("\n10",j,j.dtype,k,k.dtype)