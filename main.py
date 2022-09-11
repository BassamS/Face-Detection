import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img = cv2.imread('test.jpg')

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(grey, 1.1, 4)

# drawing rectangle around the face
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y) + (x + w, y + h), (255, 0, 0), 2)
