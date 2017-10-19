# a=2
# b=2
# c=2
# d=2

# def chequear_fermat(a,b,c,n):
# 	if (a**n)+(b**n)==(c**n):
# 		print "Oye Fermat estaba equivocado"
# else:
# 	print "No, la igual no funciona"

# chequear_fermat (2,4,6,2)

# # parte b

# def obtenervalores(va,vb,vc,vd):
# 	va=raw_imput ("valor a")
# 	vb=raw_imput ("valor b")
# 	vc=raw_imput ("valor c")
# 	vd=raw_imput ("valor d")
# 	chequear_fermat (1,2,3,4)

# parte c

# def chequear_fermat (a,b,c,n):
# 	if n>2:
# 		if (a**n)+(b**n)==(c**n):
# 			print "Oye Fermat estaba equivocado"
# 		else:
# 			print "No, la igual no funciona"
# 	if n<=2:
# 		print "El teorema no se aplica"
		
# chequear_fermat (2,4,6,1)



# punto 2
# parte a

def es_triangulo(a,b,c):
	if b<(a+c) and a<(b+c)and c<(a+b):
		print "Si, forma el triangulo"
	else:
		print "No, formar el triangulo"
	     

es_triangulo (12,6,3)
