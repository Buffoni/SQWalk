from qiskit import QuantumCircuit, transpile
from qiskit.providers import BaseBackend
from qiskit.result import Result
from qiskit.providers.models import BackendProperties, BackendConfiguration
import numpy as np
import time

class FakeBackend(BaseBackend):
    """This is a dummy backend just for transpile purposes."""

    def __init__(self, time_alive=10):
        """
        Args:
            configuration (BackendConfiguration): backend configuration
            time_alive (int): time to wait before returning result
        """
        cmap = [[i,j] for i in range(3) for j in range(3)]

        DEFAULT_BASIS_GATES = sorted([
        'p', 'rx', 'ry', 'rz', 'id', 'x',
        'y', 'z', 'h', 's', 'sdg', 'sx', 't', 'tdg', 'swap', 'cx',
        'cy', 'cz', 'csx', 'cp', 'rxx', 'ryy',
        'rzz', 'rzx', 'ccx', 'cswap', 'mcx', 'mcy', 'mcz', 'mcsx',
        'mcphase', 'mcrx', 'mcry', 'mcrz',
        'mcr', 'mcswap'
        ])

        configuration = BackendConfiguration(
            backend_name='fake_backend',
            backend_version='0.0.0',
            n_qubits=4,
            basis_gates=DEFAULT_BASIS_GATES,
            simulator=False,
            local=True,
            conditional=False,
            open_pulse=False,
            memory=False,
            max_shots=65536,
            gates=[],
            coupling_map=cmap,
        )
        super().__init__(configuration)
        self.time_alive = time_alive

    def properties(self):
        """Return backend properties"""
        properties = {
            'backend_name': self.name(),
            'backend_version': self.configuration().backend_version,
            'last_update_date': '2000-01-01 00:00:00Z',
            'qubits': [],
            'gates': [],
            'general': []
        }

        return BackendProperties.from_dict(properties)

    def run(self, qobj):
        job_id = str('fake_run')
        job = self.run_job(job_id, qobj)
        job.submit()
        return job

    def run_job(self, job_id, qobj):
        """Main dummy run loop"""
        time.sleep(self.time_alive)

        return Result.from_dict(
            {'job_id': job_id, 'result': [], 'status': 'COMPLETED'})


def gate_decomposition(unitary):
    N = unitary.shape[0]
    n_qubits = int(np.log2(N))

    # TODO: check unitarity
    assert N == 2**n_qubits, 'The dimension of the unitary must be a power of 2'

    circ = QuantumCircuit(n_qubits)
    circ.unitary(unitary, [i for i in range(n_qubits)])
    backend = FakeBackend()
    decomposition = transpile(circ, backend=backend, optimization_level=2)
    decomposition_depth = decomposition.depth()
    print('Success! Walker decomposed using', decomposition_depth, 'gates.')
    return decomposition