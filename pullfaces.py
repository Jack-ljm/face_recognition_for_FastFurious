from PIL import Image
import face_recognition
#load the photo that we want to pull indivisuals from
image = face_recognition.load_image_file('./img/grp/ff1.jpg')
face_locations = face_recognition.face_locations(image)

#interation through all locations that each made by four components
for face_location in face_locations:
    top,right,bottom,left = face_location #There are four components associating 
                                          #with one person

    face_image = image[top:bottom,left:right]
    #applying PIL library to get the visual img
    pil_image = Image.fromarray(face_image)
    #Do format to loop through, want two points to identify the img
    pil_image.save('{},{}.jpg'.format(top,right))
