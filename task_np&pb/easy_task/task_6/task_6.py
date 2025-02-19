import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

student_name = ['Tom', 'Jose', 'Bob', 'Anna', 'Karl']
subject_name = ['Mathematics', 'Physics', 'Chemistry', 'Literature', 'History']
grad_sub = {}
for subject in subject_name:
    grad_sub[subject] = np.random.randint(2,6,5)

data = pd.DataFrame(grad_sub, index=student_name)
data.index.name = "Student"
print(data)
short_subjects = [subject[:3] for subject in subject_name]
plt.subplot(121).bar(short_subjects, data.mean(axis=0))
high_grades = (data > 4).sum()
plt.subplot(122).pie(high_grades, labels=short_subjects, autopct='%1.1f%%')
plt.show()