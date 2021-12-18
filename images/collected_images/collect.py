import cv2
from datetime import datetime

cam = cv2.VideoCapture("http://raspberrypi.local:8080/stream/video.mjpeg")   # Change to own camera (url, ip, or int)

cv2.namedWindow("Press space to capture...")

img_label = "robot_"  # Sets the prefix of the image when saved. Helps to organise images, especially when training for several objects.

while True:
    # Show new frame and act upon key presses
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("Press space to capture...", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        img_name = "{}.jpg".format(img_label+datetime.now().strftime("%d%m%y_%H%M%S%f"))
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))

cam.release()

cv2.destroyAllWindows()