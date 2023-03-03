class Nodo:
    def __init__(self, celda):
        self.celda=celda
        self.nodo_siguiente=None

class ListaSimple:
    def __init__(self):
        self.primer_nodo=None

    def rngColor():
        pass
    
    def primer_elemento(self, celda):
        nuevo = Nodo(celda)
        self.primer_nodo = nuevo
    
    def agregar_celda(self, celda):
        n = self.primer_nodo
        while n.nodo_siguiente is not None:
            n = n.nodo_siguiente
        nuevo = Nodo(celda)
        n.nodo_siguiente=nuevo
    
    def imprimeEnConsola(self):
        n = self.primer_nodo
        filaActual = 501
        while n.nodo_siguiente is not None:
            if filaActual != n.celda.pos_y:
                print("")
                print("en y = " + str(n.celda.pos_y))
                filaActual = n.celda.pos_y
            print(str(n.celda.pos_x) + ", ", end="")
            
            n = n.nodo_siguiente
        print("")

    def revisarVidas(self):
        n = self.primer_nodo
        filaActual = 501
        while n.nodo_siguiente is not None:
            if filaActual != n.celda.pos_y:
                print("")
                print("\ny = " + str(n.celda.pos_y))
                filaActual = n.celda.pos_y
            ##print(str(n.celda.pos_x) + ", ", end="")
            if n.celda.viva:
                print(str(n.celda.id_organismo) + ", ", end="")
            else:
                print('-' + ", ", end="")
            
            n = n.nodo_siguiente
        print("")
    
    def seReproduceLinea(self, x, y):

        #Primero asigna a CeldaBase la celda que se busca ver si sobrevive
        y=y-1
        x=x-1
        CeldaBase = self.primer_nodo
        while CeldaBase.nodo_siguiente is not None:
            if CeldaBase.celda.pos_x == x and CeldaBase.celda.pos_y == y:
                break
            CeldaBase = CeldaBase.nodo_siguiente

        #horizontal, verifica primero linea horizontal de celdabase
        n = self.primer_nodo
        TopeAnterior = None
        TopePosterior = None
        while n.nodo_siguiente is not None: #Asigna los topes
            if n.celda.pos_y == y and n.celda.id_organismo == CeldaBase.celda.id_organismo and n.celda.pos_x < x:
                TopeAnterior = n.celda.pos_x
            if n.celda.pos_y == y and n.celda.id_organismo == CeldaBase.celda.id_organismo and n.celda.pos_x > x:
                TopePosterior = n.celda.pos_x
            n = n.nodo_siguiente

        if TopeAnterior is None:
            TopeAnterior = CeldaBase.celda.pos_x
        if TopePosterior is None:
            TopePosterior = CeldaBase.celda.pos_x

        #aqui se va a empezar a transformar los organismos atrapados en organismos del tipo celda base, usar ifs de anterior
        n = self.primer_nodo
        while n.nodo_siguiente is not None:
            if TopeAnterior == TopePosterior:
                print("No hay ninguna wea pu")
                break
            if n.celda.pos_y == y and n.celda.id_organismo != CeldaBase.celda.id_organismo and n.celda.pos_x > TopeAnterior and n.celda.pos_x < TopePosterior:
                n.celda.id_organismo = CeldaBase.celda.id_organismo

            n = n.nodo_siguiente

        #Vertical, verifica primero linea horizontal de celdabase

        n = self.primer_nodo
        TopeSuperior = None
        TopeInferior = None
        while n.nodo_siguiente is not None: #Asigna los topes
            if n.celda.pos_x == x and n.celda.id_organismo == CeldaBase.celda.id_organismo and n.celda.pos_y < y:
                TopeSuperior = n.celda.pos_y
            if n.celda.pos_x == x and n.celda.id_organismo == CeldaBase.celda.id_organismo and n.celda.pos_y > y:
                TopeInferior = n.celda.pos_y
            n = n.nodo_siguiente
        print(TopeSuperior)
        print(TopeInferior)

        if TopeSuperior is None:
            TopeSuperior = CeldaBase.celda.pos_y
        if TopeInferior is None:
            TopeInferior = CeldaBase.celda.pos_y

        #aqui se va a empezar a transformar los organismos atrapados en organismos del tipo celda base, usar ifs de anterior
        n = self.primer_nodo
        while n.nodo_siguiente is not None:
            if TopeSuperior == TopeInferior:
                print("No hay ninguna wea pu")
                break

            if n.celda.pos_x == x and n.celda.id_organismo != CeldaBase.celda.id_organismo and n.celda.pos_y > TopeSuperior and n.celda.pos_y < TopeInferior:
                n.celda.id_organismo = CeldaBase.celda.id_organismo

            n = n.nodo_siguiente

    def GraphvizParaTabla(): ##Generar tabla concatendando |'s. Recordar anadir una fila y columna extra
        pass








