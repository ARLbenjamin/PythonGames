#Sonar

import random
import sys

def dibujarTablero(tablero):
    # Dibuja la estructura de datos del tablero

    lineah = '    ' # espacio inicial para los numeros a lo largo del lado izquierdo del tablero

    for i in range(1, 6):
        lineah += (' ' * 9) + str(i)

    #imprimir los numeros a lo largo del borde superior
    print(lineah)
    print('   ' + ('0123456789' * 6))
    print()

    #imprimir cada una de las 15 filas
    for i in range(15):
        # los numeros de una sola cifra deben ser precedidos por un espacio extra

        if i < 10:
            espacioExtra = ' '
        else:
            espacioExtra = ''
        print('%s %s %s' % (espacioExtra, i, obtenerFila(tablero, i)))

    #imprimir los numeros a lo largo del borde inferior
    print()
    print('    ' + ('0123456789' * 6))
    print(lineah)

def obtenerFila(tablero, fila):
    #Devuelve una cadena con la eztructura de un tablero para una fila determinada.

    filaTablero = ''
    for i in range(60):
        filaTablero += tablero[i][fila]
    return filaTablero

def obtenerNuevoTablero():
    # Crear una nueva estructura de datos para un tablero de 60x15.
    tablero = []
    for x in range(60): # la lista principal es una lista de 60 listas
        tablero.append([])
        for y in range(15): #cada lista en la lista principal tiene 15 cadenas en un solo caracter
            # se usaran diferentes caracteres para el oceano para facilitar su lectura

            if random.randint(0, 1) == 0:
                tablero[x].append('~')
            else:
                tablero[x].append('`')
    return tablero

def obtenerCofresAleatorios(numCofres):
    #crear una lista de estructuras de datos cofre(lista de dos items con coordenadas x, y)

    cofres = []
    for i in range(numCofres):
        cofres.append([random.randint(0, 59), random.randint(0, 14)])
    return cofres

def esMovidaValida(x, y):
    #regresa True si las coordenadas pertenecen al tablero, de locontrario False.

    return x >= 0 and x <= 59 and y >= 0 and y <= 14

def realizarMovida(tablero, cofres, x, y):
    #Cambiar la estructura de datos del tablero agregando un caracter de dsipositivo sonar.
    #Elimina los cofres de la lista de cofres a medida que son encontrados.
    
    if not esMovidaValida(x, y):
        return False

    menorDistancia = 100 #Cualquier cofre estara a una distancia menor que 100

    for cx, cy in cofres:
        if abs(cx - x) > abs(cy - y):
            distancia = abs(cx - x)
        else:
            distancia = abs(cy - y)

        if distancia < menorDistancia: #queremos el cofre mas cercano
            menorDistancia = distancia

    if menorDistancia == 0:
        # xy esta directamente sobre un cofre!
        cofres.remove([x, y])
        return 'Has encontrado un cofre del tesoro hundido!'
    else:
        if menorDistancia < 11:
            tablero[x][y] = str(menorDistancia)
            return 'Tesoro detectado a una distancia %s del dispositivo sonar.' % (menorDistancia)

        else:
            tablero[x][y] = '0'
            return 'El sonar no ha detectado nada. Todos los cofres estan fuera del alcance del dispositivo.'

def ingresarMovidaJugador():
    #Permite al jugar teclear su movida. 

    print('¿Donde quieres dejar caer el siguinete dispositivo sonar? (0-59)(0-14) (o teclear salir)')

    while True:
        movida = input()
        if movida.lower() == 'salir':
            print('Gracias por jugar!')
            sys.exit()

        movida = movida.split()
        if len(movida) == 2 and movida[0].isdigit() and movida[1].isdigit() and esMovidaValida(int(movida[0]), int(movida[1])):
            return [int(movida[0]), int(movida[1])]
        print('Ingresa un numero de 0 a 59, un espacio, y luego un numero de 0 a 14.')

def jugarDeNuevo():
    #Esta funcion dvuelve True si el jugador quiere jugar de nuevo de lo contrario devuelve False.
    print('¿Quieres jugar de nuevo? (si o no)')
    return input().lower().startswith('s')

def mostrarInstrucciones():
    print('''Instrucciones: 
    Eres el capitán de Simón, un buque cazador de tesoros. Tu misión actual
    es encontrar los tres cofres con tesoros perdidos que se hallan ocultos en
    la parte del océano en que te encuentras y recogerlos.

    Para jugar, ingresa las coordenadas del punto del océano en que quieres
    colocar un dispositivo sonar. El sonar puede detectar cuál es la distancia al cofre más cercano.
    Por ejemplo, la d abajo indica dónde se ha colocado el dispositivo, y los
    números 2 representan los sitios a una distancia 2 del dispositivo. Los
    números 4 representan los sitios a una distancia 4 del dispositivo.

    444444444
    4       4
    4 22222 4
    4 2   2 4
    4 2 d 2 4
    4 2   2 4
    4 22222 4
    4       4
    444444444
    Pulsa enter para continuar...''')
    input()

    print('''Por ejemplo, qui hay un cofre del tesoro (la c) ubicado a una distancia
             2 del dispositivo sonar (la d):

             22222
             c   2
             2 d 2
             2   2
             22222

             El punto donde el dispositivo fue colocado se indicará con una d.

             Los cofres del tesoro no se mueven. Los dispositivos sonar pueden detectar
             cofres hasta una distancia 9. Si todos los cofres están fuera del alcance,
            el punto se indicará con un O.

            Si un dispositivo es colocado directamente sobre un cofre del tesoro, has
            descubierto la ubicación del cofre, y este será recogido. El dispositivo
            sonar permanecerá allí.

            Cuando recojas un cofre, todos los dispositivos sonar se actualizarán para
            localizar el próximo cofre hundido más cercano.
            Pulsa enter para continuar...''')
    input()
    print()


print('S O N A R!')
print()
print('¿Te gustaria ver las instrucciones? (si/no)')
if input().lower().startswith('s'):
    mostrarInstrucciones()

while True:
    #configuracion del juego
    dispositivosSonar = 16
    elTablero = obtenerNuevoTablero()
    losCofres = obtenerCofresAleatorios(3)
    dibujarTablero(elTablero)
    movidasPrevias = []

    while dispositivosSonar > 0:
        #comienzo de un turno:

        #mostrar el estado de los dispositivos sonar / cofres
        if dispositivosSonar > 1: 
            extraSsonar = 's'
        else:
            extraSonar = ''
        if len(losCofres) > 1:
            extraScofre = 's'
        else:
            extraScofre = ''
        print('Aun tienes %s dispositivo%s sonar. Falta encontrar %s cofre%s.' % (dispositivosSonar, extraSsonar, len(losCofres), extraScofre))

        x, y = ingresarMovidaJugador()
        movidasPrevias.append([x, y]) #registramos todas las movidas para actualizar los dispositivos sonar

        resultadoMovida = realizarMovida(elTablero, losCofres, x, y)
        if resultadoMovida == False:
            continue
        else:
            if resultadoMovida == 'Has encontrado un cofre del tesoro hundido!':
                # actualizar todos los dispositivos sonar presentes en el mapa

                for x, y in movidasPrevias:
                    realizarMovida(elTablero, losCofres, x, y)
            dibujarTablero(elTablero)

            print(resultadoMovida)

        if len(losCofres) == 0:
            print('Has encontrado todos los cofres del tesoro! Felicitacones y buena partida!')
            break

        dispositivosSonar -= 1

    if dispositivosSonar == 0:
        print('Nos hemos quedado sin dispositivos snar! Ahora tenemos que dar la vuelta y dirigirnos')
        print('de regreso a casa dejando tesoros en el mar!')
        print()
        print('J U E G O     T E R M I N A D O !!')
        print()
        print('   Los cofres restantes estaban aqui:')
        for x, y in losCofres:
            print('   %s, %s' % (x, y))

    if not jugarDeNuevo():
        sys.exit()
