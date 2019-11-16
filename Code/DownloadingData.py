#!/usr/bin/env python
# coding: utf-8

# In[20]:


import pandas as pd
import numpy as np
from fake_useragent import UserAgent
import requests
import pyprind


# In[22]:


def getRequest(table='baggage', key='jmdSHjy6WPaXwoR75E6mJ1ImhxKPRJb51v6DBS0A',
               url="https://junction.dev.qoco.fi/api/", baggageId=''):
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome), 'x-api-key':key}
    url = url + table + '/' + baggageId
    
    response = requests.get(url, headers=header).json()
    response = pd.DataFrame.from_dict(response[list(response.keys())[0]])
    
    return response


# In[23]:


baggage = getRequest(table='baggage')
print(baggage.shape)
display(baggage.info())
baggage.head()


# In[24]:


customers = getRequest(table='customers')
print(customers.shape)
display(customers.info())
customers.head()


# In[25]:


events = pd.DataFrame()
pbar = pyprind.ProgBar(baggage.shape[0], width=baggage.shape[0])
for baggageId in baggage.baggageId.unique():
    event = getRequest(table='events', baggageId=baggageId)
    events = events.append(event, sort=False, ignore_index=True)
    pbar.update()
        


# In[26]:


print(events.shape)
display(events.info())
events.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




