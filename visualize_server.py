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

led0 = GPIO.PWM(11, 50)
led1 = GPIO.PWM(12, 50)
led2 = GPIO.PWM(13, 50) # pointless comment
led3 = GPIO.PWM(15, 50)


led0.start(0)
led1.start(0)
led2.start(0)
led3.start(0)

while 1:
    # wait for next client to connect
    connection, address = s.accept() # connection is a new socket
    while 1:
        data = connection.recv(1024) # receive up to 1K bytes
        levels = data.strip('[]').split(',') 
        if data:
            led0.ChangeDutyCycle(int(levels[0])) 
            led0.ChangeDutyCycle(int(levels[1])) 
            led0.ChangeDutyCycle(int(levels[2]))
            led0.ChangeDutyCycle(int(levels[3])) 

        else:
            break

    GPIO.cleanup()
    connection.close()              # close socket
