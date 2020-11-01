import sys
from os.path import abspath, dirname
sys.path.append(abspath(dirname(__file__)))
import GPIO
import time
                       
#start LED
   

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)

state = True

# endless loop, on/off for 1 second
while True:
    GPIO.output(2,True)
    time.sleep(1)
    GPIO.output(2,False)
    time.sleep(1)
    self.speak("Led is working")  
                       
# status = GPIO.get("GPIO1")
 #       self.speak("Led is %s" % status)             


