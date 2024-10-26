import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor:
        def __init__(self, rpwm, lpwm):
                self.rpwm = rpwm     #instance variable for pwms
                self.lpwm = lpwm
                
                GPIO.setup(self.rpwm, GPIO.OUT) #setting pwms as output 
                GPIO.setup(self.lpwm, GPIO.OUT)
                
                rpwm_control = GPIO.PWM(self.rpwm, 100)   #setting up the pwm frequency as 100
                lpwm_control = GPIO.PWM(self.lpwm, 100)
                rpwm_control.start(0)
                lpwm_control.start(0)
        
        def move(self, speed=0.5, turn=0, time=0):
                speed *= 100
                self.rpwm_control.ChangeDutyCycle(speed)
                self.lpwm_control.ChangeDutyCycle(0)
                sleep(2)
                
def main():
        motor1.move(0.6,0,4)
        
if __name__ == 'main':
        motor1 = Motor(22, 23)
        main()
        
        
                


                
                 
                