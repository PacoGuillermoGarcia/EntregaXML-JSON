#1.Listar información: Listar el título, año y duración de todas las películas.
def tituloañoduracion(datos):
	listatitulos=[]
	listaaños=[]
	listaduraciones=[]
	for pelicula in datos:
		listatitulos.append(pelicula["title"])
		listaaños.append(pelicula["year"])
		listaduraciones.append(pelicula["duration"])
	return zip(listatitulos,listaaños,listaduraciones)
#2.Contar información: Mostrar los títulos de las películas y el número de actores/actrices 
#que tiene cada una.
#3.Buscar o filtrar información: Mostrar las películas que contengan en la sinopsis 
#dos palabras dadas.
#4.Buscar información relacionada: Mostrar las películas en las que ha trabajado un actor dado.
#5.Ejercicio libre: Mostrar el título y la url del póster de las tres películas 
#con una media de puntuaciones más alta y lanzadas entre dos fechas dadas.

import json
with open ("movies.json") as fichero:
	datos=json.load(fichero)
	for elem in tituloañoduracion(datos):
		print("Titulo:",elem[0])
		print("Año:",elem[1])
		print("Duracion:",elem[2])
		print("===================")
