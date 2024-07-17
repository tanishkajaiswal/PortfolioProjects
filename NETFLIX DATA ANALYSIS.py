
# coding: utf-8

# # NETFLIX DATA ANALYSIS

# In[2]:


#importing the datasheet
import pandas as pd    #import pandas library
data= pd.read_csv(r"D:\data analysis\netflix dataset.csv") #import dataset to a dataframe


# In[3]:


data


# Getting some basic information about the dataset

# In[4]:


#head()- to show top 5 records of the dataset
data.head()  


# In[5]:


#tail()- to show last 5 records of the data set
data.tail()


# In[6]:


#shape- to show the number of rows and columns
data.shape


# In[7]:


#size- to show total number of values in a dataset
data.size


# In[8]:


#columns - to show names of each column
data.columns


# In[9]:


#dtypes - to show the data types of each column
data.dtypes


# # 1. Check for any duplicates and remove them

# In[2]:


#info()- to show indexes, columns, data types of each column, memory at once
import pandas as pd    #import pandas library
data= pd.read_csv(r"D:\data analysis\netflix dataset.csv")
data.info()


# In[3]:


data.duplicated()


# In[4]:


data[data.duplicated()]                   #to check rowwwise and detect the duplicates


# In[5]:


data.drop_duplicates()                    #remove the duplicates   TEMPORARY


# In[6]:


data.drop_duplicates(inplace = True)          #Permanent removal


# In[7]:


data[data.duplicated()]                   #to check rowwwise and detect the duplicates again


# # 2. Check any null values and show using heat map

# In[8]:


data


# In[9]:


#isnull()
data.isnull()


# In[10]:


data.isnull().sum()


# Seaborn library (heat map)

# In[11]:


import seaborn as sns


# In[12]:


sns.heatmap(data.isnull())


# In[4]:


# 1. SHOW THE SHOWID AND DIRECTOR OF "HOUSE OF CARDS"
import pandas as pd
data= pd.read_csv(r"D:\data analysis\netflix dataset.csv")
#METHOD 1
data[data['Title'].isin(['House of Cards'])]


# In[7]:


#METHOD 2
data[data['Title'].str.contains('House of Cards')]


# In[9]:


#2. Bar graph to show wich year had the highest number of releases
data['Date_N']=pd.to_datetime(data['Release_Date'])  #creation of a new column in date time format
data['Date_N'].dt.year.value_counts()              #counts occurrence if all individual years in date column


# In[11]:


# BAR Graph
data['Date_N'].dt.year.value_counts().plot(kind='bar')


# In[12]:


#3. How many movies and tv shows are in the dataset with bar graph
data.groupby('Category').Category.count()


# In[13]:


data.groupby('Category').Category.count().plot(kind='bar')


# In[15]:


#second way of plotting
import seaborn as sns
sns.countplot(data['Category'])


# In[19]:


#4. All the movies released in year 2020
data['Year']=data['Date_N'].dt.year     #create new column for year


# In[20]:


data[ (data['Category']=="Movie") & (data['Year']==2020)]


# In[23]:


#5. All TV shows released in India only
data[ (data['Category']=='TV Show') & (data['Country']=='India')]


# In[24]:


data[ (data['Category']=='TV Show') & (data['Country']=='India')] ['Title']


# In[26]:


#6. Top 10 directors with highest number of movies and TV shows
data['Director'].value_counts().head(10)


# In[28]:


#7. Show all records for Comedy Movies or released in the United Kingdom
data [ (data['Category']=='Movie') & (data ['Type']=='Comedy') | (data['Country']=='United Kingdom')]


# In[29]:


#8. Movies of Tom Cruise
data[data['Cast']=='Tom Cruise']             #will show where only Tom cruise is the cast


# In[32]:


#Create a new datafrae and remove all the nul values then use str contains
data_new=data.dropna()
data_new[data_new['Cast'].str.contains('Tom Cruise')]


# In[33]:


#9. Different ratings defined by netflix

data['Rating'].unique()


# In[3]:


#9.1 Movies with TV-14 Rating in Canada
import pandas as pd
data= pd.read_csv(r"D:\data analysis\netflix dataset.csv")
data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')]


# In[4]:


data[(data['Category']=='Movie') & (data['Rating']=='TV-14') & (data['Country']=='Canada')].shape


# In[9]:


#9.2 TV Shows with R rating after 2018
import pandas as pd
data['Date_N']=pd.to_datetime(data['Release_Date'])  #creation of a new column in date time format
data['Date_N'].dt.year.value_counts()          
data['Year']=data['Date_N'].dt.year
data[(data['Category']=='TV Show') & (data['Rating']=='R') & (data['Year']>2018)]


# In[11]:


#10 Which country has the highest Number of TV Shows
#create dataframe for TV Shows
data_tvshow=data[data['Category']=='TV Show']


# In[13]:


data_tvshow.Country.value_counts().head(1)


# In[14]:


#11 Sort Dataset by year
data.sort_values(by='Year')


# In[15]:


data.sort_values(by='Year', ascending='False')


# In[16]:


#11.2 latest 10 records
data.sort_values(by='Year', ascending='False').head(10)


# In[18]:


#12. show all drama movies
data[(data['Category']=='Movie') & (data['Type']=='Dramas')]


# In[20]:


#Kids TV Show
data[(data['Category']=='TV Show') & (data['Type']=="Kids' TV")]


# In[21]:


#Either of them
data[((data['Category']=='TV Show') & (data['Type']=="Kids' TV"))|((data['Category']=='TV Show') & (data['Type']=="Kids' TV"))]

