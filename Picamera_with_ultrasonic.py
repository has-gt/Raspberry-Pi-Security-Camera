import RPi.GPIO as GPIO
import time
import picamera
GPIO.setmode(GPIO.BCM)
from datetime import datetime

TRIG = 23 
ECHO = 24
print ("Distance Measurement In Progress")

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
try:
    while True:

        GPIO.output(TRIG, False)
        print ("Waiting For Sensor To Settle")
        time.sleep(2)

        GPIO.output(TRIG, True)
        time.sleep(0.0001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
          pulse_start = time.time()

        while GPIO.input(ECHO)==1:
          pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start

        distance = pulse_duration * 17150

        distance = round(distance, 2)

        print ("Distance:",distance,"cm")
        
        if distance <= 40: #Change trigger distance in centimeters
            print("Object detected")
            with picamera.PiCamera() as camera:
                time.sleep(2)
                filename = datetime.now().strftime('%A-%y%m%d%H%M.jpg') #Saving file name using the current system date and time
                camera.capture('/home/pi/Pictures/' + datetime.now().strftime('%A-%y%m%d%H%M.jpg')) #Captured images are saved "Pictures" folder
            print("image captured")
            
            print (datetime.now().strftime("%A-%y%m%d%H%M%S.jpg"))
        else:
            print("object  not detected")

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()
