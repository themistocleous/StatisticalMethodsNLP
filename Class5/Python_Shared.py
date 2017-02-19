import pandas as pd
import numpy as np

# Pandas Data Structures
# Series


measurements = pd.Series([328259, 22781, 30857, 4164, 328387])
measurements

measurements.values

measurements.index

measurements[3]


measurements = pd.Series([328259, 22781, 30857, 4164, 328387],
    index=['USA', 'Argentina', 'Sweden', 'Ecuador', 'China'])

measurements

measurements['USA']


measurements[[name.endswith('a') or name.endswith('A') for name in measurements.index]]


[name.endswith('a') or name.endswith('A') for name in measurements.index]

measurements[3]


# Labels

measurements.name = 'Book Counts'
measurements.index.name = 'Countries'
measurements


# NumPy's math functions and other operations can be applied to Series without losing the data structure.

#%%

np.mean(measurements)


# We can also filter according to the values in the `Series`:

#%%

measurements[measurements < 20000]


#%%

measurements[measurements == 22781]


# A `Series` can be thought of as an ordered key-value store. In fact, we can create one from a `dict`:

#%%

Bookpublications = {'Italy':59743, 'Argentina':22781, 'Poland': 31500, 'Vietnam': 24589, 'Indonesia': 24000} 
                         
pd.Series(Bookpublications)


measurements2 = pd.Series(Bookpublications, index=['A','B','C','D', 'E'])
measurements2


#%%

measurements2.isnull()


measurements + measurements2

data = pd.DataFrame({'counts':[ 328259, 22781, 30857, 4164, 328387, 59743,  31500, 24589], 
                       'year':[2010, 2010, 2010, 2010, 2010, 2005, 2010, 2009], 
                    'country':['USA',  'Argentina', 'Sweden', 'Ecuador', 'China', 'Italy', 'Poland', 'Vietnam']})
data


data[['country', 'year', 'counts']]

data.columns

data['counts']

data.counts

type(data.counts)

type(data[['counts']])


data.ix[3]



data = pd.DataFrame({0:{'AA': 1, 'gender': 'Male', 'height': 168},
                    1: {'AA': 2, 'gender': 'Male', 'height': 180},
                    2: {'AA': 3, 'gender': 'Female', 'height': 170},
                    3: {'AA': 4, 'gender': 'Female', 'height': 169},
                    4: {'AA': 5, 'gender': 'Female', 'height': 170},
                    5: {'AA': 6, 'gender': 'Male', 'height': 165}})


#%%
data
data.values
#array([[1, 2, 3, 4, 5, 6],
#       ['Male', 'Male', 'Female', 'Female', 'Female', 'Male'],
#       [168, 180, 170, 169, 170, 165]], dtype=object)



#%%
df = pd.DataFrame({'A': [1,2,3], 'B':[-0.2, 3.0, -2.2]})
df.values

#In [45]:Out[44]:  
#array([[ 1. , -0.2],
#       [ 2. ,  3. ],
#       [ 3. , -2.2]])
    

#%%
# Indices of Series and DataFrames are represented by index.
data.index

#%% We cannot change the index
data.index[1] = 5


#%%
    
    
df = pd.DataFrame({'foo': [1,2,3], 'bar':[0.4, -1.0, 4.5]})
df.values   



# We probably want this transposed:        
# In[48]:

data = data.T
data


# Its important to note that the Series  returned when a DataFrame is indexted is merely a **view** on the  DataFrame, and not a copy of the
# data itself. So you must be cautious when manipulating this data:

# In[49]:

heights = data.height
heights


# %%

heights[5] = 191
heights


# In[50]:

data


# %%

ht = data.height.copy()
ht[5] = 180
data


# We can create or modify columns by assignment:

# In[51]:

data.height[2] = 177
data


# In[52]:

data['Status'] = 'Printed'
data


# But note, we cannot use the attribute indexing method to add a new column:

# In[53]:

data.libraryNo = 999
data


# In[54]:

data.libraryNo


# Specifying a `Series` as a new columns cause its values to be added according to the `DataFrame`'s index:

# In[65]:

test = pd.Series([0]*2 + [3]*2)
test


# In[66]:

data['test'] = test
data


# Other Python data structures (ones without an index) need to be the same length as the `DataFrame`:

# In[70]:

# Popular Authors
authors = ['Stephen King', 'J.K. Rowling', 'Mark Twain', 'George R. R. Martin']
data['authors'] = authors


# In[72]:

authors = ['Stephen King', 'J.K. Rowling', 'Mark Twain', 'George R. R. Martin', 'Charles Dickens', 'Arthur Conan Doyle']
data['authors'] = authors
data


# We can use `del` to remove columns, in the same way `dict` entries can be removed:

# In[73]:

del data['test']
data


# To get the data as a simple `ndarray`  we need to employ the `values` attribute:

# In[74]:

data.values


# Notice that because of the mix of string and integer (and `NaN`) values, the dtype of the array is `object`. The dtype will automatically be chosen to be as general as needed to accomodate all the columns.



# %% Importing data
# %%

get_ipython().system('cat data/duration.csv')


# This table can be read into a DataFrame using `read_csv`:

# %%

dur = pd.read_csv("data/duration.csv", sep=";")
dur


#Note that automatically Python identifies the header line, with the names of the columns. To change this behavior we need to specify that the first line is not a column name. 
# %%

pd.read_csv("data/duration.csv", header=None).head()


# %%

fricative = pd.read_table("data/fricatives.csv", sep=',')
fricative['AA'] = pd.Series(range(1,8827))


# %%
fricative.head()
# %%

list(range(1,len(fricative.index)))

# For a more useful index, we can specify the first two columns, which together provide a unique index to the data.

# %%
testfric=pd.read_csv("data/fricatives.csv", skiprows=[2,3,4,5,6])
len(testfric.index)


# Conversely, if we only want to import a small number of rows from, say, a very large data file we can use `nrows`:

# %%

pd.read_csv("data/fricatives.csv", nrows=4)


# Alternately, if we want to process our data in reasonable chunks, the `chunksize` argument will return an iterable object that can be employed in a data processing loop. For example, our microbiome data are organized by bacterial phylum, with 15 patients represented in each:

# %%

get_ipython().system('cat data/fricatives.csv')


# %%

pd.read_csv("data/fricatives.csv").head(20)


# Above, Pandas recognized `NA` and an empty field as missing data.

# %%

pd.isnull(pd.read_csv("data/fricatives.csv")).head(20)


# Unfortunately, there will sometimes be inconsistency with the conventions for missing data. In this example, there is a question mark "?" and a large negative number where there should have been a positive integer. We can specify additional symbols with the `na_values` argument:
#    

# %%

pd.read_csv("data/fricatives.csv", na_values=['?', -9999999]).head(20)


# These can be specified on a column-wise basis using an appropriate dict as the argument for `na_values`.

# ## Data summarization
# 
# We often wish to summarize data in `Series` or `DataFrame` objects, so that they can more easily be understood or compared with similar data. The NumPy package contains several functions that are useful here, but several summarization or reduction methods are built into Pandas data structures.

# %%

fricative.sum()


# Clearly, `sum` is more meaningful for some columns than others. For methods like `mean` for which application to string variables is not just meaningless, but impossible, these columns are automatically exculded:

# %%

fricative.mean()


# The important difference between NumPy's functions and Pandas' methods is that the latter have built-in support for handling missing data.

# %%

fricative.std()


# %%

fricative.count()


# Observe that we do not get the same counts in the columns.

# %%

fricative.intensity.hasnans


# %%

fricative.intensity.isnull().sum()


fricative.describe()


fricative.sdev.describe()




# ## Writing Data to Files
fricative.to_csv("fricative-01.csv")




#%%
######### MERGING DATAFRAMES WITH PANDAS

df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                    'B': ['B0', 'B1', 'B2', 'B3'],
                    'C': ['C0', 'C1', 'C2', 'C3'],
                    'D': ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])


df2 = pd.DataFrame({'A': ['A4', 'A5', 'A6', 'A7'],
                    'B': ['B4', 'B5', 'B6', 'B7'],
                    'C': ['C4', 'C5', 'C6', 'C7'],
                    'D': ['D4', 'D5', 'D6', 'D7']},
                     index=[4, 5, 6, 7])
 

df3 = pd.DataFrame({'A': ['A8', 'A9', 'A10', 'A11'],
                    'B': ['B8', 'B9', 'B10', 'B11'],
                    'C': ['C8', 'C9', 'C10', 'C11'],
                    'D': ['D8', 'D9', 'D10', 'D11']},
                     index=[8, 9, 10, 11])


frames = [df1, df2, df3]
result = pd.concat(frames)



#%%
DATE and TIME Objects
##########################################################

from datetime import datetime

#%%
now = datetime.now()
now

#%%
now.date()
#%%
now.day
#%%
now.time()
#%%
now.weekday()
#%%

from datetime import date, time

#%%
time(3, 24)

#%%

age = now - datetime(1980, 8, 16)
age/365

#%%

days=(datetime(2017, 3, 10) - datetime(2017, 8, 16))
days.days







##############################################################


# %%

guseblue = '#004b89'
fricative = pd.read_csv("data/fricatives.csv", sep=',')
fricative['duration'].plot(color=guseblue)


# %%
fricative['duration'].plot(kind='hist',color=guseblue)

# %%
fricative['duration'].plot(kind='box',showfliers=False,color=guseblue)


# %%
##########################################################

# Plots using matplot
import matplotlib.pyplot as plt
a = np.arange(1,100,5)
plt.plot(a)
plt.ylabel('Y axis')
plt.show()

#%%
import matplotlib.pyplot as plt
plt.plot([1,2,3,4], [1,4,9,16], 'ro')
plt.axis([0, 6, 0, 20])
plt.show()
#%%

import numpy as np
import matplotlib.pyplot as plt

def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.show()


#%%
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, normed=1, facecolor=guseblue, alpha=0.75)


plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
#%%
import numpy as np
import matplotlib.pyplot as plt

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure(1)

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)


# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)


# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.05)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)

plt.show()
