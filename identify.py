import face_recognition
from PIL import Image,ImageDraw

image_of_Disel= face_recognition.load_image_file('./img/known/Disel.jpg')

Disel_face_encoding = face_recognition.face_encodings(image_of_Disel)[0]

image_of_Johnson = face_recognition.load_image_file('./img/known/Dwayne_Johnson.jpg')

Johnson_face_encoding = face_recognition.face_encodings(image_of_Johnson)[0]

#We want two arrays: one is for storing idex, one is for storing names
known_people_encoding = [
    Disel_face_encoding,
    Johnson_face_encoding
]

known_people_name = [
    "Disel",
    "Johnson"
]
#load test img to find faces

given_img = face_recognition.load_image_file('./img/grp/ff1.jpg')


#Find all faces in the given_img first
face_locations = face_recognition.face_locations(given_img)
face_encodings = face_recognition.face_encodings(given_img,face_locations)

#Convert to PIL format
pil_img = Image.fromarray(given_img)

#Draw the img
draw = ImageDraw.Draw(pil_img)

#loop through
#The hardest part
for(top,right,bottom,left),face_encodings in zip(face_locations,face_encodings):
    matches = face_recognition.compare_faces(known_people_encoding,face_encodings)
    
    name = "Unknown"

    #if Matches
    if True in matches:
        first_match_index = matches.index(True)
        name = known_people_name[first_match_index]
    
    #Draw the box
    draw.rectangle(((left,top),(right,bottom)),outline=(0,0,0))
    #Show the name
    test_width,text_height = draw.textsize(name)
    draw.rectangle(((left,bottom- text_height-6),(right,bottom)),fill=(0,0,0),outline=(0,0,0))
    draw.text((left +6,bottom - text_height -5),name,fill=(255,255,255,255))
del draw

#Display the img with PIL
pil_img.show()