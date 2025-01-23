#Modulo para interaccions de voz
class PepperSpeech:
    def __init__(self, tts_proxy):
        self.tts = tts = tts_proxy
    
    def say(self, text):
        self.tts.say(text)