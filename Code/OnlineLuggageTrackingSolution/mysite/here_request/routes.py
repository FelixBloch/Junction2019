# Packages
import pandas as pd
import os
from flask import render_template, session, redirect

from here_request import app
from here_request.PlotRoutes import plotMap
from here_request.RequestRoutes import requestRoute


points = pd.read_csv('servicePoints.csv')
file_name = 'logistics'


@app.route('/')
@app.route('/home', methods = ['POST', 'GET'])
def home():


    responses = {}
    GPSdatasets = {}
    distances = {}
    times = {}
    for route in points.route.unique():
        response, time, distance = requestRoute(points, route = route)
        responses['route_'+str(route)] = response
        times['route_'+str(route)] = time
        distances['route_'+str(route)] = distance
        gpsData = pd.DataFrame(response.json()['response']['route'][0]['shape']).apply(lambda x: x.str.split(','))
        GPSdataset = pd.DataFrame()
        GPSdataset['lat'] = gpsData.iloc[:,0].apply(lambda x: x[0])
        GPSdataset['lon'] = gpsData.iloc[:,0].apply(lambda x: x[1])
        GPSdataset = GPSdataset.astype(float)
        GPSdatasets['route_' + str(route)] = GPSdataset


    if ('logistics.html' in os.listdir('mysite/here_request/templates/')):
        os.remove('mysite/here_request/templates/logistics.html')

    plotMap(points, GPSdatasets, times, distances)

    return render_template('logistics.html')#,file_name=file_name)






