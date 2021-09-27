#!/usr/bin/env python
# coding: utf-8

# <h1 style="font-size:3rem;color:blue;"> DAVE3625 Assignment 1 </h1>

# s333592

# In[3]:


import pandas as pd


# In[4]:


dataset = pd.read_excel(r'/Users/Sno/Downloads/Ruter_data.xls')
print(dataset)


# <h2 style="font-size:2rem;"> 1.1 Five Features </h2>

# 1. We can find time spent at each "Holdeplass" by substract the time the bus left "Holdeplass" with the time the bus arrived at "Holdeplass".
# 2. The capacity available can be extracted if the passengers is substracted to the vehicle capacity.
# 3. There are none travels between 01-05.
# 4. Arrival and departure are scheduled at the same time - which is impossible.
# 5. There cannot be a negative number of passengers.

# <h3 style="font-size:3rem;"> 1.2 Feature Engineering Applied </h3>

# In[11]:


holdeplass = df["Tidspunkt_Faktisk_Avgang_Holdeplass_Fra"] - df["Tidspunkt_Faktisk_Ankomst_Holdeplass_Fra"]
df["Tid_Pa_Holdeplass"] = holdeplass
print (df)


# In[12]:


Tilgjengelig_kapasitet = df["Kjørtøy_Kapasitet"] - df["Passasjerer_Ombord"]
df["Tilgjengelig_kapasitet"] = Tilgjengelig_kapasitet


# In[13]:


Passasjerer_Ombord
If("Passasjerer_Ombord") < 0
print("Passasjerer_Ombord") = 0

