#!/usr/bin/env python
# coding: utf-8

# In[1]:


import bauwerk
import gym
import numpy as np


# In[3]:


new_env = gym.make("bauwerk/SolarBatteryHouse-v0")
new_env.reset()

load_list = []
action = np.float32([0.])
for i in range(480):
    load_no = new_env.step(action)[0]['load'][0]
    load_list.append(load_no)


# In[5]:


# this is how much electricity is used by the households - as you can see, there are resting/inactive hours when the 
# household doesn't consume as much electricity, and there are more active hours

import matplotlib.pyplot as plt
for i in range(20):
    plt.plot(load_list[24*i:24*(i+1)])


# In[6]:


new_env.reset()

pv_list = []
action = np.float32([0.])
for i in range(480):
    pv_no = new_env.step(action)[0]['pv_gen'][0]
    pv_list.append(pv_no)


# In[8]:


# as you can see, bauwerk aims to simulate a typical day of solar energy - there's a peak around the middle of the day, and 
# there isn't much at the beginning and end of the day

for i in range(20):
    plt.plot(pv_list[24*i:24*(i+1)])


# In[ ]:




