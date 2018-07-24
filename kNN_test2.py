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

if __name__ == '__main__':

	filename = "datingTestSet2.txt"
	datingDataMat,datingLabels = file2matrix(filename)
	print(datingDataMat)
	print(datingLabels)