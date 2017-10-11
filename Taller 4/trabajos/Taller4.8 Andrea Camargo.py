#Taller(4)
#punto
from TurtleWorld import *
world = TurtleWorld()
bob = Turtle()
print bob
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# lt(bob)
# fd(bob, 100)
# for i in range(4):
# 	fd(bob, 100) 
# 	lt(bob)

# wait_for_user()
#punto5
# print "la tortuga hara un cuadrado"
# Andrea = Turtle()
# def cuadrado(t):
# 	for i in range(4):
# 		fd(t, 100)
# 		lt(t)

# cuadrado(Andrea)
#punto 6
# def cuadrado(t, l):
# 	for i in range (4):
# 		fd(t, l)
# 		lt(t)
# cuadrado(camargo, 100)	
#punto7
bob.delay=0.01
def poligono(c,l,n):
	for i in range(n):
		lt(c,360/n)
		fd(c,l)
# poligono(bob, 80, 8)
#wait_for_user()	

#punto8

def circulo(t,r):
	longitud=5
	n= 2*(3.1416)*r/longitud
	poligono(t,longitud, int(n))
	print "el numero de lados es"
	print n
circulo(bob, 90)
circulo(bob, 70)
circulo(bob, 60)
circulo(bob, 40)
circulo(bob, 20)
wait_for_user()


# Correccion:
# 1. l47: utilizar la constante math.pi
# 2. Hace falta la otra funcion circulo donde
# n es constante en vez de la longitud
