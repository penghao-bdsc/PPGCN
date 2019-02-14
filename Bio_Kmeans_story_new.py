from sklearn.cluster import KMeans
from sklearn.metrics import normalized_mutual_info_score
from Bio.Cluster import kcluster
from Bio.Cluster import clustercentroids
import numpy as np
data = np.load('meta_story.npy')
label = np.load("ring_story_label.npy")
print label
clusterid, error, nfound = kcluster(data, 2617, dist='k',npass=100)
nmi = normalized_mutual_info_score(label,clusterid)
  
print nmi
