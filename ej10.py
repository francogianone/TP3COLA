from cola import cola
from pila import pila

notif = [
    {'hora':'8:32', 'aplicacion:': 'instagram', 'mensaje:': 'notifiacion de instagram'},
    {'hora:':'15:17', 'aplicacion:': 'twitter', 'mensaje:': 'notifiacion de twitter'},
    {'hora:':'13:40', 'aplicacion:': 'instagram', 'mensaje:': 'notifiacion de  instagram desde python'},
    {'hora:':'9:53', 'aplicacion:': 'youtube', 'mensaje:': 'notifiacion de youtube'},
    {'hora:':'11:58', 'aplicacion:': 'facebook', 'mensaje:': 'notifiacion de facebook'},
]    

cola=cola()

for i in range(len(notif)):
    cola.arrive(notif[i])
def sacar_facebook(notif):
    aux =cola()
    cont =0
    while cont < notif.size():
        value = notif.move_to_end()
        if value['aplicacion:'] != 'facebook':
            aux.arrive(value)
        cont +=1
    return aux

def notifiTwitter(datos):  
    cola_twitter = cola()
    cont = 0
    tot = datos.size()
    while cont < tot:
        value = datos.move_to_end()
        app = value['aplicacion:']
        msj = value['mensaje:']
        if (app == 'twitter') and ('python' in msj):
            cola_twitter.arrive(value)
        cont +=1

    print('notificaciones de twitter que tienen la palabra python en el mensaje')
    cAux = 0
    while cAux < cola_twitter.size():
        aux = cola_twitter.move_to_end()
        print(aux['mensaje:'])
        print(aux['hora:'])
        print(aux['aplicacion:'])
        cAux += 1
        
def pila_temporal(notificaciones):
    pila = pila()
    cola_temporal = cola()
    cont = 0
    while cont < notificaciones.size():
        data = notificaciones.move_to_end()
        hora = data['hora:']
        if (hora >= '11:43') and (hora <= '15:57'):         
            pila.push(data)
        cont +=1
    cantidadNotif = pila.size()
    print(f'cantidad de notificaciones: {cantidadNotif}')

cola_sacando_facebook = sacar_facebook(cola)
cont = 0
while cont < cola_sacando_facebook.size() > 0:
    value = cola_sacando_facebook.move_to_end()
    print(value)
    cont +=1

notifiTwitter(cola)
pila_temporal(cola)