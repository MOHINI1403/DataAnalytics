import pandas as pd
from datetime import datetime,timedelta
from matplotlib import pyplot as plt
from matplotlib import dates as mpl_dates
import seaborn as sns
sns.set(style="darkgrid")

dates=[
    datetime(2019,5,24),
    datetime(2019,5,25),
    datetime(2019,5,26),
    datetime(2019,5,27),
    datetime(2019,5,28),
    datetime(2019,5,29),
    datetime(2019,5,30)
]

y=[0,1,3,4,6,5,7]

plt.plot_date(dates,y,linestyle='solid')

plt.gcf().autofmt_xdate()

date_format=mpl_dates.DateFormatter('%b,%d %Y') # we need to set this format as the x axis
plt.gca().xaxis.set_major_formatter(date_format)

# autofmt_xdate() :  is a method of the figure that automatically adjusts the x-axis date labels to prevent overlapping.
#gcf=>get current figure


plt.title('Time Series Data Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)

# Show the plot
plt.show()

'''
# Sample time series data
date_rng = pd.date_range(start='2023-01-01', end='2023-01-10', freq='D') #the data is spread for every day
data = [10, 15, 20, 18, 25, 30, 28, 35, 40, 38]

# Create a DataFrame
df = pd.DataFrame(data, index=date_rng, columns=['value']) #we are creating the dataFrame over here


# Plot time series data
plt.plot(df.index, df['value'], marker='o', linestyle='-', color='b')

# Customize the plot
plt.title('Time Series Data Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.grid(True)

# Show the plot
plt.show()
'''