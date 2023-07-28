# sqlalchemy-challenge

**Climate Data Analysis and Flask API**

This project involves analyzing and exploring climate data using Python, SQLAlchemy, Pandas, and Matplotlib. The data is stored in a SQLite database, and the analysis is performed using Jupyter Notebook and Flask.

**Part 1: Climate Data Analysis**

**Set up**

1. Use the create_engine() function from SQLAlchemy to connect to the SQLite database.

2. Reflect the tables into classes using the automap_base() function and save references to the classes.

3. Create a SQLAlchemy session to interact with the database.

**Precipitation Analysis** : Find the most recent date in the dataset and get the previous 12 months of precipitaion data by querying the data from the most recent data. Plot the precipitation data using the DataFrame 'plot'.

**Station Analysis** : Design a query to calculate the total number of stations in the dataset and find the most-active stations. Design a query to calculate the lowest, highest, and average temperatures for the most-active station. Design a query to get the previous 12 months of temperature observation data and plot the data as a histogram.

**Part 2: Design Your Climate App (Flask API)**

The homepage ("/") lists all available routes.

Endpoint: /api/v1.0/precipitation
  Return the last 12 months of precipitation data as a JSON dictionary.

Endpoint: /api/v1.0/stations
  Return a JSON list of all stations in the dataset.

Endpoint: /api/v1.0/tobs
  Return a JSON list of temperature observations for the previous year for the most-active station.

Endpoint: /api/v1.0/<start> and /api/v1.0/<start>/<end>
