import pandas as pd

df = pd.read_csv('csvdata/MaxOptra_Collections_20032022.csv')

print(df[['company','accountnumber']]) 

