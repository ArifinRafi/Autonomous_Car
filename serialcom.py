import serial
ser = serial.Serial('COM4', 9600)

while True:
        inp = input()

        if inp == 'a':
                ser.write('a'.encode())
        elif inp == 'b':
                ser.write('b'.encode())
        else:
                pass