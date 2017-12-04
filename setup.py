# make code as python 3 compatible as possible
from __future__ import absolute_import, division, print_function, unicode_literals

import subprocess
import setuptools
import os.path
import sys

from setuptools.command.develop import develop
from setuptools.command.install import install


# Build anltr files on installation
#   this is such a mess... it looks like there are
#   no common steps to develop and install

class AntlrDevelopCommand(develop):
    def run(self):
        compile_grammar()
        develop.run(self)

class AntlrInstallCommand(install):
    def run(self):
        compile_grammar()
        install.run(self)

def compile_grammar():
    here = os.path.dirname(__file__) or '.'
    package_dir = os.path.join(here, 'latex2sympy')
    subprocess.check_output(['antlr4',  'PS.g4', '-o', 'gen'], cwd=package_dir)

if sys.version_info.major == 3:
    REQUIRES = ['antlr4-python3-runtime',  'sympy']
else:
    REQUIRES = ['antlr4-python2-runtime',  'sympy']

setuptools.setup(
    name='latex2sympy',
    version=0.1,
    author='august.codes',
    author_email='augustt198@gmail.com',
    description='Parse latex markup into sympy: suitable for programmatic modifcation',
    license='MIT',
    keywords='MIT',
    url='https://github.com/augustt198/latex2sympy',
    packages=['latex2sympy'],
    classifiers=[
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Text Processing :: Markup'
    ],
    install_requires=REQUIRES,
    cmdclass=dict(
        install=AntlrInstallCommand,
        develop=AntlrDevelopCommand),
    test_suite='nose.collector'
)
