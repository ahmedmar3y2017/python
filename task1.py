import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

from matplotlib import rcParams

df = pd.read_csv('E:\computer and information\python projects\dataset/Hospital Returns - Hospital.csv')
# print(df.head(10))
# print(df.describe())
# print(df.isnull().any())
# print(df.dtypes)


# count attribute in the column 
# print(df['City'].value_counts())
fig = plt.figure(figsize=(12, 6))
sqft = fig.add_subplot(121)

sqft.hist(df.City, bins=80)
sqft.set_xlabel('Provider ID')
sqft.set_title(" Histogram of NPI Footage")
plt.show()
print(df['Provider ID'].hist(bins=50))
# print(df['Provider ID'].hist(bins=50))
df.boxplot(column='Provider ID')



