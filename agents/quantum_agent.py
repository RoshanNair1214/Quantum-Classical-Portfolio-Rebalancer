import numpy as np

class QuantumArchitectAgent:
    def __init__(self, returns):
        self.returns = returns
        self.cov_matrix = returns.cov().values

    def build_qubo(self, budget, penalty):
        """
        Maps risk/return to a QUBO matrix.
        Energy = Risk + Penalty[cite: 80].
        """
        num_assets = len(self.cov_matrix)
        # Create the Q matrix based on covariance [cite: 85]
        # Diagonal elements: Individual risk - 2 * penalty * budget
        # Off-diagonal: Covariance + 2 * penalty
        Q = np.zeros((num_assets, num_assets))
        
        for i in range(num_assets):
            for j in range(num_assets):
                if i == j:
                    Q[i, i] = self.cov_matrix[i, i] - (2 * penalty * budget)
                else:
                    Q[i, j] = self.cov_matrix[i, j] + (2 * penalty)
        return Q
