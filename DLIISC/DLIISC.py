import numpy as np

'''
A = np.array([[7,8], [8,9], [6,5]])
print(A)
A_ = np.matmul(A.T,A) 
A_pinv = np.matmul(np.linalg.inv(A_), A.T)
A_pinv_lib = np.linalg.pinv(A)
print(A_pinv,A_pinv_lib)
'''
print(2**3)



A = np.array([[3, 1, 1], [-1, 3, 1]])
print("Array A:\n",A)

# Singular-value decomposition
U, s, VT = np.linalg.svd(A)

# create m x n matrix called sigma
sigma = np.zeros((A.shape[0], A.shape[1]))

# populate sigma with n x n diagonal matrix
sigma[:A.shape[0], :A.shape[0]] = np.diag(s)
print("Matrix Sigma:\n",sigma)

# reconstruct the original matrix
B = U.dot(sigma.dot(VT))

print("Matrix U\n",U)
print("Matrix s\n",s)
print("Matrix VT\n",VT)
print("Reconstructed Matrix B\n",B)



df1 = pd.DataFrame({'X=0': '?', 'X=1':0.2, 'X=3': 0.3, 'X=4': 0.1}, index= ['P(X=xi)'])
