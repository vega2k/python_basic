import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set ipython's max row display
pd.set_option('display.max_row', 1000)

# Set iPython's max column width to 50
pd.set_option('display.max_columns', 50)
battles = pd.read_csv('https://raw.githubusercontent.com/chrisalbon/war_of_the_five_kings_dataset/master/5kings_battles_v1.csv')


# Make two variables of the attacker and defender size, but leaving out
# cases when there are over 10000 attackers
large_battles_mask = battles["attacker_size"] + battles["defender_size"] > 10000
large_battles = battles.loc[large_battles_mask,["attacker_size", "defender_size"]]
print(large_battles['attacker_size'],large_battles['defender_size'])

# Create bins of 2000 each
#5000.0 20000.0
print(large_battles['attacker_size'].min(),large_battles['defender_size'].max())
bins = np.arange(large_battles['attacker_size'].min(), large_battles['defender_size'].max(), 2000) # fixed bin size
#[  5000.   7000.   9000.  11000.  13000.  15000.  17000.  19000.]
print(bins)

# Plot a histogram of attacker size
plt.hist(large_battles['attacker_size'],
         bins=bins,
         alpha=0.5,
         color='#EDD834',
         label='Attacker')

# Plot a histogram of defender size
plt.hist(large_battles['defender_size'],
         bins=bins,
         alpha=0.5,
         color='#887E43',
         label='Defender')

# Set the x and y boundaries of the figure
plt.ylim([0, 10])

# Set the title and labels
plt.title('Histogram of Attacker and Defender Size')
plt.xlabel('Number of troops')
plt.ylabel('Number of battles')
plt.legend(loc='upper right')

plt.show()