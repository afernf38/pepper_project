#Módulo para movimientos
class PepperMotion:
    def __init__(self, motion_proxy):
        self.motion = motion_proxy
    
    def move_to(self, x, y, theta):
        self.motion.moveTo(x, y, theta)