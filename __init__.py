from mycroft import MycroftSkill, intent_file_handler


class RemindEvents(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('events.remind.intent')
    def handle_events_remind(self, message):
        self.speak_dialog('events.remind')




def create_skill():
    return RemindEvents()

