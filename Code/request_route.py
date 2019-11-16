import requests
import json
import pandas as pd
from flask import session
import time

# constants for request parameters
app_id = "Wze2UHyOGN8z12BqLmPb"
app_code = "vdNH_YG6zsIrMjogrUzRgw"
mode = "fastest;car;traffic:enabled;"
alternatives = "2"
routeAttributes = "sh,-wp"
legAttributes = "links,-maneuvers"
linkAttributes = "sh,le,sl,ds,ro,ma,fc"
departure = "now"
returnElevation = "true"
url = 'https://route.cit.api.here.com/routing/7.2/calculateroute.json'

params = {
    "app_id": app_id,
    "app_code": app_code,
    "mode": mode,
    "alternatives": alternatives,
    "routeAttributes": routeAttributes,
    "legAttributes": legAttributes,
    "linkAttributes": linkAttributes,
    "departure": departure,
    "returnElevation": returnElevation
}


def requestRoute(places, params,
                 url='https://route.cit.api.here.com/routing/7.2/calculateroute.json'):
    '''
    Purpose:
        requesting HERE for getting the response with routes
        from given point A to B and recording results
    Input:
        places - pd.DataFrame, a table with clusters for a user
        params - a dictionary of parameters for HERE request
        url - string, a url for requesting routes from HERE
    Output:
        response - JSON, the response from HERE
        time - timestamp, the time of request
        tableGivenPoints - pd.DataFrame, a table with two rows:
                            1st - origin,
                            2nd - destination
    '''
    # creating a table of chosen origin and destination with two columns
    # and one row
    # givenPoints = pd.DataFrame({
    #     'origin': session.get('originClusterID'),
    #     'destination': session.get('destinationClusterID'),
    # },
    #     index=[0])

    # extracting two rows of origin (1st row) and destionation (2nd row)
    # from the table of clusters for a user
    # tableGivenPoints = places.set_index('clusterID').loc[
    #     givenPoints.loc[0].values].reset_index()

    # there are only two rows: 1st - origin, 2nd - destination
    # so go over lat,lon for origin and destination in order to set
    # two new parameters: 'waypoint0', 'waypoint1'
    # 'waypoint0' = 'lat,lon' = '42.323412,43.323123'
    i = 0
    for row in places.iterrows():
        params['waypoint{}'.format(i)] = ','.join(list(row[1].loc[[
            'lat', 'lon']].astype(str).values))
        i += 1
    print(params)

    # request to HERE
    response = requests.get(url, params=params)

    # get user_id
    # user_id = session.get('userID')['id']

    # reading timestamp
    # time = pd.to_datetime(response.json()['response']['metaInfo']['timestamp']
    #                       ) + pd.Timedelta('02:00:00')

    # saving points, and JSON response of the route
    # tableGivenPoints.to_csv('data/' + str(time) + '_' + user_id + 'GivenPoints.csv', index=False)

    # saving the response in JSON file
    with open('{}_Route.json'.format(int(time.time())), 'w') as outfile:
        json.dump(response.json(), outfile)

    return response


name = ['Aalto University', 'Pajupolku', 'Airport']
column = ['lat', 'lon']
address = [(60.185387, 24.816261), (60.248700, 24.971098), (60.315113, 24.962757)]

# route 1
name_1 = ['Aalto University', 'Meilahti', 'Pasila', 'Helsinki0', 'Helsinki1', 'Vantaa', 'Airport']
route_1 = [(60.185387, 24.816261), (60.193319, 24.905651), (60.209670, 24.920983), (60.237908, 24.957755),
           (60.257046, 24.980490), (60.283576, 24.991359), (60.315113, 24.962757)]

# route 2
name_2 = ['Aalto University', 'Espoo0', 'Espoo1', 'Vantaa0', 'Vantaa1', 'Vantaa2', 'Helsinki', 'Airport']
route_2 = [(60.185387, 24.816261), (60.195840, 24.798348), (60.217703, 24.773672), (60.244716, 24.787224),
           (60.274058, 24.821864), (60.315113, 24.962757), (60.316510, 24.922798), (60.307617, 24.875765)]

# route 3
name_3 = ['Aalto University', 'Vihti0', 'Vihti1', 'Vihti2', 'Vantaa0', 'Vantaa1', 'Airport']
route_3 = [(60.185387, 24.816261), (60.307771, 24.389224), (60.466143, 24.428987), (60.605516, 24.351746),
           (60.256890, 24.797295), (60.308698, 24.854492), (60.315113, 24.962757)]

place = pd.DataFrame(route_3, index=name_3, columns=column)
requestRoute(place, params)
