from TurtleWorld import *
from math import pi

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01
# maria = Turtle()
print bob


# Punto 3: Cuadrado
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)


# Punto 4
# for i in range(4):
#     fd(bob, 100)
#     lt(bob)
#
# fd(bob, 100)
# rt(maria)
# fd(bob, 100)
# fd(maria, 100)
# lt(bob)
# rt(maria)
# fd(bob, 100)
# fd(maria, 100)
# wait_for_user()


# Punto 5
# def cuadrado(t):
#     for i in range(4):
#         fd(t,100)
#         lt(t)
#
# cuadrado(bob)


# Punto 6
# def cuadrado(t, longitud):
#         for i in range(4):
#             fd(t, longitud)
#             lt(t)
#
# cuadrado(bob, 25)
# cuadrado(bob, 75)
# cuadrado(bob, 100)


# Punto 7
def poligono(t, longitud, n):
        for i in range(n):
            fd(t, longitud)
            lt(t, 360.0/n)
#
# poligono(bob, 20, 4)
# poligono(bob, 20, 6)
# poligono(bob, 20, 8)
# poligono(bob, 40, 4)

# def poligono_b(t, n, longitud = 50):
#         for i in range(n):
#             fd(t, longitud)
#             lt(t, 360.0/n)
#
# poligono_b(bob, 4, 20)
# poligono_b(bob, 6, 20)
# poligono_b(bob, 8, 20)
# poligono_b(bob, 4, 40)
# poligono_b(bob, 4)

# print 360/70, 360.0/70
# poligono(bob, 50, 6)
# wait_for_user()


# Punto 8
def circulo(t, r):
    longitud = 10
    n = 2*pi*r/longitud
    longitud = 2*pi*r/int(n)
    print n, int(n), longitud, 2*pi*r, int(n)*longitud
    poligono(t, longitud, int(n))

# circulo(bob, 80)
# wait_for_user()


# def circulo_l(t, r, longitud=10):
#     n = 2*pi*r/longitud
#     print n, int(n), round(n,0), int(round(n,0))
#     poligono(t, longitud, int(round(n,0)))

# circulo_l(bob, 100, 20)
# circulo_l(bob, 100, 15)
# circulo_l(bob, 100, 10)
# circulo_l(bob, 100, 5)
# circulo_l(bob, 100)

# def circulo_n(t, r, n=30):
#     longitud = 2*pi*r/n
#     print longitud, int(longitud), round(longitud,0), int(round(longitud,0))
#     poligono(t, longitud, n)

# circulo_n(bob, 100, 3)
# circulo_n(bob, 100)

# The solution from the book
# def circulo(t, r):
#     perimetro = 2*pi*r
#     # n = perimetro / longitud
#     # n = int(round(n,0))
#     n = int(perimetro / 10) + 1      # => implicitly longitud is 10
#     longitud = perimetro / n
#     print perimetro/10, n, longitud, perimetro, n*longitud
#     poligono(t, longitud, n)
#
# circulo(bob, 40)



# PROYECTO CORTE 2
# Version 1: naive and incorrect => el radio del circulo del arco es incorrecto (cambia)
# def poligono(t, longitud, n, angulo):
#         for i in range(n):
#             fd(t, longitud)
#             lt(t, float(angulo)/n)
#
#
# def arco(t, r, angulo):
#     longitud = 10
#     # perimetro = 2*pi*r
#     n = int(2*pi*r/longitud) + 1
#     # arco = r*angulo*2*pi/360
#     # n_arco = int (arco/longitud) + 1
#     poligono(t, longitud, n, angulo)    # => using the same n is wrong
#
#
# Version 2: naive but correct
def poligono(t, longitud, n, angulo):
    n_arco = int(angulo/360.0*n)
    for i in range(n_arco):
        fd(t, longitud)
        lt(t, 360.0/n)

def arco(t, r, angulo):
    longitud = 10
    n = 2*pi*r/longitud
    # poligono(t, longitud, int(round(n,0)))
    poligono(t, longitud, int(n)+1, angulo)

# circulo(bob, 100)
#
# Version 3
# def arco(t, r, angulo):
#     longitud = 10
#     perimetro = 2*pi*r
#     n = 2*pi*r/longitud
#     arco = r*angulo*2*pi/360
#     n_arco = int (arco/longitud) + 1
#     for i in range(n_arco):
#         fd(t, longitud)
#         lt(t, angulo/n_arco)

arco(bob, 50, 90)
arco(bob, 50, 180)
# arco(bob, 100, 45)
# arco(bob, 30, 90)
# arco(bob, 15, 180)
wait_for_user()

