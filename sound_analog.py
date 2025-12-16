import serial

# The address of the serial port was determined above.
ser = serial.Serial('/dev/ttyACM1')

while True:
    # Read a line from the serial port. It will need to be decoded from bytes to utf-8.
    # Additionally, there are new line characters attached to the reading which must be removed. 
    reading = ser.readline().decode('utf-8').strip('\r\n')
   
    print(reading)

