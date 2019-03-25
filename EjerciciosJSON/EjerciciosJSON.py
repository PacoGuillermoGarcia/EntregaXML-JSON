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
def contaractores(datos):
	listatitulos=[]
	listaactores=[]
	for pelicula in datos:
		listatitulos.append(pelicula["title"])
		listaactores.append(len(pelicula["actors"]))
	return zip(listatitulos,listaactores)

#3.Buscar o filtrar información: Mostrar las películas que contengan en la sinopsis 
#dos palabras dadas.
def mostrarpeliculas(cad,cad2,datos):
	listatitulos=[]
	for pelicula in datos:
		if cad in pelicula["storyline"] and cad2 in pelicula["storyline"]:
			listatitulos.append(pelicula["title"])
	return listatitulos

#4.Buscar información relacionada: Mostrar las películas en las que ha trabajado un actor dado.
def peliculasdeactor(actor,datos):
	listatitulos=[]
	for pelicula in datos:
		if actor in pelicula["actors"]:
			listatitulos.append(pelicula["title"])
	return listatitulos
#5.Ejercicio libre: Mostrar el título y la url del póster de las tres películas 
#con una media de puntuaciones más alta y lanzadas entre dos fechas dadas.
def tituloyposter(fecha1,fecha2,datos):
	listatitulos=[]
	listaurls=[]
	listanotas=[]
	for pelicula in datos:
		if fecha1 <= pelicula["releaseDate"] and fecha2 >= pelicula["releaseDate"]:
			listanotas.append(sum(pelicula["ratings"])/len(pelicula["ratings"]))
			if sum(pelicula["ratings"])/len(pelicula["ratings"])==max(listanotas):
				listatitulos.append(pelicula["title"])
				listaurls.append(pelicula["posterurl"])
	return zip(listatitulos,listaurls)



import json
with open ("movies.json") as fichero:
	datos=json.load(fichero)
#Ejercicio1
	#for elem in tituloañoduracion(datos):
#		print("Titulo:",elem[0])
#		print("Año:",elem[1])
#		print("Duracion:",elem[2])
#		print("===================")

#Ejercicio2
	#for elem in contaractores(datos):
	#	print("La pelicula %s tiene %i actores/actrices"%(elem[0],elem[1]))
	#	print("================================================================================	")
#Ejercicio3
#	cad=input("Dime una palabras: ")
#	cad2=input("Dime otra palabra: ")
#	print("Las peliculas que tienen esas dos palabras en su sinopsis son: ")
#	for elem in mostrarpeliculas(cad,cad2,datos):
#		print(elem)
#Ejercicio4
#	actor=input("Dime un actor: ").title()
#	print("Las peliculas del actor %s son: "%actor)
#	for elem in peliculasdeactor(actor,datos):
#		print(elem)

#Ejercicio5
	fecha1=input("Dime una fecha(año-mes-dia): ")
	fecha2=input("Dime otra fecha(año-mes-dia): ")
	while fecha1 >= fecha2:
		print("La Segunda fecha debe ser mayor que la primera")
		fecha1=input("Dime una fecha(año-mes-dia): ")
		fecha2=input("Dime otra fecha(año-mes-dia): ")
	for elem in tituloyposter(fecha1,fecha2,datos):
		print("Titulo:",elem[0])
		print("Posterurl:",elem[1])
		print("======================================================")