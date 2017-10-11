from TurtleWorld import*
world=TurtleWorld()
dona=Turtle()
print dona


dona.delay=0.001
#print 'ingresa el nombre de la tortuga, el numero de lados del poligono que desea dibujar y por ultimo el angulo de inclincion al cual la tortuga debe dibujar'
# def poligono(t,l,n):
# 	for i in range(l):
# 		lt(t,360/l)
# 		fd(t,n)
# poligono (dona,40,15)
# wait_for_user()

#punto 8
#print 'ingresa el nombre de la tortuga y el numero de lados correspondietnes para que la tortuga dibuje un circulo perfecto'
def circulo (t,r):
    longitud=3.1416
    n = (2* 3.1416*r)/longitud
    for i in range (int(n)):
        fd(t,r)
        lt(t,360/n)

print circulo (dona,15)
# wait_for_user()

print 'ingresa el nombre de la tortuga y el radio correspondiente para que la tortuga dibuje un circulo'

def circulo (t,r):
	n=45
	longitud=(2* 3.1416*r)/n
	for i in range (int(n)):
		fd(t,r)
		lt(t,360/n)

print circulo (dona,15)
wait_for_user()


# Correccion:
# 1. Utilizar la constante math.pi
# 2. La funcion circulo tenia que llamar a la  
# funcion poligono
