import numpy as np
import matplotlib.pyplot as plt

data1 = np.random.normal(1,3,100000)
# print(data1)

count,bins,ignored=plt.hist(data1,30,density=True)
plt.plot(bins,1/(3*np.sqrt(2*np.pi))*np.exp((-(bins-1)**2)/18),color='red')
plt.savefig('C:/helloPyAnalysis.jpg')