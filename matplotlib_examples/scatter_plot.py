import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'last_name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze'],
        'female': [0, 1, 1, 0, 1],
        'age': [42, 52, 36, 24, 73],
        'preTestScore': [4, 24, 31, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70]}

df = pd.DataFrame(raw_data, columns = ['first_name', 'last_name', 'age', 'female', 'preTestScore', 'postTestScore'])

fig = plt.figure()
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

#Scatterplot of preTestScore and postTestScore, with the size of each point determined by age
ax1.scatter(df.preTestScore, df.postTestScore, s=df.age)

#Scatterplot of preTestScore and postTestScore with the size = 300 and the color determined by sex
ax2.scatter(df.preTestScore, df.postTestScore, s=300, c=df.female)
#plt.legend()
plt.show()