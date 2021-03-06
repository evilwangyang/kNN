#!/usr/bin/python3
# -*- coding:utf-8 -*-

# @Time      :  2018/7/19 22:25
# @Auther    :  WangYang
# @Email     :  evilwangyang@126.com
# @Project   :  kNN
# @File      :  kNN_test1.py
# @Software  :  PyCharm Community Edition

# ********************************************************* 
import numpy as np
import operator

def createDataSet():
	group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def classify0(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0]
	diffMat = np.tile(inX,(dataSetSize,1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	sortedDistIndicies = distances.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]

if __name__ == '__main__':

	group,labels = createDataSet()
	test = [0,0]
	testclass = classify0(test,group,labels,3)
	print(testclass)

