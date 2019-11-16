import pandas as pd
import numpy as np
from fake_useragent import UserAgent
import requests
import pyprind
import matplotlib.pyplot as plt
import seaborn as sns


def getRequest(table='baggage', key='jmdSHjy6WPaXwoR75E6mJ1ImhxKPRJb51v6DBS0A',
               url="https://junction.dev.qoco.fi/api/", baggageId=''):
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome), 'x-api-key':key}
    url = url + table + '/' + baggageId
    
    response = requests.get(url, headers=header).json()
    response = pd.DataFrame.from_dict(response[list(response.keys())[0]])
    
    return response



def combineDataBases():
    
    '''
    table = info about parameters, function
    
    '''
    baggage = getRequest(table='baggage')
    print(baggage.shape)
    display(baggage.head())

    customers = getRequest(table='customers')
    print(customers.shape)
    display(customers.head())

    events = pd.DataFrame()
    pbar = pyprind.ProgBar(baggage.shape[0], width=baggage.shape[0])
    for baggageId in baggage.baggageId.unique():
        event = getRequest(table='events', baggageId=baggageId)
        events = events.append(event, sort=False, ignore_index=True)
        pbar.update()
    print(events.shape)
    display(events.head())

    baggage_customer = pd.merge(baggage, customers, how='inner', on='customerId')
    events_baggage_customer = pd.merge(events, baggage_customer, how='inner', on='baggageId')
    display(events_baggage_customer.info())
    display(events_baggage_customer.head())

    return events_baggage_customer, baggage_customer, events, customers, baggage


# In[4]:


travels, baggage_customer, events, customers, baggage = combineDataBases()
travels.to_csv('travels.csv', index=False)
baggage_customer.to_csv('baggage_customer.csv', index=False)
events.to_csv('events.csv', index=False)
customers.to_csv('customers.csv', index=False)
baggage.to_csv('baggage.csv', index=False)



missed = events.groupby(['baggageId']).apply(lambda x: x.type.unique()[-1]).rename('status')
origin_airport = events.groupby(['baggageId']).apply(lambda x: x.airport.unique()[0]).rename('origin_airport')
baggage_customer_a = pd.merge(baggage_customer, missed, on=['baggageId'], how='inner')
baggage_customer_a = pd.merge(baggage_customer_a, origin_airport, on=['baggageId'], how='inner')
baggage_customer_a.replace({'rushbag':{'N':"baggage is in a hurry",
                                      'Y':"baggage isn't in a hurry"}},inplace=True)
baggage_customer_a.replace({'special':{'N':"Normal",
                                      'A':"Animal",
                                       'L':'Long',
                                       'H':'Heavy',
                                       'C':'Special',
                                       'T':'Toxic',
                                       'W':'Weapons',
                                      'CH':'Special(H)',
                                       'LCT':'Long(CT)',
                                       'TH':'Toxic(H)',
                                       'LW':'Long(W)',
                                       'LC':'Long(C)',
                                       'LTW':'Long(TW)',
                                      
                                      }},inplace=True)
fig = plt.figure(figsize=(30,15))
ax1 = fig.add_subplot(221)
df2 = baggage_customer_a.groupby(['rushbag','status'])['rushbag'].count().unstack('status').fillna(0).plot(kind='bar',
                                                                                                          stacked=False,
                                                                                                          figsize=(15,8),
                                                                                                           ax=ax1,
                                                                                                          grid=True)
plt.xlabel('Rush status')
plt.ylabel('# of examples')
plt.xticks(rotation=0)
ax2 = fig.add_subplot(222)
df2 = baggage_customer_a.groupby(['special','status'])['special'].count().unstack('status').fillna(0).plot(kind='bar',
                                                                                                          stacked=False,
                                                                                                          figsize=(15,8),
                                                                                                           ax=ax2,
                                                                                                          grid=True)
plt.xticks(rotation=0,fontsize=9)
plt.xlabel('baggage type')
ax3 = fig.add_subplot(223)
df2 = baggage_customer_a.groupby(['target','status'])['target'].count().unstack('status').fillna(0).plot(kind='bar',
                                                                                                          stacked=False,
                                                                                                          figsize=(15,8),
                                                                                                         ax=ax3,
                                                                                                          grid=True)
plt.ylabel('# of examples')
plt.xlabel('Origin airport')
ax4 = fig.add_subplot(224)
df2 = baggage_customer_a.groupby(['origin_airport','status'])['origin_airport'].count().unstack('status').fillna(0).plot(kind='bar',
                                                                                                          stacked=False,
                                                                                                          figsize=(15,8),
                                                                                                            ax=ax4,
                                                                                                          grid=True)
plt.xlabel('Destination airport')
plt.tight_layout()
plt.savefig('DataAnalytics.png')


