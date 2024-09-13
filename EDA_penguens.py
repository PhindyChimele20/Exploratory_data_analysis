# -*- coding: utf-8 -*-


Created on Fri Nov 17 11:58:16 2023

@author: Chimele


#Importing libraries
import numpy as np
import pandas as pd
peng = pd.read_csv(r"C:\Users\Chimele\Desktop\datasets\penguins_size.csv")


#description summary of data
peng.describe()
#Checking missing values
peng.isnull().sum()
#replacing missing values
process_column = ['culmen_length_mm', 'culmen_depth_mm', 'flipper_length_mm',
                  'body_mass_g', 'sex']
for item in process_column:
    peng[item].fillna(peng[item].mean(), inplace = True)
    print(peng.iloc())
    peng
peng.isnull().sum()

#data visualization
import matplotlib.pyplot as plt
import seaborn as sns
sns.pairplot(peng.drop(['island'], axis = 1),hue='species')
#body mass distribution
sns.boxplot(x=peng.species,y=peng.body_mass_g,palette='pastel')
plt.title("Body mass distribution",fontsize=18)