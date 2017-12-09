# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(60,90,20)
y = np.random.randint(2000,8000,20)

x2 = np.random.randint(120,150,20)
y2 = np.random.randint(8200,12000,20)

plt.scatter(x,y , color='r', label ='small size')
plt.scatter(x2,y2 , color='g' , label='big size')
 
plt.title('Home Visualization') 
plt.xlabel('Home Size') 
plt.ylabel('Price')
plt.legend() 
plt.show ()