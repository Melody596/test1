import csv
import matplotlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np





def age_Dis():
    df = pd.read_csv('E:\\python\\excel.csv')
    print(df)
    print()
    age = []
    for i in df['age']:
        age1=[]
        age2=[]
        age3=[]
        age4=[]
        age5=[]
        for i in age:
            if 18<=i<25:
                age1.append(i)
            elif 25<=i<35:
                age2.append(i)
            elif 35<=i<45:
                age3.append(i)
            elif 45<=i<55:
                age4.append(i)
            else:
                age5.append(i)

                index=['18~25','25~35','35~45','45~55','others']
                values=[len(age1),len(age2),len(age3),len(age4),len(age5)]
                plt.bar(index,values)
                plt.show()


