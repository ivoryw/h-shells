#include<math.h>
#include<complex.h>
#include<stdbool.h>
#include<stdio.h>
#include"polynomials.h"

/*-------- Useful Functions------------------*/
unsigned int factorial(unsigned int n){
 	unsigned int fact = 1;
 	int i;
 	for (i = n; i > 1; --i)
 		fact *= i;
 	return fact;
 }

unsigned int doubleFactorial(int n){
	unsigned int fact;
	if(n%2 == 0)
		fact =  pow(2,(n/2)) * factorial(n/2);
	else
		fact = factorial(n)/(doubleFactorial(n-1));
	if(n < 0)
		fact *= pow(-1,n);
	return fact;
}

double binomial(int n, int k)
{
	double bin = 1;
	int i;
	for(i=1; i<=k; i++)
		bin *= (n+1-i) / i;
	return bin;
}

/*--------Associated Laguerre Functions-----------*/
double laguerrePoly(int n, int k, double x){
	double L = 0;
	int i;
	for(i = 0; i<=n; i++){
		L += pow(-1,i) * binomial(n+k, n-i) * (pow(x,i) / factorial(i));
	}
	return L;
}

/*--------Associated Legendre Functions-------------*/
double complex startingPoly_mm(int m, double x){
	return (pow(-1,m) * doubleFactorial(2*m-1) * csqrt(pow(1-pow(x,2),m)) );
}

double complex lPlus_ll(int l, double x, double complex P_l_1){
	return x * (2*l+1) * P_l_1;
}

double complex lPlus(int l,int m, double x, double complex P_l_1, complex double P_l_2){
	return (x * (2*l-1)/(l-m)) * P_l_1 - ((l+m-1) * P_l_2/(l-m));
}

double complex legendrePoly(int l, int m, double x){
	bool negM;
	double complex P[l-m+1];
	int currentL = m;

	if(m < 0){
		negM = true;
		m = -1 * m;
	}
	else
		negM = false;
	
	if(m == 0)
		P[0] = 1;
	else
		P[0] = (startingPoly_mm(m, x));

	if(l!=m){
		P[1] = lPlus_ll(m, x, P[0]);
		currentL++;
	}
	for(;currentL < l; currentL++){
			P[currentL-m+1] = lPlus(currentL+1, m, x, P[currentL-m], P[currentL-m-1]);
	}
	
	if(negM)
		P[l-m] = pow(-1,m) * (factorial(l-m)/factorial(l+m)) * P[l-m];

	return P[l-m];
}
