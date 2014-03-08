import pynmea2
import serial
import string
import threading


"""
https://github.com/Knio/pynmea2

Some format documentation here:
http://www.kh-gps.de/nmea.faq


GLL - Geographic position, Latitude and Longitude
GLL,4916.45,N,12311.12,W,225444,A
   4916.46,N    Latitude 49 deg. 16.45 min. North
   12311.12,W   Longitude 123 deg. 11.12 min. West
   225444       Fix taken at 22:54:44 UTC
   A            Data valid
     (Garmin 65 does not include time and status)
"""

class GPS:
    def __init__(self):
        self.ser = serial.Serial('/dev/tty.usbserial', baudrate=4800)
        self.lat = 0
        self.lng = 0
        self.polling_thread = threading.Thread(target=self.poll)
        self.polling_thread.daemon = True
        self.polling_thread.start()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.ser.close()
        print "Exited GPS"

    def poll(self):
        print "Polling"
        streamreader = pynmea2.NMEAStreamReader()
        while self.ser.isOpen():
            data = self.ser.readline()
            for msg in streamreader.next(data):
                if (msg.type == 'GGA'):
                    self.lat = self.toDecimalDegrees(msg.lat)
                    self.lng = self.toDecimalDegrees(msg.lon)

                    print self.lat, self.lng


    def toDecimalDegrees(self, ddmm):
        """
        Converts a string from ddmm.mmmm or dddmm.mmmm format
        to a float in dd.dddddd format
        """
        splitat = string.find(ddmm, '.') - 2
        return self._float(ddmm[:splitat]) + self._float(ddmm[splitat:]) / 60.0


    def _float(self, s):
        """
        Returns the float value of string s if it exists,
        or None if s is an empty string.
        """
        if s:
            return float(s)
        else:
            return None


    # def parseGLL(self, fields):
    #     """
    #     Parses the Geographic Position-Latitude/Longitude sentence fields.
    #     """
    #     data = {}
    #
    #     # GLL has 8 fields
    #     assert len(fields) == 7
    #
    #     # MsgId = fields[0]
    #     data['Latitude'] = self.toDecimalDegrees(fields[1])
    #     data['NsIndicator'] = fields[2]
    #     data['Longitude'] = self.toDecimalDegrees(fields[3])
    #     data['EwIndicator'] = fields[4]
    #     data['UtcTime'] = fields[5]
    #     data['GllStatus'] = fields[6]
    #
    #     # Attend to lat/lon plus/minus signs
    #     if data['NsIndicator'] == 'S':
    #         data['Latitude'] *= -1.0
    #     if data['EwIndicator'] == 'W':
    #         data['Longitude'] *= -1.0
    #
    #     return data


