from ListaSimple import*
from xml.dom import minidom
from tkinter.filedialog import askopenfilename
from random import*
import os

class Celda:
    def __init__(self, pos_x, pos_y):
        self.pos_x=pos_x    ## empieza de 0
        self.pos_y=pos_y    ## empieza de 0
        self.viva=None
        self.id_organismo=None
    
    def darVida(self, ID, viva):
        self.id_organismo = ID
        self.viva=viva

def crearCuadricula(x,y,Lista):    ## empiezan de 1
    Lista.primer_elemento(Celda(0,0))
    PrimerElemento = True

    for i in range(y): 
        for j in range(x):
            if PrimerElemento:
                PrimerElemento = False
            else:
                Lista.agregar_celda(Celda(j,i))
    
    Lista.agregar_celda(Celda(x,y))

def anadirOrganismos(x, y, ID, Lista):
    n = Lista.primer_nodo
    while n.nodo_siguiente is not None:
        if n.celda.pos_x == x and n.celda.pos_y == y:
            break
        n = n.nodo_siguiente
    n.celda.darVida(ID, True)

def GenerarGrafica(Lista):
    docGraphviz = "digraph structs {\n"
    docGraphviz += "    node [shape=record];\n"
    docGraphviz += "    rankdir = LR"
    docGraphviz += "    MATRIZ [fontname = \"Courier New\",\n"
    docGraphviz += "        label=\"\n" + Lista.GraphvizParaTabla()
    docGraphviz += "\"]"
    docGraphviz += "\n                }"
    print(docGraphviz)
    archivoDOT = open("muestra.dot","w")
    archivoDOT.write(docGraphviz)
    archivoDOT.close()
    os.system("dot.exe -Tpng muestra.dot -o  muestra.png")

def LeerXml(Lista):
    filename = askopenfilename()
    objetoXML = minidom.parse(filename)

    coleccionX  = objetoXML.getElementsByTagName('columnas')
    coleccionY  = objetoXML.getElementsByTagName('filas')
    muestra     = objetoXML.getElementsByTagName('muestra')

    dimensionX = coleccionX[0].childNodes[0].data
    dimensionY = coleccionY[0].childNodes[0].data

    crearCuadricula(int(dimensionX), int(dimensionY), Lista)
    organismosXML = objetoXML.getElementsByTagName('organismo')
    celdasVivasXML = objetoXML.getElementsByTagName('celdaViva')
    print('         || Datos de la Muestra||\n')
    contador=1
    for organismo in organismosXML:

        codigo = organismo.childNodes[1].firstChild.data
        nombre = organismo.childNodes[3].firstChild.data
        
        print('codigo: ' + codigo)
        print('nombre: ' + nombre + "\n")
        ##nuevoOrganismo = Organismo(codigo,nombre,letra)
        ##nuevaMuestra.listaOrganismos.agregar_al_inicio(nuevoOrganismo)
        ##letra = letra + 1
        print('     Se encuentra en:')
        for celdaViva in celdasVivasXML:
            fila            = celdaViva.childNodes[1].firstChild.data
            columna         = celdaViva.childNodes[3].firstChild.data
            codigoOrganismo = celdaViva.childNodes[5].firstChild.data
            if codigoOrganismo == codigo:
                print('el contador esta en ' + str(contador))
                anadirOrganismos(int(columna)+1, int(fila)+1, contador, Lista)
                print('                         x=' + fila + ', y=' + columna)
        contador +=1

##Ejecucion principal!!!!!!!!!!!!!!!!!!!!!1


ListaCeldas = ListaSimple()
crearCuadricula(14, 18, ListaCeldas)
##ListaCeldas.imprimeEnConsola()
#organismo de prueba 
for i in range(0,14):
    anadirOrganismos(i,4,2,ListaCeldas)
for i in range(0,18):
    anadirOrganismos(4,i,2,ListaCeldas)
for i in range(0,14):
    contador=4
    anadirOrganismos(i,i,2,ListaCeldas)
for i in range(0,9):
    contador=4
    anadirOrganismos(8-i,i,2,ListaCeldas)
#organismo de prueba 1

anadirOrganismos(4,4,1,ListaCeldas) ## Base
anadirOrganismos(4,1,1,ListaCeldas) ## Tope Superior
anadirOrganismos(4,8,1,ListaCeldas) ## Tope Inferior
anadirOrganismos(1,4,1,ListaCeldas) ## Tope Anterior
anadirOrganismos(8,4,1,ListaCeldas) ## Tope Posterior
anadirOrganismos(10,10,1,ListaCeldas)
anadirOrganismos(1,1,1,ListaCeldas)
anadirOrganismos(5,5,69,ListaCeldas)
anadirOrganismos(2,6,1,ListaCeldas)
anadirOrganismos(7,1,1,ListaCeldas)
ListaCeldas.seReproduceLinea(4,4)

ListaCeldas.ReproducirDiagonal4(4,4,1,ListaCeldas.seReproduceDiagonal4(4,4,1))
ListaCeldas.ReproducirDiagonal1(4,4,1,ListaCeldas.seReproduceDiagonal1(4,4,1))
ListaCeldas.ReproducirDiagonal2(4,4,1,ListaCeldas.seReproduceDiagonal2(4,4,1))
ListaCeldas.ReproducirDiagonal3(4,4,1,ListaCeldas.seReproduceDiagonal3(4,4,1))
anadirOrganismos(5,7,69,ListaCeldas)
##ListaCeldas.revisarVidas()
##ListaCeldas.GraphvizParaTabla()
GenerarGrafica(ListaCeldas)


##ListaCeldas = ListaSimple()

##LeerXml(ListaCeldas)
##GenerarGrafica(ListaCeldas)











