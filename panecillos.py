import random
def obtenerNumeroSecreto(digitosNum):
    #retorna el numero secreto, el cual se crea al alzar

    numeros = list(range(10))
    random.shuffle(numeros)
    numSecreto = ''
    for i in range(digitosNum):
        numSecreto += str(numeros[i])
    return numSecreto

def obtenerPista(conjetura, numSecreto):
    #regresa una palabra clave a manera de pista

    if conjetura == numSecreto:
        return 'Lo has adivinado!!'

    pista = []

    for i in range(len(conjetura)):
        if conjetura[i] == numSecreto[i]:
            pista.append('Fermi')
        elif conjetura[i] in numSecreto:
            pista.append('Pico')
    if len(pista) == 0:
        return 'Panecillos'

    pista.sort()
    return ' '.join(pista)

def esSoloDigitos(num):
    #verifica si lo que se introduce es un numero

    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def jugarDeNuevo():
    #verificar si el jugador desea jugar de nuevo

    print('Deseas volver a jugar? (sí o no)')
    return input().lower().startswith('s')

digitosNum = 3
MaxIntentos = 10
print(' ')
print('Estoy pensando en un número de %s digitos. Intenta adivinar cuál es' % (digitosNum))
print('Aqui hay algunas pistas: ')
print('Cuando digo:     Eso significa:')
print('  Pico           Un digito es correcto pero en la posición incorrecta.')
print('  Fermi          Un digito es correcto y en la posición correcta.')
print('  Panecillos     Ningún dígito es correcto.')
print(' ')

while True:
    numSecreto = obtenerNumeroSecreto(digitosNum)
    print('He pensado un número. Tienes %s intentos para adivinarlo.' % (MaxIntentos))

    numIntentos = 1
    while numIntentos <= MaxIntentos:
        conjetura = ''
        while len(conjetura) != digitosNum or not esSoloDigitos(conjetura):
            print('Conjetura #%s (): ' % (numIntentos))
            conjetura = input()
            print(' ')
            if len(conjetura) != digitosNum or not esSoloDigitos(conjetura):
                print('Ingresó un valor inválido, por favor intente de nuevo.')

        pistas = obtenerPista(conjetura, numSecreto)
        print(pistas)
        print(' ')
        numIntentos += 1

        if conjetura == numSecreto:
            break
        if numIntentos > MaxIntentos:
            print('Te has quedado sin intetos. La respuesta era %s,' % (numSecreto))

    if not jugarDeNuevo():
        break


