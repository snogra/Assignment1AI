#!/usr/bin/env python
# coding: utf-8

# <h1 style="font-size:3rem;color:blue;"> DAVE3625 Assignment 1 </h1>

# s333592

# In[1]:


import pandas as pd


# In[29]:


import numpy as np
import matplotlib.pyplot as plt
import datetime


# In[8]:


df = pd.read_excel(r'/Users/Sno/Downloads/Ruter_data.xls')
df.head()


# <h2 style="font-size:2rem;"> 1.1 Five Features </h2>

# 1. We can find time spent at each "Holdeplass" by substract the time the bus left "Holdeplass" with the time the bus arrived at "Holdeplass".
# 2. The capacity available can be extracted if the passengers is substracted to the vehicle capacity.
# 3. There are none travels between 01-05.
# 4. Arrival and departure are scheduled at the same time - which is impossible.
# 5. There cannot be a negative number of passengers.

# <h3 style="font-size:3rem;"> 1.2 Feature Engineering Applied </h3>

# In[22]:


df['Tidspunkt_Faktisk_Avgang_Holdeplass_Fra'] = pd.to_datetime(df['Tidspunkt_Faktisk_Avgang_Holdeplass_Fra'], 
                                                               errors='coerce') 
df['Tidspunkt_Faktisk_Ankomst_Holdeplass_Fra'] = pd.to_datetime(df['Tidspunkt_Faktisk_Ankomst_Holdeplass_Fra'], 
                                                                errors='coerce')
df['Tidspunkt_Planlagt_Ankomst_Holdeplass_Fra'] = pd.to_datetime(df['Tidspunkt_Planlagt_Ankomst_Holdeplass_Fra'], 
                                                                errors='coerce')
df['Tidspunkt_Planlagt_Avgang_Holdeplass_Fra'] = pd.to_datetime(df['Tidspunkt_Planlagt_Avgang_Holdeplass_Fra'], 
                                                                errors='coerce')


# 1. Beregner tid brukt på hver enkelt holdeplass. 

# In[33]:


df['Tid_På_Holdeplass']=df['Tidspunkt_Faktisk_Avgang_Holdeplass_Fra']-df['Tidspunkt_Faktisk_Ankomst_Holdeplass_Fra']
df.head()


# 2. Beregner tilgjengelig kapasitet på hvert kjøretøy.

# In[35]:


df['Tilgjengelig_kapasitet']=df['Kjøretøy_Kapasitet']-df['Passasjerer_Ombord']
df.head()


# 3. Ønsker å få feilmelding hvis "Passasjerer_Ombord" er et negativt tall.

# In[41]:


df['Passasjerer_Ombord']
If (df['Passasjerer_Ombord']) < 0
print('Passasjerer_Ombord',"må være enten 0 eller større.")
df.head()


# 4. Viser de forskjellige linjenavnene, og frekvensen av de.

# In[42]:


from scipy import stats
import seaborn as sns
import re


# In[44]:


df.head(50)


# In[49]:


sns.countplot(x='Linjenavn', data=df);

