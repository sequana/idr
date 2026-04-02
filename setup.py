import numpy
from setuptools import setup, Extension

try:
    from Cython.Build import cythonize
    extensions = cythonize([
        Extension("idr.inv_cdf",
                  ["idr/inv_cdf.pyx"],
                  include_dirs=[numpy.get_include()]),
    ])
except ImportError:
    extensions = [
        Extension("idr.inv_cdf",
                  ["idr/inv_cdf.c"],
                  include_dirs=[numpy.get_include()]),
    ]

setup(ext_modules=extensions)
