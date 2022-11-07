"""Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo,
para lo cual se deben tener en cuenta las siguientes actividades:
    a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
    uno en las naturales) y tipo (natural o arquitectónica);
    b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
    la distancia que las separa;
    c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
    d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
    e. determinar si algún país tiene más de una maravilla del mismo tipo;
    f. deberá utilizar un grafo no dirigido."""
from grafo import Grafo

grafoo = Grafo(dirigido=False)

#maravillas arquitectonicas modernas
grafoo.insertar_vertice('Chichén Itzá',{'pais':'México','natural':False})
grafoo.insertar_vertice('Coliseo de Roma',{'pais':'Italia','natural':False})
grafoo.insertar_vertice('estatua del Cristo Redentor',{'pais':'Brasil','natural':False})
grafoo.insertar_vertice('Gran Muralla China',{'pais':'China','natural':False})
grafoo.insertar_vertice('Machu Picchu',{'pais':'Perú','natural':False})
grafoo.insertar_vertice('Petra',{'pais':'Jordania','natural':False})
grafoo.insertar_vertice('Taj Mahal',{'pais':'India','natural':False})


#maravillas naturales
grafoo.insertar_vertice('río subterráneo de Puerto Princesa',{'pais':'Filipinas','natural':True})
grafoo.insertar_vertice('isla Jeju',{'pais':' Corea del Sur','natural':True})
grafoo.insertar_vertice('Cataratas del Iguazú',{'pais':'argentina-Brasil','natural':True})
grafoo.insertar_vertice('Amazonía',{'pais':'Brasil-Perú-Colombia-Bolivia-Venezuela-Ecuador-Guyana-Surinam-Guayana Francesa','natural':True})
grafoo.insertar_vertice('parque nacional de Komodo',{'pais':'Indonesia','natural':True})
grafoo.insertar_vertice('Bahía de Ha Long',{'pais':'Vietnam','natural':True})
grafoo.insertar_vertice('Montaña de la Mesa',{'pais':'Sudáfrica','natural':True})


#B)
#conecto las maravillas del mismo tipo
grafoo.conectar_maravillas_del_mismo_tipo()

#C)
print()
print('C) hallar el árbol de expansión mínimo de cada tipo de las maravillas')
arbol_minimo_natu, arbol_minimo_arqui=grafoo.arboles_de_expansion_minima_de_los_dos_tipos_de_maravillas()
print('arbol minimo de las maravillas naturales:')
print(arbol_minimo_natu)

print()
print('arbol minimo de las maravillas arquitectonicas:')
print(arbol_minimo_arqui)

#D)
print()
print('D) determinar si existen países que dispongan de maravillas arquitectónicas y naturales;')
paises_con_dos_maravi_dife = grafoo.determinar_pais_que_tengan_los_dos_tipos_de_maravillas()
print(paises_con_dos_maravi_dife)

#E)
print()
print('E) determinar si algún país tiene más de una maravilla del mismo tipo;')
print('Brasil:')
maravillas_del_pais = grafoo.obtener_las_maravillas_de_un_pais_x('Brasil')    
print(maravillas_del_pais)
contador_naturales= 0
contador_arqui= 0
for maravilla in maravillas_del_pais:
    if maravilla['natural']:
        contador_naturales = contador_naturales+1
    else:
        contador_arqui = contador_arqui+1
if contador_arqui>1 or contador_naturales>1:
    print('el pais tiene mas de una maravillas del mismo tipo')
else:
    print('el pais no tiene maravillas o no tiene maravillas del mismo tipo')

