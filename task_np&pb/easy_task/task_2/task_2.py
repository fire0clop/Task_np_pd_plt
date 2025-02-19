import numpy as np

data = np.random.randint(-10,36,365)
print(f'Average temp - {data.mean().round(2)}\u00B0C, Minimum - {data.min()}\u00B0C, Maximum - {data.max()}\u00B0C')
print('The number of days when the temperature was below 0°C is', len(np.where(data < 0)[0]))
# По моему методу решения 365 невозможно разбить на дни недели в массив правильно,
# поэтому я вычеркиваю последний день и нахожу его среднюю температуру отдельно,
# а остальные полноценные дни недели нахожу через среднюю строк массива
last_day = data[len(data) - 1]
massive_data = data[:-1].reshape(-1, 7)
avg_list = massive_data.mean(axis=1).round(2)
print(np.append(avg_list, last_day))