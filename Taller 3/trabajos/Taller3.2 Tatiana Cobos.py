import math
r=1
# v=(4*3.14*r*r*r)/3
# print "volumen:", v
# r=raw_input()
# v=(4*3.14* float(r) * float(r)* float(r)) /3
# print "volumen:",v
# print "volumen: %f cm3 % (v)"
def volumen_esf(r):
	print r                             # porque esta imprimiendo r?
	v=4*(math.pi)*float(r)*float(r)*float(r)/3
	return v
print volumen_esf(raw_input())          # debería indicar los que espera el programa y que es lo que se calcula


