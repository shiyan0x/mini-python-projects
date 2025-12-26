import pandas as pd

#create series
#s = pd.Series([1,2,3,4,5], name='number')
#print(s)

#creating dataframe 
df = pd.DataFrame({
  'A':[1,2,3,4],
  'B':['a','b','c','d'],
  'C':[4.5,5.5,6.5,7.5]
})
print(df)

value = df.loc[0,'A']
print(value)

#select multiple column
sel_column = df.loc[:,['A','C']]
print(sel_column)

#selct range of rows
sel_rows = df.loc[1:3,:]
print(sel_rows)







