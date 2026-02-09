# Quantum-Classical-Portfolio-Rebalancer
A multi-agent quantum-classical hybrid pipeline for NSE stock portfolio optimization using QAOA and Qiskit 1.0.

# 🚀 Quantum-Classical Portfolio Rebalancer
**A Multi-Agent Hybrid Pipeline for NSE Stock Optimization using QAOA and Qiskit 1.0.**

## 🧠 Project Architecture
[cite_start]This project utilizes a **Multi-Agent Framework** to navigate a search space of $2^{25}$ possible portfolios[cite: 115]:
- [cite_start]**Data Retrieval Agent:** Fetches cleaned NSE market data for 25 tickers[cite: 64].
- [cite_start]**Quantum Architect:** Translates financial risk into a QUBO Matrix[cite: 64].
- [cite_start]**Optimization Agent:** Solves the Ising Hamiltonian using QAOA[cite: 64].
- [cite_start]**Risk Analyst:** Benchmarks performance against the NIFTY 50[cite: 64].

## 🧬 Methodology
### Phase 1 & 2: Data & QUBO Transformation
[cite_start]We selected 25 volatile NSE stocks across IT, Banking, FMCG, Auto, and Healthcare, covering ~70% of the NIFTY 50 weightage[cite: 36, 46]. [cite_start]We mapped these into a **Quadratic Unconstrained Binary Optimization (QUBO)** problem where $Energy = Risk + Penalty$[cite: 80].

### Phase 3: Hybrid Optimization
[cite_start]Using **QAOA**, we ran a variational loop where the **Quantum Side** (Gamma/Beta parameters) and **Classical Side** (COBYLA) collaborated to find the ground state[cite: 104, 108]. [cite_start]We achieved an optimal energy state of **-49.997**, proving the 10-stock budget constraint was met[cite: 115].

### Phase 4: Backtesting
View the full performance analysis and Alpha breakdown in the [RESULTS.md](./RESULTS.md) file.
