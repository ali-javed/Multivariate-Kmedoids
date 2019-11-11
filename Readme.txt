

#if you use this code in your work, please cite it as
#@article{Javed_CoRR2019,
#  author    = {Ali Javed and Scott Hamshaw and Donna M. Rizzo and Byung Suk Lee},
#  title     = {Hydrological and Suspended Sediment Event Analysis using Multivariate Time Series Clustering},
#  journal   = {CoRR},
#  year      = {2019},
#  archivePrefix = {arXiv},
#  bibsource = {dblp computer science bibliography, https://dblp.org}
    
 

%%author: Ali Javed 
%email: ajaved@uvm.edu
%Version history:
%Version 1 . basis implementation of Kmedoids algorithm for multi-variate time series that uses dynamic time warping -dependent for distance measure 


##########################################################################################
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
    
    
    
########################################################################

This is code for multivariate time series dynamic time warping using euclidean distance. The code by default calculated dynamic time warping dependent. If you are interested in dynamic time warping independent, simply call the dtw_d function on each variable separately and sum the resulting distances.