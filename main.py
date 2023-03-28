# Import Preprocess from your library
from tweets_preprocess import Preprocess
import pandas as pd
import numpy as np

# Instantiate a Preprocess object
data = pd.read_excel(r"D:\Ipac_new\My_Python_Lib\tweet_preprocess\sample.xlsx")
data['pre_text'] = ""

p = Preprocess(data,'Text')
d = p.process()

data['pre_text'] = pd.Series(d)

#print(data.isna().sum())
print(data.shape)

d1 = data.loc[data['pre_text']!='']
print(d1.shape)

d1.to_csv('pre-data.csv')




