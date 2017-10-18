# Punto 1a
def chequear_fermat(a, b, c, n):
    if a**n + b**n == c**n:
        print 'Oye, Fermat estaba equivocado'
    else:
        print 'No, la igualdad no funciona.'
        print '%d^%d + %d^%d != %d^%d' % (a, n, b, n, c, n)
        print '%d != %d' %(a**n+b**n, c**n)


# Punto 1b
def obtener_valores():
    """Obtener 4 valores del usuario"""
    print 'a^n + b^n = c^n'
    a = raw_input('Valor de a: ')
    b = raw_input('Valor de b: ')
    c = raw_input('Valor de c: ')
    d = raw_input('Valor de n: ')
    chequear_fermat(int(a), int(b), int(c), int(d))

# a, b, c, n = 1, 2, 4, 5
# chequear_fermat(a, b, c, n)
# obtener_valores()


# Punto 1c
def chequear_fermat(a, b, c, n):
    if n <= 2:
        print "n tiene que ser mas grande que 2: n = %d" % n
        return
    # if n > 2: is also posible
    if a**n + b**n == c**n:
        print 'Oye, Fermat estaba equivocado'
    else:
        print 'No, la igualdad no funciona.'
        print '%d^%d + %d^%d != %d^%d' % (a, n, b, n, c, n)
        print '%d != %d' %(a**n+b**n, c**n)

# obtener_valores()



# Punto 2.a
def es_triangulo_a(a, b, c):
    """Determina si tres longitudes forman un triangulo"""
    if (a > c + b) or (b > a + c) or (c > a + b):
        print 'No'
    else:
        print 'Si'

# es_triangulo_a(1, 2, 4)
# es_triangulo_a(1, 2.5, 3)
# es_triangulo_a(5, 2, 4)
# es_triangulo_a(1, 2, 3)


# Punto 2.b
def es_triangulo_b(a, b, c):
    """Determina si tres longitudes forman un triangulo"""
    if (a > c + b) or (b > a + c) or (c > a + b):
        print 'No'
    else:
        if (a == c + b) or (b == a + c) or (c == a + b):
            print 'Si, pero es degenerado'#,': ', c, '=', a+b
        else:
            print 'Si'

# es_triangulo_b(1, 2, 4)
# es_triangulo_b(1, 2.5, 3)
# es_triangulo_b(5, 2, 4)
# es_triangulo_b(1, 2, 3)


# Punto 2.c
def es_triangulo_c(a, b, c):
    """Determina si tres longitudes forman un triangulo"""
    if (a > c + b) or (b > a + c) or (c > a + b):
        print 'No'
    else:
        # Careful: with or, the degenerated case is never 
        if (a != c + b) and (b != a + c) and (c != a + b): # with 
            print 'Si: '
        else:
            print 'Si, pero es degenerado'#,': ', c, '=', a+b

# es_triangulo_c(1, 2, 4)
# es_triangulo_c(1, 2.5, 3)
# es_triangulo_c(5, 2, 4)
# es_triangulo_c(1, 2, 3)

def obtener_valor():
    print 'Valores de los lados a, b y c del triangulo'
    a = raw_input('Valor de a: ')
    b = raw_input('Valor de b: ')
    c = raw_input('Valor de c: ')
    es_triangulo_c(int(a), int(b), int(c))
    
# obtener_valor()


# Punto 3a
# from random import randint
#
# print 'Hola, Cual es tu nombre?'
# nombre = 'Paloma'
# print nombre
# # nombre = raw_input('Hola, Cual es tu nombre?\n')
# print 'Bueno %s, estoy pensando en un numero de 1 a 20.' % nombre
# numero = randint(1, 20)
#
# for i in range(4):
#     print 'Adivina cual es.'
#     intento = randint(1, 20)
#     print intento
#     # intento = int(raw_input('Adivina cual es.\n'))
#     if numero != intento:
#         print 'No. Eso era el intento %d' % (i+1)
#     else:
#         print 'Buen trabajo, %s. Encontraste mi numero en %d intento(s)' % (nombre, i+1)
#         break
#
# if numero != intento:
#     print 'El numero que tenia en la mente era el %d' % numero


# Punto 3b
from random import randint

# print 'Hola, Cual es tu nombre?'
# nombre = 'Paloma'
# print nombre
nombre = raw_input('Hola, Cual es tu nombre?\n')
print 'Bueno %s, estoy pensando en un numero de 1 a 20.' % nombre
numero = randint(1, 20)

for i in range(4):
    # print 'Adivina cual es.'
    # intento = randint(1, 20)
    # print intento
    intento = int(raw_input('Adivina cual es.\n'))
    if numero < intento:
        print 'Su numero mas grande.'
    elif numero > intento:
        print 'Su numero mas pequeno.'
    else:
        break

if numero == intento:
    print 'Buen trabajo, %s. Encontraste mi numero en %d intento(s)' % (nombre, i+1)
else:
    print 'El numero que tenia en la mente era el %d' % numero 

