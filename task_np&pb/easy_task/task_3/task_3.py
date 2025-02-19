import pandas as pd

data = pd.read_csv('table.csv')
data.set_index('Date', inplace=True)
data['Summa'] = data['Price'] * data['Quantity']
group_by_category = data.groupby('Category').sum()[['Summa']]
print('\nСategory with the highest revenue is', group_by_category['Summa'].idxmax())
group_by_category['Average'] = data.groupby('Category')['Price'].mean()
print(group_by_category)
print('\nDay with the highest revenue is', data['Summa'].idxmax())