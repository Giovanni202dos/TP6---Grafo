from cola import Cola
from heap import HeapMin, HeapMax


def criterio(dato, campo=None):
    dic = {}
    if(hasattr(dato, '__dict__')):
        dic = dato.__dict__
    if(campo is None or campo not in dic):
        return dato
    else:
        return dic[campo]


class nodoArista():
    info, sig, peso = None, None, None
    #? info es el destino


class nodoVertice():
    info, sig, visitado, adyacentes, dato_extra = None, None, False, None, None #(dato_extra lo agregue para ejer 4)


class Arista():
    
    def __init__(self):
        self.__inicio = None
        self.__tamanio = 0

    def get_inicio(self):
        return self.__inicio

    def insertar_arista(self, dato, peso, campo=None):
        nodo = nodoArista()
        nodo.info = dato
        nodo.peso = peso

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def tamanio(self):
        return self.__tamanio

    def barrido_aristas(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info, aux.peso)
            aux = aux.sig
    
    def busqueda_arista(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def eliminar_arista(self, clave, campo=None):
        dato, peso = None, None
        if self.__inicio is not None:
            if(criterio(self.__inicio.info, campo) == clave):
                dato = self.__inicio.info
                peso = self.__inicio.peso
                self.__inicio = self.__inicio.sig
            else:
                anterior = self.__inicio
                actual = self.__inicio.sig
                while(actual is not None and criterio(actual.info, campo) != clave):
                    anterior = anterior.sig
                    actual = actual.sig

                if(actual is not None):
                    dato = actual.info
                    peso = actual.peso
                    anterior.sig = actual.sig
            if dato:
                self.__tamanio -= 1 

        return dato, peso

    def obtener_elemento_arista(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None
    
    ##### METODOS PARA EL EJER 1 ##########
    def tiene_aristas(self):    # FUNCIONA PARA GRAFOS NO DIRIGIDOS (aun no lo probe para dirigidos)
        aux = self.__inicio
        if aux is not None:
            #print(aux.info, aux.peso)
            return True
            #aux = aux.sig
        else:
            return False

    def obetener_arista_con_peso(self):
        aux = self.__inicio
        vector = []
        while (aux is not None):
            #print(aux.info, aux.peso)
            vector.append([aux.info, aux.peso])
            aux = aux.sig
        return vector

    #devuelve un vector con las aristas de mayor peso (si hay aristas de igual peso va a ser un vector de vectores)
    def obetener_arista_con_mayor_peso(self):
        aux = self.__inicio
        vector_de_pesos_iguales = []
        peso_mayor = [1,0]
        while (aux is not None):
            if aux.peso >peso_mayor[1]:
                peso_mayor = [aux.info, aux.peso]
                if len(vector_de_pesos_iguales)==0:#si es cero es porque en el vector no hay arista con la misma canti
                    vector_de_pesos_iguales.append(peso_mayor)
                else:
                    vector_de_pesos_iguales =[] #ENTONCES LO DEBO VACIAR (porque se supone q las arsitas guardada tienen menor  peso)
                    vector_de_pesos_iguales.append(peso_mayor)
            elif aux.peso == peso_mayor[1]: #si tienen la misma peso entonces los debo agregar al vector
                peso_mayor = [aux.info, aux.peso]
                vector_de_pesos_iguales.append([aux.info, aux.peso])
            #print(aux.info, aux.peso)
            aux = aux.sig
        return vector_de_pesos_iguales

    ##### FIN DE METODOS PARA EL EJER 1 ##########


class Grafo():

    def __init__(self, dirigido=True):
        self.__inicio = None
        self.__tamanio = 0
        self.__dirigido = dirigido


    def insertar_vertice(self, dato, dato_extra=None, campo=None):
        nodo = nodoVertice()
        nodo.info = dato
        nodo.adyacentes = Arista()
        nodo.dato_extra = dato_extra    #lo agregue para el ejer 4

        if(self.__inicio is None or criterio(nodo.info, campo) < criterio(self.__inicio.info, campo)):
            nodo.sig = self.__inicio
            self.__inicio = nodo
        else:
            anterior = self.__inicio
            actual = self.__inicio.sig
            while(actual is not None and criterio(nodo.info, campo) > criterio(actual.info, campo)):
                anterior = anterior.sig
                actual = actual.sig

            nodo.sig = actual
            anterior.sig = nodo

        self.__tamanio += 1

    def insertar_arista(self, origen, destino, peso):
        vert_origen = self.busqueda_vertice(origen)
        vert_destino = self.busqueda_vertice(destino)
        if(vert_origen and vert_destino):
            vert_origen.adyacentes.insertar_arista(destino, peso)
            if not self.__dirigido:
                vert_destino.adyacentes.insertar_arista(origen, peso)

    def tamanio(self):
        return self.__tamanio

    def barrido_vertice(self):
        aux = self.__inicio
        while(aux is not None):
            print(aux.info)
            aux = aux.sig
    
    def marcar_no_visitado(self):
        aux = self.__inicio
        while(aux is not None):
            aux.visitado = False
            aux = aux.sig

    def barrido_lista_lista(self):
        aux = self.__inicio
        while(aux is not None):
            print('Vertice:', aux.info)
            print('arsitas:')
            aux.adyacentes.barrido_aristas()
            aux = aux.sig

    def busqueda_vertice(self, buscado, campo=None):
        pos = None
        aux = self.__inicio
        while(aux is not None and pos is None):
            if(criterio(aux.info, campo) == buscado):
                pos = aux
            aux = aux.sig

        return pos

    def barrido_no_visitado(self):
        aux = self.__inicio
        while(aux is not None):
            if not aux.visitado:
                print(aux.info)
            aux = aux.sig

    def eliminar_vertice(self, clave, campo=None):
        dato = None
        if self.__inicio is not None:
            if(criterio(self.__inicio.info, campo) == clave):
                dato = self.__inicio.info
                self.__inicio = self.__inicio.sig
            else:
                anterior = self.__inicio
                actual = self.__inicio.sig
                while(actual is not None and criterio(actual.info, campo) != clave):
                    anterior = anterior.sig
                    actual = actual.sig

                if(actual is not None):
                    dato = actual.info
                    anterior.sig = actual.sig
            if dato:
                self.__tamanio -= 1 

            #! eliminar todas las aristas que apuntan al vertice
            aux = self.__inicio
            while(aux is not None):
                aux.adyacentes.eliminar_arista(clave)
                aux = aux.sig
            
        return dato

    def eliminar_arista(self, origen, destino):
        vert_origen = self.busqueda_vertice(origen)
        valor, peso = None, None
        if vert_origen:
            valor, peso = vert_origen.adyacentes.eliminar_arista(destino)
            if valor:
                vert_destino = self.busqueda_vertice(destino)
                vert_destino.adyacentes.eliminar_arista(origen)

        return peso

    def obtener_elemento_vertice(self, indice):
        if(indice <= self.__tamanio-1 and indice >= 0):
            aux = self.__inicio
            for i in range(indice):
                aux = aux.sig
            return aux.info            
        else:
            return None
    
    def es_adyacente(self, origen, destino):
        resultado = False
        vert_origen = self.busqueda_vertice(origen)
        if vert_origen:
            aux = vert_origen.adyacentes.busqueda_arista(destino)
            if aux:
                resultado = True
        return resultado

    def adyacentes(self, origen):
        vert_origen = self.busqueda_vertice(origen)
        if vert_origen:
            vert_origen.adyacentes.barrido_aristas()

    def existe_paso(self, origen, destino):
        resultado = False
        vert_origen = self.busqueda_vertice(origen)
        #print(vert_origen)
        if not vert_origen.visitado:
            vert_origen.visitado = True
            #print(vert_origen.info)
            adyacentes = vert_origen.adyacentes.get_inicio()
            # resultado = g.es_adyacente(origen, destino)
            while adyacentes is not None and not resultado:
                if adyacentes.info == destino:
                    resultado = True
                else:
                    resultado = self.existe_paso(adyacentes.info, destino)
                adyacentes = adyacentes.sig
        return resultado

    def barrido_profundidad(self, origen):
        vert_origen = self.busqueda_vertice(origen)
        #print(vert_origen.visitado)
        if not vert_origen.visitado:    #SI LE PASO UN VERTICE Q NO EXISTE ME SALTA ERROR(RECORDAR) porque me devuelve un None
            print(vert_origen.info)
            vert_origen.visitado = True
            adyacentes = vert_origen.adyacentes.get_inicio()
            while adyacentes is not None:
                self.barrido_profundidad(adyacentes.info)
                adyacentes = adyacentes.sig
    
    def barrido_amplitud(self, origen):
        self.marcar_no_visitado()
        vert_origen = self.busqueda_vertice(origen)
        pendientes = Cola()
        if not vert_origen.visitado:
            vert_origen.visitado = True
            pendientes.arribo(vert_origen)
            while not pendientes.cola_vacia():
                vertice_actual = pendientes.atencion()
                print(vertice_actual.info)
                adyacentes = vertice_actual.adyacentes.get_inicio()
                while adyacentes is not None:
                    adyacente = self.busqueda_vertice(adyacentes.info)
                    if not adyacente.visitado:
                        adyacente.visitado = True
                        pendientes.arribo(adyacente)
                    adyacentes = adyacentes.sig

    def dijkstra(self, origen):
        from math import inf
        # self.marcar_no_visitado()
        no_visitado = HeapMin()
        camino = {}

        aux = self.__inicio
        while aux is not None:
            if aux.info == origen:
                no_visitado.agregar([aux, None], 0)
            else:
                no_visitado.agregar([aux, None], inf)
            aux = aux.sig

        while no_visitado.tamanio > 0:
            elemento, peso = no_visitado.quitar()
            vertice, previo = elemento[0], elemento[1]
            camino[vertice.info] = {'previo': previo, 'peso': peso}
            adyacentes = vertice.adyacentes.get_inicio()
            while adyacentes is not None:
                buscado = no_visitado.buscar(adyacentes.info)
                if buscado:
                    if no_visitado.vector[buscado][1] > peso + adyacentes.peso:
                        no_visitado.vector[buscado][1] = peso + adyacentes.peso
                        no_visitado.vector[buscado][0][1] = vertice.info
                        no_visitado.flotar(buscado)
                adyacentes = adyacentes.sig
        return camino

    def kruskal(self):
        def buscar_en_bosque(bosque, buscado):
            for arbol in bosque:
                if buscado in arbol:
                    return arbol

        bosque = []
        aristas = HeapMin()
        aux = self.__inicio
        while aux is not None:
            bosque.append(str(aux.info))
            adyacentes = aux.adyacentes.get_inicio()
            while adyacentes is not None:
                aristas.arribo([aux.info, adyacentes.info], adyacentes.peso)
                adyacentes = adyacentes.sig
            aux = aux.sig

        while len(bosque) > 1 and aristas.tamanio > 0:
            arista, peso = aristas.quitar()
            # print(bosque)
            # print(arista[0])
            # print(arista[1])
            origen = buscar_en_bosque(bosque, arista[0])
            destino = buscar_en_bosque(bosque, arista[1])
            # print(origen, destino, 'posiciones')
            if origen is not None and destino is not None:
                if origen != destino:
                    # print(arista[0], origen)
                    # print(arista[1], destino)
                    bosque.remove(origen)
                    bosque.remove(destino)
                    if ';' not in origen and ';' not in destino:
                        bosque.append(f'{origen};{destino};{peso}')
                    elif ';' in origen and ';' not in destino:
                        bosque.append(origen+f'-{arista[0]};{destino};{peso}')
                    elif ';' not in origen and ';' in destino:
                        bosque.append(destino+f'-{origen};{arista[1]};{peso}')
                    else:
                        bosque.append(origen+'-'+destino+f'-{arista[0]};{arista[1]};{peso}')

            # print(bosque)
            # a = input()
        return bosque

    def camino(self, resultados, origen, destino):
        camino_mas_corto = {'camino': [],
                            'costo': None}
        if destino in resultados:
            vert_destino = resultados[destino]
            camino_mas_corto['costo'] = vert_destino['peso']
            camino_mas_corto['camino'].append(destino)
            while vert_destino['previo'] is not None:
                camino_mas_corto['camino'].append(vert_destino['previo'])
                vert_destino = resultados[vert_destino['previo']]
            camino_mas_corto['camino'].reverse()
        return camino_mas_corto
    
    ########## metodo para el ejercicio 1 ####################################################

    #ESTA EN DESUSO (ya que creo una copia de todos los vertices)
    def obtener_vector_con_los_vertices(self):
        vector= []
        while self.tamanio() != len(vector):
            aux = self.__inicio
            while(aux is not None):
                vector.append(aux.info)
                #print(aux.info)
                aux = aux.sig
        return vector
    
    #este tambien esta en desuso
    def tiene_adyacentes(self, origen): # FUNCIONA PARA GRAFOS NO DIRIGIDOS (aun no lo probe para dirigidos)
        vert_origen = self.busqueda_vertice(origen)
        if vert_origen:
            return vert_origen.adyacentes.tiene_aristas()

    
    #POR AHORA FUNCIONA
    def eliminar_vertices_que_no_tengan_ninguna_arista(self):   # FUNCIONA PARA GRAFOS NO DIRIGIDOS (aun no lo probe para dirigidos)
        aux = self.__inicio #me posisiono en el inicio
        datos_eliminados = []
        while(aux is not None):
            if aux.adyacentes.tiene_aristas() == False: #si es false es porque no tiene niguna aristas (osea no esta conectado con nadie)
                datos_eliminados.append(self.eliminar_vertice(aux.info))
            aux = aux.sig   #PASO AL SUIGUIENTE
        return datos_eliminados

    #POR AHORA FUNCIONA (DEVUELVE UN VECTOR CON EL NOMBRE DEL VERTICE Y LA CANTIDAD DE ARISTAS Q TIENE)  
    def vertice_con_mayor_aristas_o_con_mayor_conexion_con_adyacentes(self):   # FUNCIONA PARA GRAFOS NO DIRIGIDOS (aun no lo probe para dirigidos)
        aux = self.__inicio #me posisiono en el inicio
        vertices_con_mayores_aristas = []
        vertice_mayor = [1,0]   #pongo un vertice cualquiera con donde 1 =vertice y 0 = cantidas de aristas o adyacentes
        while (aux is not None):
            if aux.adyacentes.tiene_aristas(): #si es true tiene adyacentes
                cantidad = aux.adyacentes.tamanio()
                if cantidad >vertice_mayor[1]:
                    vertice_mayor = [aux.info, cantidad]
                    if len(vertices_con_mayores_aristas)==0: #si es cero es porque en el vector no hay vertices con la misma canti
                        vertices_con_mayores_aristas.append(vertice_mayor)
                    else:
                        vertices_con_mayores_aristas =[]    #ENTONCES LO DEBO VACIAR (porque se supone q tiene menor canti de adyacentes o aristas)
                        vertices_con_mayores_aristas.append(vertice_mayor)
                elif cantidad == vertice_mayor[1]: #si tienen la misma cantidad entonces los debo agregar a un vector
                            vertices_con_mayores_aristas.append([aux.info,cantidad])
            aux = aux.sig   #PASO AL SUIGUIENTE
        return vertices_con_mayores_aristas
    
    # DEVUELVE UN VECTOR CON TODAS LAS ARISTAS CON SU PESO
    def obtener_aristas_con_peso_de_un_vertice_x(self, origen): # FUNCIONA PARA GRAFOS NO DIRIGIDOS (aun no lo probe para dirigidos)
        vert_origen = self.busqueda_vertice(origen)
        if vert_origen:
            return vert_origen.adyacentes.obetener_arista_con_peso()

    #DEVUELVE UN DICCIONARIO PARA MEJOR COMPRESION (donde dice desde q vertice hacia donde es la arista mayor)
    def obtener_arista_de_mayor_peso_de_todo_el_grafo(self):
        aux = self.__inicio
        arista_con_mayor_peso = [0]
        diccionario_con_aristas_mayor_peso = {}
        while (aux is not None):
            if aux.adyacentes.tiene_aristas(): #si es true tiene adyacentes 
                vector_de_aristas = aux.adyacentes.obetener_arista_con_mayor_peso()  #(ACÁ QUEDE) nose q hace no me acuerdo
                #print('del vertice:',aux.info)
                #print('hacia el vertice o los vertices:')
                #print(vector_de_aristas)
                #print()
                for arista_mayor_peso_aux in vector_de_aristas:
                    #print(arista_con_mayor_peso[0])
                    if arista_mayor_peso_aux[1]> arista_con_mayor_peso[0]:
                        arista_con_mayor_peso = arista_mayor_peso_aux
                        #print(arista_con_mayor_peso)
                        adyacente = str(arista_con_mayor_peso[0])
                        arista_con_mayor_peso.pop(0)
                        if len(diccionario_con_aristas_mayor_peso)==0: #si es cero es porque en el vector no hay aristas con la mismo peso
                            diccionario_con_aristas_mayor_peso['de '+str(aux.info)+' hacia '+adyacente]= arista_con_mayor_peso
                        else:
                            diccionario_con_aristas_mayor_peso ={}    #ENTONCES LO DEBO VACIAR (porque se supone q tienen menor peso)
                            diccionario_con_aristas_mayor_peso['de '+str(aux.info)+' hacia '+adyacente]= arista_con_mayor_peso
                    elif arista_mayor_peso_aux[1] == arista_con_mayor_peso[0]: #si tienen el mismo peso  entonces los debo agregar al vector
                        arista_con_mayor_peso = arista_mayor_peso_aux
                        #print(arista_con_mayor_peso)
                        adyacente = str(arista_con_mayor_peso[0])
                        arista_con_mayor_peso.pop(0)
                        diccionario_con_aristas_mayor_peso['de '+str(aux.info)+' hacia '+adyacente]= arista_con_mayor_peso
            aux = aux.sig
        return  diccionario_con_aristas_mayor_peso
    ########## FIN metodo para el ejercicio 1 ####################################################

    ########## METODOS PARA EL EJERCICIO 4 ####################################################
    #utilizo en el dato extra un obejto antena
    def obtener_antena_de_ubi_x(self,ubicacion):
        ubi = None
        aux = self.__inicio
        while(aux is not None) and (ubi ==None):
            #print(aux.info)
            if aux.dato_extra.ubicacion == ubicacion:
                ubi = aux
            aux = aux.sig
        return ubi
    ########## FIN DE METODOS PARA EL EJERCICIO 4 ####################################################

    ########## METODOS PARA EL EJERCICIO 15 ####################################################
    def conectar_maravillas_del_mismo_tipo(self):
        aux = self.__inicio
        peso = 0
        while(aux is not None):
            aux_destino = aux.sig
            #print(aux.info)
            while(aux_destino is not None):
                #print('ff ',aux_destino.info)
                if aux.dato_extra['natural'] == True and aux_destino.dato_extra['natural'] == True: #conecto las q son naturales
                    peso = peso+1
                    #print(aux.info,' con ',aux_destino.info,' peso: ',peso)
                    self.insertar_arista(aux.info,aux_destino.info,peso)
                elif aux.dato_extra['natural'] == False and aux_destino.dato_extra['natural'] == False: #conecto las q son arquitectonicas
                    peso = peso+1
                    #print(aux.info,' con ',aux_destino.info,' peso: ',peso)
                    self.insertar_arista(aux.info,aux_destino.info,peso)
                aux_destino = aux_destino.sig
            aux = aux.sig

    def arboles_de_expansion_minima_de_los_dos_tipos_de_maravillas(self):   #POR AHORA FUNCIONA
        arbol_natu = None
        arbol_arqui = None
        arbol_minimo_completo = self.kruskal()  #devuelve los arboles separados(en la posi 0 estan las maravillas de un tipo y en la otra posi las otras)
        #print(arbol_minimo_completo)
        arbol_aux_1 = arbol_minimo_completo[0]  #separo los arboles(aun nose sabe cual es natural o arqui)
        arbol_aux_2 = arbol_minimo_completo[1]
        if self.busqueda_vertice(arbol_aux_1.split(';')[0]).dato_extra['natural']:  #acá averiguo q tipo es... buscando un vertice del arbol y consultando el dato extra
            arbol_natu= arbol_aux_1
            arbol_arqui = arbol_aux_2
        else:
            arbol_natu= arbol_aux_2
            arbol_arqui = arbol_aux_1
        return arbol_natu, arbol_arqui
    
    def obtener_las_maravillas_de_un_pais_x(self,pais):
        aux = self.__inicio
        maravillas_q_posee = []
        #maravillas_q_posee.append({'pais':pais})
        while (aux is not None):
            if pais in aux.dato_extra['pais']:
                maravilla = {'maravilla':aux.info,'natural':aux.dato_extra['natural']}
                maravillas_q_posee.append(maravilla)
            aux = aux.sig
        return maravillas_q_posee
    
    def determinar_pais_que_tengan_los_dos_tipos_de_maravillas(self):   #por ahora funciona
        aux = self.__inicio
        paises_con_dos_maravillas =[]
        while(aux is not None):
            #print('de: ',aux.info)
            lista_de_paises = aux.dato_extra['pais'].split('-') #por si tiene varios paises
            for pais in lista_de_paises:    #voy a buscar este pais en el grafo de maravilla diferente
                #print('pais: ', pais)
                aux_destino = aux.sig       #paso al siguiente
                while(aux_destino is not None):
                    #print('     yy ',aux_destino.info)
                    if aux.dato_extra['natural'] != aux_destino.dato_extra['natural']:  #si son maravillas de diferente tipo(busco si el pais esta en una de ellas)
                        #print('     son diferentes')
                        if pais in aux_destino.dato_extra['pais']:  #si encuentra una maravilla con el mismo pais
                            #print('         si lo tieneee')
                            pais_ux ={'pais':pais,'arquitectonica': True,'natural':True}
                            #print('vector ',paises_con_dos_maravillas)
                            #print(pais_ux)
                            if len(paises_con_dos_maravillas)>0:    #esto es para que no guarde paises repetidos(si ya hay guardados comparo si el pais ya esta guardado)
                                #print('hay cargados')
                                tamanio =len(paises_con_dos_maravillas)
                                for i in range(0,tamanio):
                                    #print(paises_con_dos_maravillas[i]['pais'],' != ', pais,' ?')
                                    if paises_con_dos_maravillas[i]['pais'] != pais:    #comparo(si son diferentes lo agrego)
                                        #print('yess')
                                        paises_con_dos_maravillas.append(pais_ux)
                                    break   #si ya esta cargado freno el bucle for y paso al siguiente vertice 
                            else:
                                #print('non hay cargados')
                                paises_con_dos_maravillas.append(pais_ux)
                            #paises_con_dos_maravillas
                    aux_destino = aux_destino.sig
            aux = aux.sig
        return paises_con_dos_maravillas

        


#! algoritmos especiales dijkstra prim kruskal

# g = Grafo(dirigido=False)

# g.insertar_vertice('T')
# g.insertar_vertice('Z')
# g.insertar_vertice('F')
# g.insertar_vertice('X')
# g.insertar_vertice('R')
# g.insertar_vertice('K')
# # g.insertar_vertice('U')


# g.insertar_arista('T', 'X', 6)
# g.insertar_arista('T', 'F', 3)
# g.insertar_arista('T', 'R', 8)
# g.insertar_arista('F', 'X', 2)
# g.insertar_arista('F', 'R', 2)
# g.insertar_arista('X', 'Z', 9)
# g.insertar_arista('R', 'Z', 4)
# g.insertar_arista('K', 'Z', 3)
# g.insertar_arista('R', 'X', 5)
# g.insertar_arista('K', 'A', 31)
# g.insertar_arista('J', 'F', 31)
# g.insertar_arista('A', 'J', 0)

# arbol_min = g.kruskal()

# arbol_min = arbol_min[0].split('-')
# peso_total = 0
# for nodo in arbol_min:
#     nodo = nodo.split(';')
#     peso_total += int(nodo[2])
#     print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

# print(f"el peso total es {peso_total}")

# if g.existe_paso('T', 'Z'):
#     resultados1 = g.dijkstra('T')
#     camino = g.camino(resultados1, 'T', 'Z')
#     print(camino)
# else:
#     print('no se puede llega de T a Z')

###### HASTA ACA ESTABA COMENTADO #########
# g.eliminar_arista('A', 'C')
# g.eliminar_vertice('C')

#g.barrido_profundidad('K')
# print()
# g.barrido_amplitud('K')
# print()
# g.barrido_no_visitado()

# g.adyacentes('A')

# print(g.es_adyacente('A', 'F'))
# print(g.es_adyacente('Z', 'A'))