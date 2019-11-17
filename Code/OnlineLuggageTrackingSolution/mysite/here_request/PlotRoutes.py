def plotMap(points, GPSdatasets, times, distances):


    import folium
    from folium.plugins import TimestampedGeoJson
    from folium import plugins

    import numpy as np
    import pandas as pd
    # initializing the map
    routesOnMap = folium.Map(location=[points.lat.iloc[0],points.lon.iloc[0]],
                                 zoom_start=10,
                                 )


    # setting a Layer of a map
    folium.TileLayer('openstreetmap').add_to(routesOnMap)


    for route, color in zip(points.route.unique(), ['red','green','blue']):
        GPSdata = GPSdatasets['route_'+str(route)]
        time = times['route_'+str(route)]
        distance = distances['route_'+str(route)]
        exp_fc = distance * 0.26
        exp_cost = str(np.round(exp_fc*1.5,1))
        distance = str(np.round(distance,1))
        exp_fc = str(np.round(exp_fc,1))
        fg = folium.FeatureGroup(name='route '+str(route)+': travel time - '+time+', distance,km: '+distance+', fuel consumption,l: '+exp_fc+', cost,€: '+exp_cost)
        routesOnMap.add_child(fg)

        folium.PolyLine(locations=GPSdata[['lat','lon']].values, color=color).add_to(fg)


    popups = ['Service Point ' + str(i) for i in range(points.drop_duplicates(['place']).shape[0])]
    plugins.MarkerCluster(points.drop_duplicates(['place']).iloc[:,1:3], popups=popups, name='Service Points').add_to(routesOnMap)

    plugins.Fullscreen(
        position='topleft',
        title='Expand me',
        title_cancel='Exit me',
        force_separate_button=True
    ).add_to(routesOnMap)

    # # setting ability to control check boxes with option to collapse them
    folium.LayerControl(collapsed=True).add_to(routesOnMap)

    # plugins.LocateControl(position='topleft').add_to(routesOnMap)

    from datetime import datetime, timedelta

    def datetime_range(start, end, delta):
        current = start
        while current < end:
            yield current
            current += delta

    dts = [dt.strftime('%Y-%m-%d T%H:%M Z') for dt in
           datetime_range(datetime(2014, 9, 1, 0), datetime(2018, 9, 10, 10),
           timedelta(minutes=1))]

    for route, color in zip(points.route.unique(), ['red','green','blue']):
        GPSdata = GPSdatasets['route_'+str(route)]

        GPSdata['dates'] = pd.to_datetime(pd.DataFrame(dts[:GPSdata.shape[0]]).iloc[:,0]).astype(str).apply(lambda x: x[:]).values
        GPSdata['color'] = color
        GPSdata[['lat','lon']] = GPSdata[['lat','lon']].astype(float)

        table = """\
        <table style=\'width:100%\'>
          <tr>
            <th>Firstname</th>
            <th>Lastname</th>
            <th>Age</th>
          </tr>
          <tr>
            <td>Jill</td>
            <td>Smith</td>
            <td>50</td>
          </tr>
          <tr>
            <td>Eve</td>
            <td>Jackson</td>
            <td>94</td>
          </tr>
        </table>
        """

        # Lon, Lat order.
        points_ = []
        for i in range(GPSdata.shape[0]):
            if i==GPSdata.shape[0]-1:
                popup = table
            else:
                popup = '1'

            points_.append([
                {
                'coordinates': [GPSdata.loc[i,'lon'], GPSdata.loc[i,'lat']],
                'time': GPSdata.loc[i,'dates'],
                'popup': popup,
                'color': GPSdata.loc[i,'color']
            }])


        features = []
        for point in points_:

            features.append([
                {
                    'type': 'Feature',
                    'geometry': {
                        'type': 'LineString',
                        'coordinates': point[0]['coordinates'],
                    },
                    'properties': {
                        'times': point[0]['time'],
                        'popup': point[0]['popup'],
                        'id': 'house',
                        'icon': 'marker',
                    'iconstyle': {
                        'iconUrl': 'http://downloadicons.net/sites/default/files/small-house-with-a-chimney-icon-70053.png',
                        'iconSize': [20, 20]
                    }
                    }
                }
            ])

        features.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'LineString',
                    'coordinates': GPSdata[['lon','lat']].values.tolist(),
                },
                'properties': {
                    'popup': 'Current address',
                    'times': list(GPSdata['dates'].values),
                    'icon': 'circle',
                    'iconstyle': {
                        'fillColor': color,
                        'fillOpacity': 0.6,
                        'stroke': 'false',
                        'radius': 13
                    },
                    'style': {'weight': 0},
                    'id': 'man'
                }
            }
        )



        plugins.TimestampedGeoJson(
            {
                'type': 'FeatureCollection',
                'features': features
            },
            period='PT1M',
            add_last_point=True,
            auto_play=True,
            loop=True,
            max_speed=3,
            loop_button=True,
            date_options='YYYY/MM/DD HH:mm:ss',
            time_slider_drag_update=True,
            duration='PT1M'
        ).add_to(routesOnMap)


    # saving the route in html file
    routesOnMap.save('mysite/here_request/templates/logistics.html')


