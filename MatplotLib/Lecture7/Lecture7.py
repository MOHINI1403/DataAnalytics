import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")

x=[5,7,8,5,6,7,9,2,3,4,4,4,2,6,3,6,8,6,4,1]
y=[7,4,3,9,1,3,2,5,2,4,8,7,1,6,4,9,7,7,5,1]
#argument s sets the size of the dots

colors=[7,5,9,7,5,7,2,5,3,7,1,2,8,1,9,2,5,6,7,5]
sizes=[209,486,381,255,191,315,185,228,174,538,239,394,399,153,273,293,436,501,397,539]
plt.scatter(x,y,s=sizes,marker='o',c=colors,cmap='Greens',edgecolors='black',linewidths=1,alpha=0.75)
cbar=plt.colorbar()
cbar.set_label('_Satisfaction Level_')

'''
This parameter maps scalar values to colors using a colormap. In your case, it's set to 'Greens'.
'''
plt.tight_layout()
plt.show()
plt.savefig('Lecture7.png')

'''
    SCATTER PLOTS
We are using the plot style of seaborn 

'''