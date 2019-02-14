#--encodeing=UTF-8--
import numpy as np 
import math 
from sklearn.cluster import KMeans
from sklearn import metrics
 
def kmeans_building(x,types_num):
    kmeans_model = KMeans(n_clusters=types_num).fit(x)
    result=[]
    for i in range(types_num):
        temp=[]
        result.append(temp)
    label = kmeans_model.labels_
    print(label)
    #for i, l in enumerate(kmeans_model.labels_):
    #    print("label:",l)  
    #    result[l].append(x1[i])
    return label#kmeans_model,x1_result,x2_result
def NMI(A,B):
    total = len(A)
    A_ids = set(A)
    B_ids = set(B)
    MI = 0
    eps = 1.4e-45
    for idA in A_ids:
        for idB in B_ids:
            idAOccur = np.where(A==idA)
            idBOccur = np.where(B==idB)
            idABOccur = np.intersect1d(idAOccur,idBOccur)
            px = 1.0*len(idAOccur[0])/total
            py = 1.0*len(idBOccur[0])/total
            pxy = 1.0*len(idABOccur)/total
            MI = MI + pxy*math.log(pxy/(px*py)+eps,2)
    Hx = 0
    for idA in A_ids:
        idAOccurCount = 1.0*len(np.where(A==idA)[0])
        Hx = Hx - (idAOccurCount/total)*math.log(idAOccurCount/total+eps,2)
    Hy = 0
    for idB in B_ids:
        idBOccurCount = 1.0*len(np.where(B==idB)[0])
        Hy = Hy - (idBOccurCount/total)*math.log(idBOccurCount/total+eps,2)
    MIhat = 2.0*MI/(Hx+Hy)
    return MIhat

if __name__ == "__main__": 
    x = np.load("xdata.npy") 
    label = np.load("story_label.npy")
    label_num = 2084 #9941
    
    result = kmeans_building(x ,label_num) 
    np.save("story_result.npy",np.array(result))
    nmi = NMI(result,label)
    print nmi
