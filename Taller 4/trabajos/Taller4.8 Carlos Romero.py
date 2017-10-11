# # Ejercicio clase
# # Ejercicio clase
# # from TurtleWorld import *
# # world=TurtleWorld()
# # bob=Turtle()
# # print bob
# # fd(bob,100)
# # lt(bob)
# # fd(bob,100)
# # lt(bob)
# # fd(bob,100)
# # lt(bob)
# # fd(bob,100)
# # lt(bob)

# PROGRAMA(TALLER 4.3)23|1|1|>
from TurtleWorld import *

world = TurtleWorld()
leonardi = Turtle()
# print bob
# for i in range (4):
# 	fd(bob, 100),lt(bob)

# wait_for_user()
# punto6
# def cuadrado(t, l):
# 	for i in range (4):
# 		fd(t, l)
# 		lt(t)
# cuadrado(leonardi, 100)	
# punto7
def poligono(u,n,l):
	for i in range (n):
		lt(u,360/n)
		fd(u,l)
# poligono(leonardi,8,45)
# wait_for_user()	

# punto8


def circulo(t,r):
	leonardi.delay=0.01
	longitud=3.1416
	n=(2*(3.1416)*r/longitud)
	poligono(t,longitud,n)
	print "# de lados"
	print n
circulo(leonardi,95)
# circulo(leonardi,85)
# circulo(leonardi,75)
# circulo(leonardi,65)
# circulo(leonardi,52)
# circulo(leonardi,45)
# circulo(leonardi,35)
# circulo(leonardi,25)
# circulo(leonardi,15)
wait_for_user()


# Correccion:
# 1. El programa no funciona:
#   - l34: float en vez de int en function range
# 2. Una vez corregido, no hace un circulo:
#   - l47: argumentos longitud y n invertidos con respecto
# a la definicion de la formula
# 
# 3. Hace falta la otra version de circulo (con n constante) 
# 1. Utilizar la constante math.pi
