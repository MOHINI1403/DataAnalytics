import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
plt.style.use('fivethirtyeight')

#these are static plots 
x_vals=[]
y_vals=[]
index=count() # it just counts out one number at a time and eery time we get the next value 
def animate(i):
    x_vals.append(next(index))
    y_vals.append(random.randint(0,5))
    plt.cla() #this would clear the previous axis 
    plt.plot(x_vals,y_vals) #plotting the new line from scratch
    
    
    '''
        data=pd.read_csv('data.csv')
        x=data['x_value']
        y1=data['total_1']
        y2=data['total_2']
        
        plt.cla()
        plt.plot(x,y1,y2)
        plt.legend(loc='upper left')
        
    '''
    
    
ani=FuncAnimation(plt.gcf(),animate,interval=1000)#first pass the figure we want to animate 

plt.tight_layout()
plt.show()


'''
We are going to see the live changing the data 

'''


'''
# Using the csv file to read data
import csv
import random
import time 
x_value=0
total_1=1000
total_2=1000

fieldnames=['x_value","total_1","total_2"]
with open('data.csv','w') as csv_file:
    csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
    csv_writer.writeheader()
    
while True:
    with open('data.csv','a') as csv_file:
    csv_writer=csv.DictWriter(csv_file,fieldnames=fieldnames)
    info={
        "x_value":x_value,
        "total_1":total_1,
        "total_2":total_2
    }
    csv_writer.writerow(info)
    print(x_value,total_1,total_2)
    
    x_value+=1
    total_1=total_1+random.randint(-6,8)
    total_2=total_2+random.radnint(-5,6)
    
time.sleep(1)

'''