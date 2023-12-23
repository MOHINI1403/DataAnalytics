# How to plot histogram
import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
ages=[18,19,20,21,25,26,26,30,32,38,45,55]
c=['red','blue','green','black','#444444']
bins=[20,30,40,50,60] # we have total 5 bins 10-20 20-30 30-40 40-50 50-60 
plt.hist(ages,bins=bins,edgecolor='black') #this will divide all the data into five different bins 

#plt.hist(ages,bins=bins,edgecolor='black',log=True) 
'''
when log value is set true it uses the logarithemic scale on the y axis 
This is useful when dealing with data that spans several orders of magnitude, 
as it can make the distribution more visually interpretable.

'''
median_age=53677

plt.axvline(median_age,color='red',label='Age Median') #this is a line in the histogram which is the age median 
plt.title('Ages of the Respondents')
plt.xlabel('Ages')
plt.ylabel('Total Respondents')

plt.tight_layout()
plt.show()

'''
Histograms allows to create the bin and helps to put the data into those bins and then plot them 

'''