import pygame
from time import sleep

# Initialize pygame and joystick module
pygame.init()
pygame.joystick.init()

# Check if a joystick is connected
if pygame.joystick.get_count() < 1:
    print("No joystick detected!")
else:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
    print(f"Detected joystick: {joystick.get_name()}")

def main():
    try:
        while True:
            pygame.event.pump()
            
            # Get the X and Y axis values for the left joystick
            left_stick_x = joystick.get_axis(0)  # X-axis of left joystick (horizontal movement)
            left_stick_y = joystick.get_axis(1)  # Y-axis of left joystick (vertical movement)

            # Define a threshold to detect significant movement
            threshold = 0.1

            # Check if either axis has moved beyond the threshold
            if abs(left_stick_x) > threshold or abs(left_stick_y) > threshold:
                print(f"Left Joystick - X: {left_stick_x:.2f}, Y: {left_stick_y:.2f}")

            sleep(0.1)

    except KeyboardInterrupt:
        print("Joystick test ended.")
    finally:
        pygame.quit()

if __name__ == '__main__':
    main()
