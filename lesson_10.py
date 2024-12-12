#1
import pandas as pd
import numpy as np

tudish = pd.Series([4.309, 4.340, 4.365, 4.376, 4.402, 4.429, 4.452, 4.476])
print(tudish1)
tudish1 = pd.Series(np.arange(0, 20, 2))
print(tudish1)
tudish2 = pd.Series({'Неплохо': 1, 'было': 3, 'бы': 5, 'поесть': 7})
print(tudish2)'

# №2
import pandas as pd
import numpy as np

purr1 = pd.Series(np.arange(0, 8, 2))
purr2 = pd.Series(np.arange(2, 10, 1))
print(purr1, purr)
wow = set.union(set(pururu1), set(pururu2))
wown = pd.Series(list(wow))
print(wown)

# №3
import matplotlib.pyplot as plt
import pandas as pd

badabum = pd.Series({0: 'female',1: 'male',2: 'male',3: 'female',4: 'female',5: 'male',
  6: 'male',7: 'male',8: 'male',9: 'female',10: 'female',11: 'female',12: 'female',
  13: 'female',14: 'male',15: 'male',16: 'male',17: 'male',18: 'male',19: 'female',
  20: 'female',21: 'female',22: 'male',23: 'male',24: 'male',25: 'male',26: 'female',
  27: 'female',28: 'male',29: 'female',30: 'male',31: 'female',32: 'female',
  33: 'male',34: 'female'})

x = badabum.value_counts().index
y = badabum.value_counts().values
plt.bar(x, y, color=['pink', 'blue'])
plt.xlabel('количество учеников')  # для оси x
plt.ylabel('пол учеников')  # для оси y
plt.title('соотношение студентов')
plt.show()
