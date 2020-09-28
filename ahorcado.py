import random
IMAGENES_AHORCADO = ['''

  +---+
  |   |
      |
      |
      |
      | 
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      | 
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      | 
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      | 
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
      |
      | 
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 /    |
      | 
=========''', '''

  +---+
  |   |
  O   |
 /|\  |
 / \  |
      | 
=========''']
palabras = {
    'Colores': 'rojo naranja amarillo verde azul añil violeta blanco negro marron'.split(),
    'Formas': 'cuadrado triangulo rectangulo circulo elipse rombo trapezoide chevron pentagono hexagono heptagono octogono'.split(),
    'Frutas': 'manzana naranja limon lima pera sandia uva pomelo cereza banana melon mango fresa tomate mora ciruela'.split(),
    'Animales': 'murcielago oso castor gato pantera cangrejo ciervo perro burro pato aguila pez rana cabra sanguijuela leon lagarto mono alce raton nutria buho panda piton conejo rata tiburon oveja mofeta calamar tigre pavo tortuga comadreja ballena lobo wombat cebra'.split()
}

def palabraAlAzar(bancoPalabras):
    clavePalabras= random.choice(list(bancoPalabras.keys()))
    indicePalabras= random.randint(0, len(bancoPalabras[clavePalabras])-1)
    
    return [bancoPalabras[clavePalabras][indicePalabras], clavePalabras]

def mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta, categoriaPalabra):
    print(IMAGENES_AHORCADO[len(letrasIncorrectas)])
    print()
    print('La categoria de la paltabra secreta es '+ categoriaPalabra)
    print()
    print('letras Incorrectas:', end=' ')
    for letra in letrasIncorrectas:
        print(letra, end= ' ')
    print() 

    espaciosVacios= '_' * len(palabraSecreta)

    for i in range(len(palabraSecreta)):

        if palabraSecreta[i] in letrasCorrectas:
            espaciosVacios= espaciosVacios[:i] + palabraSecreta[i] + espaciosVacios[i+1:]

    for letra in espaciosVacios:
        print(letra, end=' ')
    print()

def obtenerIntento(letrasProbadas):

    while True:
        print('Adivina una letra.')
        intento = input()
        intento = intento.lower()
        if len(intento) != 1:
            print('Por favor, introduce una letra.')
        elif intento in letrasProbadas:
            print('Ya has probado esa letra. Elige otra')
        elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
            print('Por favor ingresa una LETRA!!!')
        else:
            return intento

def jugarDeNuevo():
    print('¿Quieres jugar de nuevo? (si o no)')
    return input().lower().startswith('s')

print('A H O R C A D O')
letrasIncorrectas = ''
letrasCorrectas = ''
palabraSecreta, categoriaPalabra= palabraAlAzar(palabras)
juegoTerminado = False

while True:
    mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta, categoriaPalabra)
   
    intento = obtenerIntento(letrasIncorrectas + letrasCorrectas)

    if intento in palabraSecreta:
        letrasCorrectas = letrasCorrectas + intento

        encontradoTodasLasLetras = True
        for i in range(len(palabraSecreta)):
             if palabraSecreta[i] not in letrasCorrectas:
                 encontradoTodasLasLetras = False
                 break
    
        if encontradoTodasLasLetras == True:
            print('Si!! La palabra secreta es "' + palabraSecreta + '"! has ganado!')
            juegoTerminado= True
    else:
        letrasIncorrectas = letrasIncorrectas + intento

        if len(letrasIncorrectas) == len(IMAGENES_AHORCADO) - 1:
            mostrarTablero(IMAGENES_AHORCADO, letrasIncorrectas, letrasCorrectas, palabraSecreta, categoriaPalabra)
            print('Te has quedado sin intentos!')
            print('Despues de ' + str(len(letrasIncorrectas)) + ' intentos fallidos y ' + str(len(letrasCorrectas)) + ' aciertos, la palabra era "' + palabraSecreta + '" ')
            juegoTerminado = True

    if juegoTerminado:
        if jugarDeNuevo():
            letrasIncorrectas = ''
            letrasCorrectas = ''
            juegoTerminado = False
            palabraSecreta, categoriaPalabra = palabraAlAzar(palabras)
        else:
            break


    



