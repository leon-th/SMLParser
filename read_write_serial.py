import serial

def readSerial(serialport, count):
        ser = serial.Serial(serialport)
        output = ser.read(count)
        ser.close()
        return output

def writeSerial(serialport, content):
        ser = serial.Serial(serialport)
        ser.write(content)
        ser.close()
        return