# Import the dependencies.
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime as dt
import numpy as np
#################################################
# Database Setup
#################################################
engine = create_engine ("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect = True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    return "Welcome to the home page!"

# Define a route to get the precipitation query results for the last 12 months
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Calculate the date one year from the last date in data set
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent_date = most_recent_date[0]
    most_recent_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d").date()
   
    # Calculate the date one year from the last date in data set
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    last_year_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year_ago).all()

    #Create a dictionary to store the precipitation data for the last 12 months
    precipitation_data = {}
    for date, prcp in last_year_data:
        precipitation_data[date] = prcp

    return jsonify(precipitation_data)

# Design a route to calculate the total number of stations in the dataset
@app.route("/api/v1.0/stations")
def station_count():
    total_stations = session.query(Station.station).count()

    #Return the station data as a list:
    station_data = [total_stations]

    return jsonify(station_data)

# Define a route to find the most active station ID and its lowest, highest, and average temperature
@app.route ("/api/v1.0/tobs")
def tobs ():
    # Query the most active stations and their counts in descending order
    active_stations_query = session.query(Measurement.station, func.count(Measurement.station).label('count')).group_by(Measurement.station).order_by(func.count(Measurement.station).desc())
    active_stations = active_stations_query.all()

    # Get the most active station id from the previous query
    most_active_id = active_stations[0][0]

    # Query the lowest, highest, and average temperature of the most active id
    temp_most_active_id = session.query(func.min(Measurement.tobs),func.max(Measurement.tobs),func.avg(Measurement.tobs)).filter(Measurement.station == most_active_id).first()

    # Convert into a list
    temp_data = list(np.ravel(temp_most_active_id)
                     )
    return jsonify(temp_data)

# Define a route to find the last 12 months of temperature observation data for the most active station
@app.route ("/api/v1.0/prev_year_temperature")
def prev_year_temperature ():
    active_stations_query = session.query(Measurement.station, func.count(Measurement.station).label('count')).group_by(Measurement.station).order_by(func.count(Measurement.station).desc())
    active_stations = active_stations_query.all()
    most_active_id = active_stations[0][0]
    
    # Calculate the date one year from the last date in data set
    most_recent_date = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    most_recent_date = most_recent_date[0]
    most_recent_date = dt.datetime.strptime(most_recent_date, "%Y-%m-%d").date()
   
    # Calculate the date one year from the last date in data set
    one_year_ago = most_recent_date - dt.timedelta(days=365)

    # Query the temperature observation data for the last 12 months
    temp_data_prev_year = session.query(Measurement.tobs).filter(Measurement.date >= one_year_ago).filter(Measurement.station == most_active_id).all()

    #Convert into a list
    temp_data_list = list(np.ravel(temp_data_prev_year))

    return jsonify(temp_data_list)

# Run the Flask app if script is executed directly
if __name__ == "__main__":
    app.run(debug = True)