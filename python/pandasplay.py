from pandas import DataFrame, read_csv

import matplotlib.pyplot as plt
import pandas as pd
import sys

filepath = r'C:\Users\Local Fister\OneDrive\Code\data\CO2emissions\API_EN.ATM.CO2E.PC_DS2_en_csv_clean.csv'
indata = pd.read_csv(filepath)
df = pd.DataFrame(data=indata)
print(df.max(level=0))
