import pandas as pd
from matplotlib import pyplot as plt

data=pd.read_csv('data.csv')

ages=data['Age']
dev_salaries=data['All Devs']
py_salaries=data['Python']
js_salaries=data['Javascript']

plt.plot(ages,dev_salaries,color='#444444',linestyle='--',label='All Devs')
plt.plot(ages,py_salaries,label='Python')
overall_median=57287

plt.fill_between(ages,py_salaries,overall_median,where=(py_salaries>overall_median),interpolate=True,alpha=0.25)


#y2 is set to 0 by default 
plt.legend()

plt.title('Median Salary (USD) by Age')
plt.xlabel('Ages')
plt.ylabel('Median Salary (USD) ')
plt.tight_layout()

'''
A common application for fill_between is the indication of confidence bands.

fill_between uses the colors of the color cycle as the fill color. These may be a bit strong when applied to fill areas. 
It is therefore often a good practice to lighten the color by making the area semi-transparent using alpha.

'''


'''

'''