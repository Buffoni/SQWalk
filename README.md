# SQWalk

WARNING: This project has now been merged with [QWAK](https://github.com/JaimePSantos/QWAK) and it will now be updated there. This version is deprecated.

[![Unitary Fund](https://img.shields.io/badge/Supported%20By-UNITARY%20FUND-brightgreen.svg?style=for-the-badge)](http://unitary.fund)
[![PyPi Version](https://img.shields.io/pypi/v/sqwalk.svg?style=for-the-badge)](https://pypi.python.org/pypi/sqwalk/)

In development, use with discretion.

A Stochastic Quantum Walk simulator based on [QuTiP](https://qutip.org).

Dependencies:

```
qutip
qiskit
numpy
matplotlib
```

The implementation of the walker class is contained in `sqwalk/objects.py`.

The `tutorials`  folder contains some tutorial notebooks to familiarize yourself with this package
and review the principal features.

SQWalk can be easily incorporated in any existing pipeline with any custom
topology or network class, provided with the adjacency matrix. It can deal both
with Continuous-Time ([ref](https://arxiv.org/abs/0905.2942)) and Discrete-Time
(or Coined) ([ref](https://arxiv.org/abs/1006.5556)) Quantum Walks, usage
examples for both classes can be found in the tutorials.

### Install

The package is avaiable on [PyPi](https://pypi.org/project/sqwalk/), it can be installed by running

```
python3 -m pip install sqwalk
```

If one wants to build it from here using setuptools, clone this repository and 
install the package by running 

```
python3 -m pip install .
```
inside the directory. 

The package and its dependencies are tested to run on Python 3.8, we recommend
installing the package inside a conda env or a virtualenv to avoid conflicting
dependencies.

To discuss any questions you are welcomed to open an issue or to cantact the author. 

Stay tuned!
