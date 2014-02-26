from flask import Flask, url_for
import flask
from gps import GPS
import serial
import string

app = Flask(__name__)
ser = serial.Serial('/dev/tty.usbserial', baudrate=4800)

gps_obj = None


@app.route("/position")
def position():
    print "Checking for position"
    return str(gps_obj.lat)
    # return flask.jsonify(lat=data['Latitude'], lng=data['Longitude'])

if __name__ == "__main__":
    with GPS() as gps_obj:
        app.run(debug=True)
        url_for('static', filename='index.html')


