#Modulo para manejar interacciones con la tablet
class PepperTablet:
    def __init__(self):
        self.commands = {
            "hola": self.say_hello,
            "baila": self.start_dance
        }
    
    def handle_command(self, command, speech_module, motion_module):
        action = self.commands.get(command)
        if action:
            action(speech_module, motion_module)
    
    def say_hello(self, speech_module, motion_module):
        speech_module.say("Hola, ¿como estas?")
    
    def start_dance(self, speech_module, motion_module):
        speech_module.say("Voy a bailar ahora.")
        motion_module.move_to(0, 0, 1.57)