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
    x1 = [1, 2, 3, 1, 5, 6, 5, 5, 6, 7, 8, 9, 7, 9] 
    x2 = [1, 3, 2, 2, 8, 6, 7, 6, 7, 1, 2, 1, 1, 3]
    colors = ['b', 'g', 'r'] 
    shapes = ['o', 's', 'D']
    labels=['A','B','C'] 
    kmeans_model,x1_result,x2_result=kmeans_building(x1, x2, 3, labels, colors, shapes) 
    print kmeans_model
    print x1_result
    print x2_result
