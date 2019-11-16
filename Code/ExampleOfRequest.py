import requests
import json
import pandas as pd
from flask import session

# constants for request parameters
app_id="Wze2UHyOGN8z12BqLmPb"
app_code="vdNH_YG6zsIrMjogrUzRgw"
mode="fastest;car;traffic:enabled;"
alternatives="3"
routeAttributes="sh,-wp"
legAttributes="links,-maneuvers"
linkAttributes="sh,le,sl,ds,ro,ma,fc"
departure="now"
returnElevation="true"
url='https://route.cit.api.here.com/routing/7.2/calculateroute.json'

params = {
    "app_id":app_id,
    "app_code":app_code,
    "mode":mode,
    "alternatives":alternatives,
    "routeAttributes":routeAttributes,
    "legAttributes":legAttributes,
    "linkAttributes":linkAttributes,
    "departure":departure,
    "returnElevation":returnElevation
}

def requestRoute(places,params,
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
    givenPoints = pd.DataFrame({
        'origin':session.get('originClusterID'),
        'destination':session.get('destinationClusterID'),
        },
        index=[0])

    # extracting two rows of origin (1st row) and destionation (2nd row)
    # from the table of clusters for a user
    tableGivenPoints = places.set_index('clusterID').loc[
        givenPoints.loc[0].values].reset_index()

    # there are only two rows: 1st - origin, 2nd - destination
    # so go over lat,lon for origin and destination in order to set
    # two new parameters: 'waypoint0', 'waypoint1'
    # 'waypoint0' = 'lat,lon' = '42.323412,43.323123'
    for row in tableGivenPoints.iterrows():
        params['waypoint'+str(row[0])]=','.join(list(row[1].loc[[
            'lat','lon']].astype(str).values))

    # request to HERE
    response = requests.get(url, params=params)

    # get user_id
    user_id = session.get('userID')['id']

    # reading timestamp
    time = pd.to_datetime(response.json()['response']['metaInfo']['timestamp']
    ) + pd.Timedelta('02:00:00')

    # saving points, and JSON response of the route
    tableGivenPoints.to_csv('data/'+str(time)+'_'+user_id+'GivenPoints.csv',index=False)

    # saving the response in JSON file
    with open('data/'+str(time)+'_'+user_id+'Route.json', 'w') as outfile:
        json.dump(response.json(), outfile)

    return response, time, tableGivenPoints


