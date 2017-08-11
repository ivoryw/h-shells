from distutils.core import setup, Extension

setup(name="poly", version="0.0",
	ext_modules = [Extension("poly", ["poly.c","polynomials.c"])],
    )