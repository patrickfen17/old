import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify, request
import datetime as dt

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]<br/>"
        f"/api/v1.0/[start_date format:yyyy-mm-dd]/[end_date format:yyyy-mm-dd]"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query measurements for precipitation data
    results = session.query(measurement.date, measurement.prcp).all()

    session.close()

    # Convert the query results to a dictionary
    precipt_scores = list(np.ravel(results))

    return jsonify(precipt_scores)

@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    results = session.query(station.station).all()

    session.close()

    # Turn query results into a list of stations
    all_stations = list(np.ravel(results))
    
    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(measurement.date, measurement.tobs, measurement.prcp).\
        filter(measurement.date >= "2016-08-23").\
        filter(measurement.date <= "2017-08-23").all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_passengers = []
    for name, age, sex in results:
        passenger_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        all_passengers.append(passenger_dict)

    return jsonify(all_passengers)

@app.route("/api/v1.0/gender/<gen>/<survival>")
def passengers_gender_survival(gen, survival):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(Passenger.name, Passenger.age, Passenger.sex, Passenger.survived)\
        .filter(Passenger.sex==gen).filter(Passenger.survived==survival).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_passengers = []
    for name, age, sex, survived in results:
        passenger_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        passenger_dict["survival"] = survived
        all_passengers.append(passenger_dict)

    return jsonify(all_passengers)

@app.route("/api/v1.0/gender/alt")
def passengers_gender_survival_alt():

    #http://127.0.0.1:5000/api/v1.0/gender/alt?gen=male&survival=1
    # Create our session (link) from Python to the DB
    session = Session(engine)

    print(request.args['gen'])
    print(request.args['survival'])

    if 'gen' in request.args:
        gen = request.args['gen']
    else:
        return "Error: No gender field provided. Please specify a gender."

    if 'survival' in request.args:
        survival = request.args['survival']
    else:
        return "Error: No survival field provided. Please specify a survival."

    """Return a list of passenger data including the name, age, and sex of each passenger"""
    # Query all passengers
    results = session.query(Passenger.name, Passenger.age, Passenger.sex, Passenger.survived)\
        .filter(Passenger.sex==gen).filter(Passenger.survived==survival).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_passengers = []
    for name, age, sex, survived in results:
        passenger_dict = {}
        passenger_dict["name"] = name
        passenger_dict["age"] = age
        passenger_dict["sex"] = sex
        passenger_dict["survival"] = survived
        all_passengers.append(passenger_dict)

    return jsonify(all_passengers)


if __name__ == '__main__':
    app.run(debug=True)
