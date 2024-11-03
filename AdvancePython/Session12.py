import face_recognition
from PIL import image
import uuid


shajarian = face_recognition.load_image_file('./test.jpeg')
shajarian_encoding = face_recognition.face_encoding(shajarian)[0]

unknown_image = face_recognition.load_image_file('./test2.jpeg')
unknown_encoding = face_recognition.face_encoding(unknown_image)[0]

result = face_recognition.compare_faces([shajarian_encoding],unknown_encoding)
print(result)

###################################################################################

image = face_recognition.load_image_file('./test.jpeg')
face_location = face_recognition.face_locations(image)
#print(face_location)

for face in face_location:
    top,right,bottom,left = face
    face_image = image[top:bottom, left:right]
    show_img = image.fromarray(face_image)
    show_img.show()
    show_img.save('%s.jpg'%uuid.uuid1())


