import cv2
import requests
import numpy as np

# Replace with your phone's IP Webcam URL
URL = "http://100.85.131.104:8080/shot.jpg"

while True:
    # Fetch the image from the webcam
    img_resp = requests.get(URL, timeout=10)  # Timeout set to 10 seconds

    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
    frame = cv2.imdecode(img_arr, -1)

    # Show the live feed
    cv2.imshow("IP Webcam", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()