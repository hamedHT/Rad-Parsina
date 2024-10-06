import pandas as pd

#CSV
df = pd.read_csv('data.csv')
print(df.head())

#writing
df.to_csv('output.csv', index=False)

#JSON
df = pd.read_json('data.json')
print(df.head())

#writing
df.to_json('output.json', orient='records', lines=True)

# Convert CSV to JSON
df.to_json('data.json', orient='records')

#XML
df = pd.read_xml('data.xml')
print(df.head())

#writing
df.to_xml('output.xml', root_name='root', row_name='row')



