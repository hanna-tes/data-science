#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import neccessary modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# read csv file 
tweet=pd.read_csv('C:/Users/Dejen/Desktop/sample_tweets.csv')


# In[3]:


# display the first 10 rows
tweet.head(10)


# In[4]:


# drop irrelevant column
tweet.drop(['Unnamed: 0'],axis=1,inplace=True)


# In[47]:


# check if we drop the column unnamed 0 from our dataset
tweet.head()


# In[6]:


# view some basic statistical details like percentile, mean, std and min max values.
tweet.describe()


# In[7]:


# display the list of all the columns in the dataset and the type of data each column contains. 
# here we have 4 int or numerical values and 12 catagorical and string values
tweet.info()


# In[8]:


# display the number of rows and columns 
tweet.shape


# In[9]:


tweet.describe(include='O')# list only non-numeric values


# In[10]:


# check non or missing values for each attributes
tweet.isna().sum()


# In[11]:


# fill categorical column values with mode and contineous values with mean

cat=tweet.select_dtypes(include=['object']).columns.tolist()
intt=tweet.select_dtypes(include=['int64']).columns.tolist()
for column in tweet:
    if tweet [column].isnull().any():
        if(column in cat):
            tweet[column]=tweet[column].fillna(tweet[column].mode()[0])
        else:
            tweet[column]=tweet[column].fillna(tweet[column].mean)


# In[12]:


tweet.isnull().sum()


# In[66]:


# duplicated contents or tweets
tweet.content[tweet.content.duplicated()==True]


# In[71]:


# to the number of tweets which are duplicated
tweet.content.duplicated().sum()


# Identify the group of accounts on the dataset

# In[14]:


# identify all unique groups of account category column
tweet.account_category.unique()


# Identify subgroups based on volume of tweets in each category

# In[15]:


tweet.account_category.value_counts()


# Identify number of unique account for each category

# In[16]:


tweet['account_type'].value_counts()


# In[17]:


# replace account type value denoted as ? with unknown
tweet["account_type"] = tweet["account_type"].str.replace('?', 'unkonwn')


# In[18]:


# unique account for each account category and from the out put we can see that the highest number of tweets
# are from RightTroll category and this tells us most of the tweets in this dataset are trolls which spreads provokes,
# rumors, disinformation, and speculation contents.

tweet[['account_type','account_category']].value_counts()


# In[19]:


# number of unique account for each categorical values in the dataset
tweet[['account_type','account_category','post_type','region','language']]


# Who is the most prominent author for each catagory 
# 
# The out put shows the most prominent author is ameliebaldwin, and this author is in the right troll category and most of his 
# activities focus on retweeting

# In[20]:


#identify the most prominant author for each catagorical value
tweet[['author','account_category','account_type','post_type','region','language']].value_counts()


# In[21]:


# converting the object dtype to datetime format
import datetime
tweet["publish_date"]= pd.to_datetime(tweet["publish_date"])
tweet['publish_date'] = pd.to_datetime(tweet['publish_date'], format='%Y%m%d')


# In[22]:


tweet.publish_date


# In[23]:


#total tweets
len(tweet.index)
print ('Total tweets :', len(tweet.index), '\n')


# identify the account name and who posted the first tweet

# In[24]:


# the first tweet were made by author ABIGAILSSILK in 2014/27/11 
tweet.groupby('author').agg({'publish_date':'min'}).sort_values(['publish_date'], ascending=True)


# In[25]:


len(tweet.content.unique())


# identify the date that has the highest volume of tweet 

# In[26]:


# covert datetime format in to date so that we can get the only the y/m/d values
tweet['date'] = tweet['publish_date'].dt.date


# In[27]:


tweet.date.value_counts()


# In[28]:


# in the date 2018/20/3 we have highest volume of tweets

tweet["date"].agg(np.max)


# Identify the author of this tweet
# 
# "I am here for a purpose and that purpose is to grow into a mountain, not to shrink to a grain of sand. - Mandino #quote via @roxanamjones"

# In[29]:


# here we can see that the author of this tweet is AMELIEBALDWIN

tweet[tweet.content == "I am here for a purpose and that purpose is to grow into a mountain, not to shrink to a grain of sand. - Mandino #quote via @roxanamjones"]


# Create a subset with all tweets from the same author

# In[49]:


pd.set_option("display.max.rows", None)# display all row instances 
Author=input("Type here the Author you want to discplay : ")
tweet[tweet.author == Author]


# Daily number of tweets with the top two categories

# In[36]:


tweetss = tweet[tweet['retweet'] == True]
print(f"The percentage of retweets is {round(len(tweetss)/len(tweet)*100)}% of all the tweets")


# In[69]:


# top 2 tweets grouped by account category
# from all the categories we have highest number of trolls grouped in to righttroll which is 28789
import matplotlib.pyplot as plt
n = 2
tweet['account_category'].value_counts()[:n].plot(kind='bar')


# In[73]:


# the 3rd and 4th catagory of tweets
n = 2
tweet['account_category'].value_counts()[2:4].plot(kind='pie')


# In[ ]:




