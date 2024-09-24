import cv2
import numpy as np
import os

#easy use cls to clear screen / shell history
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

class ImageHandler:
    def divImage(self, image, num_parts_y_x = ( 2 , 2 ) ) :
        #gray image
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

        #split horizontally
        hor_list = np.array_split(image, num_parts_y_x[0])
        
        #split vertically
        split_image_list = []

        for block in hor_list :
            split_image_list.append(np.array_split(block , num_parts_y_x[1], axis= 1))

        return split_image_list

    def getAvgBrightness(self, image) :
        #turn into hsv
        hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
        #grab only the value
        _ , _ , v = cv2.split(hsv_image)

        return int(np.average(v.flatten()))
    
    def getAvgBrightnessGRAY(self, image) :
        #just get the value since grayscale
        return int(np.mean(image))

#grab video feed

#vidCamera = cv2.VideoCapture(0)
vidCamera = cv2.VideoCapture(0)

ret = True

while ret :

    #quit if camera stream closed
    if not vidCamera.isOpened():
        print("Camera stream closed unexpectedly")
        break

    #get next frame
    ret , imgGray = vidCamera.read()

    #if frame fails to load , quit
    if not ret:
        print("Could not load frame")
        break

    #get max brightness
    intMaxBrightFrac = int( cv2.minMaxLoc(cv2.cvtColor(imgGray,cv2.COLOR_BGR2GRAY))[1]/5 )

    #set max parts number and base division to attempt
    intDivMod = 5
    intMaxParts = 100

    #keep increasing divmod until we meet the max parts requirement
    while (int(imgGray.shape[0]/intDivMod) > intMaxParts) | (int(imgGray.shape[1]/intDivMod) > intMaxParts) :
        intDivMod += 5

    #set the amount of splits
    intYSplit = int(imgGray.shape[0]/intDivMod)
    intXSplit = int(imgGray.shape[1]/intDivMod)

    #split the image
    imgProcessList = ImageHandler.divImage(ImageHandler, imgGray, (intYSplit,intXSplit))

    #prepare the string output array
    lstOutArray : list = [""]

    # loop through both dimensions
    for idYAx in range (len(imgProcessList)):
        
        #add our Y layer
        lstOutArray.append("")

        #loop current y layer in x dimension
        for idXAx in range (len(imgProcessList[idYAx])):

            #determine the current chunks average brightness
            intCurBright = ImageHandler.getAvgBrightnessGRAY(ImageHandler, imgProcessList[idYAx][idXAx])

            #allocate buffer
            strCharBuffer = ""

            #set buffer accodring to brightness of current chunk compared to image max brightness
            if intCurBright < intMaxBrightFrac :
                strCharBuffer = "   "
            elif intCurBright < intMaxBrightFrac*3 :
                strCharBuffer = "░░░"
            elif intCurBright < intMaxBrightFrac*4 :
                strCharBuffer = "▒▒▒"
            else :
                strCharBuffer = "▓▓▓"

            #add the current buffer to our Y line
            lstOutArray[idYAx] = lstOutArray[idYAx] + strCharBuffer


    #print line by line
    cls()
    for line in lstOutArray :
        print(line)

    #this doesn't work but very cool
    if cv2.waitKey() & 0xFF == ord('q'):
        break