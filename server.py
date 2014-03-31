from StringIO import StringIO
from flask import Flask, url_for
import flask
import serial
import string

from gps import GPS
from camera import Camera

PHOTODIR = 'static/photos/'

app = Flask(__name__)
ser = serial.Serial('/dev/tty.usbserial', baudrate=4800)

gps_obj = None
camera_obj = None

@app.route("/position")
def position():
    print "Checking for position", gps_obj.lat, gps_obj.lng
    # return str(gps_obj.lat)
    return flask.jsonify(lat=gps_obj.lat, lng=gps_obj.lng)


"""
Take a photo and save it with the ll as the filename.
Also send it as a response
"""
@app.route("/photo")
def photo():
    print "Getting a photo"
    image = camera_obj.snap()

    # We'll first save the image locally
    # Filename is based on position
    lat = gps_obj.lat
    lng = gps_obj.lng
    filename = PHOTODIR + str(lat) + str(lng) + ".png"
    image.save(filename) # Save the image for later


    return flask.jsonify(lat=lat, lng=lng, photo=filename)
    # # We'll also save the image as a buffer so we can send it by http
    # fp = StringIO()
    # image.save(fp, 'png')
    # response = flask.make_response(fp.getvalue())
    # response.headers['Content-Type'] = 'image/png'
    # return response


if __name__ == "__main__":
    with GPS() as gps_obj:
        with Camera() as camera_obj:
            app.run(debug=True)
            url_for('static', filename='index.html')


