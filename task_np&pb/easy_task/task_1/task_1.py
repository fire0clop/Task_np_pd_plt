import numpy as np

#Question 1
array_np = np.random.randint(1, 51, (10, 5))
print(array_np)

#Question 2
mean_col = np.mean(array_np, axis=0)
print(mean_col)

#Question 3
sum_rows = array_np.sum(axis=1)
rows_above_200 = np.where(sum_rows > 200)
print(f'Answer on question 3 - {rows_above_200[0]}')