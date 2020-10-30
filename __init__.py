class RemindEvents(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('events.remind.intent')
    def handle_events_remind(self, message):
        self.speak_dialog('events.remind')


# we import the Twilio client from the dependency we just installed


# the following line needs your Twilio Account SID and Auth Token
client = Client("AC429a4c06f04eb36287f1c2a682c90a2a", "cc764e749192f49c9869c8e16630424a")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="+16267095806", 
                       from_="+2012400693", 
                       body="Hello from Python!")

def create_skill():
    return RemindEvents()

