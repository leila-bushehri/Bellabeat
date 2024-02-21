#!/usr/bin/env python
# coding: utf-8

# In[41]:


#importing everything we need 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# loading all our csv files to clean 

# In[7]:


daily_activity_df = pd.read_csv('dailyActivity_merged.csv')
daily_steps_df = pd.read_csv('dailySteps_merged.csv')
sleep_day_df = pd.read_csv('sleepDay_merged.csv')
heart_rate_df = pd.read_csv('heartrate_seconds_merged.csv')
weight_log_df = pd.read_csv('weightLogInfo_merged.csv')


# Gathering information about our columns 

# In[9]:


daily_activity_df.head(), daily_steps_df.head(), sleep_day_df.head(), heart_rate_df.head(), weight_log_df.head()


# checking the types for cleaning 

# In[12]:


daily_activity_df.dtypes


# In[24]:


daily_steps_df.dtypes


# changing Activity from object to Datetime

# In[11]:


daily_activity_df['ActivityDate'] = pd.to_datetime(daily_activity_df['ActivityDate'], format='%m/%d/%Y')


# In[17]:


daily_steps_df['ActivityDay'] = pd.to_datetime(daily_steps_df['ActivityDay'], format='%m/%d/%Y')


# In[23]:


sleep_day_df.dtypes


# In[19]:


sleep_day_df['SleepDay']= pd.to_datetime(sleep_day_df['SleepDay'].str.split(' ').str[0], format='%m/%d/%Y')


# In[21]:


heart_rate_df['Time']= pd.to_datetime(heart_rate_df['Time'])


# In[22]:


weight_log_df['Date']= pd.to_datetime(weight_log_df['Date'].str.split(' ').str[0],format='%m/%d/%Y' )


# In[27]:


heart_rate_df.dtypes,weight_log_df.dtypes


# checking for missing values 

# In[38]:


missing_values_summary = {
    'daily_activity_df': daily_activity_df.isnull().sum(),
    'daily_steps_df': daily_steps_df.isnull().sum(),
    'sleep_day_df': sleep_day_df.isnull().sum(),
    'heart_rate_df': heart_rate_df.isnull().sum(),
    'weight_log_df': weight_log_df.isnull().sum()
}

missing_values_summary


# removing missing values from our "Fat" column

# In[39]:


weight_log_df_clean = weight_log_df.dropna(subset=['Fat'])
weight_log_df_clean.head()


# Checking for duplicates in our dataset and dropping if there is any 

# In[29]:


daily_activity_df.drop_duplicates(inplace=True)
daily_steps_df.drop_duplicates(inplace=True)
sleep_day_df.drop_duplicates(inplace=True)
heart_rate_df.drop_duplicates(inplace=True)
weight_log_df.drop_duplicates(inplace=True)


# In[30]:


daily_activity_df.shape


# In[31]:


daily_activity_summary_stats = daily_activity_df.describe()

daily_activity_summary_stats


# creating visualization and setting the aesthetic style
# figure one is the distribution of total steps
# figure two is Daily Active Minutes (Very Active vs Lightly Active)
# figure three is Relationship Between Active Minutes and Calories Burned

# In[32]:


sns.set_style("whitegrid")


plt.figure(figsize=(12, 6))
sns.histplot(daily_activity_df['TotalSteps'], bins=30, kde=True)
plt.title('Distribution of Total Daily Steps')
plt.xlabel('Total Steps')
plt.ylabel('Frequency')
plt.axvline(daily_activity_df['TotalSteps'].mean(), color='red', linestyle='--', label='Mean Steps')
plt.legend()
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(x='LightlyActiveMinutes', y='VeryActiveMinutes', data=daily_activity_df)
plt.title('Daily Lightly Active Minutes vs Very Active Minutes')
plt.xlabel('Lightly Active Minutes')
plt.ylabel('Very Active Minutes')
plt.show()

plt.figure(figsize=(12, 6))
sns.scatterplot(x='TotalSteps', y='Calories', data=daily_activity_df)
plt.title('Relationship Between Total Steps and Calories Burned')
plt.xlabel('Total Steps')
plt.ylabel('Calories Burned')
plt.show()


# here we Analyze Activity and Sleep Patterns and calculate avg daily steps, sleep duration and quality metrics

# In[33]:


avg_daily_steps = daily_activity_df['TotalSteps'].mean()
avg_sleep_duration = sleep_day_df['TotalMinutesAsleep'].mean() / 60  # Convert to hours
avg_sleep_efficiency = (sleep_day_df['TotalMinutesAsleep'] / sleep_day_df['TotalTimeInBed']).mean() * 100

activity_sleep_summary = {
    "Average Daily Steps": avg_daily_steps,
    "Average Sleep Duration (hours)": avg_sleep_duration,
    "Average Sleep Efficiency (%)": avg_sleep_efficiency
}

activity_sleep_summary


# saving documents to use for tableau 

# In[40]:


daily_activity_df.to_csv('daily_activity_cleaned.csv', index=False)

sleep_day_df.to_csv('sleep_day_cleaned.csv', index=False)

heart_rate_df.to_csv('heart_rate_cleaned.csv', index=False)

weight_log_df.to_csv('weight_log_cleaned.csv', index=False)

