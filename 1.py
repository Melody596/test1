
import csv
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_excel('E:\\python\\excel.xlsx')
total = pd.read_excel('E:\\python\\total.xlsx')

#print(df.fever.value_counts())

#允许显示汉字
plt.rcParams['font.sans-serif'] = ['SimHei']

#窗格大小及标题
plt.figure(figsize = [10,7])
plt.suptitle("疫情统计图")

#数据
#num_cols = ['fever','infect','school']
#print(num_cols)
#print(df.fever.value_counts())

#柱状图
plt.bar(x = total.index.values,height = total['fever'],color = 'steelblue',
        label = 'fever',tick_label = ['2020/1/19','2020/1/20','2020/1/21'])
plt.bar(x = total.index.values,height = total['infect'],color = 'yellow',
        label = 'infect',bottom = total['fever'],
        tick_label = ['2020/1/19','2020/1/19','2020/1/21'])
plt.bar(x = total.index.values,height = total['school'],color = 'red',
        label = 'school',bottom = total['fever']+total['infect'],
        tick_label = ['2020/1/19','2020/1/20','2020/1/21'])
plt.ylabel('人数（人）')
plt.legend(loc = 'best')
plt.show()

