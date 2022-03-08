import RPi.GPIO as GPIO
import datetime
import time
import cv2

def captureImage(folderName):
    videoCapture=cv2.VideoCapture(0)

    videoCapture.set(3,640)
    videoCapture.set(4,480)
    ret,frame=videoCapture.read()
    
    currentTime=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')

    cv2.imwrite(folderName+"/"+currentTime+".jpg",frame)
    GPIO.output(7,True)
    print(folderName+" 폴더에 "+currentTime+".jpg 저장")
    time.sleep(1)
    GPIO.output(7,False)

    videoCapture.release()

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(7,GPIO.OUT)

while True:
    if GPIO.input(37)==0:
        if GPIO.input(10)==0:
            captureImage("Dataset_Jikjin")
        elif GPIO.input(12)==0:
            captureImage("Dataset_Kkeut")
        else:
            captureImage("Dataset_Galimgil")
