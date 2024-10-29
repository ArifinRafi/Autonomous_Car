import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor:
        def __init__(self, right_rpwm, right_lpwm, left_rpwm, left_lpwm ):
                self.right_rpwm = right_rpwm     #instance variable for pwms
                self.right_lpwm = right_lpwm
                self.left_rpwm = left_rpwm
                self.left_lpwm = left_lpwm
                
                GPIO.setup(self.right_rpwm, GPIO.OUT) #setting pwms as output 
                GPIO.setup(self.right_lpwm, GPIO.OUT)
                GPIO.setup(self.left_rpwm, GPIO.OUT) 
                GPIO.setup(self.left_lpwm, GPIO.OUT)
                
                self.right_rpwm_control = GPIO.PWM(self.right_rpwm, 100)   #setting up the pwm frequency as 100
                self.right_lpwm_control = GPIO.PWM(self.right_lpwm, 100)
                self.left_rpwm_control = GPIO.PWM(self.left_rpwm, 100)   #setting up the pwm frequency as 100
                self.left_lpwm_control = GPIO.PWM(self.left_lpwm, 100)
                
                self.right_rpwm_control.start(0)
                self.right_lpwm_control.start(0)
                self.left_rpwm_control.start(0)
                self.left_lpwm_control.start(0)
        
        
        def move(self, speed=0.5, turn=0, time=0):
                speed *= 100
                turning_max = speed*(1+turn)
                turning_min = speed*(1-turn)
                
                if turn > 0:
                        self.right_rpwm_control.ChangeDutyCycle(0)  #turning right directions
                        self.left_rpwm_control.ChangeDutyCycle(0)
                        self.right_lpwm_control.ChangeDutyCycle(turning_min)
                        self.left_lpwm_control.ChangeDutyCycle(turning_max)
                
                elif turn < 0:
                        self.right_rpwm_control.ChangeDutyCycle(turning_max)  #turning towards left directions
                        self.left_rpwm_control.ChangeDutyCycle(turning_min)
                        self.right_lpwm_control.ChangeDutyCycle(0)
                        self.left_lpwm_control.ChangeDutyCycle(0)
                elif turn == 0:
                        self.right_rpwm_control.ChangeDutyCycle(speed)  #turning towards left directions
                        self.left_rpwm_control.ChangeDutyCycle(speed)
                        self.right_lpwm_control.ChangeDutyCycle(0)
                        self.left_lpwm_control.ChangeDutyCycle(0)
                else:
                        self.right_rpwm_control.ChangeDutyCycle(speed)  #turning towards left directions
                        self.left_rpwm_control.ChangeDutyCycle(speed)
                        self.right_lpwm_control.ChangeDutyCycle(0)
                        self.left_lpwm_control.ChangeDutyCycle(0)
                        
        def stop(self):
                        self.right_rpwm_control.ChangeDutyCycle(0)  
                        self.left_rpwm_control.ChangeDutyCycle(0)
                        self.right_lpwm_control.ChangeDutyCycle(0)
                        self.left_lpwm_control.ChangeDutyCycle(0)
                
                       
                        
                        
                        
                                  
                
                
def main():
        motor1.move(0.6,0,4)
        
if __name__ == '__main__':
        motor1 = Motor(22, 23,24,25)
        main()
        
        
                


                
                 
                