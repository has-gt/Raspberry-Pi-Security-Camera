This project can be used to capture images using Pi camera when Ultrasonic sensor is triggered.

The captured images will be saved to Pictures folder in Raspberry Pi and 
files are named by the current date and time of the capture so that the files
are not replaced and it's easy to find the images using the filename.

HC - SR04 Ultrasonic sensor is used to measure the distance of a target object which 
is within 2cm to 400cm range. It has a resolution of 0.3cm and a frequency of 40kHz. 

HC - SR04 is an electronic device which uses a similar technique like radars execute
to identify objects. It emits ultrasonic sound waves using its transmitter and then wait 
for the receiver to capture the reflected sound waves back. The distance can be 
calculated based on the time required for this process.

However, the HC - SR04 Ultrasonic Sensor is not compatible with Raspberry Pi as the 
Raspberry Pi works at 3.3V and the Ultrasonic Sensor works at 5V. HC - SR04 can be 
connected the Raspberry Pi but the high voltage output from the sensor can cause 
damage to the GPIO pins of Raspberry Pi. So, you have to use a voltage divider to overcome 
this problem.

Voltage divider for the ultrasonic sensor as the Raspberry Pi works at 3.3V 
and the Ultrasonic Sensor works at 5V. The output (ECHO pin) of the ultrasonic is 0V 
unless it’s been triggered. It outputs 5V when the sensor is triggered. But its reduced 
to 3.3V by the voltage divider. This voltage divider consists of a 1KΩ resistor and a 
2KΩ which are connected to an input voltage in series method. A bread board and few 
jumper cables are required for the connection.
