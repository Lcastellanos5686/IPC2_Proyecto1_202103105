import LogicaCeldas


ListaCeldas = LogicaCeldas.ListaEjemplo

en_menu = True

def pedirEnter():
    prGreen('Presione una tecla para continuar \n')
    input()

def pedirOpcion():
    try:
        opcion = int(input())
        return opcion
    except:
        prRed("Por favor ingrese un numero\n")
        opcion = 0
        return opcion
    
def seCreoArchivo(Lista):
    if Lista is None:
        return False
    else:
        return True

def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))

def prRed(skk): print("\033[91m {}\033[00m" .format(skk))

def prYellow(skk): print("\033[93m {}\033[00m" .format(skk))

def pedirCoordenadas():
    coordenadas = None
    while 1:
        try:
            prYellow('Ingrese la coordenada de la fila\n')
            x = int(input())
            prYellow('Ingrese la coordenada de la columna\n')
            y = int(input())
            coordenadas = [x,y]
            return coordenadas
        except:
            prRed("Por favor ingrese un numero\n")
            opcion = 0

def noArchivo():
    prRed('Aún no se ha añadido ninguna muestra\n')
    pedirEnter()

while en_menu:
    print("--------------------------------")
    print("MENU PRINCIPAL")
    print("1. Cargar Archivo de Entrada\n2. Generar y exportar Grafica\n3. Añadir organismo\n4. Verificar si Organismo se reproduce\n5. Salir")
    print("--------------------------------\n")

    opcion = pedirOpcion()

    if opcion == 1:
        ListaCeldas = LogicaCeldas.ListaSimple()
        prYellow("Elija un archivo a continuación...\n")
        LogicaCeldas.LeerXml(ListaCeldas)
        prGreen('Muestra cargada con éxito\n')
        pedirEnter()

    elif opcion == 2:
        if seCreoArchivo(ListaCeldas):
            LogicaCeldas.GenerarGrafica(ListaCeldas)
            prGreen('Se genero una grafica con éxito\n')
            pedirEnter()
        else:
            noArchivo()

    elif opcion == 3:
        if seCreoArchivo(ListaCeldas):
            coordenadas = pedirCoordenadas()
            print('\n'+ListaCeldas.ids+'\n')
            prYellow("Elija el id del organismo\n")
            id = int(input())
            LogicaCeldas.anadirOrganismos(coordenadas[0],coordenadas[1],id,ListaCeldas)
            prGreen('Organismo añadido\n')
            pedirEnter()
        else:
            noArchivo()

    elif opcion == 4:
        if seCreoArchivo(ListaCeldas):
            cor = pedirCoordenadas()
            id = None
            id = ListaCeldas.encontrarID(cor[0],cor[1])
            
            if id is not None:
                prGreen('La celda no se pudo reprodicir a las siguientes posiciones: ')
                ListaCeldas.seReproduceLinea(cor[0], cor[1])
                ListaCeldas.ReproducirDiagonal1(cor[0],cor[1],id,ListaCeldas.seReproduceDiagonal1(cor[0], cor[1], id))
                ListaCeldas.ReproducirDiagonal2(cor[0],cor[1],id,ListaCeldas.seReproduceDiagonal2(cor[0], cor[1], id))
                ListaCeldas.ReproducirDiagonal3(cor[0],cor[1],id,ListaCeldas.seReproduceDiagonal3(cor[0], cor[1], id))
                ListaCeldas.ReproducirDiagonal4(cor[0],cor[1],id,ListaCeldas.seReproduceDiagonal4(cor[0], cor[1], id))
                pedirEnter
            else:
                prRed('La celda en estas coordenadas no está viva')
                pedirEnter()
        else:
            noArchivo()
    elif opcion == 5:
        en_menu = False

print('Gracias por usar el programa')






