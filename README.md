## CASE STUDY - Weather Forecast Data

This is a simple beginners python script that consults and extracts weather data from the [Darksky Weather API ](https://darksky.net/dev/docs).  

In this first version, it only extracts data from São Paulo [(-23.5489, -46.6388)](https://pt.db-city.com/Brasil--S%C3%A3o-Paulo--S%C3%A3o-Paulo) and Rio de Janeiro [(-22.9035, -43.2096)](https://pt.db-city.com/Brasil--Rio-de-Janeiro--Rio-de-Janeiro). 

Before executing the .py script, it's necessary to create the table that will store the forecast data in the database. For that, you previously need to create a database. More information in the [PostgreSQL Documentation](https://www.postgresql.org/docs/9.0/sql-createdatabase.html).
The script create_weather_forecast_table.sql presents the code used to create the table.

After creating the database and the table, it's necessary to edit the darksky_weather_data.py script, informing your API KEY, and adding into the psycopg2 connection with PostgreSQL your on database information of  **user**, **password**, **host** and **database**.

If you will run locally, probably your **user** will be the default "**postgres**" and the **host** will be **127.0.0.1**. The **database** and **password** are configured by yourself.

### Tools used in this study:
* PostgreSQL 11.5
* Spyder 3.3.4 with Python 3.7
* darkskylib 0.3.91
* datetime 4.3
* psycopg2 2.8.4


