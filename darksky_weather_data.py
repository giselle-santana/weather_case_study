# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:10:53 2019

@author: gisa_
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 10:08:43 2019

@author: gisa_
"""

"""
@author: gisa_
"""

import psycopg2
from darksky import forecast
from datetime import date, timedelta

def main():

    SAOPAULO = -23.5489, -46.6388 #latitude e longitude de São Paulo
    RIO = -22.9035, -43.2096 # latitude e longetude do Rio de Janeiro
    
    KEY = 'INSERT YOUR API KEY FROM THE DARKSKY WEATHER API'
    
    
    insert_query = """
        INSERT INTO weather_forecast
        (city, minimum_temp, maximum_temp, date)
        VALUES(%s, %s, %s, %s) """
    
    datasetsp = []
    datasetrio = []
    weekday = date.today()
    
    
    with forecast(KEY, *SAOPAULO, units='si') as saopaulo:
        print("Summary for Sao Paulo")
        print(saopaulo.daily.summary, end='\n---\n')
        for day in saopaulo.daily:
            datasetsp.append(
                    ['sao paulo', day['temperatureMin'], day['temperatureMax'], 
                     datetime.utcfromtimestamp(day['time']).strftime('%Y-%m-%d')])
        
            weekday += timedelta(days=1) 
        
        print(datasetsp)
    
    
    with forecast(KEY, *RIO, units='si') as rio:
        print("Summary for Rio de Janeiro")
        print(rio.daily.summary, end='\n---\n')
        for day in rio.daily:
            datasetrio.append(
                    ['rio de janeiro', day['temperatureMin'], day['temperatureMax'], 
                     datetime.utcfromtimestamp(day['time']).strftime('%Y-%m-%d')])
        
            weekday += timedelta(days=1) 
        
        print(datasetrio)
    
        try:
            
            con = psycopg2.connect(user="INSERT_YOUR_USER", password="INSERT_YOUR_PASSWORD", host="127.0.0.1", database="INSERT_YOUR_DB_NAME")
            cur = con.cursor()
            cur.executemany(insert_query, datasetsp)
            cur.executemany(insert_query, datasetrio)
            con.commit()
            con.close()
        except (Exception):
            print("Database error!")
            raise
            
if __name__ == '__main__':
	main()  