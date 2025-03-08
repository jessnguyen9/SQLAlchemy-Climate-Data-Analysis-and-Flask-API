# SQLAlchemy Climate Data Analysis and Flask API

## Overview
This project analyzes climate data using Python, SQLAlchemy, Pandas, and Matplotlib. The dataset is stored in a SQLite database and explored using Jupyter Notebook. A Flask API is also developed to provide endpoints for querying climate data.

## Tools and Technologies Used
**Python:** Used for data analysis and API development.

**SQLite:** Database storing historical climate data.

**SQLAlchemy:** ORM for querying and managing the database.

**Pandas:** For data manipulation and analysis.

**Matplotlib:** For visualizing precipitation and temperature trends.

**Flask:** Web framework to create API endpoints.

**Part 1: Climate Data Analysis**

## Dataset
The dataset contains climate records from multiple weather stations in Hawaii. Key tables:

- Measurement: Includes daily temperature, precipitation, and station data.

- Station: Contains information about weather stations.

## Part 1: Climate Data Analysis
1. **Connecting to the Database**

Used SQLAlchemy to establish a connection with the SQLite database.

Reflected the database schema into Python classes.

2. **Precipitation Analysis**

Retrieved precipitation data for the last 12 months.

Stored the data in a Pandas DataFrame and sorted by date.

Visualization: A bar chart was created to display precipitation trends.

**Precipitation Trends Over the Last 12 Months**

![Precipitation Trends Over the Last 12 Months](https://github.com/user-attachments/assets/59b9e515-e82f-4b9e-afd9-4e49de27dea5)

3. **Station Analysis**

Identified the total number of weather stations.

Found the most active station based on data records.

Queried the highest, lowest, and average temperature for the most active station.

Retrieved temperature observations for the past year and plotted them as a histogram.

**Temperature Frequency Distribution for the Most Active Station**

![Temperature Observations at the Most Active Station](https://github.com/user-attachments/assets/2b78665a-d709-46e2-95da-f795810446e0)

## Part 2: Building a Flask API

A Flask application was developed to provide access to climate data through API endpoints.

###Available API Endpoints

1. **Home Route (/)**

Displays available API routes.

2. **Precipitation Data (/api/v1.0/precipitation)**

Returns the last 12 months of precipitation data in JSON format.

3. **Station Data (/api/v1.0/stations)**

Returns a list of all weather stations.

4. **Temperature Observations (/api/v1.0/tobs)**

Returns the last 12 months of temperature data for the most active station.

5. **Temperature Statistics (/api/v1.0/prev_year_temperature)**

Returns a JSON list of temperature observations from the last 12 months.

## Conclusion
This project demonstrates how historical climate data can be analyzed and shared through an API. It provides valuable insights into temperature and precipitation trends while allowing easy access to climate data for further analysis.
