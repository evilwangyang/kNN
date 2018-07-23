#!/usr/bin/python3
# -*- coding:utf-8 -*-

# @Time      :  2018/7/19 22:25
# @Auther    :  WangYang
# @Email     :  evilwangyang@126.com
# @Project   :  kNN
# @File      :  kNN.py
# @Software  :  PyCharm Community Edition

# ********************************************************* 
from numpy import *
import operator

def createDataSet():
	group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
	labels = ['A','A','B','B']
	return group,labels

def classify0(inX,dataSet,labels,k):
	dataSetSize = dataSet.shape[0]
	diffMat = tile(inX,(dataSetSize,1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistance = sqDiffMat.sum(axis=1)
	distance = sqDistance**0.5
	sortedDistIndicies = distance.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritesms(),key=operator.itemgetter(1),reverse=True)
	return sortedClassCount[0][0]