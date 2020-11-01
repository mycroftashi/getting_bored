from mycroft import MycroftSkill, intent_file_handler
from twilio.rest import Client
import RPi.GPIO as GPIO
import time

class RemindEvents(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('events.remind.intent')
    def handle_events_remind(self, message):
        self.speak_dialog('events.remind')

#start - send sms
# we import the Twilio client from the dependency we just installed


# the following line needs your Twilio Account SID and Auth Token
#client = Client("AC429a4c06f04eb36287f1c2a682c90a2a", "2d7e4dc79393ccbbd8d4827d076fa24c")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
#client.messages.create(to="+12012400693", 
                       from_="+16267095806", 
                       body="Hello from Python!")
#start - finish sms
                       
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

def create_skill():
    return RemindEvents()


