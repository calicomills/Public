import numpy as np

data = [(0, 2), (1, 3), (2, 4), (3, 5), (4, 6)]
X = []
Y = []
for x in data:
    X.append(x[0])
    Y.append(x[1])

print(X,Y)

x = np.array(X)
y = np.array(Y)
A = np.vstack([x, np.ones(len(x))]).T

m,c= np.linalg.lstsq(A, y, rcond=None)[0]


import matplotlib.pyplot as plt

_ = plt.plot(x, y, 'o', label='Original data', markersize=10)

_ = plt.plot(x, m*x + c, 'r', label='Fitted line')

_ = plt.legend()

plt.show()