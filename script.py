import cv2

# Pre-trained cascade classifier that I will be using
model = cv2.CascadeClassifier('car.xml')

def render_cars(frame):
      cars = model.detectMultiScale(frame,1.15,4)

      for (x,y,w,h) in cars:
            cv2.rectangle(frame, (x,y), (x+w,y+h), color=(0,255,0), thickness=2)
      return frame
