# Quantitative-Option-Pricing-Python

## Project Overview

This project implements European option pricing models using Python, focusing on both analytical and numerical valuation techniques widely used in quantitative finance. The objective is to understand option valuation, payoff structures, and risk-neutral pricing through practical implementation.

## Models Implemented

1. **Black–Scholes Model**
- Analytical pricing of European call and put options
- Computation of D1 and D2 using log-normal stock price assumptions
- Custom implementation of the normal cumulative distribution function using math.erf (no external dependencies)

2. **Binomial Option Pricing Model**
- Multi-step recombining binomial tree
- Explicit modeling of option payoffs at maturity
- Backward induction to compute present option value
- Pricing under the risk-neutral probability framework

## Key Concepts Covered
- European option payoff modeling (Call & Put)
- Risk-neutral valuation
- Discounting expected payoffs
- Backward induction in binomial trees

## Technologies Used
- Python
- Math library

## Parameters
- Initial Stock Price (S0)
- Strike Price (K)
- Time to Maturity (T)
- Risk Free Interest (r)
- Volatility (σ)
- Number of steps (N)
