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
import matplotlib.lines as mlines
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
	ax2.scatter(datingDataMat[:, 1], datingDataMat[:, 2], color= Labelscolor, alpha=0.5)
	plt.xlabel('玩视频游戏所耗时间百分比')
	plt.ylabel('每周消费的冰淇淋公升数')
	plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
	plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
	plt.show()

if __name__ == '__main__':

	filename = "datingTestSet2.txt"
	datingDataMat,datingLabels = file2matrix(filename)
	print(datingDataMat)
	print(datingLabels)

	showdata(datingDataMat,datingLabels)