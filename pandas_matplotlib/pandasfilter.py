import pandas as pd
import numpy as np

"""#create data 
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
print(filled_df)"""


"""data = {
  "Name":['Shivam', 'Sachin', 'Anas', 'sharoj'],
  "Age": [23, 34, 43, 35],
  "Marks": [54,76,45,98]
}
df = pd.DataFrame(data)
df.to_csv("studentdata.csv", index=False)
"""


"""df = pd.read_csv("studentdata.csv")
print(df)

#filter
filtered_df = df[df['Marks'] > 50]
print(filtered_df)
"""

df = pd.read_csv("studentdata.csv")
print(df.head(2))
print(df.tail(2))
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df.index)
print(df.dtypes)
print(df.values)
print(df.T)
print(df.sort_values(by='Marks'))
print(df.sort_values(by='Marks', ascending=False))
print(df.sort_values(by=['Marks', 'Age']))
print(df.sort_values(by=['Marks', 'Age'], ascending=[False, True]))
print(df.sort_values(by=['Marks', 'Age'], ascending=[False, True], inplace=True))
print(df.sort_values(by=['Marks', 'Age'], ascending=[False, True], inplace=True))