import cv2
import tensorflow as tf
import numpy as np

def preprocessing(frame):
    frame_cropped=frame[160:480, 160:480].copy()
    frame_resized=cv2.resize(frame_cropped, (224, 224), interpolation=cv2.INTER_AREA)
    frame_nomalized=(frame_resized.astype(np.float32)/127.0)-1
    frame_reshaped=frame_nomalized.reshape((1, 224, 224, 3))
    return frame_reshaped

model_filename='./model/keras_model.h5'
model=tf.keras.models.load_model(model_filename)

capture=cv2.VideoCapture(0)

capture.set(3, 640)
capture.set(4, 480)

while True:
    ret,frame=capture.read()
    #frame=cv2.flip(frame, 1)

    if cv2.waitKey(200)>0:
        break

    frame_preprocessed=preprocessing(frame)
    prediction=model.predict(frame_preprocessed)

    if prediction[0,1] < prediction[0,0] and prediction[0,2] < prediction[0,0]:
        cv2.putText(frame, 'Jikjin', (10, 10), cv2.FONT_HERSHEY_DUPELX, 2, (0, 0, 0))
    elif prediction[0,0] < prediction[0,1] and prediction[0,2] < prediction[0,1]:
        cv2.putText(frame, "Galimgil", (10, 10), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 0))
    elif prediction[0,0] < prediction[0,2] and prediction[0,1] < prediction[0,2]:
        cv2.putText(frame, 'Kkeut', (10, 10), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 0))

    cv2.imshow("Predicted Frame", frame)

capture.release()

cv2.destroyAllWindows()
