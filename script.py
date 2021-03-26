import cv2

# Pre-trained cascade classifier that I will be using
model = cv2.CascadeClassifier('car.xml')

def render_cars(frame):
      cars = model.detectMultiScale(frame,1.15,4)

      for (x,y,w,h) in cars:
            cv2.rectangle(frame, (x,y), (x+w,y+h), color=(0,255,0), thickness=2)
      return frame

def simulator():
      
      video = cv2.VideoCapture('cars.mp4')
      while video.isOpened():
            car, frame = video.read()
            await_key = cv2.waitKey(1)
            if car:
                  car_frame = render_cars(frame)
                  cv2.imshow('frame',car_frame)
            else:
                  break
            if await_key == ord('q'):
                  break
      video.release()
      cv2.destroyAllWindows()

if __name__ == "__main__":
      simulator()
