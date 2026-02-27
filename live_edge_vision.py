import cv2, time
cap = cv2.VideoCapture(0)
t0, frames = time.time(), 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    edges = cv2.Canny(frame, 120, 240)
    frames += 1
    elapsed = time.time() - t0
    fps = frames / elapsed 
    cv2.putText(frame, f'FPS: {fps:.2f}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow('Live Edge Vision', edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()