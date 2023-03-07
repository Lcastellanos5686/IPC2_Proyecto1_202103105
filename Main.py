import LogicaCeldas

ListaCeldas = LogicaCeldas.ListaEjemplo

en_menu = True

def pedirEnter():
    input('Presione una tecla para continuar \n')

def pedirOpcion():
    try:
        opcion = int(input())
        return opcion
    except:
        print("Por favor ingrese un numero\n")
        opcion = 0
        return opcion
    
def seCreoArchivo(Lista):
    if Lista is None:
        return False
    else:
        return True

def pedirCoordenadas():
    coordenadas = None
    while 1:
        try:
            x = int(input('Ingrese la coordenada de la fila\n'))
            y = int(input('Ingrese la coordenada de la columna\n'))
            coordenadas = [x,y]
            return coordenadas
        except:
            print("Por favor ingrese un numero\n")
            opcion = 0

def noArchivo():
    print('Aún no se ha añadido ninguna muestra\n')
    pedirEnter()

while en_menu:
    print("--------------------------------")
    print("MENU PRINCIPAL")
    print("1. Cargar Archivo de Entrada\n2. Generar y exportar Grafica\n3. Añadir organismo\n4. Verificar si Organismo se reproduce\n5. Salir")
    print("--------------------------------\n")

    opcion = pedirOpcion()

    if opcion == 1:
        ListaCeldas = LogicaCeldas.ListaSimple()
        LogicaCeldas.LeerXml(ListaCeldas)
        print('Muestra cargada con éxito\n')
        pedirEnter()

    elif opcion == 2:
        if seCreoArchivo(ListaCeldas):
            LogicaCeldas.GenerarGrafica(ListaCeldas)
            print('Se genero una grafica con éxito\n')
            pedirEnter()
        else:
            noArchivo()

    elif opcion == 3:
        if seCreoArchivo(ListaCeldas):
            coordenadas = pedirCoordenadas()
            id = int(input("Elija el organismo"))
            LogicaCeldas.anadirOrganismos(coordenadas[0],coordenadas[1],id,ListaCeldas) ##CAMBIAR EL ID 1 EN EL PEDIRCOORDENADAS!!!!!!
        else:
            noArchivo()

    elif opcion == 4:
        if seCreoArchivo(ListaCeldas):
            cor = pedirCoordenadas()
            id = None
            id = ListaCeldas.encontrarID(cor[0],cor[1])
            
            if id is not None:
                ListaCeldas.seReproduceLinea(cor[0], cor[1])
                ListaCeldas.ReproducirDiagonal1(cor[0],cor[1],id,ListaCeldas.seReproduceDiagonal1(cor[0], cor[1], id))
                ListaCeldas.ReproducirDiagonal2(cor[0],cor[1],id,ListaCeldas.seReproduceDiagonal2(cor[0], cor[1], id))
                ListaCeldas.ReproducirDiagonal3(cor[0],cor[1],id,ListaCeldas.seReproduceDiagonal3(cor[0], cor[1], id))
                ListaCeldas.ReproducirDiagonal4(cor[0],cor[1],id,ListaCeldas.seReproduceDiagonal4(cor[0], cor[1], id))

            else:
                print('La celda en estas coordenadas no está viva')
                pedirEnter()
        else:
            noArchivo()
    elif opcion == 5:
        en_menu == 'False'

print('Gracias por usar el programa')





