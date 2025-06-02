import cv2

capture = cv2.VideoCapture(0)
if not capture.isOpened():
    print("Error: Could not open video.")
    exit()


while True:
    ret, frame = capture.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    cv2.imshow('Video Capture', frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
capture.release()
cv2.destroyAllWindows()