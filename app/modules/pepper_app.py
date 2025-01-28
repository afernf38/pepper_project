from app.modules.pepper_motion import PepperMotion
from app.modules.pepper_speech import PepperSpeech


class PepperApp:
    def __init__(self, tts_proxy, motion_proxy):
        self.speech_module = PepperSpeech(tts_proxy)
        self.motion_module = PepperMotion(motion_proxy)
        self.tablet_module = PepperTablet()
    
    def handle_tablet_command(seld, command):
        self.tablet_module.handle_command(command, seld.speech_module, self.motion_module)