import math
import cmath

global obritalAng, bohrRad, m_e, hbar, bohrRad
m_e = 9.10938356E-31
hbar = 1.0545718E-34
bohrRad = 5.2917721067E-11

orbitalAng = m_e * hbar
#bohrRad = const.physical_constants["Bohr radius"][0]

#--------Associated Laguerre Functions-----------
def binomial(n,k):
	i = 1
	bin = 1
	while(i<=k):
		bin *= (n+1-i) / i
		i += 1
	return bin

def LaguerrePoly(n, k, x):
	i = 0
	L = 0
	while(i <= n):
		L += ((-1)**i) * binomial(n+k, n-i) * ((x**i)/math.factorial(i))
		i += 1
	return L

#--------Associated Legendre Functions-------------
def doubleFactorial(n):
	if(math.fmod(n,2) == 0):
		fact =  2**(n/2) * math.factorial(n/2)
	else:
		fact = math.factorial(n)/(doubleFactorial(n-1))
	if(n < 0):
		fact *= (-1)**(n)
	return fact

def startingPoly_mm(x ,m):
	return ((-1)**m * doubleFactorial(2*m-1) * cmath.sqrt(1-x**2)**m)

def lPlus_ll(l, x, P_l_1):
	return x * (2*l+1) * P_l_1

def lPlus(l,m,x, P_l_1, P_l_2):
	return (x * (2*l-1)/(l-m)) * P_l_1 - ((l+m-1)/(l-m)) * P_l_2

def LegendrePoly(l,m,x):
	if(m < 0):
		negM = True
		m = -1 * m
	else:
		negM = False
	
	P = []
	if(m == 0):
		P.append(1)
	else:
		P.append(startingPoly_mm(x, m))
	currentL = m
	if(l!=m):
		P.append(lPlus_ll(m, x, P[0]))
		currentL += 1
	while(currentL != l):
		currentL += 1
		P.append(lPlus(currentL, m, x, P[-1], P[-2]))

	if(negM):
		P.append((-1)**m * math.factorial(l-m)/math.factorial(l+m) * P[-1])
	return P[-1]

#--------Normalization--------
def normalizationConst(n,l,r):
	rho = 2*r/(n*bohrRad)
#	print(cmath.sqrt((2/(n*bohrRad))**3 * math.factorial(n-l-1)/(2*n*math.factorial(n+l))))
	return cmath.sqrt((2/(n*bohrRad))**3 * math.factorial(n-l-1)/(2*n*math.factorial(n+l))) * math.exp(-1 * rho/2) * rho**l


