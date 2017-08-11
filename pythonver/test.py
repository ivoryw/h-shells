import polymodnomials as poly
from termcolor import colored
import math
import cmath

fail = colored("FAILED", 'red')
passed = colored("PASSED", 'green')

print("-------Associated Laguerre Polynomials --------")
n = 1; l = 0; rad = 3 * poly.bohrRad; x  = 2*rad/(n*poly.bohrRad)
if(poly.findLaguerrePoly(n-l-1, 2*l+1, x) == 1):
	print("L10: ", passed)
else:
	print("L10: ", fail)
n = 2; l = 0
if(poly.findLaguerrePoly(n-l-1, 2*l+1, x) == 1 + (2*l+1) - x):
	print("L20: ", passed)
else:
	print("L20: ", fail)
l = 1
if(poly.findLaguerrePoly(n-l-1, 2*l+1, x) == 1):
	print("L21: ", passed)
else:
	print("L21: ", fail)
n = 3; l = 0
if(poly.findLaguerrePoly(n-l-1, 2*l+1, x) == x**2/2 - (2*l+3)*x + (2*l+3)*(2*l+2)/2):
	print("L30: ", passed)
else:
	print("L30: ", fail)
l = 1
if(poly.findLaguerrePoly(n-l-1, 2*l+1, x) == 1 + (2*l+1) - x):
	print("L31: ", passed)
else:
	print("L31: ", fail)
l=2
if(poly.findLaguerrePoly(n-l-1, 2*l+1, x) == 1):
	print("L32: ", passed)
else:
	print("L32: ", fail)


print("\n------Associated Legendre Polynomials------")
l = 0; m = 0; x= 2
if(poly.findLegendrePoly(l,m,x) == 1):
	print("P00: ", passed)
else:
	print("P00: ",fail)
l = 1; m = 0
if(poly.findLegendrePoly(l,m,x) == x):
	print("P10: ", passed)
else:
	print("P10: ", fail)
m = 1
if(poly.findLegendrePoly(l,m,x) == -1 * cmath.sqrt(1-x**2)):
	print("P11: ", passed)
else:
	print("P11: ", fail)

m = -1
if(poly.findLegendrePoly(l,m,x) == 1/2 * cmath.sqrt(1-x**2)):
	print("P1-1:", passed)
else:
	print("P1-1:", fail)

l=2; m=0
if(poly.findLegendrePoly(l,m,x) == 1/2 * (3*x**2-1)):
	print("P20: ", passed)
else:
	print("P20: ", fail)

m=1
if(poly.findLegendrePoly(l,m,x) == -3*x*cmath.sqrt(1-x**2)):
	print("P21: ", passed)
else:
	print("P21: ", fail)

m=2
if(poly.findLegendrePoly(l,m,x) == 3 * (1-x**2)):
	print("P22: ", passed)
else:
	print("P22: ", fail, "Inaccuracy starts to creep in here")

print("\n-------Radial Wavefunction--------")
n=1; l = 0
if(poly.findLaguerrePoly(n-l-1, 2*l+1, x) *  poly.normalizationConst(n,l,rad) == 2 * ((cmath.sqrt(1/poly.bohrRad))**3) * math.exp(-1* rad/poly.bohrRad)):
	print("R20: ", passed)
else:
	print("R20: ", fail,)
	print(poly.findLaguerrePoly(n-l-1, 2*l+1, x) *  poly.normalizationConst(n,l,rad), 2 * ((cmath.sqrt(1/poly.bohrRad))**3) * math.exp(-1* rad/poly.bohrRad) )

