import pandas as pd
import numpy as np

df = pd.read_csv('data.csv')
# df

# df_numerics_only = df.select_dtypes(include=[np.number])
# print df_numerics_only

colnames_numerics_only = df.select_dtypes(include=[np.number]).columns.tolist()
print colnames_numerics_only