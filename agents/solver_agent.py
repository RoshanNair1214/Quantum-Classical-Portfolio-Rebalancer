from qiskit_algorithms import NumPyMinimumEigensolver
from qiskit_optimization.problems import QuadraticProgram
from qiskit_optimization.algorithms import MinimumEigenOptimizer

class OptimizationAgent:
    def __init__(self, qubo_matrix):
        self.qubo_matrix = qubo_matrix

    def solve(self):
        """Solves the Ising Hamiltonian to find the ground state[cite: 97, 113]."""
        qp = QuadraticProgram()
        for i in range(len(self.qubo_matrix)):
            qp.binary_var(name=f'x{i}')
        
        qp.minimize(quadratic=self.qubo_matrix)
        
        # Using exact solver to bypass V2 primitive bottlenecks [cite: 113]
        exact_solver = MinimumEigenOptimizer(NumPyMinimumEigensolver())
        result = exact_solver.solve(qp)
        return result
