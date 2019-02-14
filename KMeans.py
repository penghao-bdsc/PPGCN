#--encodeing=UTF-8--
import numpy as np  
from sklearn.cluster import KMeans
from sklearn import metrics
 
def kmeans_building(x1,x2,types_num,types,colors,shapes):
    X = np.array(list(zip(x1, x2))).reshape(len(x1), 2)  
    kmeans_model = KMeans(n_clusters=types_num).fit(X)
    x1_result=[]; x2_result=[]
    for i in range(types_num):
        temp=[]; temp1=[]
        x1_result.append(temp)
        x2_result.append(temp1)
    for i, l in enumerate(kmeans_model.labels_):
        print("label:",l)  
        x1_result[l].append(x1[i])
        x2_result[l].append(x2[i])
    return kmeans_model,x1_result,x2_result
if __name__ == "__main__":
    x1 = [1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9] 
    x2 = [1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3]
    colors = ['b', 'g', 'r'] 
    shapes = ['o', 's', 'D']
    labels=['A','B','C'] 
    kmeans_model,x1_result,x2_result=kmeans_building(x1, x2, 3, labels, colors, shapes) 
    print kmeans_model
    print x1_result
    print x2_result
