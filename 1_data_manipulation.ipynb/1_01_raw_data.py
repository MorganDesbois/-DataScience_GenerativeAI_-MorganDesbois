#This code downloads historical daily price data for the GLD gold ETF
#from January 1, 2015, to today using Yahoo Finance. It d provides a preview along
#with the total number of rows downloaded.


# Raw Data

import yfinance as yf
import pandas as pd
from datetime import datetime
import os


os.makedirs("Raw_Data", exist_ok=True)


gold = yf.Ticker("GLD")
start_date = "2023-01-01"
end_date = "2025-12-01"
data = gold.history(start=start_date, end=end_date)

if data.empty:
    print("Aucune donnée téléchargée ! Vérifiez la connexion internet ou le ticker.")
else:
    # Affiche un aperçu
    print("Aperçu des données :")
    print(data.head().to_string())
    print(f"Total de lignes téléchargées : {len(data)}")

    # Sauvegarde en CSV dans Raw_Data
    csv_filename = f"gold_prices_2015_{end_date}.csv"
    csv_path = os.path.join("Raw_Data", csv_filename)
    data.to_csv(csv_path)
    print(f"CSV créé à : {csv_path}")

    # Liste les fichiers dans Raw_Data
    print("\nFichiers dans le dossier Raw_Data :")
    print(os.listdir("Raw_Data"))











