# SQWalk

[![Unitary Fund](https://img.shields.io/badge/Supported%20By-UNITARY%20FUND-brightgreen.svg?style=for-the-badge)](http://unitary.fund)

(In development, use at you own risk!)

A Stochastic Quantum Walk simulator based on [QuTiP](https://qutip.org).\
Dependecies:
```
qutip
numpy
matplotlib
```

The phyton implementation of the walker class is contained in ```sqwalk.py```.\
The ```tutorials```  folder contains some tutorial notebooks to familiarize yourself with the
walker class and review the principal fatures.\
SQWalk can be easily incorporated in any existing pipeline with any custom topology or 
network class, provided the adjacency matrix. It can deal both with Continuous-Time ([ref](https://arxiv.org/abs/0905.2942)) and 
Discrete-Time (or Coined) ([ref](https://arxiv.org/abs/1006.5556)) Quantum Walks, usage examples for both classes can be found in the tutorials.

### Install
As of now you need to download the ```sqwalk.py``` file in the same directory where
you intend to use it, packaging will come in the future. 

Stay tuned!


