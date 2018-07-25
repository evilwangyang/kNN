#!/usr/bin/python3
# -*- coding:utf-8 -*-

# @Time      :  2018/7/25 10:12
# @Auther    :  WangYang
# @Email     :  evilwangyang@126.com
# @Project   :  kNN
# @File      :  kNN_test3.py
# @Software  :  PyCharm

# ********************************************************* 
import numpy as np
import operator
from os import listdir

def img2vector(filename):
	returnVect = np.zeros((1,1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0,32*i+j] = int(lineStr[j])
	return returnVect

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

def handwritingClassTest():
	hwLabels = []
	traningFileList = listdir('trainingDigits')
	m = len(traningFileList)
	trainingMat = np.zeros((m,1024))
	for i in range(m):
		fileNameStr = traningFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
	testFileList = listdir('testDigits')
	errorCount = 0.0
	mTest = len(testFileList)
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
		classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels,3)
		print('the classifier result is : %d , the real answer is : %d' % (classifierResult, classNumStr))
		if classifierResult != classNumStr:
			errorCount += 1.0
	print('\n the total number of error is : %d' % errorCount)
	print('\n the total error rate is : %f' % (errorCount/float(mTest)))

if __name__ == '__main__':

	handwritingClassTest()
