class Nodo:
    def __init__(self, celda):
        self.celda=celda
        self.nodo_siguiente=None

class ListaSimple:
    def __init__(self):
        self.primer_nodo=None
    
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
                filaActual = n.celda.pos_y
            ##if n.celda.viva:
                ##print(str(n.celda.id_organismo) + ", ", end="")
            ##else:
                ##print('-' + ", ", end="")
            
            n = n.nodo_siguiente
        print("")
    
    def encontrarID(self, x, y):
        n = self.primer_nodo
        while n.nodo_siguiente is not None:
            if x == n.celda.pos_x and y == n.celda.pos_y:
                if n.celda.id_organismo is not None:
                    return n.celda.id_organismo
            n = n.nodo_siguiente

    def seReproduceLinea(self, x, y):

        #Primero asigna a CeldaBase la celda que se busca ver si sobrevive
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
        ##print(TopeSuperior)
        ##print(TopeInferior)

        if TopeSuperior is None:
            TopeSuperior = CeldaBase.celda.pos_y
        if TopeInferior is None:
            TopeInferior = CeldaBase.celda.pos_y

        #aqui se va a empezar a transformar los organismos atrapados en organismos del tipo celda base, usar ifs de anterior
        n = self.primer_nodo
        while n.nodo_siguiente is not None:
            if TopeSuperior == TopeInferior:
                break

            if n.celda.pos_x == x and n.celda.id_organismo != CeldaBase.celda.id_organismo and n.celda.pos_y > TopeSuperior and n.celda.pos_y < TopeInferior:
                n.celda.id_organismo = CeldaBase.celda.id_organismo

            n = n.nodo_siguiente

    def seReproduceDiagonal4(self, x, y, id): #tiene que salir 69, ya nos reconoce la primera diagonal siguiente, ahora hay que reconocer recursivamente
        n = self.primer_nodo

        y_tope = x
        x_tope = y
        while n.nodo_siguiente is not None:
            if y_tope + 1 == n.celda.pos_y and x_tope + 1 == n.celda.pos_x:
                if n.celda.id_organismo == id:
                    ##print('se encontro tope en x= ' +  str(x_tope+1) + ", y= " + str(y_tope+1))
                    Coordenadas = [x_tope+1, y_tope+1]
                    return Coordenadas
                else:
                    return self.seReproduceDiagonal4(x_tope+1, y_tope+1, id)
            n=n.nodo_siguiente
    
    def ReproducirDiagonal4(self, x_base, y_base, id, coordenadas):
        n = self.primer_nodo
        if coordenadas is None:
            return 
        while n.nodo_siguiente is not None:
            if y_base + 1 == n.celda.pos_y and x_base + 1 == n.celda.pos_x:

                if n.celda.pos_x == coordenadas[0] and n.celda.pos_y == coordenadas[1]:
                    n.celda.id_organismo = id
                    return
                else:
                    n.celda.id_organismo = id
                    self.ReproducirDiagonal4(x_base + 1,y_base +1, id,coordenadas)
            n=n.nodo_siguiente
    
    def seReproduceDiagonal1(self, x, y, id): 
        n = self.primer_nodo
        y_tope = y
        x_tope = x
        while n.nodo_siguiente is not None:
            if y_tope - 1 == n.celda.pos_y and x_tope + 1 == n.celda.pos_x: ##si la celda seleccionada tiene las mismas coordenadas que la celda siguiente a la base
                
                if n.celda.id_organismo == id:
                    Coordenadas = [x_tope+1, y_tope-1]
                    return Coordenadas
                else:
                    return self.seReproduceDiagonal1(x_tope+1, y_tope-1, id)
            n=n.nodo_siguiente
    
    def ReproducirDiagonal1(self, x_base, y_base, id, coordenadas):
        n = self.primer_nodo
        if coordenadas is None:
            return 
        while n.nodo_siguiente is not None:
            if y_base - 1 == n.celda.pos_y and x_base + 1 == n.celda.pos_x:
                if n.celda.pos_x == coordenadas[0] and n.celda.pos_y == coordenadas[1]:
                    n.celda.id_organismo = id
                    return
                else:
                    n.celda.id_organismo = id
                    self.ReproducirDiagonal1(x_base + 1,y_base -1, id,coordenadas)
            n=n.nodo_siguiente
        
    def seReproduceDiagonal2(self, x, y, id): 
        n = self.primer_nodo
        y_tope = y
        x_tope = x
        while n.nodo_siguiente is not None:
            if y_tope - 1 == n.celda.pos_y and x_tope - 1 == n.celda.pos_x: ##si la celda seleccionada tiene las mismas coordenadas que la celda siguiente a la base
                
                if n.celda.id_organismo == id:
                    Coordenadas = [x_tope-1, y_tope-1]
                    return Coordenadas
                else:
                    return self.seReproduceDiagonal2(x_tope-1, y_tope-1, id)
            n=n.nodo_siguiente
    
    def ReproducirDiagonal2(self, x_base, y_base, id, coordenadas):
        n = self.primer_nodo
        if coordenadas is None:
            return 
        while n.nodo_siguiente is not None:
            if y_base - 1 == n.celda.pos_y and x_base - 1 == n.celda.pos_x:
                if n.celda.pos_x == coordenadas[0] and n.celda.pos_y == coordenadas[1]:
                    n.celda.id_organismo = id
                    return
                else:
                    n.celda.id_organismo = id
                    self.ReproducirDiagonal2(x_base - 1,y_base -1, id,coordenadas)
            n=n.nodo_siguiente
        
    def seReproduceDiagonal3(self, x, y, id): 
        n = self.primer_nodo
        y_tope = y
        x_tope = x
        while n.nodo_siguiente is not None:
            if y_tope + 1 == n.celda.pos_y and x_tope - 1 == n.celda.pos_x: ##si la celda seleccionada tiene las mismas coordenadas que la celda siguiente a la base
                
                if n.celda.id_organismo == id:
                    Coordenadas = [x_tope-1, y_tope+1]
                    return Coordenadas
                else:
                    return self.seReproduceDiagonal3(x_tope-1, y_tope+1, id)
            n=n.nodo_siguiente
    
    def ReproducirDiagonal3(self, x_base, y_base, id, coordenadas):
        n = self.primer_nodo
        if coordenadas is None:
            return 
        while n.nodo_siguiente is not None:
            if y_base + 1 == n.celda.pos_y and x_base - 1 == n.celda.pos_x:
                if n.celda.pos_x == coordenadas[0] and n.celda.pos_y == coordenadas[1]:
                    n.celda.id_organismo = id
                    return
                else:
                    n.celda.id_organismo = id
                    self.ReproducirDiagonal3(x_base - 1,y_base +1, id,coordenadas)
            n=n.nodo_siguiente

    def GraphvizParaTabla(self) -> str: ##Generar tabla concatendando |'s. Recordar anadir una fila y columna extra
        contador=-1
        Texto = ""
        n = self.primer_nodo
        Fila = n.celda.pos_y
        m = self.primer_nodo
        while n.nodo_siguiente is not None:
            #Anade la fila inicial
            if contador == -1:
                Texto = "{x y|"
                while m.nodo_siguiente is not None:
                    if m.celda.pos_y != 0:
                        break
                    if m.celda.pos_x < 10:
                        Texto += str(m.celda.pos_x) + "."
                    else:
                        Texto += str(m.celda.pos_x)
                    m = m.nodo_siguiente
                    Texto += "|"
                Texto = Texto[:len(Texto)-1]
                Texto += "}|\n{0 .|"
                
            #Anade celdas
            if contador != -1:
                #Anade celdas vivas
                if Fila != n.celda.pos_y:
                    Texto = Texto[:len(Texto)-1]
                    if n.celda.pos_y < 10:
                        Texto+="}|\n{" + str(n.celda.pos_y) + " .|"
                    else:
                        Texto+="}|\n{" + str(n.celda.pos_y) + ".|"
                    Fila= n.celda.pos_y
                
                if n.celda.id_organismo == None:
                    Texto += "``|"
                else: 
                    if n.celda.id_organismo < 10:
                        Texto += str(n.celda.id_organismo) + ".|"
                    else:
                        Texto += str(n.celda.id_organismo) + "|"
                n = n.nodo_siguiente
            contador += 1
        Texto = Texto[:len(Texto)-1]
        Texto += "}"
        ##print(Texto)
        return Texto











