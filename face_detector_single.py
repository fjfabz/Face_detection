import cv2

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread("me.jpg")
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
'''
cv2.imshow("gray_image",gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
faces = face_cascade.detectMultiScale(gray_image,scaleFactor=1.5,minNeighbors=5) #decrease the image by 5% in each consecutive search
#scaleFactor=1.5 50% script will run quicker but Less accurate
for x, y , w, h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,0,255), 5) #5 is the border (rectangle) width
print(type(faces))
print(faces) #[[155  83 382 382]] First point is 155 from left, 83 from top, 382 is width and height of the rectangle.

resize_img = cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("image",resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
