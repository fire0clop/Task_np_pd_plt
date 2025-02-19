import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sel = np.random.randint(10,201,730)
date = pd.date_range(start='2022-01-01', periods=730)
data = pd.DataFrame({'Date':date, 'Sales':sel})
data['Average_30'] = data['Sales'].rolling(window=30).mean()
plt.figure(figsize=(12, 5))
plt.plot(data['Date'], data['Sales'])
plt.plot(data['Date'], data['Average_30'])
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Sales Trend Over 2 Years')
plt.show()
data['Month'] = data['Date'].dt.to_period('M')
grouped = data.groupby(['Month']).mean()
best_month = grouped['Sales'].idxmax()
print('Month with highest average sales:', best_month)