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

def crearCuadricula(x,y,Lista):
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

def prLightPurple(skk): print("\033[94m {}\033[00m" .format(skk))

def prCyan(skk): print("\033[96m {}\033[00m" .format(skk))

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

def GenerarGrafica(Lista):
    docGraphviz = "digraph structs {\n"
    docGraphviz += "    node [shape=record];\n"
    docGraphviz += "    rankdir = LR"
    docGraphviz += "    MATRIZ [fontname = \"Courier New\",\n"
    docGraphviz += "        label=\"\n" + Lista.GraphvizParaTabla()
    docGraphviz += "\"];\n\""
    docGraphviz += Lista.ids
    docGraphviz += "\""
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

    dimensionX = coleccionX[0].childNodes[0].data
    dimensionY = coleccionY[0].childNodes[0].data

    crearCuadricula(int(dimensionX), int(dimensionY), Lista)
    organismosXML = objetoXML.getElementsByTagName('organismo')
    celdasVivasXML = objetoXML.getElementsByTagName('celdaViva')
    prGreen('         || Datos de la Muestra||\n')
    contador=1

    Lista.ids = ""
    for organismo in organismosXML:
        
        codigo = organismo.childNodes[1].firstChild.data
        nombre = organismo.childNodes[3].firstChild.data

        Lista.ids += str(contador) +  " -> " + codigo + "\n"


        
        prLightPurple('Codigo: ' + codigo)
        prLightPurple('Nombre: ' + nombre + "\n")
        print('     Se encuentra en:')
        for celdaViva in celdasVivasXML:
            fila            = celdaViva.childNodes[1].firstChild.data
            columna         = celdaViva.childNodes[3].firstChild.data
            codigoOrganismo = celdaViva.childNodes[5].firstChild.data
            if codigoOrganismo == codigo:
                anadirOrganismos(int(columna)+1, int(fila)+1, contador, Lista)
                prCyan('                         x=' + fila + ', y=' + columna)
        contador +=1

ListaEjemplo = ListaSimple()
crearCuadricula(14, 18, ListaEjemplo)

#organismo de prueba 
for i in range(0,14):
    anadirOrganismos(i,4,2,ListaEjemplo)
for i in range(0,18):
    anadirOrganismos(4,i,2,ListaEjemplo)
for i in range(0,14):
    contador=4
    anadirOrganismos(i,i,2,ListaEjemplo)
for i in range(0,9):
    contador=4
    anadirOrganismos(8-i,i,2,ListaEjemplo)
#organismo de prueba 1

anadirOrganismos(4,4,1,ListaEjemplo) ## Base
anadirOrganismos(4,1,1,ListaEjemplo) ## Tope Superior
anadirOrganismos(4,8,1,ListaEjemplo) ## Tope Inferior
anadirOrganismos(1,4,1,ListaEjemplo) ## Tope Anterior
anadirOrganismos(8,4,1,ListaEjemplo) ## Tope Posterior
anadirOrganismos(10,10,1,ListaEjemplo)
anadirOrganismos(1,1,1,ListaEjemplo)
anadirOrganismos(6,5,69,ListaEjemplo)
anadirOrganismos(2,6,1,ListaEjemplo)
anadirOrganismos(7,1,1,ListaEjemplo)












