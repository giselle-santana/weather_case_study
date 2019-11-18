CREATE TABLE weather_forecast (
    cod_request SERIAL PRIMARY KEY,
    city VARCHAR(40) NOT NULL,
    minimum_temp REAL NOT NULL,
    maximum_temp REAL NOT NULL,
	date DATE NOT NULL
);