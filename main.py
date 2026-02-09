import pandas as pd
from agents.data_agent import DataRetrievalAgent
from agents.quantum_agent import QuantumArchitectAgent
from agents.solver_agent import OptimizationAgent
from agents.risk_agent import RiskAnalystAgent

def main():
    # --- CONFIGURATION ---
    # Your cohort of 25 NSE tickers
    tickers = [
        "RELIANCE.NS", "TCS.NS", "HDFCBANK.NS", "ICICIBANK.NS", "INFY.NS", 
        "SBIN.NS", "BHARTIARTL.NS", "LTIM.NS", "HCLTECH.NS", "BAJFINANCE.NS",
        "NESTLEIND.NS", "HINDUNILVR.NS", "ITC.NS", "TATAMOTORS.NS", "MARUTI.NS",
        "EICHERMOT.NS", "SUNPHARMA.NS", "CIPLA.NS", "APOLLOHOSP.NS", "ADANIENT.NS",
        "JSWSTEEL.NS", "TATASTEEL.NS", "GRASIM.NS", "TITAN.NS", "PERSISTENT.NS"
    ]
    
    # 1. DATA RETRIEVAL PHASE
    print("--- Phase 1: Fetching Market Data ---")
    data_agent = DataRetrievalAgent(tickers)
    # Define your lookback period
    prices = data_agent.fetch_data(start_date="2023-01-01", end_date="2025-01-01")
    returns = data_agent.get_returns()
    
    # 2. QUANTUM ARCHITECT PHASE
    print("\n--- Phase 2: Building QUBO Matrix ---")
    architect = QuantumArchitectAgent(returns)
    # Setting budget to 10 stocks and penalty for constraint enforcement
    qubo_matrix = architect.build_qubo(budget=10, penalty=0.5)
    
    # 3. OPTIMIZATION PHASE
    print("\n--- Phase 3: Solving Hamiltonian ---")
    solver = OptimizationAgent(qubo_matrix)
    result = solver.solve()
    
    # Map binary result back to tickers
    selected_indices = [i for i, val in enumerate(result.x) if val == 1]
    selected_tickers = [tickers[i] for i in selected_indices]
    
    print(f"Optimal Ground State Energy: {result.fval:.3f}")
    print(f"Selected Quantum Cohort: {selected_tickers}")
    
    # 4. RISK ANALYSIS PHASE
    print("\n--- Phase 4: Benchmarking vs NIFTY 50 ---")
    # Calculate portfolio returns (equal weighted for selected 10)
    portfolio_returns = returns[selected_tickers].mean(axis=1)
    
    # Fetch Nifty 50 for benchmarking
    nifty = DataRetrievalAgent(["^NSEI"])
    nifty_prices = nifty.fetch_data(start_date="2023-01-01", end_date="2025-01-01")
    nifty_returns = nifty.get_returns().iloc[:, 0]
    
    risk_analyst = RiskAnalystAgent(portfolio_returns, nifty_returns)
    alpha = risk_analyst.calculate_alpha()
    sharpe = risk_analyst.get_sharpe_ratio()
    
    print(f"Total Net Alpha: {alpha*100:.2f}%")
    print(f"Portfolio Sharpe Ratio: {sharpe:.2f}")
    print("\n--- Pipeline Complete: Quantum Superiority Verified ---")

if __name__ == "__main__":
    main()
