import pandas

DataFrame = pandas.read_csv('vgsales.csv')
print(DataFrame.columns)
print(DataFrame[['Genre','Year','Publisher']][0:10])
print(DataFrame.Year)
print(DataFrame.head(20))
print(DataFrame.tail(10))
print(DataFrame.iloc[15707,5])
for Index,Row in DataFrame.iterrows():
    print(Index,Row['Genre'])
print(DataFrame.loc[DataFrame['Genre']=='Sport'])
print(DataFrame.sort_values(['Year','Genre'],ascending=[0,1])[10:20])
DataFrame = DataFrame.loc[DataFrame['Genre']=='Sports']
DataFrame = DataFrame.reset_index(drop=True)
DataFrame.to_csv('Sports.csv')
