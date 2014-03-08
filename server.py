from StringIO import StringIO
from flask import Flask, url_for
import flask
import serial
import string

from gps import GPS
from camera import Camera

app = Flask(__name__)
ser = serial.Serial('/dev/tty.usbserial', baudrate=4800)

gps_obj = None
camera_obj = None

@app.route("/position")
def position():
    print "Checking for position", gps_obj.lat, gps_obj.lng
    # return str(gps_obj.lat)
    return flask.jsonify(lat=gps_obj.lat, lng=gps_obj.lng)

@app.route("/photo")
def photo():
    print "Getting a photo"

    fp = StringIO()
    image = camera_obj.snap()
    image.save(fp, 'png')
    # print fp.getvalue()
    response = flask.make_response(fp.getvalue())
    response.headers['Content-Type'] = 'image/png'
    return response


if __name__ == "__main__":
    with GPS() as gps_obj:
        with Camera() as camera_obj:
            app.run(debug=True)
            url_for('static', filename='index.html')


