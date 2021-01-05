import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

raw_data = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'pre_score': [4, 24, 31, 2, 3],
        'mid_score': [25, 94, 57, 62, 70],
        'post_score': [5, 43, 23, 23, 51]}
df = pd.DataFrame(raw_data, columns = ['first_name', 'pre_score', 'mid_score', 'post_score'])

# Create a list of the mean scores for each variable
#[12.800000000000001, 61.600000000000001, 29.0]
mean_values = [df['pre_score'].mean(), df['mid_score'].mean(), df['post_score'].mean()]

# Create a list of variances, which are set at .25 above and below the score
#[3.2000000000000002, 3.2000000000000002, 3.2000000000000002]
variance = [df['pre_score'].mean() * 0.25, df['pre_score'].mean() * 0.25, df['pre_score'].mean() * 0.25]

# Set the bar labels
bar_labels = ['Pre Score', 'Mid Score', 'Post Score']

# Create the x position of the bars
#[0, 1, 2]
x_pos = list(range(len(bar_labels)))

# Create the plot bars
# In x position
plt.bar(x_pos,
        # using the data from the mean_values
        mean_values,
        # with a y-error lines set at variance
        #yerr=variance,
        # aligned in the center
        align='center',
        # with color
        color='#FFC222',
        # alpha 0.5
        alpha=0.5)

# add a grid
plt.grid()

# set height of the y-axis
#(61.600000000000001, 3.2000000000000002)
max_y = max(zip(mean_values, variance)) # returns a tuple, here: (3, 5)
#[0,71.280000000000001]
plt.ylim([0, (max_y[0] + max_y[1]) * 1.1])

# set axes labels and title
plt.ylabel('Score')
plt.xticks(x_pos, bar_labels)
plt.title('Mean Scores For Each Test')

plt.show()