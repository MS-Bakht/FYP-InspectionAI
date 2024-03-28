import cv2

# Replace with your phone's IP camera address
ip_address = "http://172.16.53.64:4747/"

# Open video capture stream
cap = cv2.VideoCapture(ip_address)

if not cap.isOpened():
    print("Error opening video stream or invalid IP address")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Check if frame is read correctly
    if not ret:
        print("Failed to capture frame")
        break

    # Display the resulting frame
    cv2.imshow('Live Feed', frame)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) == ord('q'):
        break

# Release capture and close all windows
cap.release()
cv2.destroyAllWindows()
