from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")

minutes=[1,2,3,4,5,6,7,8,9]
player1=[1,2,3,3,4,4,4,4,5]
player2=[1,1,1,1,2,2,2,3,4]
player3=[1,1,1,2,2,2,3,3,3]
#plt.pie([1,1,1],labels=['Player 1',"player 2","Player 3"])
labels=['Player 1','Player 2','Player 3']
colors=['red','green','blue']
plt.stackplot(minutes,player1,player2,player3,labels=labels,colors=colors)
plt.legend(loc='upper left') #where the marking for various color are located 

#First pass the x axis value that represent progression
plt.title("My Awesome Stack Plot")
plt.tight_layout()
plt.show()
plt.savefig('Lecture4.png')

'''
    This could be used when some team are working on a project and which person is working the most onto the project
'''


'''
Stackplot is used to draw a stacked area plot. 
It displays the complete data for visualization. 
It shows each part stacked onto one another and how each part makes the complete figure.
It displays various constituents of data and it behaves like a pie chart. 
It has x-label, y-label, and title in which various parts can be represented by different colors. 

'''