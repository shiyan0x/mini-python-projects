import pandas as pd
import numpy as np

#create data 
df = pd.DataFrame({
  'A':[1,2,np.nan, 4],
  'B':[np.nan,'b','c','d'],
  'C':[4.5,np.nan,6.5,7.5]
})

#detecting
missing_value = df.isna()
print(missing_value)

#filtering
filled_df = df.fillna(0)
print(filled_df)