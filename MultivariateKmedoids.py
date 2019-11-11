
import numpy as np
import random
from DTW_D import *

#if you use this code in your work, please cite it as
#@article{Javed_CoRR2019,
#  author    = {Ali Javed and Scott Hamshaw and Donna M. Rizzo and Byung Suk Lee},
#  title     = {Hydrological and Suspended Sediment Event Analysis using Multivariate Time Series Clustering},
#  journal   = {CoRR},
#  year      = {2019},
#  archivePrefix = {arXiv},
#  bibsource = {dblp computer science bibliography, https://dblp.org}
#  }    
 

def assign(timeseries, k, centeroids, window_size):
    #####################################################
    #inputs: 
    #timeseries : shape x by y by z, where x is the number of time series to cluster, y is the dimensionality, and z is the length of each timeseries.
    #k          : Number of clusters
    #centeroids : Index of each medoid in timeseries
    #window size: Absolute window size i.e. number of time steps to consider in window
    
    #output:
    #labels   : Assigned labels to each time series in the input of all time series
    #sse      : Sum of squared error
    
    ##########################################################
    
    labels = []
    sse = 0
    
    #for all points in time series
    for i in range(0, len(timeseries)):
        #initilize distance to each centeroid as infinity
        dist_to_center = np.zeros(k)
        dist_to_center = dist_to_center+float('inf')

        #calculate distance to each centeroid
        for j in range(0, len(centeroids)):
            ob1 = timeseries[i]
            ob2 = timeseries[centeroids[j]]
            ob1 = np.reshape(ob1, (1, np.shape(ob1)[0], np.shape(ob1)[1]))
            ob2 = np.reshape(ob2, (1, np.shape(ob2)[0], np.shape(ob2)[1]))
            dist_to_center[j] = dtw_d(ob1,ob2,window_size)
            
        #find closest medoid to ith time series

        c = np.argmin(dist_to_center)
        labels.append(c)
        

        #error checking
        if dist_to_center[c]!=dist_to_center[c]:
            print('Error: Possible nan values in data')
            
        sse = sse + dist_to_center[c]

    labels = np.asarray(labels)
    if len(set(labels))< k:
        #one cluster never got made
        # create random centeroid for that cluster
        for i in range(k):
            if i not in set(labels):

                centeroid_index = random.sample(range(0, len(timeseries)), 1)
                labels[centeroid_index]=i

    return labels, sse



def find_central_node(timeseries,window_size,labels,k):
    labels = np.asarray(labels)
    centeroids = []
    closest_observations = []
    
    #for each cluster
    for i in range(k):
        
        #get observations of assigned to that cluster
        elements = np.where(labels == i)[0]
        
        #we will make each observation as a centeroid. Set the SSE to zero if a particular observation is the centeroid
        distances = np.zeros(len(elements))
        
        #for each observation in the cluster
        for j in range(0,len(elements)):

            #make observation temperarily as centeroid
            temp_centeroid = timeseries[elements[j]]
            
            #for each observation in the cluster measure its distance to temperary centeroid
            for l in range(0,len(elements)):
                ob1 = temp_centeroid
                ob2 = timeseries[elements[l]]
                ob1 = np.reshape(ob1, (1, np.shape(ob1)[0], np.shape(ob1)[1]))
                ob2 = np.reshape(ob2, (1, np.shape(ob2)[0], np.shape(ob2)[1]))
                distances[j] = distances[j]+dtw_d(ob1,ob2,window_size)
                
                
        #select observation that minimizes SSE

        c = np.argmin(distances)
        #the actual time series of centeroid
        centeroids.append(timeseries[elements[c]])
        #the index number of centeroid in time series
        closest_observations.append(elements[c])
        
        
    if len(centeroids)<k:
        print('Error: centeroids are not k')
        
    
    return np.asarray(centeroids), np.asarray(closest_observations)
        
    


def MultivariateKmedoids(timeseries, k, max_iter, window_size):
    ###########################################################################################################
    #Author: Ali Javed
    #Date September 17th 2019. 
    #Email: ali.javed@uvm.edu
    #Please note the code is not maintained. 
    
    #Inputs
    #timeseries : shape x by y by z, where x is the number of time series to cluster, y is the dimensionality, and z is the length of each timeseries.
    #k          : is the number of clusters.
    #max_iter   : maximum iterations to perform incase of no convergence.
    #window_size: is the dynamic time wrapping window size as a ration i.e. 0 to 1.
    
    
    #outputs
    #labels    : cluster number for each time series.
    #sse_all   : sum of squared errors in each iteration. 
    #j         : number of iterations performed.
    #closest_observations_prev: Centeroids
    
    
    
    ###########################################################################################################

    #create a empty labels array set to -1
    labels = np.ones(len(timeseries))
    labels = labels * -1

    #number of series
    dimensions = np.shape(timeseries)[1]
    
    # DECLARE LISTS
    sse_all = []



    #create random centeroids
    centeroid_index = random.sample(range(0, len(timeseries)), k)


    #take centeroids of all series
    centeroids = np.zeros((k, dimensions, np.shape(timeseries)[2]))
    for i in range(0,dimensions):
        centeroids_temp = timeseries[:,i,:][centeroid_index]
        centeroids[:,i,:] = centeroids_temp
        #centeroids.append(centeroids_temp)
        
    #reshape centeroids for the first index to represent centeroid
    #centeroids = np.asarray(centeroids)
    #centeroids = np.reshape(centeroids,(k,dimensions,np.shape(timeseries)[2]))


    
        
        
    
    sse_current = float('inf')
    conv_itr = 0
    closest_observations = centeroid_index
    
    
    #start iterations
    for j in range(0, max_iter):
        sse_previous = sse_current
        closest_observations_prev = closest_observations
        
        #assign observation to each centeroid
        labels, sse_current = assign(timeseries, k, closest_observations, window_size)
        

        if sse_current != sse_current:
            print('Error 888: value of k voilated or presence of nan values.')
            break

        # calculate new centeroids
        centeroids, closest_observations= find_central_node(timeseries,window_size,labels,k)
        


        # TERMINATION CRITERIA
        if np.abs(sse_current - sse_previous) == 0:
            conv_itr += 1
            if conv_itr > 1:
                labels, sse_current = assign(timeseries, k, closest_observations, window_size)
                break
        

    return labels, sse_current, j, closest_observations_prev


