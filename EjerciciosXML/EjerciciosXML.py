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

#5.Ejercicio libre: Pedir por teclado una carretera, cuenta los radares que tiene 
#y muestra las coordenadas de los radares.(Se puede obtener la URL de OpenStraeetMap 
#para ver donde está el radar).

from lxml import etree
doc=etree.parse("Radares.xml")


#Ejercicio3
Nombre=input("Dime el Nombre de una provincia: ")
Nombre2=Nombre.title()
listacarreteras,radares=CarreterasyRadares(Nombre2,doc)
for elem in listacarreteras:
	print(elem)
print("El numero de radares de la provincia %s es: "%Nombre2)
print(radares)



#Ejercicio2
#print(ContarRadares(doc))



#Ejercicio1
#for elem in ListarProvincias(doc):
	#print(elem)