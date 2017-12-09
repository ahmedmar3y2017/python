

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



df = pd.read_csv('E:\computer and information\python projects\dataset/Medicare Hospital Spending by Claim.csv')

print(df.dtypes)

x1=df._getitem_column("Avg_Spending_Per_Episode_Hospital")
x2=df._getitem_column("Avg_Spending_Per_Episode_Nation")


# l1,gpa,histtype='bar',rwidth=0.8
plt.hist(x2, bins=10)
plt.title('our Grades')
# plt.xlabel('Grade')
# plt.ylabel('Gpa')
plt.show ()


