from TurtleWorld import *
world=TurtleWorld()
carlota=Turtle()
print carlota
carlota.delay=0.001
# def poligono(u,n,l):
# 	for i in range(n):
# 		lt(u,360/n)
# 		fd(u,l)
# poligono(carlota,3,150)



# def circulo(u,n,l):
# 	for i in range(n):
# 		lt(u,360/n)
# 		fd(u,360/l)
# circulo (carlota,2*(3,1416)50)
# wait_for_user_()

# carlota.delay=0.001
def circulo (t,r):
    longitud=3.1416
    n=(2 * 3.14 * r)/ longitud
    for i in range(int(n)):
        fd(t,r)
        lt(t,(360/n))
print circulo (carlota,15)
# wait_for_user_()


def circulo (t,r):
 	n=45
 	longitud=(2*3.1416*r)/n
 	for i in range (int(n)):
 		fd(t,r)
 		lt(t,360/n)
print circulo (carlota,10)


# circulo (carlota,20)
# circulo (carlota,30)
# circulo (carlota,40)

# Correccion:
# 1. Utilizar la constante math.pi
# 2. La funcion circulo tenia que llamar a la  
# funcion poligono

