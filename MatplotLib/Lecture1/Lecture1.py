import matplotlib.pyplot as plt
print(plt.style.available)

#plt.style.use('ggplot')
#this is actually a method than actually a style
 #plt.xkcd() #comic style 

dev_x=[25,26,27,28,29,30,31,32,33,34,35]
#median salary of the ages 
dev_y=[38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
plt.plot(dev_x,dev_y,color='k',linestyle='--',marker='.')
'''
plt.title('Median Salary (USD) be Age')

plt.xlabel('Ages')
plt.ylabel('Median Salary')
plt.show()
'''
#How to add label to the plots


py_dev_x=[25,26,27,28,29,30,31,32,33,34,35]
py_dev_y=[45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]
plt.plot(py_dev_x,py_dev_y,color='b',marker='o')


plt.title('Median Salary (USD) be Age')

plt.xlabel('Ages')
plt.ylabel('Median Salary')
plt.legend(['All Devs','Python Devs'])

plt.savefig('Lecture1.png') #this would save the image obtained in the png format 

plt.show()

#we need to add the legend to tell which line reperent which set of data 
'''
 We can also add label by adding the label while plotting the graph only 
 plt.plot(ages_x,ages_y,label='All Devs')
 
'''

# to pass the color information while plotting the graph 
'''
    A format string contains of 
    [marker][line][color]
    
    markers: which type of marker 
    Each of them is optional.If not provided the value from the style cycle is used.Exception: If the line is given but no marker
    the data will be line without markers
    
'''


#to make the line more thicker try linewidth parameter

#plt.plot(dev_x,dev_y,color='',linewidth=3,label='Python')

'''
 plt.tight_layout() This improves the padding of the line 
 plt.grid(True) this will give the grid while drawing the graph 
 
 
 Built in styles to use with matplotlib 
 plt.style
    plt.style.available an attirubute that gives me the list of all the styles availbale in matplotlib 
    
plt.style.use('fivethirtyeight') By this we are using a style 
'''