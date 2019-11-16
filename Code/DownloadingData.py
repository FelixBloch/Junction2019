import pandas as pd
import numpy as np
from fake_useragent import UserAgent
import requests
import pyprind




def getRequest(table='baggage', key='jmdSHjy6WPaXwoR75E6mJ1ImhxKPRJb51v6DBS0A',
               url="https://junction.dev.qoco.fi/api/", baggageId=''):
    ua = UserAgent()
    header = {'User-Agent':str(ua.chrome), 'x-api-key':key}
    url = url + table + '/' + baggageId
    
    response = requests.get(url, headers=header).json()
    response = pd.DataFrame.from_dict(response[list(response.keys())[0]])
    
    return response




baggage = getRequest(table='baggage')
print(baggage.shape)
display(baggage.info())
baggage.head()




customers = getRequest(table='customers')
print(customers.shape)
display(customers.info())
customers.head()




events = pd.DataFrame()
pbar = pyprind.ProgBar(baggage.shape[0], width=baggage.shape[0])
for baggageId in baggage.baggageId.unique():
    event = getRequest(table='events', baggageId=baggageId)
    events = events.append(event, sort=False, ignore_index=True)
    pbar.update()
        




print(events.shape)
display(events.info())
events.head()


