#!/usr/bin/python
# coding=utf-8
from numpy import *
import math

def NMI(A,B):
    total = len(A)
    A_ids = set(A)
    B_ids = set(B)
    MI = 0
    eps = 1.4e-45
    for idA in A_ids:
        for idB in B_ids:
            idAOccur = where(A==idA)
            idBOccur = here(B==idB)
            idABOccur = intersect1d(idAOccur,idBOccur)
            px = 1.0*len(idAOccur[0])/total
            py = 1.0*len(idBOccur[0])/total
            pxy = 1.0*len(idABOccur)/total
            MI = MI + pxy*math.log(pxy/(px*py)+eps,2)
    Hx = 0
    for idA in A_ids:
        idAOccurCount = 1.0*len(where(A==idA)[0])
        Hx = Hx - (idAOccurCount/total)*math.log(idAOccurCount/total+eps,2)
    Hy = 0
    for idB in B_ids:
        idBOccurCount = 1.0*len(where(B==idB)[0])
        Hy = Hy - (idBOccurCount/total)*math.log(idBOccurCount/total+eps,2)
    MIhat = 2.0*MI/(Hx+Hy)
    return MIhat

def loadDataSet(fileName): 
    dataMat = []           
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float, curLine)  
        dataMat.append(fltLine)
    return dataMat


def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))


def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k,n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        maxJ = max(dataSet[:,j])
        rangeJ = float(maxJ - minJ)
        centroids[:,j] = minJ + rangeJ * random.rand(k, 1)
    return centroids

def kMeans(dataSet, k, distMeans =distEclud, createCent = randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m,2)))  
    centroids = createCent(dataSet, k)
    clusterChanged = True   
    while clusterChanged:
        clusterChanged = False;
        for i in range(m):  
            minDist = inf; minIndex = -1;
            for j in range(k):
                distJI = distMeans(centroids[j,:], dataSet[i,:])
                if distJI < minDist:
                    minDist = distJI; minIndex = j 
            if clusterAssment[i,0] != minIndex: clusterChanged = True;  
            clusterAssment[i,:] = minIndex,minDist**2  
       # print centroids
        for cent in range(k): 
            ptsInClust = dataSet[nonzero(clusterAssment[:,0].A == cent)[0]]
            centroids[cent,:] = mean(ptsInClust, axis = 0)
    return centroids, clusterAssment
datMat = load("ring_xdata.npy")

myCentroids,clustAssing = kMeans(datMat,2617)
print myCentroids
print clustAssing

result = clustAssing[:,0]
save("KIES_result.npy",result)
label = load("story_label.npy")
nmi = NMI(result,label)
print nmi
