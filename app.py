import serial
import string


def toDecimalDegrees(ddmm):
    """
    Converts a string from ddmm.mmmm or dddmm.mmmm format
    to a float in dd.dddddd format
    """

    splitat = string.find(ddmm, '.') - 2
    return _float(ddmm[:splitat]) + _float(ddmm[splitat:]) / 60.0


def _float(s):
    """
    Returns the float value of string s if it exists,
    or None if s is an empty string.
    """
    if s:
        return float(s)
    else:
        return None


def parseGLL(fields):
    """
    Parses the Geographic Position-Latitude/Longitude sentence fields.
    Stores the results in the global data dict.
    """
    data = {}

    # GLL has 8 fields
    assert len(fields) == 7

    # MsgId = fields[0]
    data['Latitude'] = toDecimalDegrees(fields[1])
    data['NsIndicator'] = fields[2]
    data['Longitude'] = toDecimalDegrees(fields[3])
    data['EwIndicator'] = fields[4]
    data['UtcTime'] = fields[5]
    data['GllStatus'] = fields[6]

    # Attend to lat/lon plus/minus signs
    if data['NsIndicator'] == 'S':
        data['Latitude'] *= -1.0
    if data['EwIndicator'] == 'W':
        data['Longitude'] *= -1.0

    return data


ser = serial.Serial('/dev/tty.usbserial', baudrate=4800)
# might be tty.usbserial or cu.usbserial
while ser.isOpen():
    line = ser.readline()
    print line.strip()
    if 'GPGLL' in line:
        reading = line.split(',')
        data = parseGLL(reading[:-1])
        # print data['Latitude'], data['Longitude']

ser.close()
