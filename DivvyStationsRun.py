import os
import sqlite3 as sql
import pandas as pd
import numpy as np

from math import radians, cos, sin, asin, sqrt
from matplotlib import rc, pyplot as plt
import seaborn

import calendar as cal
import datetime as dt

from functools import reduce

def divvy_create_graph(station_id, station_name):
    
    def haversine(row):
        """
        Calculate the Great Circle Distance between two points 
        on the earth (specified in decimal degrees)
        Credit: @MichaelDunn (http://stackoverflow.com/a/4913653/1422451)
        """     
        # convert lon, lat to floats
        row['FROM LONGITUDE'], row['FROM LATITUDE'], row['TO LONGITUDE'], row['TO LATITUDE'] = \
              map(float, [row['FROM LONGITUDE'], row['FROM LATITUDE'], row['TO LONGITUDE'], row['TO LATITUDE']])

        # convert decimal degrees to radians     
        lon1, lat1, lon2, lat2 = \
              map(radians, [row['FROM LONGITUDE'], row['FROM LATITUDE'], row['TO LONGITUDE'], row['TO LATITUDE']])

        # haversine formula 
        dlon = lon2 - lon1 
        dlat = lat2 - lat1 
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        
        c = 2 * asin(sqrt(a))
        # Radius of earth in miles
        r = 3956                       
            
        return c * r
    
    def runplot(pvtdf, title, path):        
        pvtdf.plot(kind='bar', edgecolor='w',figsize=(15,5), width=0.5, fontsize = 10)
        locs, labels = plt.xticks()    
        plt.title(title, weight='bold', size=24)
        lgd = plt.legend(loc='right', ncol=14, frameon=True, shadow=False, prop={'size': 12},
                         bbox_to_anchor=(1, 0.95))

        for i in range(len(lgd.get_texts())):        
            txt = lgd.get_texts()[i].get_text().replace('(DISTANCE_Miles, ', '(')
            lgd.get_texts()[i].set_text(txt)

        plt.xlabel('Year', weight='bold', size=24)
        plt.ylabel('Distance', weight='bold', size=20)
        plt.tick_params(axis='x', bottom='off', top='off', labelsize=15)
        plt.tick_params(axis='y', left='off', right='off', labelsize=15)
        
        plt.grid(b=True)
        plt.setp(labels, rotation=0, rotation_mode="anchor", ha="center")
        plt.tight_layout()
        plt.savefig(path)
        plt.clf()
        plt.close()

    def htmlpage(datastring, title, filename):
        html = '''<!DOCTYPE html>
                  <html>
                      <head>
                         <style type="text/css">
                              body{{ 
                                      margin:15px; padding: 20px 100px 20px 100px;
                                      font-family:Arial, Helvetica, sans-serif; font-size:88%; 
                              }}
                              h1, h2 {{
                                      font:Arial black; color: #383838;
                                      valign: top;
                              }}       
                              img {{
                                    float: right;
                              }}
                              table{{
                                      width:100%; font-size:13px;                  
                                      border-collapse:collapse;
                                      text-align: right;                  
                              }}
                              th{{ color: #383838 ; padding:2px; text-align:right; }}
                              td{{ padding: 2px 5px 2px 5px; }}
                              .footer{{
                                      text-align: right;
                                      color: #A8A8A8;
                                      font-size: 12px;
                                      margin: 5px;
                              }}                   
                         </style>
                      </head>                      
                      <body>
                        <h3>{0}<img src="../../DivvyLogo.png" alt="divvy icon" height="50px"></h3>
                        {1}
                      </body>
                      <div class="footer">Source: City of Chicago Data Portal</div>
                  </html>'''.format(title, datastring)

        with open(os.path.join(cd, 'stations', station_name, filename), 'w') as f:
            f.write(html)
        
    # PLOT SETTINGS    
    font = {'family' : 'arial', 'weight' : 'bold', 'size' : 12}
    rc('font', **font); rc("figure", facecolor="white"); rc('axes', edgecolor='darkgray');

    # QUERY DATABASE
    cd = os.path.dirname(os.path.abspath(__file__))
    
    try:
        conn = sql.connect(os.path.join(cd, "Divvy_Trips.db"))
        stations = "SELECT * FROM trips WHERE [FROM STATION ID] = {0} OR [TO STATION ID] = {0}".format(station_id);
        df = pd.read_sql(stations, con = conn)
    except Exception as e:
        print(e)
    finally:
        conn.close()

    # CREATE FOLDER   
    if os.path.exists(os.path.join(cd, 'stations', station_name.replace('*', ''))) == False:
        station_name = station_name.replace('*', '')
        os.makedirs(os.path.join(cd, 'stations', station_name.replace('*', '')))

    if '*' in station_name: station_name = station_name.replace('*', '')
   
    # DISTANCE
    df = df.rename(columns={'\ufeffTRIP ID':'TRIP ID'})    
    df['DISTANCE_Miles'] = df.apply(haversine, axis=1)
    df['TRIP DURATION'] = df['TRIP DURATION'].astype(float) / 60

    # TIME VARIABLES
    df["START TIME"] = pd.to_datetime(df["START TIME"], format="%m/%d/%Y %I:%M:%S %p")
    df["STOP TIME"] = pd.to_datetime(df["STOP TIME"], format="%m/%d/%Y %I:%M:%S %p")

    df.loc[:, 'START TIME MONTH'] = df['START TIME'].dt.month
    df.loc[:, 'START TIME YEAR'] = df['START TIME'].dt.year

    df.loc[:, 'STOP TIME MONTH'] = df['STOP TIME'].dt.month
    df.loc[:, 'STOP TIME YEAR'] = df['STOP TIME'].dt.year

    df.loc[:, 'START WEEKDAY'] = [cal.day_name[i] for i in df['START TIME'].dt.weekday]

    df.loc[:, 'START TIME HOUR'] = df['START TIME'].dt.hour

    df['TIME FRAME'] = np.where(df['START TIME HOUR'].between(0,1, inclusive = True), '00:00-01:00',
                                np.where(df['START TIME HOUR'].between(1,2, inclusive = True), '01:00-02:00',
                                         np.where(df['START TIME HOUR'].between(2,3, inclusive = True), '02:00-03:00',
                                                  np.where(df['START TIME HOUR'].between(3,4, inclusive = True), '03:00-04:00',
                                                           np.where(df['START TIME HOUR'].between(4,5, inclusive = True), '04:00-05:00',
                                                                    np.where(df['START TIME HOUR'].between(5,6, inclusive = True), '05:00-06:00',
                                                                             np.where(df['START TIME HOUR'].between(6,7, inclusive = True), '06:00-07:00',
                                                                                      np.where(df['START TIME HOUR'].between(7,8, inclusive = True), '07:00-08:00',
                                                                                               np.where(df['START TIME HOUR'].between(8,9, inclusive = True), '08:00-09:00',
                                                                                                        np.where(df['START TIME HOUR'].between(9,10, inclusive = True), '09:00-10:00',
                                                                                                                 np.where(df['START TIME HOUR'].between(10,11, inclusive = True), '10:00-11:00',
                                                                                                                          np.where(df['START TIME HOUR'].between(11,12, inclusive = True), '11:00-12:00',
                                                                                                                                   np.where(df['START TIME HOUR'].between(12,13, inclusive = True), '12:00-13:00', 
                                                                                                                                             np.where(df['START TIME HOUR'].between(13,14, inclusive = True), '13:00-14:00', 
                                                                                                                                                      np.where(df['START TIME HOUR'].between(14,15, inclusive = True), '14:00-15:00',
                                                                                                                                                      np.where(df['START TIME HOUR'].between(15,16, inclusive = True), '15:00-16:00',
                                                                                                                                                      np.where(df['START TIME HOUR'].between(16,17, inclusive = True), '16:00-17:00',
                                                                                                                                                      np.where(df['START TIME HOUR'].between(17,18, inclusive = True), '17:00-18:00',
                                                                                                                                                      np.where(df['START TIME HOUR'].between(18,19, inclusive = True), '18:00-19:00',
                                                                                                                                                      np.where(df['START TIME HOUR'].between(19,20, inclusive = True), '19:00-20:00',
                                                                                                                                                      np.where(df['START TIME HOUR'].between(20,21, inclusive = True), '20:00-21:00',
                                                                                                                                                      np.where(df['START TIME HOUR'].between(21,22, inclusive = True), '21:00-22:00',
                                                                                                                                                      np.where(df['START TIME HOUR'].between(22,23, inclusive = True), '22:00-23:00',
                                                                                                                                                      np.where(df['START TIME HOUR'].between(23,24, inclusive = True), '23:00-24:00', np.nan))))))))))))))))))))))))


    
    df['WEEKDAY TYPE'] = np.where(df['START WEEKDAY'].isin(['Saturday', 'Sunday']), 'WEEKEND', 'WEEKDAY')


    # AGE VARIABLE
    df['BIRTH YEAR'] = np.where(df['BIRTH YEAR'] == '', np.nan, df['BIRTH YEAR'])
    df['BIRTH YEAR'] = df['BIRTH YEAR'].astype('float')
    df.loc[:, 'AGE'] = df['START TIME YEAR'] - df['BIRTH YEAR']

    df['AGE_GROUP'] = np.where(df['AGE'].between(0,18, inclusive = True), '0 - 18',
                               np.where(df['AGE'].between(19,29, inclusive = True), '19 - 29',
                                        np.where(df['AGE'].between(30,39, inclusive = True), '30 - 39',
                                                 np.where(df['AGE'].between(40,49, inclusive = True), '40 - 49',
                                                          np.where(df['AGE'].between(50,65, inclusive = True), '50 - 65',
                                                                   np.where(df['AGE'].between(65,80, inclusive = True), '65+', np.nan))))))


    # OVERALL    
    df.groupby(['START TIME YEAR', 'START TIME MONTH'])['TRIP DURATION'].count().reset_index()\
               .rename(columns={'TRIP DURATION':'BIKE TRIPS'})\
               .to_csv(os.path.join(cd, 'stations', station_name, 'BikeTrips.csv'))
    htmlpage(df.groupby(['START TIME YEAR', 'START TIME MONTH'])['TRIP DURATION'].count().reset_index()\
             .rename(columns={'TRIP DURATION':'BIKE TRIPS'})\
             .to_html(), '{} - Trip Count'.format(station_name), 'BikeTrips.html')
    
    df.groupby(['START TIME YEAR', 'START TIME MONTH'])['TRIP DURATION'].mean().reset_index().to_csv(os.path.join(cd, 'stations', station_name, 'AvgDuration.csv'))
    htmlpage(df.groupby(['START TIME YEAR', 'START TIME MONTH'])['TRIP DURATION'].mean().reset_index().to_html(), '{} - Trip Duration'.format(station_name), 'AvgDuration.html')    
    
    df.groupby(['START TIME YEAR', 'START TIME MONTH'])['DISTANCE_Miles'].mean().reset_index().to_csv(os.path.join(cd, 'stations', station_name, 'AvgMiles.csv'))
    htmlpage(df.groupby(['START TIME YEAR', 'START TIME MONTH'])['DISTANCE_Miles'].mean().reset_index().to_html(), '{} - Avg Miles'.format(station_name), 'AvgMiles.html')
    seaborn.set()
    
    # DISTANCE BY GENDER
    distanceByGender = pd.pivot_table(df[(df['USER TYPE'] == 'Subscriber') & (df['GENDER'] != '')], index=['START TIME YEAR', 'START TIME MONTH'], columns=['GENDER'], values=['DISTANCE_Miles'], aggfunc=len)

    if len(distanceByGender) > 0:
        distanceByGender.plot(figsize=(20,5), fontsize=12)
        plt.title("{} - Distance in Miles by Gender".format(station_name), weight='bold', size=24)
        lgd = plt.legend(prop={'size': 12})
        for i in range(len(lgd.get_texts())):        
            txt = lgd.get_texts()[i].get_text().replace('(DISTANCE_Miles, ', '(')
            lgd.get_texts()[i].set_text(txt)
        plt.savefig(os.path.join(cd, 'stations', station_name, 'DistanceByGender.png'))
        plt.clf()
        plt.close()

    # MILES BY GENDER BAR
    miles_by_gender = pd.pivot_table(df[(df['USER TYPE'] == 'Subscriber') & (df["AGE"] < 80) & (df["GENDER"].str.len() > 0) & (df["DISTANCE_Miles"] > 0)],
                                     index = ['START TIME YEAR'], columns=['GENDER'], values=['DISTANCE_Miles'], aggfunc = len)
    miles_by_gender.reset_index().to_csv(os.path.join(cd, 'stations', station_name, 'MilesByGender.csv'))    
    htmlpage(miles_by_gender.reset_index().to_html(), '{} - Miles By Gender'.format(station_name), 'MilesByGender.html')

    if len(miles_by_gender) > 0:
        runplot(miles_by_gender, '{} - Divvy Data subscribers, Distance by Gender'.format(station_name), os.path.join(cd, 'stations', station_name, 'MilesByGender.png'))

    # MILES BY GENDER PIE
    mergelist = []
    
    for yr in list(range(df['START TIME YEAR'].min(), df['START TIME YEAR'].max()+1)):
        miles_by_gender_pie = df[(df['USER TYPE'] == 'Subscriber') & (df['START TIME YEAR']==yr) & (df["GENDER"].str.len() > 0)].\
                              groupby(["GENDER", "START TIME YEAR"])["DISTANCE_Miles"].apply(len).reset_index()
        if len(miles_by_gender_pie) > 0:
            mergelist.append(miles_by_gender_pie[['GENDER', 'DISTANCE_Miles']])

    if len(mergelist) > 0:
        miles_by_gender_pie = reduce(lambda left,right: pd.merge(left, right, on='GENDER'), mergelist).set_index('GENDER')   
        miles_by_gender_pie.columns = [str(i) for i in list(range(df['START TIME YEAR'].min(), df['START TIME YEAR'].max()+1))]

    if len(miles_by_gender_pie) > 0:
        if len(miles_by_gender_pie.columns) == 4: graphsize = 14
        if len(miles_by_gender_pie.columns) == 3: graphsize = 10
        if len(miles_by_gender_pie.columns) == 2: graphsize = 7
        if len(miles_by_gender_pie.columns) == 1: graphsize = 14
        
        labels = 'Female', 'Male'    
        miles_by_gender_pie.plot.pie(subplots=True, labels=['', ''], figsize=(graphsize,3.8), autopct='%.2f', title="{} - Miles By Gender".format(station_name), fontsize=12)    
        plt.axis('equal')
        plt.legend(labels=labels, prop={'size': 12})    
        plt.savefig(os.path.join(cd, 'stations', station_name, 'MilesByGenderPie.png'))
        plt.clf()
        plt.close()
    
    # MILES BY AGE
    miles_by_age = pd.pivot_table(df[(df['USER TYPE'] == 'Subscriber') & (df["AGE"] < 80) & (df["GENDER"].str.len() > 0) & (df["DISTANCE_Miles"] > 0)], index = ['START TIME YEAR'],
                                  columns=['AGE_GROUP'], values=['DISTANCE_Miles'], aggfunc = np.sum)

    miles_by_age.reset_index().to_csv(os.path.join(cd, 'stations', station_name, 'MilesByAge.csv'))        
    htmlpage(miles_by_age.reset_index().to_html(), '{} - Miles By Age'.format(station_name), 'MilesByAge.html')

    if len(miles_by_age) > 0:
        runplot(miles_by_age, '{} - Divvy Data subscribers, Distance by Age'.format(station_name), os.path.join(cd, 'stations', station_name, 'MilesByAge.png'))

    # TRIP COUNT IN 24 HOURS
    trips = pd.pivot_table(df, index=['TIME FRAME'], columns=['START WEEKDAY'], values=['TRIP DURATION'], aggfunc='count')
    trips.plot(figsize=(15,10), fontsize=12)
    plt.title("Bike Trips over 1 day for weekday/weekend", weight='bold', size=24)
    
    lgd = plt.legend(prop={'size': 12})
    for i in range(len(lgd.get_texts())):        
        txt = lgd.get_texts()[i].get_text().replace('(TRIP DURATION, ', '(')
        lgd.get_texts()[i].set_text(txt)
    plt.savefig(os.path.join(cd, 'stations', station_name, 'TripDurationDaily24Hours.png'))
    plt.clf()
    plt.close()
    
    trips = pd.pivot_table(df, index=['TIME FRAME'], columns=['WEEKDAY TYPE'], values=['TRIP DURATION'], aggfunc='count')
    trips.plot(figsize=(15,10), fontsize=12)
    plt.title("Bike Trips over 1 day for weekday/weekend", weight='bold', size=24)
    
    lgd = plt.legend(prop={'size': 12})
    for i in range(len(lgd.get_texts())):        
        txt = lgd.get_texts()[i].get_text().replace('(TRIP DURATION, ', '(')
        lgd.get_texts()[i].set_text(txt)
    plt.savefig(os.path.join(cd, 'stations', station_name, 'TripDurationWeekType24Hours.png'))
    plt.clf()
    plt.close()

