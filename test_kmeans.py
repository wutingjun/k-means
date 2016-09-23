from numpy import *
import kmeans

## step 1: load data
print "step 1: load data..."
dataSet = []
fileIn = open('testSet.txt')
for line in fileIn.readlines():
	lineArr = line.strip().split('\t')
	dataSet.append([float(lineArr[0]), float(lineArr[1])])
dataSet = mat(dataSet)

# step 2: clustering...
print "step 2: clustering..."
k = 4
centroids,clusterAssment =kmeans.kmeans(dataSet, k)
print centroids
print clusterAssment

# step 3: show the result
print "step 3: show the result..."
kmeans.showCluster(dataSet,k,centroids,clusterAssment)