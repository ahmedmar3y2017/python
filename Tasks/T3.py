

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

grades = [4,9,15,10,13,43,40,36,34,77,75,68,58,22,28,15,28,62,74,23,35,56,50,37] 
gpa = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(grades,gpa,histtype='bar',rwidth=0.8)
plt.title('our Grades')
plt.xlabel('Grade')
plt.ylabel('Gpa')
plt.show ()

