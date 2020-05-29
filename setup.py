import glob

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

source_files = ['yoga.pyx'] + glob.glob('yoga/yoga/**/*.cpp', recursive=True)
include_dirs = ['yoga']
setup(
    name='pyyoga',
    ext_modules=cythonize([
        Extension(
            'yoga',
            source_files,
            include_dirs=include_dirs,
            extra_compile_args=[
                '-fno-omit-frame-pointer',
                '-fexceptions',
                '-Wall',
                '-Werror',
                '-std=c++1y',
                '-fPIC'
                ],
        )
    ])
)
