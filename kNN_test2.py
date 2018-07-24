#!/usr/bin/python3
# -*- coding:utf-8 -*-

# @Time      :  2018/7/24 10:29
# @Auther    :  WangYang
# @Email     :  evilwangyang@126.com
# @Project   :  kNN
# @File      :  kNN_test2.py
# @Software  :  PyCharm

# ********************************************************* 
import numpy as np
import operator
import matplotlib.pyplot as plt

def file2matrix(filename):
	fr = open(filename)
	arrayOLines = fr.readlines()
	numberOfLines = len(arrayOLines)
	returnMat = np.zeros((numberOfLines,3))
	classLabelVector = []
	index = 0
	for line in arrayOLines:
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat,classLabelVector

def showdata(datingDataMat,datingLabels):
	fig = plt.figure(figsize=(13,8))
	Labelscolor = []
	for i in datingLabels:
		if i == 1:
			Labelscolor.append('black')
		if i == 2:
			Labelscolor.append('green')
		if i == 3:
			Labelscolor.append('red')
	ax1 = fig.add_subplot(221)
	ax1.scatter(datingDataMat[:,1],datingDataMat[:,2])
	plt.xlabel('玩视频游戏所耗时间百分比')
	plt.ylabel('每周消费的冰淇淋公升数')
	plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
	plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
	ax2 = fig.add_subplot(222)
	ax2.scatter(datingDataMat[:, 0], datingDataMat[:, 1], color= Labelscolor, alpha=0.5)
	plt.xlabel('每年获得的飞行常客里程数')
	plt.ylabel('玩视频游戏所耗时间百分比')
	plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
	plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
	ax3 = fig.add_subplot(223)
	ax3.scatter(datingDataMat[:, 1], datingDataMat[:, 2], color=Labelscolor, alpha=0.5)
	plt.xlabel('玩视频游戏所耗时间百分比')
	plt.ylabel('每周消费的冰淇淋公升数')
	plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
	plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
	ax4 = fig.add_subplot(224)
	ax4.scatter(datingDataMat[:, 0], datingDataMat[:, 2], color=Labelscolor, alpha=0.5)
	plt.xlabel('每年获得的飞行常客里程数')
	plt.ylabel('每周消费的冰淇淋公升数')
	plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
	plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
	plt.show()

def autoNorm(dataSet):
	minVals = dataSet.min(0)
	maxVals = dataSet.max(0)
	ranges = maxVals - minVals
	normDataSet = np.zeros(np.shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - np.tile(minVals,(m,1))
	normDataSet = normDataSet/np.tile(ranges,(m,1))
	return normDataSet,ranges,minVals

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

def datingClassTest(hoRatio):
	datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
	normMat, ranges, minVals = autoNorm(datingDataMat)
	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0
	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m,:], datingLabels[numTestVecs:m], 3)
		print('the classifierResult is %d , the real answer is %d' % (classifierResult, datingLabels[i]))
		if classifierResult != datingLabels[i]:
			errorCount += 1.0
	print('the total error rate is: %f' % (errorCount/float(numTestVecs)))

def classifyperson():
	resultList = ['not at all', 'in small doses', 'in large doses']
	percentTats = float(input('percentage of time spent playing video game?'))
	ffMiles = float(input('frequent flier miles earned per year?'))
	iceCream = float(input('liters of ice cream consumed per year?'))
	datingDateMat,datingLabels = file2matrix('datingTestSet2.txt')
	normMat,ranges,minVals = autoNorm(datingDateMat)
	inArr = np.array([percentTats,ffMiles,iceCream])
	classifierResult = classify0((inArr-minVals)/ranges,normMat,datingLabels,3)
	print('You will probably like this person:',resultList[classifierResult-1])

if __name__ == '__main__':

	# filename = "datingTestSet2.txt"
	# datingDataMat,datingLabels = file2matrix(filename)
	# print(datingDataMat)
	# print(datingLabels)
	#
	# showdata(datingDataMat,datingLabels)
	#
	# autoNorm(datingDataMat)
	#
	# datingClassTest(0.1)

	classifyperson()