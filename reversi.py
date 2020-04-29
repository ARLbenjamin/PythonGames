#reversi

import random
import sys

def dibujarTablero(tablero):

    LINEAH = '  +---+---+---+---+---+---+---+---+'

    print('    1   2   3   4   5   6   7   8')
    print(LINEAH)
    for y in range(8):
        
        print(y+1, end=' ')
        for x in range(8):
            print('| %s' % (tablero[x][y]), end=' ')
        print('|')
       
        print(LINEAH)
    print('    1   2   3   4   5   6   7   8')
    


def reiniciarTablero(tablero):
    #dejar en blanco el tablero recibido como argumento, exepto la posicion inicial

    for x in range(8):
        for y in range(8):
            tablero[x][y] = ' '

    #piezas iniciales:
    tablero[3][3] = 'X'
    tablero[3][4] = 'O'
    tablero[4][3] = 'O'
    tablero[4][4] = 'X'


def obtenerNuevoTablero():
    #crea un tablero nuevo vacio

    tablero= []
    for i in range(8):
        tablero.append([' '] * 8)

    return tablero

def esJugadaValida(tablero, baldosa, comienzox, comienzoy):
    #comprueba si la jugada es valida

    if tablero[comienzox][comienzoy] != ' ' or not estaEnTablero(comienzox, comienzoy):
        return False

    tablero[comienzox][comienzoy] = baldosa  #coloca temporalmente la baldosa sobre el tablero

    if baldosa == 'X':
        otraBaldosa = 'O'
    else:
        otraBaldosa = 'X'

    baldosasAConvertir = []
    for direccionx, direcciony in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:

        x, y = comienzox, comienzoy
        x += direccionx   #primer paso en la direccion
        y += direcciony   #primer paso en la dirrecion

        if estaEnTablero(x, y) and tablero[x][y] == otraBaldosa:
            #se entra a este if si hay una pieza perteneciente al otro jugador al lado de nuestra pieza

            x += direccionx
            y += direcciony
            if not estaEnTablero(x,y):
                continue
            while tablero[x][y] == otraBaldosa:
                x += direccionx
                y += direcciony
                if not estaEnTablero(x, y): #sale del bucle while uan vez pase las dimenciones del tablero y continua con el bucle for
                    break
            if not estaEnTablero(x, y):
                continue
            if tablero[x][y] == baldosa:
                #registar las posiciones de las fichas que se puedenc onvertir

                while True:
                    x -= direccionx
                    y -= direcciony
                    if x == comienzox and y == comienzoy:
                        break
                    baldosasAConvertir.append([x, y])

    tablero[comienzox][comienzoy] = ' '   # restablecer el espacio vacio
    if len(baldosasAConvertir) == 0:
        return False     # si no se puede convertir ninguna baldosa al jugada no es valida
    return baldosasAConvertir


def estaEnTablero(x, y):
    # verifica si las coordenadas estan dentro del tablero
    return x >= 0 and x <=7 and y >= 0 and y <=7

def obtenerTableroConJugadasValidas(tablero, baldosa):
    # retorna un tablero, marcando con "." las juagdas validas que el jugador peude realizar

    replicaTablero = obtenerCopiaTablero(tablero)

    for x, y in obtenerJugadasValidas(replicaTablero, baldosa):
        replicaTablero[x][y] = '.'
    return replicaTablero

def obtenerJugadasValidas(tablero, baldosa):

    jugadasValidas = []

    for x in range(8):
        for y in range(8):
            if esJugadaValida(tablero, baldosa, x, y) != False:
                jugadasValidas.append([x, y])
    return jugadasValidas


def obtenerPuntajeTablero(tablero):
    #  Determinar el puntaje contando als piezas. devuelve un diccionario con clave 'X' y 'O'

    puntajex = 0
    puntajeo = 0

    for x in range(8):
        for y in range(8):
            if tablero[x][y] == 'X':
                puntajex += 1
            if tablero[x][y] == 'O':
                puntajeo += 1
    return {'X': puntajex, 'O': puntajeo}

def ingresarBaldosaJugador():
    # el jugador elije entre ser 'X' o 'O'

    baldosa = ''
    while not (baldosa == 'X' or baldosa == 'O'):
        print('¿Deseas ser X u O?')
        baldosa = input().upper()

    # El primer elementos sera la ficha que represente al jugador, la segunda sera la computadora
    if baldosa == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def quienComienza():
    # elije al azar quine comienza

    if random.randint(0, 1) == 0:
        return 'La computadora'
    else:
        return 'El jugador'

def jugarDeNuevo():
    # Retorna True si se quiere jugar de nuevo
    print('¿Quieres jugar de nuevo? (sí o no)')
    return input().lower().startswith('s')

def hacerJugada(tablero, baldosa, comienzox, comienzoy):
    # Verifica si la jugada es valida y transform las valdosas

    baldosasAConvertir = esJugadaValida(tablero, baldosa, comienzox, comienzoy)

    if baldosasAConvertir == False:
        return False
    
    tablero[comienzox][comienzoy] = baldosa
    for x, y in baldosasAConvertir:
        tablero[x][y] = baldosa
    return True
    
def obtenerCopiaTablero(tablero):
    # hace un duplicado del tablero
    replicaTablero = obtenerNuevoTablero()

    for x in range(8):
        for y in range(8):
            replicaTablero[x][y] = tablero[x][y]
    return replicaTablero

def esEsquina(x, y):
    # Determinar si al posicion es una esquina
    return (x == 0 and y == 0) or (x == 7 and y == 0) or (x == 0 and y == 7) or (x == 7 and y == 7)

def obtenerJugadaJugador(tablero, baldosaJugador):
    # toma la jugada del jugador y reorna esta como [x, y] o tambien 'salir' o 'pista'

    cifas1A8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Ingresa tu jugada, puedes ingresar salir para termianr el juego o pistas para activar/desactivar las pistas (las coordenadas se colocan juntas sin espacio entre ellas, en el orden xy).')
        jugada = input().lower()
        if jugada == 'salir':
            return 'salir'
        if jugada == 'pistas':
            return 'pistas'

        if len(jugada) == 2 and jugada[0] in cifas1A8 and jugada[1] in cifas1A8:
            x = int(jugada[0]) - 1
            y = int(jugada[1]) - 1
            if esJugadaValida(tablero, baldosaJugador, x, y) == False:
                continue
            else:
                break
        else:
            print('Esta no es una jugada válida. Ingresa la coordenada x (1-8), luego la coordenada y (1-8). ')
            print('Por ejemplo, 81 que cooresponderia a la esquina superior derecha.')
    return [x, y]

def obtenerJugadaComputadora(tablero, baldosaComputadora):
    # Determinar la jugada de la computadora
    jugadaPosible = obtenerJugadasValidas(tablero, baldosaComputadora)

    random.shuffle(jugadaPosible)

    # Siempre jugar en una esquina si esta disponible
    for x, y in jugadaPosible:
        if esEsquina(x, y):
            return [x, y]

    # Elejir entre las opciones la de mayor puntaje
    mejorPuntaje = -1
    for x, y in jugadaPosible:
        replicaTablero = obtenerCopiaTablero(tablero)
        hacerJugada(replicaTablero, baldosaComputadora, x, y)
        puntaje = obtenerPuntajeTablero(replicaTablero)
       
        if puntaje[baldosaComputadora] > mejorPuntaje:
            mejorJugada = [x, y]
            mejorPuntaje = puntaje[baldosaComputadora]
    return mejorJugada

def mostrarPuntajes(tableroPrincipal, baldosaJugador, baldosaComputadora):
    # Imprime el puntaje actual
    puntajes = obtenerPuntajeTablero(tableroPrincipal)
    print('Tienes %s puntos. La computadora tiene %s puntos.' % (puntajes[baldosaJugador], puntajes[baldosaComputadora]))


print('Bienvenido a Reversi!')

while True:
    # Reiniciar el tablero y la partida.
    tableroPrincipal = obtenerNuevoTablero()
    reiniciarTablero(tableroPrincipal)
    baldosaJugador, baldosaComputadora = ingresarBaldosaJugador()
    mostrarPistas = False
    turno = quienComienza()
    print(turno + ' comenzará.')

    while True:
        if turno == 'El jugador':
            if mostrarPistas:
                tableroConJugadasValidas = obtenerTableroConJugadasValidas(tableroPrincipal, baldosaJugador)
                dibujarTablero(tableroConJugadasValidas)
            else:
                dibujarTablero(tableroPrincipal)
            
            mostrarPuntajes(tableroPrincipal, baldosaJugador, baldosaComputadora)
            jugada = obtenerJugadaJugador(tableroPrincipal, baldosaJugador)

            if jugada == 'salir':
                print('Gracias por jugar!!')
                sys.exit()  # Termina el programa
            elif jugada == 'pistas':
                mostrarPistas = not mostrarPistas
                continue
            else:
                hacerJugada(tableroPrincipal, baldosaJugador, jugada[0], jugada[1])

            if obtenerJugadasValidas(tableroPrincipal, baldosaComputadora) == []:
                break
            else:
                turno = 'La computadora'
        else:
            # Turno de la computadora
            dibujarTablero(tableroPrincipal)
            mostrarPuntajes(tableroPrincipal, baldosaJugador, baldosaComputadora)
            input('Preciona enter para ver la jugada de la computadora.')
            x, y = obtenerJugadaComputadora(tableroPrincipal, baldosaComputadora)
            hacerJugada(tableroPrincipal, baldosaComputadora, x, y)

            if obtenerJugadasValidas(tableroPrincipal, baldosaJugador) == []:
                break
            else:
                turno = 'El jugador'

    # Mostrar el puntaje final
    dibujarTablero(tableroPrincipal)
    puntajes = obtenerPuntajeTablero(tableroPrincipal)
    print('X ha obtenido %s puntos. O ha obtenido %s puntos.' % (puntajes['X'], puntajes['O']))

    if puntajes[baldosaJugador] > puntajes[baldosaComputadora]:
        print('Has vencido a la computadora por %s !!' % (puntajes[baldosaJugador] - puntajes[baldosaComputadora]))
    elif puntajes[baldosaJugador] < puntajes[baldosaComputadora]:
        print('Has perdido. la computadora te ha vencido por %s puntos.' % (puntajes[baldosaComputadora] - puntajes[baldosaJugador]))
    else:
        print('Ha sido un empate!!')

    if not jugarDeNuevo():
        break
    





