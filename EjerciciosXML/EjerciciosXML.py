#1.Listar información: Mostrar el nombre de las provincias de las que tenemos información sobre radares.
def ListarProvincias(doc):
	lista=doc.xpath('//PROVINCIA/NOMBRE/text()')
	return lista
#2.Contar información: Mostrar la cantidad de radares de los que tenemos información.
def ContarRadares(doc):
	Numeroradares=doc.xpath('count(//PROVINCIA/CARRETERA/RADAR)')
	return int(Numeroradares)

#3.Buscar o filtrar información: Pedir por teclado una provincia y mostrar el nombre 
#de las carreteras que tiene y la cantidad de radares.
def CarreterasyRadares(cad,doc):
	lista=doc.xpath('//PROVINCIA[NOMBRE="%s"]/CARRETERA/DENOMINACION/text()'%cad)
	Numeroradares=doc.xpath('count(//PROVINCIA[NOMBRE="%s"]/CARRETERA/RADAR)'%cad)
	return lista,int(Numeroradares)
#4.Buscar información relacionada: Pedir por teclado una carretera, muestra las provincias 
#por la que pasa y sus respectivos radares.
def provinciasyradares(cad,doc):
	listaprovincias=doc.xpath('//PROVINCIA[CARRETERA/DENOMINACION="%s"]/NOMBRE/text()'%cad)
	cantidadradares=doc.xpath('count(//CARRETERA[DENOMINACION="%s"]/RADAR)'%cad)
	return listaprovincias,int(cantidadradares)

#5.Ejercicio libre: Pedir por teclado una carretera, cuenta los radares que tiene 
#y muestra las coordenadas de los radares.(Se puede obtener la URL de OpenStraeetMap 
#para ver donde está el radar).
def Coordenadas(cad,doc):
	cantidadradares=doc.xpath('count(//CARRETERA[DENOMINACION="%s"]/RADAR)'%cad)
	listalatitud=doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LATITUD/text()'%cad)
	listalongitud=doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_INICIAL/LONGITUD/text()'%cad)
	listalatitud2=doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_FINAL/LATITUD/text()'%cad)
	listalongitud2=doc.xpath('//CARRETERA[DENOMINACION="%s"]/RADAR/PUNTO_FINAL/LONGITUD/text()'%cad)
	return int(cantidadradares),zip(listalatitud,listalongitud),zip(listalatitud2,listalongitud2)



from lxml import etree
doc=etree.parse("Radares.xml")
while True:
	print('''
		1.-Listar nombre de las provincias
		2.-Cantidad total de radares
		3.-Introducir una provincia y obtener el nombre de sus carreteras y la cantidad de radares
		4.-Introducir una carretera y obtener las provincias por las que pasa y los radares que tiene
		5.-Introducir una carretera y obtener la cantidad de radares que tiene, las coordenadas de los radares y su URL en OpenStreetMap
		0.-Salir''')
	opcion=input("Opcion: ")
	if opcion=="1":
		for elem in ListarProvincias(doc):
			print(elem)
	elif opcion=="2":
		print("Numero total de radares:",ContarRadares(doc))
	elif opcion=="3":
		Nombre=input("Dime el Nombre de una provincia: ")
		Nombre2=Nombre.title()
		while Nombre2 not in doc.xpath('//PROVINCIA/NOMBRE/text()'):
			print("No tengo esa provincia en mis datos")
			Nombre=input("Dime el nombre de una provincia: 	")
			Nombre2=Nombre.title()
		listacarreteras,radares=CarreterasyRadares(Nombre2,doc)
		for elem in listacarreteras:
			print(elem)
		print("El numero de radares de la provincia %s es: %i"%(Nombre2,radares))
	elif opcion=="4":
		Carretera=input("Dime el nombre de una carretera: ")
		Carretera2=Carretera.upper()
		while Carretera2 not in doc.xpath('//CARRETERA/DENOMINACION/text()'):
			print("No tengo esa carretera en mis datos")
			Carretera=input("Dime el nombre de una carretera: ")
			Carretera2=Carretera.upper()
		print("La carretera %s pasa por las provincias: "%Carretera2)
		listaprovincias,numradares=provinciasyradares(Carretera2,doc)
		for elem in listaprovincias:
			print(elem)
		print("La cantidad de radares que tiene esa carretera es: %i"%numradares)
	elif opcion=="5":
		Carretera=input("Dime el nombre de una carretera: ")
		Carretera2=Carretera.upper()
		while Carretera2 not in doc.xpath('//CARRETERA/DENOMINACION/text()'):
			print("No tengo esa carretera en mis datos")
			Carretera=input("Dime el nombre de una carretera: ")
			Carretera2=Carretera.upper()
		numrad,latitudlongitud,latitudlongitud2=Coordenadas(Carretera2,doc)
		print("La carretera %s tiene estos radares: %i"%(Carretera2,numrad))
		print("Las coordenadas del punto inicial de los radares son las siguientes: ")
		for elem in latitudlongitud:
			print("======================")
			print("Latitud: ",elem[0])
			print("Longitud: ",elem[1])
			print("La URL de OpenStraeetMap de este punto es: https://www.openstreetmap.org/#map=16/%s/%s"%(elem[0],elem[1]))
		print("======================")
		print("Las coordenades del punto final de los radares son las siguiente: ")
		for elem in latitudlongitud2:
			print("======================")
			print("Latitud: ",elem[0])
			print("Longitud: ",elem[1])
			print("La URL de OpenStraeetMap de este punto es: https://www.openstreetmap.org/#map=16/%s/%s"%(elem[0],elem[1]))
		print("======================")
	elif opcion=="0":
		print("Adios")
		break
