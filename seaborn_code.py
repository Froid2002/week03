# -*- coding: utf-8 -*-

import seaborn as sns 
import matplotlib.pyplot as plt
import os

#create week04 directory if it doesn´t exist to avoid errors
if not os.path.exists("./week04"): os.makedirs("./week04")

#Load the dataset from seaborn library 
df_tips = sns.load_dataset("tips")

#check the first few rows to see the data sctruture
print(df_tips.head())
df_tips.info()

#Part 1
#Creating a figure with 2 areas
