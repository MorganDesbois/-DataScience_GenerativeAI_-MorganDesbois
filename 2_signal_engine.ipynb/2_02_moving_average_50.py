# Moving Average 50 days 
# In this code, the objective is similar to the #moving_average_10 but this time we create the 50-day moving average still using "clean data"


## Read cleaned CSV from Clean_Data
clean_files = os.listdir("Clean_Data")
clean_csv = [f for f in clean_files if f.endswith(".csv")][0]
clean_path = os.path.join("Clean_Data", clean_csv)
gold_data = pd.read_csv(clean_path, index_col=0, parse_dates=True)

## Reset index to make Date a column
gold_data = gold_data.reset_index()

## Calculate 50-day moving average of 'Close' price
gold_data['50_day_MA'] = gold_data['Close'].rolling(window=50).mean()

##  Display first 15 rows with new column
display(gold_data.head(15))


# This code uses the cleaned gold price data from Clean_Data and calculates a 50-day moving average of the closing prices. 
