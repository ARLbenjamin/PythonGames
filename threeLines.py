# juego triqui

import random

def dibujarTablero(tablero):
    #Esta funcion dibuja el tablero
    #Recibe una lista con las posiciones de las jugadas, sin tener en cuenta el indice 0

    print(' ')
    print(' '+ tablero[7]+' | '+ tablero[8]+' | '+tablero[9])
    print('-----------')
    print(' '+ tablero[4]+' | '+ tablero[5]+' | '+tablero[6])
    print('-----------')
    print(' '+ tablero[1]+' | '+ tablero[2]+' | '+tablero[3])
    print(' ')

def ingresarLetraJugador():
    #seleccionar que letra quiere ser 
    letra = ''

    while not (letra == 'X' or letra == 'O'):
        print('Desea ser X u O ?')
        letra = input().upper()

    #El primer elementos era la letra del jugador, el segundo al letra de la computadora

    if letra == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def quienComienza():
    
    #Elije al azar el jugador que comenzara

    if random.randint(0, 1) == 0:
        
        return 'La computadora'
    else:
        return 'El jugador'

def jugarDeNuevo():
    #definira si el jugador quiere jugar de nuevo (true) o no (false)
   
   print('¿Desesas volver a jugar? (si/no)' )
   return input().lower().startswith('s')

def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra

def esGanador(ta, le):
    #Comprobamos si el jugador ha ganado

    return ((ta[7] == le and ta[8] == le and ta[9] == le) or
    (ta[4] == le and ta[5] == le and ta[6] == le) or 
    (ta[1] == le and ta[2] == le and ta[3] == le) or
    (ta[7] == le and ta[4] == le and ta[1] == le) or
    (ta[8] == le and ta[5] == le and ta[2] == le) or
    (ta[9] == le and ta[6] == le and ta[3] == le) or 
    (ta[7] == le and ta[5] == le and ta[3] == le) or 
    (ta[9] == le and ta[5] == le and ta[1] == le))

def duplicarTablero(tablero):
    # Duplica la lista del tablero y returna el duplicado
    duptablero= []

    for i in tablero:
        duptablero.append(i)
    return duptablero

def espacioLibre(tablero, jugada):
    # regresa true si aun hay espacio para efectuar una jugada

    return tablero[jugada] == ' '

def jugadaJugador(tablero):
    #permite que el jugador ingrese su jugada
    jugada= ' '

    while jugada not in '1 2 3 4 5 6 7 8 9'.split() or not espacioLibre(tablero, int(jugada)):
        print('¿Cual es tu próxima jugada? (1-9)')
        jugada = input()
    return int(jugada)

def elejirAzarLista(tablero, listaJugada):
    #Returna una jugada valida en el tablero
    #Avisa cuando se a tratado de realzar una jugada no valida

    jugadasPosibles = []
    for i in listaJugada:
        if espacioLibre(tablero, i):
            jugadasPosibles.append(i)

    if len(jugadasPosibles) != 0:
        return random.choice(jugadasPosibles)
    else:
        return None

def obtenerJugadaComputadora(tablero, letraComputadora):
    #Dado un tablero y la letra de al computadora determinar que jugada efectuar

    if letraComputadora == 'X':
        letraJugador = 'O'
    else:
        letraJugador = 'X'

    #Primero verificar si podemos aganr en la siguiente jugada
    for i in range(1, 10):
        copia = duplicarTablero(tablero) 

        if espacioLibre(copia, i):
            hacerJugada(copia, letraComputadora, i)

            if esGanador(copia, letraComputadora):
                return i

    #Verificar si el jugador podria ganar en la proxima jugada y lo bloquea
    for i in range(1, 10):
        copia = duplicarTablero(tablero)
        if espacioLibre(copia, i):
            hacerJugada(copia, letraJugador, i)
            if esGanador(copia, letraJugador):
                return i

    jugada = elejirAzarLista(tablero, [1, 3, 7, 9])
    if jugada != None:
        return jugada
    
    #Intentarocupar el centro si las esquinas no estan libres
    if espacioLibre(tablero, 5):
        return 5

    #Ocupar alguno de lso lados.
    
    return elejirAzarLista(tablero, [2, 4, 6, 8])

def tableroCompleto(tablero):
    #verifica si todos los espacios del tablero fueron ocupados
    for i in range(1, 10):
        if espacioLibre(tablero, i):
            return False
    return True

print('Bienvenido a Three Lines')

while True:
    #se plantea el ciclo apra reiniciar el juego
    elTablero = [' ']*10
    letraJugador, letraComputadora = ingresarLetraJugador()
    turno = quienComienza()
    print(turno + ' ira primero.')
    juegoEnCurso = True

    while juegoEnCurso:
        if turno == 'El jugador':
            #turno del jugador
            dibujarTablero(elTablero)
            jugada = jugadaJugador(elTablero)
            hacerJugada(elTablero, letraJugador, jugada)
            
            if esGanador(elTablero, letraJugador):
                dibujarTablero(elTablero)
                print('Felicidades, has ganado!')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('Es un empate!')
                    break
                else:
                    turno = 'La computadora'

        else:
            if turno == 'La computadora':
                jugada = obtenerJugadaComputadora(elTablero, letraComputadora)
                hacerJugada(elTablero, letraComputadora, jugada)

            if esGanador(elTablero, letraComputadora):
                dibujarTablero(elTablero)
                print('La computadora te ha vencido!.')
                juegoEnCurso = False
            else:
                if tableroCompleto(elTablero):
                    dibujarTablero(elTablero)
                    print('Es un empate!!')
                    break
                else:
                    turno = 'El jugador'
    if not jugarDeNuevo():
        break
    
        


    
    
    