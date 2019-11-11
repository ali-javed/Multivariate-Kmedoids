#if you use this code in your work, please cite it as
#@article{Javed_CoRR2019,
#  author    = {Ali Javed and Scott Hamshaw and Donna M. Rizzo and Byung Suk Lee},
#  title     = {Hydrological and Suspended Sediment Event Analysis using Multivariate Time Series Clustering},
#  journal   = {CoRR},
#  year      = {2019},
#  archivePrefix = {arXiv},
#  bibsource = {dblp computer science bibliography, https://dblp.org}
#  }    



from MultivariateKmedoids import *
import numpy as np

data = []

#variables for observation 1
m1_1 = [1,2,3,4,5,6]
m2_1 = [6,7,8,4,3,2]
temp = []
temp.append(m1_1)
temp.append(m2_1)

data.append(temp)

#variables for observation 2
m1_2 = [200,100,30,40,50,60]
m2_2 = [60,700,800,40,30,20]
temp = []
temp.append(m1_2)
temp.append(m2_2)

data.append(temp)



#variables for observation 3 identical to observation 1
m1_1 = [1,2,3,4,5,6]
m2_1 = [6,7,8,4,3,2]
temp = []
temp.append(m1_1)
temp.append(m2_1)

data.append(temp)



#variables for observation 4 identical to observation 2
m1_2 = [200,100,30,40,50,60]
m2_2 = [60,700,800,40,30,20]
temp = []
temp.append(m1_2)
temp.append(m2_2)

data.append(temp)



data = np.asarray(data)


print(np.shape(data))

window_size = 0.1
max_iter = 10
k = 2
labels, sse_current, iterations, centeroids = MultivariateKmedoids(data, k, max_iter, window_size)

print('ground truth is 0 1 0 1')
print(labels)

