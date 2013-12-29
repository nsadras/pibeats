from socket import *
import RPi.GPIO as GPIO
myHost = ''
myPort = 2000

# socket setup
s = socket(AF_INET, SOCK_STREAM)    # create a TCP socket
s.bind((myHost, myPort))            # bind it to the server port
s.listen(5)                         # allow 5 simultaneous pending connections

# GPIO setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11 , GPIO.OUT)
GPIO.setup(12 , GPIO.OUT)
GPIO.setup(13 , GPIO.OUT)
GPIO.setup(15 , GPIO.OUT)



while 1:
    # wait for next client to connect
    connection, address = s.accept() # connection is a new socket
    while 1:
        data = connection.recv(1024) # receive up to 1K bytes
        print data
        if data:
            connection.send('echo -> ' + data)
        else:
            break
    connection.close()              # close socket
