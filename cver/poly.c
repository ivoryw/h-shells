#include<Python.h>
#include<complex.h>
#include"polynomials.h"

static PyObject * 
poly_legendrePoly(PyObject *self, PyObject *args){
	int l, m;
	double x;

	if(!PyArg_ParseTuple(args, "iid", &l, &m, &x)){
		return NULL; 
	}
	double complex legendre = legendrePoly(l,m,x);
	return PyComplex_FromDoubles(creal(legendre), cimag(legendre));
}

static PyObject * 
poly_laguerrePoly(PyObject *self, PyObject *args){
	int n,k;
	double x;

	if(!PyArg_ParseTuple(args, "iid", &n, &k, &x))
		return NULL;
	
	double laguerre = laguerrePoly(n,k,x);

	return PyLong_FromDouble(laguerre);
}

static PyMethodDef poly_methods[] = {
    {"legendrePoly", poly_legendrePoly, METH_VARARGS,
     "Calculate the associated Legendre polynomial for x"},
     {"laguerrePoly", poly_laguerrePoly, METH_VARARGS,
     "Calculate the associated Laguerre polynomial for x"},
    {NULL, NULL, 0, NULL}        /* Sentinel */
};

static struct PyModuleDef polymodule = {
    PyModuleDef_HEAD_INIT,
    "poly",
    NULL,
    -1,
    poly_methods
};

PyMODINIT_FUNC
PyInit_poly(void){
	return PyModule_Create(&polymodule);
}


