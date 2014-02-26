import serial
import string
import threading

class GPS:
    def __init__(self):
        self.ser = serial.Serial('/dev/tty.usbserial', baudrate=4800)
        self.lat = 0
        self.lng = 0
        polling_thread = threading.Thread(target=self.poll)
        polling_thread.start()
        # polling_thread.join()

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        # do things
        self.ser.close()
        print "Exited GPS"

    def poll(self):
        print "Polling"
        # might be tty.usbserial or cu.usbserial
        try:
            while self.ser.isOpen():
                line = self.ser.readline()
                print line.strip()
                if 'GPGLL' in line:
                    reading = line.split(',')
                    data = self.parseGLL(reading[:-1])
                    self.lat = data['Latitude']
                    self.lng = data['Longitude']
                    print self.lat, self.lng
        except:
            print "Exception."


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


    def parseGLL(self, fields):
        """
        Parses the Geographic Position-Latitude/Longitude sentence fields.
        """
        data = {}

        # GLL has 8 fields
        assert len(fields) == 7

        # MsgId = fields[0]
        data['Latitude'] = self.toDecimalDegrees(fields[1])
        data['NsIndicator'] = fields[2]
        data['Longitude'] = self.toDecimalDegrees(fields[3])
        data['EwIndicator'] = fields[4]
        data['UtcTime'] = fields[5]
        data['GllStatus'] = fields[6]

        # Attend to lat/lon plus/minus signs
        if data['NsIndicator'] == 'S':
            data['Latitude'] *= -1.0
        if data['EwIndicator'] == 'W':
            data['Longitude'] *= -1.0

        return data


