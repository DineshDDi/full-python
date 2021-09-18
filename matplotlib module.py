#import pandas as pd
import matplotlib.pyplot as plt

plt.bar([.25, 1.25, 2.25, 3.25, 4.25], [11, 20, 14, 19, 15], label="CSK", color='yellow', width=.5)
plt.bar([.75, 1.75, 2.75, 3.75, 4.75], [15, 10, 11, 12, 15], label="MI", width=.5)
plt.xlabel('Overs')
plt.ylabel('Runs')
plt.title('Statistic Board')
x = [.25, .75, 2.25, 3.75, 4.25, 4.75]
y = [13, 17, 16, 14, 17, 17]
plt.scatter(x,y, label="Wickets", color='black', marker=".", s=1300)
plt.legend()
plt.show()






