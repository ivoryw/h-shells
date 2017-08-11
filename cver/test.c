#include <stdio.h>
#include "polynomials.c"

#define RED   "\x1B[31m"
#define GRN   "\x1B[32m"
#define RESET "\x1B[0m"
#define PLAG {printf("P%d%d: ", n,l); printf(GRN " Passed\n" RESET);}
#define NLAG {printf("P%d%d: ", n,l); printf(RED " FAILED\n" RESET);}
#define PLEG {printf("L%d%d: ", l,m); printf(GRN " Passed\n" RESET);}
#define NLEG {printf("L%d%d: ", l,m); printf(RED " FAILED\n" RESET);}

int main(){
	double bohrRad = 5.2917721067;
	double rad = 3 * bohrRad;
	int n = 1; int l = 0;
	double x  = 2*rad/(n*bohrRad);
	
	if(laguerrePoly(n-l-1, 2*l+1, x) == 1)
		PLAG
	else
		NLAG
	n = 2; l = 0;
	if(laguerrePoly(n-l-1, 2*l+1, x) == 1 + (2*l+1) - x)
		PLAG
	else{
		NLAG
	}

	l = 1;
	if(laguerrePoly(n-l-1, 2*l+1, x) == 1)
		PLAG
	else
		NLAG
	n = 3; l = 0;
	if(laguerrePoly(n-l-1, 2*l+1, x) == pow(x,2)/2 - (2*l+3)*x + (2*l+3)*(2*l+2)/2)
		PLAG
	else
		NLAG

	l = 1;
	if(laguerrePoly(n-l-1, 2*l+1, x) == 1 + (2*l+1) - x)
		PLAG
	else
		NLAG

	l = 0; int m = 0; x= 2;
	if(legendrePoly(l,m,x) == 1)
		PLEG
	else	
		NLEG	
	l = 1; m = 0;
	if(legendrePoly(l,m,x) == x)
		PLEG
	else	
		NLEG	
	m = 1;
	if(legendrePoly(l,m,x) == -1 * csqrt(1-pow(x,2)))
		PLEG
	else	
		NLEG	
	m=-1;
	if(legendrePoly(l,m,x) == 1/2 * csqrt(1-pow(x,2)))
		PLEG
	else	
		NLEG

	x = 2; l=2; m=0;
	if(legendrePoly(l,m,x) == 0.5 * (3*pow(x,2)-1))
		PLEG
	else{
		NLEG
		printf("%lf should be %lf\n", creal(legendrePoly(l,m,x)) , creal(0.5 * (3*pow(x,2)  -1)));
	}
		return 0;
}