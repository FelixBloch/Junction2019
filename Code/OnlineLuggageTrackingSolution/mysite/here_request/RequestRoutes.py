import requests
import json
import pandas as pd
import datetime


# constants for request parameters
app_id = "Wze2UHyOGN8z12BqLmPb"
app_code = "vdNH_YG6zsIrMjogrUzRgw"
mode = "fastest;car;traffic:enabled;"
alternatives = "0"
routeAttributes = "sh,-wp"
legAttributes = "links,-maneuvers"
linkAttributes = "sh,le,sl,ds,ro,ma,fc"
departure = "now"
returnElevation = "true"
url = 'https://route.cit.api.here.com/routing/7.2/calculateroute.json'




def requestRoute(places, route,
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
                },
                 url='https://route.cit.api.here.com/routing/7.2/calculateroute.json'):


    i = 0
    for row in places[(places.route==route)].iterrows():
        params['waypoint{}'.format(i)] = ','.join(list(row[1].loc[[
            'lat', 'lon']].astype(str).values))
        i += 1

    # request to HERE
    response = requests.get(url, params=params)
    distance = response.json()['response']['route'][0]['summary']['distance']/1000
    time = response.json()['response']['route'][0]['summary']['travelTime']
    time = str(datetime.timedelta(seconds=time))
    
    # saving the response in JSON file
    with open('data/route_' + str(route), 'w') as outfile:
        json.dump(response.json(), outfile)

    return response, time, distance

