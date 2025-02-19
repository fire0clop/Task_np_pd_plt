import numpy as np
import pandas as pd
value = np.random.randint(1, 11, 12)
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
       'August', 'September', 'October', 'November', 'December']
data = pd.DataFrame({'month': month, 'revenue': value})
print('Average is',data['revenue'].mean().round(2))
print('Minimum is',data['revenue'].min())
print('Maximum is',data['revenue'].max())
indx = 0
list_dif = []
while indx < len(data['month']):
    if indx == 0:
        list_dif.append(0)
        indx += 1
    else:
        list_dif.append(data.at[indx, 'revenue'] - data.at[indx - 1, 'revenue'])
        indx += 1
data['Grow'] = list_dif
print(data)
#Когда искал альтернативы решению узнал о методе diff(),
# то есть можно без цикла и ручной индексации вычислить разницу текущего и предыдущего значения