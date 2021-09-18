import numpy as np
#import pandas as pd
import matplotlib.pyplot as plt

time = np.arange(100)
delta = np.random.uniform(10,10,size=100)
y = 3*time - 7+delta

plt.plot(time,y)
plt.title("matplotlib")
plt.xlabel("time")
plt.ylabel("function")

plt.show()
