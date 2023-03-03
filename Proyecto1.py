from ListaSimple import*
from xml.dom import minidom
from tkinter.filedialog import askopenfilename
from random import*

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
    
    Lista.agregar_celda(Celda(x-1,y-1))

def anadirOrganismos(x, y, ID, Lista):
    n = Lista.primer_nodo
    x=x-1
    y=y-1
    while n.nodo_siguiente is not None:
        if n.celda.pos_x == x and n.celda.pos_y == y:
            break
        n = n.nodo_siguiente
    n.celda.darVida(ID, True)



def GenerarGrafica(Lista):
    docGraphviz = "digraph structs {\n"
    docGraphviz += "    node [shape=record];\n"
    docGraphviz += "    MATRIZ [\n"
    docGraphviz += "        label=\"\n"



    
    



##Ejecucion principal!!!!!!!!!!!!!!!!!!!!!1


ListaCeldas = ListaSimple()

crearCuadricula(14, 18, ListaCeldas)

ListaCeldas.imprimeEnConsola()

#organismo de prueba 2
for i in range(1,15):
    anadirOrganismos(i,5,2,ListaCeldas)

for i in range(1,19):
    anadirOrganismos(5,i,2,ListaCeldas)

#organismo de prueba 1
anadirOrganismos(5,5,1,ListaCeldas) ## Base
anadirOrganismos(5,2,1,ListaCeldas) ## Tope Superior
anadirOrganismos(5,9,1,ListaCeldas) ## Tope Inferior
anadirOrganismos(2,5,1,ListaCeldas) ## Tope Anterior
anadirOrganismos(9,5,1,ListaCeldas) ## Tope Posterior
ListaCeldas.seReproduceLinea(5,5)
ListaCeldas.revisarVidas()








