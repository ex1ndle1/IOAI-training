import pandas as pd
import numpy as np

df = pd.read_csv("titanic.csv")
sorted_df = df.sort_values(by=['Age' , 'Pclass'])
print(df.isna().mean())