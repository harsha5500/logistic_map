# Simple python script to plot logistic map
import matplotlib.pyplot as plt
import random
import numpy as np
import pandas as pd

# Number of terms or generations
NUM_TERMS = 100

def get_next_X(r,x):
    next_x = r * x * (1 - x)
    return next_x

def get_map(r,inital_x):
    x_vals = []
    x_vals.append(inital_x)
    for term in range(0,NUM_TERMS):
        current_x = x_vals[-1]
        x_vals.append(get_next_X(r,current_x))
    return x_vals

# get a random number between 0,1 for inital growth number
x_n = random.uniform(0,1)
R = np.arange(1,4,0.5)
data =[]

for r in R:
    data.append(get_map(r,x_n))

numpy_data = np.array(data)
df = pd.DataFrame(data=numpy_data).T
df.columns = R

ax = df.plot(figsize=(7,7),legend=True,title="Logistic Map")
ax.set_xlabel("R value")
ax.set_ylabel("Population Growth")
plt.show()
