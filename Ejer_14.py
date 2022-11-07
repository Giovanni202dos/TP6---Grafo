"""Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
    a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
    baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
    b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la distancia entre los ambientes, se debe cargar en metros;
    c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
    para conectar todos los ambientes;
    d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
    determinar cuántos metros de cable de red se necesitan para conectar el router con el
    Smart Tv."""

from grafo import Grafo

grafoo = Grafo(dirigido=False)

#vertices
grafoo.insertar_vertice('cocina')
grafoo.insertar_vertice('comedor')
grafoo.insertar_vertice('cochera')
grafoo.insertar_vertice('quincho')
grafoo.insertar_vertice('baño_1')
grafoo.insertar_vertice('baño_2')
grafoo.insertar_vertice('habitacion_1')
grafoo.insertar_vertice('habitacion_2')
grafoo.insertar_vertice('sala_de_estar')
grafoo.insertar_vertice('terraza')
grafoo.insertar_vertice('patio')

#aristas
grafoo.insertar_arista('cocina','comedor',1)
grafoo.insertar_arista('cocina','cochera',2)
grafoo.insertar_arista('cocina','quincho',3)
grafoo.insertar_arista('comedor','cochera',4)
grafoo.insertar_arista('comedor','quincho',5)
grafoo.insertar_arista('cochera','quincho',6)

grafoo.insertar_arista('baño_1','baño_2',7)
grafoo.insertar_arista('baño_1','habitacion_1',8)
grafoo.insertar_arista('baño_1','habitacion_2',9)
grafoo.insertar_arista('baño_2','habitacion_1',10)
grafoo.insertar_arista('baño_2','habitacion_2',11)
grafoo.insertar_arista('habitacion_1','habitacion_2',12)

grafoo.insertar_arista('sala_de_estar','terraza',13)
grafoo.insertar_arista('sala_de_estar','quincho',15)
grafoo.insertar_arista('terraza','habitacion_1',16)
grafoo.insertar_arista('terraza','habitacion_2',17)

#al patio y a habitacion_2 le carge 5 aristas
grafoo.insertar_arista('sala_de_estar','patio',14)
grafoo.insertar_arista('patio','baño_2',18)
grafoo.insertar_arista('patio','habitacion_2',19)
grafoo.insertar_arista('patio','baño_1',20)
grafoo.insertar_arista('patio','cochera',21)

print()
#C
print('C). obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan para conectar todos los ambientes;')
arbol_minimo = grafoo.kruskal()
arbol_minimo = arbol_minimo[0].split('-')
print(arbol_minimo)
metros = 0
for nodo in arbol_minimo:
    nodo = nodo.split(';')
    #print(nodo)
    metros = metros + int(nodo[2])
print('la cantidade de cables que se van a necesitar es de: ',metros,' metros')

print()
#D
print('d) determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.')
caminos = grafoo.dijkstra('habitacion_1')   #OBTENGO TODOS LOS CAMINOS DESDE habitacion_1

if grafoo.existe_paso('habitacion_1','sala_de_estar'):
    camino = grafoo.camino(caminos,'habitacion_1','sala_de_estar')
    print(camino)
    print('los metros q se van a necesitar son: ',camino['costo'],' metros de cable')
else:
    print('no existe paso')
#print(caminos)