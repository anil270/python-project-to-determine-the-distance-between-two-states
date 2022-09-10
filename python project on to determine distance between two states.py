#!/usr/bin/env python
# coding: utf-8

# In[5]:


##python project to determine distance between two states:


# In[1]:


import warnings


# In[6]:


#!pip install geopy


# In[7]:


#!pip install geocoder


# In[8]:


from geopy.geocoders import Nominatim
from geopy import distance
from tkinter import *
a = Nominatim(user_agent = "fun with data science")
place_1 = "Maharashtra"
place_2 = "Gujarat"

des_1 = a.geocode(place_1)
des_2 = a.geocode(place_2)

lat_1,long_1 = (des_1.latitude),(des_1.longitude)
lat_2,long_2 = (des_2.latitude),(des_2.longitude)

length_1 = (lat_1,long_1)
length_2 = (lat_2,long_2)

print(distance.distance(length_1,length_2))


# In[ ]:




