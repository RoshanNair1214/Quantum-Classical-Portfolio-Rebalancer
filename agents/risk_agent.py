import numpy as np

class RiskAnalystAgent:
    def __init__(self, portfolio_returns, benchmark_returns):
        self.portfolio_returns = portfolio_returns
        self.benchmark_returns = benchmark_returns

    def calculate_alpha(self):
        """Calculates the excess return relative to NIFTY 50[cite: 121, 122]."""
        total_portfolio_return = (1 + self.portfolio_returns).prod() - 1
        total_benchmark_return = (1 + self.benchmark_returns).prod() - 1
        alpha = total_portfolio_return - total_benchmark_return
        return alpha

    def get_sharpe_ratio(self, risk_free_rate=0.07):
        """Calculates risk-adjusted performance[cite: 69, 127]."""
        excess_returns = self.portfolio_returns - (risk_free_rate / 252)
        return np.sqrt(252) * excess_returns.mean() / excess_returns.std()
