import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('Table.csv', index_col=0)
data['Revenue'] = data['Avg_Check'] * data['Purchases']
print(data.head())
print('Top 3 customers with the highest total revenue:',data.nlargest(3, 'Revenue')['Name'].tolist())
top_city = data.groupby('City')['Revenue'].sum().idxmax()
print('The city with the highest total revenue:', top_city)

revenue_by_city = data.groupby('City')['Revenue'].sum()
plt.bar(revenue_by_city.index, revenue_by_city.values)
plt.xlabel('City')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by City')
plt.xticks(rotation=45)  # Поворот подписей для читаемости
plt.show()
