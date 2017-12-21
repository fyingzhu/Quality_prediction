# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 20:21:10 2017

@author: dys
"""

import pandas as pd #数据分析
import numpy as np #科学计算
from pandas import Series,DataFrame

data_train = pd.read_excel("input/训练.xlsx")
data = data_train.drop(['ID','Y','TOOL_ID','Tool','Tool (#2)','TOOL_ID (#1)','TOOL_ID (#2)','TOOL_ID (#3)','tool (#1)','TOOL','TOOL (#1)','TOOL (#2)'],axis=1) # 删除第一列ID
data_drop = data.T.drop_duplicates()