from cola import cola

marvel_universe = [
    {'nombre':'natasha romanoff,', 'superheroe':'viuda negra', 'genero':'F'},
    {'nombre':'peter parker', 'superheroe':'spiderman', 'genero':'M'},
    {'nombre':'steve rogers', 'superheroe':'capitan america', 'genero':'M'},
    {'nombre':'carol danvers', 'superheroe':'capitana marvel', 'genero':'F'},
    {'nombre':'profesor hulk', 'superheroe':'hulk', 'genero':'M'},
    {'nombre':'tony stark', 'superheroe':'iron man', 'genero':'M'},
]

cola = cola()
for i in range(len(marvel_universe)):
    value = marvel_universe[i]
    cola.arrive(value)
def A(datos):
    cont=0
    while cont < datos.size():
        value = datos.move_to_end()
        if value['superheroe'] == 'capitana marvel':
            print('nombre de capitana marvel: ', value['nombre'])
        cont+=1
def B(datos):
    cont=0
    while cont < datos.size():
        value = datos.move_to_end()
        if value['genero'] == 'F':
            print('Nombre: ',value['nombre'], 'Superheroina: ',value['superheroe'])
        cont+=1       
def C(datos):
    cont=0
    while cont < datos.size():
        value = datos.move_to_end()
        if value['genero'] == 'M':
            print('Nombre: ',value['nombre'])
        cont+=1
def D(datos):
    cont =0
    cont2=0
    while cont < datos.size():
        value = datos.move_to_end()
        if value['nombre'] == 'scott lang':
            cont2 +=1
            print('nombre de superheroe: ', value['superheroe'])
        cont +=1
    if cont2 == 0:
        print('no se pudo encontrar ese personaje')
def E(datos):
    cont=0
    total = cola.size()
    print('superheroes/personajes cuyo nombre comienza con S')
    while cont < total:
        value = datos.move_to_end()
        nombre = value['nombre']
        personaje = value['superheroe']
        genero = value['genero']
        if (nombre[0] == 'S') or (personaje[0] == 'S'):
            print()
            print(f'Nombre: {nombre}, Personaje: {personaje}, Genero: {genero}') 
        cont +=1
def F(datos):
    cont = 0
    total = cola.size()
    while cont < total:
        value = datos.move_to_end()
        if value['nombre'] == 'carol danvers':
            print('personaje que interpreta carol danvers: ', value['superheroe'])
        cont +=1


print('A)')
A(cola)
print()
print('B)')
B(cola)
print()
print('C)')
C(cola)
print()
print('D)')
D(cola)
print()
print('E)')
E(cola)
print()
print('F)')
F(cola)
print()
