import cv2
import time

timeStart = time.perf_counter()

vidCamera = cv2.VideoCapture("BadApple.mp4")

ret = True
intCurFrame = 0

while ret :

    intCurFrame+=1
    ret , imgNext = vidCamera.read()

    if not ret:
        print("End of file")
        break

    if intCurFrame%2 != 0 :
        continue

    cv2.imwrite(f"./Output/frame_{intCurFrame}.png" , imgNext)

timeEnd = time.perf_counter() - timeStart
print(timeEnd)