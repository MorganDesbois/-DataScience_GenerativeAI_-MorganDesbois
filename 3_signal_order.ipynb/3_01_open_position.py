# Open position
Using the new column with created in #signal_ma_cross, the goal is to generate a new column for buy/sell postions.


# Generate Buy signals based on Crossover_Signal
gold_data['Buy_Signal'] = (gold_data['Crossover_Signal'] == 1).astype(int)

# Generate Sell signals based on Crossover_Signal
gold_data['Sell_Signal'] = (gold_data['Crossover_Signal'] == -1).astype(int) * -1


# Finally, this code generates buy and sell signals based on the 10-day and 50-day moving average crossovers.
It adds two new columns (Buy_Signal and Sell_Signal) that indicate when to enter or exit positions.**
