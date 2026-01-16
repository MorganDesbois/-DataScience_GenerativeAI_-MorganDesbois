# CLose position
Once the positions are open, in order to adjust the risk management of our strategy,
we need to define an exit strategy to cut profits or losses.


# Exit long position when 10-day MA crosses below 50-day MA
gold_data['Exit_Long_Signal'] = (gold_data['Crossover_Signal'] == -1).astype(int)

# Exit short position when 10-day MA crosses above 50-day MA
gold_data['Exit_Short_Signal'] = (gold_data['Crossover_Signal'] == 1).astype(int)


#We defined the position output with the inverse signal at the position opening.
