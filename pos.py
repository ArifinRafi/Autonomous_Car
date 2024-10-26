import cv2
import numpy as np
import time  # For delay

# Initialize the camera
cap = cv2.VideoCapture(1)  # Use 0 for the default camera, or change if using another one

def get_object_position(frame):
    """
    Function to detect an object based on color (e.g., black) and return its position.
    Returns the object's x and y coordinates (center of the object).
    """
    # Convert the frame to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the color range for black
    lower_black = np.array([78,158,124])
    upper_black = np.array([138,255,255])
    
    # Create a mask to extract the black object
    mask = cv2.inRange(hsv, lower_black, upper_black)

    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # If contours are found, calculate the object's position
    if contours:
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)
        cx = x + w // 2
        cy = y + h // 2

        # Draw the bounding box and center point on the frame (optional)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

        return (cx, cy)
    else:
        return None

while True:
    # Capture each frame from the camera
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    # Get the frame dimensions
    height, width, _ = frame.shape
    middle_x = width // 2  # Calculate the middle point of the x-axis
    tolerance = 20         # Set a tolerance range for detecting "center"

    # Get the position of the object
    object_position = get_object_position(frame)

    if object_position:
        cx, cy = object_position
        print(f"Object position: X = {cx}, Y = {cy}")
        
        # Check if the object is to the left, right, or center (within a tolerance range)
        if cx < middle_x - tolerance:
            print("left of the center")
        elif cx > middle_x + tolerance:
            print("right of the center")
        else:
            print("center")  # Now, you'll see "center" when the object is near the middle
    else:
        print("Object not detected")

    # Display the frame
    cv2.imshow('Object Detection', frame)

    # Add a half-second delay
    time.sleep(0.5)

    # Break the loop on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
