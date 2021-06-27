import seaborn as sns
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd
from scipy import integrate
import math

X = [0, 1, 2, 3]   # Number of heads we can get are

P_X0 = 1/8   # P(X=0)     {TTT}
P_X1 = 3/8   # P(X=1)     {HTT, THT, TTH}
P_X2 = 3/8   # P(X=2)     {HHT, HTH, THH}
P_X3 = 1/8   # P(X=3)     {HHH}
P_Xi = [P_X0, P_X1, P_X2, P_X3]

'''
sns.barplot(x= X, y= P_Xi)
plt.title('PMF'); plt.xlabel('Number of heads'); plt.ylabel('Probability')
plt.show()

sns.barplot(x= X, y= np.array(P_Xi).cumsum())
plt.title('Cumulative Distribution Function'); plt.xlabel('Number of heads'); plt.ylabel('Cumulative Probability')
plt.show()

k = 1 / (integrate.quad(lambda x: x**3, 0, 3)[0])        # integrate  x^3  w.r.t  x from 0 to 3
print('k= ', round(k,4))

x = np.linspace(0,3,100)
df2 = pd.DataFrame({'X':[], 'PDF':[], 'CDF':[]})
df2['X'] = x
df2['PDF'] = df2['X'].apply(lambda v: k*v**3)
df2['CDF'] = df2['X'].apply(lambda v: integrate.quad(lambda u: k*u**3, 0, v)[0])
df2.head()

lis = []
lis2 = []
for i in range(6):
    lis2.append(i)
    if  i<=2:
       i+=4
       lis.append(i) 
    else:
      lis.append(i)

k = 1/sum(lis)
print("The value of K is:", k)
data  = {
    "values": lis,
    "keys": lis2
    }
df = pd.DataFrame(data)
print(df["values"].keys)
df["probability_distribution"] = df["values"] *k
print(df["probability_distribution"].sum())
#creating a new column with the product of the columns of values and probability
df['expected_value'] = df['keys']*df['probability_distribution']
#expected value 
print("The expected value is:",df['expected_value'].sum())


from scipy.stats import bernoulli

data_bernoulli = bernoulli.rvs(size=10000,p=0.5)
ax= sns.displot(data_bernoulli,
                 kde=False)
ax.set(xlabel='Bernoulli Distribution', ylabel='Frequency')
plt.show()
'''

k = [9, 2, 5, 4, 12, 7, 8, 11]
mean = sum(k)/len(k)
diff = 0
for num in k:
    diff += (num - mean)**2

sd = math.sqrt(diff/ len(k))
print(sd)

def bern_post(n_params=1000, n_sample=1000, true_p=.5, prior_p=.5, n_prior=1000):
    # Creating the samples   
    params = np.linspace(0, 1, n_params)
    sample = np.random.binomial(n=1, p=true_p, size=n_sample)

    # Calculating the Likelihood
    likelihood = np.array([np.product(st.bernoulli.pmf(sample, p)) for p in params])
    likelihood = likelihood / np.sum(likelihood)

    # Prior sample
    prior_sample = np.random.binomial(n=1, p=prior_p, size=n_prior)
    prior = np.array([np.product(st.bernoulli.pmf(prior_sample, p)) for p in params])
    prior = prior / np.sum(prior)

    # Finding the posterior  
    posterior = [prior[i] * likelihood[i] for i in range(prior.shape[0])]
    posterior = posterior / np.sum(posterior)
    
    # Plotting the graph
    fig, axes = plt.subplots(3, 1, sharex=True, figsize=(8,8))
    axes[0].plot(params, likelihood)
    axes[0].set_title("Sampling Distribution")
    axes[1].plot(params, prior)
    axes[1].set_title("Prior Distribution")
    axes[2].plot(params, posterior)
    axes[2].set_title("Posterior Distribution")
    sns.despine()
    plt.tight_layout()
     
    return posterior

    matrix = np.random.randint(10, size=(3, 3))
print("The matrix is:", matrix)
cov_matrix = np.cov(matrix)
var_matrix = np.var(matrix, dtype = np.float64)
print("The covariance of the matrix is :",cov_matrix)
print("\n Variance of array is : ", var_matrix) 