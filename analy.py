# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:21:10 2017

@author: dys
"""

import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame

data_train = pd.read_excel("input/训练.xlsx")
data_testA = pd.read_excel("input/测试A.xlsx")
data_testB = pd.read_excel("input/测试B.xlsx")

#对训练集和测试集同时进行操作，以保持一致性
combine = [data_train, data_testA, data_testB] # combine为list类型
print("Before:", data_train.shape, data_testA.shape, data_testB.shape, combine[0].shape, combine[1].shape, combine[2].shape)

# 机台号数字化转换
## 设置字典，其中'E0':6, 'N0':7, 'XY1':8, 'YX1':9
DICT = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'E0':6, 'N0':7, 'XY1':8, 'YX1':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14,
    'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24 }  #'F':6, 'G':7, 'H':8, 'I':9,'Y':25, 'Z':26
for dataset in combine:
    dataset['TOOL_ID'] = dataset['TOOL_ID'].map(DICT).astype(int)
    dataset['Tool'] = dataset['Tool'].map(DICT).astype(int)
    dataset['Tool (#2)'] = dataset['Tool (#2)'].map(DICT).astype(int)
    dataset['TOOL_ID (#1)'] = dataset['TOOL_ID (#1)'].map(DICT).astype(int)
    dataset['TOOL_ID (#2)'] = dataset['TOOL_ID (#2)'].map(DICT).astype(int)
    dataset['TOOL_ID (#3)'] = dataset['TOOL_ID (#3)'].map(DICT).astype(int)
    dataset['tool (#1)'] = dataset['tool (#1)'].map(DICT).astype(int)
    dataset['TOOL'] = dataset['TOOL'].map(DICT).astype(int)
    dataset['TOOL (#1)'] = dataset['TOOL (#1)'].map(DICT).astype(int)
    dataset['TOOL (#2)'] = dataset['TOOL (#2)'].map(DICT).astype(int)
	
