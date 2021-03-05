#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stochastic quantum walker on QuTip.
Class containing an open quantum system described by a Lindblad equation obtained from the adjacency matrix.

Theoretical model:
Whitfield, J. D., Rodríguez-Rosario, C. A., & Aspuru-Guzik, A. (2010).
Quantum stochastic walks: A generalization of classical random walks and quantum walks.
Physical Review A, 81(2), 022323.

@author: Lorenzo Buffoni
"""

import numpy as np
from qutip import *

# TODO: implement a discrete-time and a continuous-time class or two methods within the same class?

class QWalker(object):
    def __init__(self, adjacency, noise_param=0, sink_node=None, sink_rate=1.):
        self.adjacency = adjacency
        self.N = adjacency.shape[0]
        # degree vector representing the connectivity degree of each node
        self.degree = np.sum(adjacency, axis=0)
        # normalized laplacian of the classical random walk
        self.laplacian = np.array([[self.adjacency[i, j] / self.degree[j] if self.degree[j] > 0 else 0
                                    for i in range(self.N)] for j in range(self.N)])
        self.sink_node = sink_node
        # TODO: implement multiple sinks
        self.create_walker_from_graph(noise_param, sink_rate)

    def create_walker_from_graph(self, noise_param, sink_rate):
        self.p = noise_param
        if self.sink_node is not None:
            # TODO: add check for directed graphs
            H = Qobj((1 - self.p) * np.pad(self.adjacency, [(0, 1), (0, 1)], 'constant'))
            L = [np.sqrt(self.p * self.laplacian[i, j]) * (basis(self.N + 1, i) * basis(self.N + 1, j).dag())
                for i in range(self.N) for j in range(self.N) if self.laplacian[i, j] > 0]
            S = np.zeros([self.N + 1, self.N + 1])  # transition matrix to the sink
            S[self.N, self.sink_node] = np.sqrt(2 * sink_rate)
            L.append(Qobj(S))
        else:
            H = Qobj((1 - self.p) * self.adjacency)
            L = [np.sqrt(self.p * self.laplacian[i, j]) * (basis(self.N, i) * basis(self.N, j).dag())
                 for i in range(self.N) for j in range(self.N) if self.laplacian[i, j] > 0]
        self.quantum_hamiltonian = H
        self.classical_hamiltonian = L

    def run_walker(self, initial_quantum_state, time_samples, dt=1e-2, observables=[], opts=None):
        """ Run the walker on the graph. The solver for the Lindblad master equation is mesolve from QuTip.

        Parameters
        ----------
        initial_quantum_state : qutip.qobj.Qobj
            quantum state of the system at the beginning of the simulation
        time_samples :
            number of time samples considered in the time equation
        dt : float (default 10**-2)
            single step time interval
        observables: list (default empty)
            list of observables to track during the dynamics.
            If a sink is present in the maze an observable is created automatically.
        opts: qutip.Options (default None)
            options for QuTip's solver mesolve.

        Returns
        -------
        (qutip.Result)
            return the final quantum state at the end of the quantum simulation.
        """
        if self.sink_node is not None:
            observables.append(basis(self.N + 1, self.sink_node) * basis(self.N + 1, self.sink_node).dag())
        times = np.arange(1, time_samples + 1) * dt  #timesteps of the evolution

        return mesolve(self.quantum_hamiltonian, initial_quantum_state, times,
                       self.classical_hamiltonian, observables, options=opts)
