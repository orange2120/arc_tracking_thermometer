import serial

ser = serial.Serial('/dev/ttyUSB0', 115200)

text = 'test message\n'
#ser.write(text.encode())
#ser.write(bytes.encode(text,"ASCII"))
data = ser.readline()
print(data.decode('utf8'))

ser.close()
