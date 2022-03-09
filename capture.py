import RPi.GPIO as GPIO # 라즈베리 파이의 GPIO를 제어하는 모듈을 불러옵니다.
import datetime # 현재 시간을 불러오는 모듈을 불러옵니다.
import time # sleep 함수가 내장된 모듈을 불러옵니다.
import cv2 # OpenCV 모듈을 불러옵니다.

# 캡쳐된 이미지를 폴더에 저장하는 함수 (매개변수 folderName = 이미지를 저장할 폴더 이름)
def captureImage(folderName):
    # 카메라 입력 받기
    videoCapture=cv2.VideoCapture(0)

    # 이미지 크기 조절하기
    videoCapture.set(3,640)
    videoCapture.set(4,480)
    ret,frame=videoCapture.read()
    
    # 현재 시간(파일명) 불러오기
    currentTime=datetime.datetime.now().strftime('%Y%m%d-%H%M%S')

    # 이미지 저장하고 LED 켰다 끄기
    cv2.imwrite(folderName+"/"+currentTime+".jpg",frame)
    GPIO.output(7,True)
    print(folderName+" 폴더에 "+currentTime+".jpg 저장")
    time.sleep(1)
    GPIO.output(7,False)

    # 카메라 입력 그만 받기
    videoCapture.release()

# GPIO 설정
GPIO.setmode(GPIO.BOARD) # GPIO 모드를 보드로 설정하여 보드 내 순차적인 핀 번호를 사용함니다.
GPIO.setup(37,GPIO.IN,pull_up_down=GPIO.PUD_UP) # 촬영 버튼
GPIO.setup(12,GPIO.IN,pull_up_down=GPIO.PUD_UP) # 토글 스위치 (끝)
GPIO.setup(10,GPIO.IN,pull_up_down=GPIO.PUD_UP) # 토글 스위치 (직진)
GPIO.setup(8,GPIO.IN,pull_up_down=GPIO.PUD_UP) # ?
GPIO.setup(7,GPIO.OUT) # 촬영 시 점등하는 LED

# 소스 실행을 중단할 때까지 반복
while True:
    # 촬영 버튼이 눌리면
    if GPIO.input(37)==0:
        # 직진 폴더에 이미지를 저장
        if GPIO.input(10)==0:
            captureImage("Dataset_Jikjin")
        # 끝 폴더에 이미지를 저장
        elif GPIO.input(12)==0:
            captureImage("Dataset_Kkeut")
        # 갈림길 폴더에 이미지를 
        else:
            captureImage("Dataset_Galimgil")
