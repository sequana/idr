import os
import numpy
from setuptools import Extension


def build(setup_kwargs):
    USE_CYTHON = os.path.exists("idr/inv_cdf.pyx")
    try:
        from Cython.Build import cythonize
    except ImportError:
        USE_CYTHON = False

    if USE_CYTHON:
        ext = cythonize([
            Extension("idr.inv_cdf",
                      ["idr/inv_cdf.pyx"],
                      include_dirs=[numpy.get_include()]),
        ])
    else:
        ext = [
            Extension("idr.inv_cdf",
                      ["idr/inv_cdf.c"],
                      include_dirs=[numpy.get_include()]),
        ]

    setup_kwargs.update({"ext_modules": ext})
