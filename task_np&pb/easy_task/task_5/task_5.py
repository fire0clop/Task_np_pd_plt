import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('table_data.csv')
plt.plot(data['revenue'])
plt.xticks(ticks=range(len(data['month'])), labels=data['month'].str[:3])
plt.grid()
plt.ylabel('Revenue')
plt.title('Sales Growth Visualization')
max_revenue = data['revenue'].max()
max_index = data[data['revenue'] == max_revenue].index[0]
plt.scatter(max_index, max_revenue, color='red', s=100, label='Max Revenue', zorder=3)
plt.show()
plt.savefig('revenue_plot.png')