import pandas as pd
import numpy as np
import random
import pdb
from matplotlib import pyplot as plt

# The algorithm starts at x=3
cur_x = 3
# Learning rate
rate = 0.01 
# This tells us when to stop the algorithm
#precision = 0.000001 
precision = 0.0000000001
previous_step_size = 1
# Maximum number of iterations 
max_iters = 10000
# Iteration counter 
iters = 0 
# Gradient of our function
f = lambda x: (x+5)**2
df = lambda x: 2*(x+5)

y_m = []
x_m = []
while previous_step_size > precision and iters < max_iters:
    # Store current x value in prev_x
    x_m.append(cur_x)
    y_m.append(f(cur_x))
    prev_x = cur_x 
    # Gradient descent
    cur_x = cur_x - rate * df(prev_x) 
    # Change in x
    previous_step_size = abs(cur_x - prev_x) 
    # Iteration count
    iters = iters+1 
    # Print iterations
    print("Iteration",iters,"\nX value is",cur_x) 
    
print("The local minimum occurs at", cur_x)