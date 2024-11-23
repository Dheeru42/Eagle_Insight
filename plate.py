import cv2
import imutils
import numpy as np
import requests
harscade = r"D:\ai project\number_plate\haarcascade_russian_plate_number.xml"

# Camera Configuration
# cam = cv2.VideoCapture(0)
# cam.set(3,640) # height
# cam.set(4,480) # width
min_area = 500

def cap():
    # _,img = cam.read()  
    
    images = requests.get("http://192.168.2.100:8080/shot.jpg")
    vedionp = np.array(bytearray(images.content),dtype=np.uint8)
    ved = cv2.imdecode(vedionp,-1)
    img = imutils.resize(ved,width=1000)
    # cv2.imshow("Mobile IPCamera",img)
    if ord("q") == cv2.waitKey(1):
        exit(0)
        
    plate_cascade = cv2.CascadeClassifier(harscade)
    
    img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    plates = plate_cascade.detectMultiScale(img_gray,1.1,4) 
    
    for(x,y,w,h) in plates:
        area = w*h
        if area > min_area:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(img,'Number Plate Detect',(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,255),2)
            img_roi = img[y:y+h,x:x+w]
            cv2.imshow('ROI',img_roi)
            gray=cv2.cvtColor(img_roi,cv2.COLOR_BGR2GRAY)
            # gray1=cv2.bilateralFilter(gray,11,17,17)
            thres=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)[1]
            image=imutils.resize(thres,width=500)
            # name = 1  # count
            cv2.imwrite(r'D:\project\ml model\eagle\eagleinsight\static\images\1.png',image)
    cv2.imshow('Number Plate',img) # Show Image
    # cv2.imshow("Mobile IPCamera",img)
    
# # # Program Start
# while True:
#     cap()
#     if cv2.waitKey(1) == ord('q'): # interrupt
#         break

# # cam.release()    
# cv2.destroyAllWindows()
            