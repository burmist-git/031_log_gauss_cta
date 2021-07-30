from distutils.core import setup, Extension
from Cython.Build import cythonize

exts = (
    cythonize("log_gaussian_cython.pyx")
)

setup(
    ext_modules = exts,
)
