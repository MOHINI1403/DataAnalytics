import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

plt.style.use("fivethirtyeight")
slices=[100,80,30,20] #the value is not supposed to be equal to 100%

labels=['Sixty','Forty','Extra1','Extra2']
explode=[0,0,0.1,0] #this represent by how much radius the pie is exploded from the circle 
colors=['blue','red','yellow','green']
plt.pie(slices,labels=labels,explode=explode,wedgeprops={'edgecolor':'black'},shadow=True,startangle=90,autopct='%1.1f%%')

#passing some wedge properties 
plt.title("My Awesome Pie Chart")
plt.tight_layout()
plt.show()

#to display the percentage of data hold by various portion within the pie chart 
'''
To add the percentage of pie in pie charrt

add autopct='%1.1%%' into the plotting function 
'''








