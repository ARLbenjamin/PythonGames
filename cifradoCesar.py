#Cifrado Cesar

TAM_MAX_CLAVE = 26

def obtenerModo():
    while True:
        print('¿Deseas encriptar, desencriptar o decifrar por fuerza bruta un mensaje?')
        modo = input().lower()
        if modo in 'encriptar e desencriptar d bruta b'.split():
            return modo
        else:
            print('Ingresar "encriptar" o "e" o desencriptar o "d" o bruta o b')

def obtenerMensaje():
    print('Ingresa tu mensaje:')
    return input()

def obtenerClave():
    clave = 0
    while True:
        print('Ingresa el número de clave (1-%s)' % (TAM_MAX_CLAVE))
        clave = int(input())
        if (clave >= 1 and clave <= TAM_MAX_CLAVE):
            return clave

def obtenerMensajeTraducido(modo, mensaje, clave):
    if modo[0] == 'd':
        clave= -clave
   
    traduccion = ''

    for simbolo in mensaje:
        if simbolo.isalpha():
            num = ord(simbolo)
            num += clave

            if simbolo.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            
            traduccion += chr(num)
        else:
            traduccion += simbolo
    return traduccion

modo = obtenerModo()
mensaje = obtenerMensaje()
if modo[0] != 'b':
    clave = obtenerClave()

print('Tu texto traducido es:')
if modo[0] != 'b':
    print(obtenerMensajeTraducido(modo, mensaje, clave))
else:
    for clave in range(1, TAM_MAX_CLAVE + 1):
        print(clave, obtenerMensajeTraducido('desencriptar', mensaje, clave))
        