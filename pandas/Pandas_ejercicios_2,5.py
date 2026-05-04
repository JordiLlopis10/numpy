import numpy as np
import pandas as pd
#Parte 1: Series
#1.Crea un objeto Series de Pandas llamado presupuesto que contenga el presupuesto de producción (en millones de dólares) de las siguientes películas: Titanic (200), Avatar (237), Avengers: Endgame (356), El Señor de los Anillos: Las Dos Torres (94) e Interstellar (165). Usa un diccionario como fuente de datos.
presupuesto = pd.Series({'Titanic': 200, 'Avatar': 237, 'Avengers: Endgame': 356, 'El Señor de los Anillos: Las Dos Torres': 94, 'Interstellar': 165})

#2
recaudacion = pd.Series({'Titanic': 2187, 'Avatar': 2788, 'Avengers: Endgame': 2798, 'El Señor de los Anillos: Las Dos Torres': 926, 'Interstellar': 677})

beneficio = recaudacion - presupuesto

#3
puntuacion = pd.Series({'Titanic': 7.9, 'Avatar': 7.8, 'Avengers: Endgame': 8.4, 'El Señor de los Anillos: Las Dos Torres': 8.8, 'Interstellar': 8.7})

#print(puntuacion.sort_values(ascending=False))
#puntuacion.rename({'Avatar': 'Avatar (2009)'}, inplace=True)
#print(puntuacion)

#Parte 2: DataFrame

peliculas = pd.DataFrame({'presupuesto': presupuesto, 'recaudacion': recaudacion, 'puntuacion': puntuacion})

peliculas["beneficio"] = beneficio
peliculas["es_taquillera"] = beneficio >= 1000
peliculas["es_top"] = puntuacion > 7

registros = [
{'nombre': 'Leonardo DiCaprio', 'peliculas': 35, 'oscar': True},
{'nombre': 'Cate Blanchett', 'peliculas': 52, 'oscar': True},
{'nombre': 'Tom Hanks', 'peliculas': 60}, # sin oscar
{'nombre': 'Natalie Portman', 'peliculas': 47, 'oscar': True},
]
actores = pd.DataFrame(registros)


print(actores,peliculas)
print(peliculas["puntuacion"])
print(peliculas["presupuesto"],peliculas["recaudacion"])
print(peliculas["beneficio"]>500)
print(peliculas.loc["Avatar", "presupuesto"])

#Crea un DataFrame de 4 filas y 3 columnas a partir de un array NumPy de números aleatorios enteros entre 1 y 10 (simularán puntuaciones de críticos). Asigna como nombres de columna 'Critico1', 'Critico2' y 'Critico3', y como índice los títulos de cuatro películas. Por último, usa .describe() para obtener el resumen estadístico y calcula la puntuación media de cada película añadiendo una columna media

np.random.seed(0)
puntuaciones = np.random.randint(1, 11, size=(4, 3))
peliculas_criticos = pd.DataFrame(puntuaciones, columns=['Critico1', 'Critico2', 'Critico3'], index=['Pelicula A', 'Pelicula B', 'Pelicula C', 'Pelicula D'])
print(peliculas_criticos.describe())
peliculas_criticos['Media'] = peliculas_criticos.mean(axis=1)
print(peliculas_criticos)