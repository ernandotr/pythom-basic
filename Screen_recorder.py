import pyautogui 
import cv2
import numpy as np

resolution = pyautogui.size()
fourcc = cv2.VideoWriter_fourcc(*"CLCO")
filename = "Recording.mp4"
fps = 30.0
out = cv2.VideoWriter(filename, fourcc, fps, (resolution.width, resolution.height))
cv2.namedWindow("Recording", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Recording", 480, 370)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("Recording", frame)

    if cv2.waitKey(1) == ord("q"):
        break

print("Recording started.")
out.release()
cv2.destroyAllWindows()
print("Recording stopped. Video saved as " + filename)
