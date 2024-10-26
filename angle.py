import cv2
import numpy as np

def calculate_steering_angle(segmentation_mask, frame_width):
    if segmentation_mask is None:
        print("Segmentation mask is not loaded properly.")
        return 0  # Return a default steering angle

    # Find the center of the path in the segmentation mask
    path_pixels = np.where(segmentation_mask == 255)  # Assuming the path is white (255)
    
    if len(path_pixels[1]) > 0:
        # Calculate the x-coordinate of the path's center (average x value of path pixels)
        cx_path = int(np.mean(path_pixels[1]))  # The x-values of the path pixels

        # Calculate the center of the frame (middle of the x-axis)
        cx_frame = frame_width // 2

        # Calculate the error (difference between path center and frame center)
        error = cx_frame - cx_path

        # Use the error to determine the steering angle (for example, proportional control)
        steering_angle = -error * 0.1  # Adjust the multiplier for your steering sensitivity

        return steering_angle
    else:
        print("No path detected in the segmentation mask.")
        return 0  # Default steering angle if no path is detected

# Open the camera stream (0 is typically the default camera, change if needed)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open video stream from camera.")
else:
    while True:
        # Capture frame-by-frame from the camera
        ret, frame = cap.read()

        if not ret:
            print("Error: Unable to read frame from camera.")
            break

        # Resize or process frame if needed
        frame_height, frame_width = frame.shape[:2]

        # Dummy segmentation mask for testing purposes
        # Replace this with your segmentation model's output
        # Example: assume the path is in the middle of the image for now
        segmentation_mask = np.zeros((frame_height, frame_width), dtype=np.uint8)
        cv2.rectangle(segmentation_mask, (frame_width//3, frame_height//2), 
                      (2*frame_width//3, frame_height), 255, -1)  # Simulating a white path

        # Calculate steering angle based on the mask
        steering_angle = calculate_steering_angle(segmentation_mask, frame_width)
        print(f"Steering Angle: {steering_angle}")

        # Show the frame and segmentation mask for debugging
        cv2.imshow('Camera Feed', frame)
        cv2.imshow('Segmentation Mask', segmentation_mask)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
