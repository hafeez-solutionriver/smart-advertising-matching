from flask import Flask, render_template, Response, request
import cv2
import time
import os, sys
import numpy as np
from keras.models import load_model
from flask import jsonify
import random
global gender,group

gender = -1
group =-1

age_model = load_model('./bestWeights_2.hdf5')
gender_model = load_model('./bestGenderModel.hdf5')
app = Flask(__name__, template_folder='./templates')
camera = cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    while True:
        success, frame = camera.read() 
        if success:
            cv2.imwrite('dummy.png', frame)
            image = cv2.imread('dummy.png')
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            faces = faceCascade.detectMultiScale(
                        image,
                        scaleFactor=1.3,
                        minNeighbors=3,
                        minSize=(30, 30)
            )
            i =1
            for (x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                    roi_color = image[y:y + h, x:x + w]
                    if len(roi_color) !=0:

                        
                        cv2.imwrite('face.png', roi_color)
                        
                        image=cv2.imread('face.png')
                        # image=cv2.imread('./baby2.PNG')
                        image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
                        image=cv2.resize(image,(100,100))
                        image =np.array(image)
                        image  = image.reshape((-1, 100, 100, 1))
                        box_color = (255, 0, 0)
                        font_scale = 0.5
                        global gender, group
                        gender = gender_model.predict(image)
                        group = np.argmax(age_model.predict(image))
                        url=""  
                        if gender==0:
                          if group==0:
                            url="https://www.youtube.com/embed/UojsFeHfij0"
                          elif group==1:
                            url="https://www.youtube.com/embed/mhMuZ6DNVq0"
                          elif group==2:
                            temp = ["https://www.youtube.com/embed/CnUnU-EhOsQ","https://www.youtube.com/embed/QDwvOZ5XOHg","https://www.youtube.com/embed/4p6D23Auudk"]
                            url=temp[random.randint(0,2)]
                          elif group==3:
                            url="https://www.youtube.com/embed/kkIkD8bsT9c"
                          elif group==4:
                            url="https://www.youtube.com/embed/WrBe4-BUMnY"
                          elif group==5:
                            url="https://www.youtube.com/embed/DTP6pO9B_3E"
                        else:
                          if group==0:
                            url="https://www.youtube.com/embed/UojsFeHfij0"
                          elif group==1:
                            url="https://www.youtube.com/embed/mhMuZ6DNVq0"
                          elif group==2:
                            temp = ["https://www.youtube.com/embed/7hyBfuEbdn8","https://www.youtube.com/embed/2QlGz7PMP10","https://www.youtube.com/embed/44PkE78Gd4A"]
                            url=temp[random.randint(0,2)]
                          elif group==3:
                            url="https://www.youtube.com/embed/kkIkD8bsT9c"
                          elif group==4:
                            url="https://www.youtube.com/embed/WrBe4-BUMnY"
                          elif group==5:
                            url="https://www.youtube.com/embed/DTP6pO9B_3E"
                        Func = open("link.txt","w")
                        Func.write(url)
                        Func.close()

                        cv2.putText(frame, genderName(gender)+ageGroup(group), (x, y-20),
                        4, font_scale, (0, 255, 0))
                        i=i+1
                   
                
            try:
                ret, buffer = cv2.imencode('.jpeg', frame)
                frame = buffer.tobytes()
                yield (b'--frame\r\n'
                       b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
            except Exception as e:
                pass
                
        else:
            pass

def ageGroup(age):
  if age==0:
    return " 1-4 "
  elif age==1:
    return " 5-15"
  elif age==2:
    return " 16-30 "
  elif age==3:
    return " 31-45 "
  elif age==4:
    return " 46-60 "
  elif age==5:
    return " 61-116 "
    
@app.route("/getfile", methods=["GET", "POST"])
def getfile():
  fs=open("link.txt", 'r')
  content=fs.readline()
  fs.close()
  jsonResp = {'content': content}

    
  return jsonify(jsonResp)


def genderName(num):
    if num==0:
        return 'Male'
    else:
        return 'Female'


@app.route('/')
def index():
    return render_template('index.html')

    
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')



if __name__ == '__main__':
    app.run()
    
camera.release()
cv2.destroyAllWindows()     
