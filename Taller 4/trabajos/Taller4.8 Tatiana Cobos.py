# #Punto 2
# from TurtleWorld import *
# world=TurtleWorld()
# bob=Turtle()
# print bob
# fd(bob, 100)
# lt(bob)
# fd(bob,100)
# lt(bob)
# fd(bob,100)
# fd(bob,100)
# fd(bob,100)
# lt(bob)

# #Punto 4
# from TurtleWorld import *
# world=TurtleWorld()
# bob=Turtle()
# print bob
# for i in range(4)
# fd(bob, 100)
# lt (bob)

#Punto 5
from TurtleWorld import *
world=TurtleWorld()
Joe=Turtle()
print Joe

# def cuadrado (t):
# 	for i in range(4):
# 		fd(t, 100)
# 		lt(t)

# print cuadrado(Joe)

#Punto 6
# def cuadrado (t, longitud):
# 	for i in range(4):
# 		fd(t,longitud)
# 		lt(t)

# print cuadrado(Joe,160)

# def cuadrado (t, longitud):
# 	for i in range(4):
# 		fd(t,longitud)
# 		lt(t)

# print cuadrado(Joe,10)

#Punto 7
# def poligono (t, longitud, n):
# 	for i in range(n):
# 		fd(t,longitud)
# 		lt(t,(360/n))

# print poligono (Joe,50,5)

#Punto 8
Joe.delay=0.001
def circulo (t,r):
    longitud= 3.14
    n = (2 * 3.14 * r) / longitud
    for i in range (int(n)):
        fd(t,r)
        lt(t,(360/n))

print circulo (Joe,15)

def circulo (t,r):
	n=40
	longitud=(2*3.1415*r)/n
	for i in range (int(n)):
		fd(t,r)
		lt(t,360/n)

# print circulo (Joe,15)

circulo(Joe,17)
# circulo(Joe,20)
# circulo(Joe,22)

# Correccion:
# 1. Utilizar la constante math.pi
# 2. La funcion circulo tenia que llamar a la  
# funcion poligono



