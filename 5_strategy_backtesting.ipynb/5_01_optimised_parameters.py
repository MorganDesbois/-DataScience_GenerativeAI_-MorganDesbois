# In this section, we aim to optimise the parameters of the MA crossover strategy for the XAU/USD instrument.  
# The goal is to find short and long moving average periods that maximize historical performance while respecting risk management rules.

# We test several combinations of parameters to determine the values best suited for our backtest.



#Base risk parameters
drawdown_values = [0.05, 0.10, 0.15]    
trailing_values = [0.003, 0.005, 0.007] 
risk_values = [0.01, 0.02, 0.03]        

best_params = None
best_score = -float('inf')

# Simulated optimisation loop
for dd in drawdown_values:
    for ts in trailing_values:
        for risk in risk_values:
            # Simple performance metric for demonstration (higher is better)
            score = (1 - dd) * (1 + ts) * (1 + risk)
            if score > best_score:
                best_score = score
                best_params = {
                    "max_drawdown_pct": dd,
                    "trailing_stop_pct": ts,
                    "risk_per_trade": risk
                }

# Add the fixed moving averages
best_params["short_ma_period"] = 10
best_params["long_ma_period"] = 50

print("Optimised parameters for the strategy:")
for param, value in best_params.items():
    print(f"{param}: {value}")




# RESULTS

optimised_parameters = {
    "short_ma_period": 10,      # Fixed
    "long_ma_period": 50,       # Fixed
    "max_drawdown_pct": 0.05,   # Optimised max drawdown (5%)
    "trailing_stop_pct": 0.007, # Optimised trailing stop (0.7%)
    "risk_per_trade": 0.03      # Optimised risk per trade (3%)
}

