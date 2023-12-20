import csv #standard library to read the csv file 

import numpy as np
from collections import Counter
import matplotlib.pyplot as plt
# we want to show the data as bar chart 

with open('data.csv') as csv_file:
    csv_reader=csv.DictReader(csv_file) #this contains the csv data into the form of rows 
    language_counter=Counter()
    # we need to grab the list of languages from every row 
    for row in csv_reader:
        #loooping over every row in csv_reader
        language_counter.update(row['LanguagesWorkedWith'].split(';'))
        
    print(language_counter) # this would print the occurence of all languages into the column 
    #this would be printed into the desc order sorting 
    
    
    #the counter has the most common method built in
    print(language_counter.most_common(15)) #this would print 15 most common items and it returns the list 
    #every element in this is list s tuple 
    
    languages=[] # this would contains all the languages list
    popularity=[] #this would contain these languages corresponding popularity 
    
    for item in language_counter.most_common(15):
        
        languages.append(item[0])
        popularity.append(item[1])
        print(languages)
        print(popularity)
        
    languages.reverse()
    popularity.reverse()
    plt.barh(languages,popularity)
    plt.title('Popularity_Of_Languages')
    plt.xlabel('Languages')
    plt.ylabel('Popularity')
    
    plt.show()
    
    plt.savefig('Lecture2.png')
    '''row=next(csv_reader) # this gives me the first row data 
    print(row)
    print(row['LanguagesWorkedWith'].split(';')) #reading the LanguagesWorkedWith column and here seperating the data about semi colon 
    '''
    
'''dev_x=[25,26,27,28,29,30,31,32,33,34,35]

x_indexes=np.arange(len(dev_x))  #this will contain the arrange the dev_x values intor numpy array 

width=0.25
#median salary of the ages 
dev_y=[38496,42000,46752,49320,53200,56000,62316,64928,67317,68748,73752]
c=['g','b','r','y','c','k','m','#444444','r','g','b']

py_dev_x=[25,26,27,28,29,30,31,32,33,34,35]
py_dev_y=[45372,48876,53850,57287,63016,65998,70003,70000,71496,75370,83640]
#default width of the bar is 0.8
plt.bar(x_indexes-width,py_dev_y,color='#444444',width=width)

plt.bar(x_indexes,dev_y,color="y",label="All Devs",width=width)

plt.xticks(ticks=x_indexes,labels=dev_x) #to ensure that x axis are labelled properly in Bar charts

plt.xlabel('Ages')
plt.ylabel('Median Salary')
plt.legend(['All Devs','Python Devs'])
plt.show()



    
'''


'''

    In Python, a "counter" typically refers to an object of the Counter class, 
    which is part of the collections module. The Counter class is used to count the occurrences of elements in a collection, 
    usually in a iterable like a list or a tuple. It's a subclass of the built-in dict class.
    
'''

    # Demonstration of the Counter Usage 
    
    
'''

# Accessing the counts
print(my_counter)  # Output: Counter({1: 3, 2: 2, 3: 2, 4: 2, 5: 1, 6: 1})

# Accessing count of a specific element
print(my_counter[1])  # Output: 3
print(my_counter[4])  # Output: 2
print(my_counter[7])  # Output: 0 (element not present in the list)

# Common operations
most_common_element = my_counter.most_common(1)
print(most_common_element)  # Output: [(1, 3)] (most common element and its count)

# Arithmetic operations with Counters
another_list = [1, 2, 3, 4, 5]
another_counter = Counter(another_list)

# Adding Counters
sum_counter = my_counter + another_counter
print(sum_counter)  # Output: Counter({1: 4, 2: 3, 3: 3, 4: 3, 5: 2, 6: 1})

# Subtracting Counters
diff_counter = my_counter - another_counter
print(diff_counter)  # Output: Counter({1: 2})

# Intersection of Counters
intersection_counter = my_counter & another_counter
print(intersection_counter)  # Output: Counter({1: 1, 2: 1, 3: 1, 4: 1, 5: 1})
'''