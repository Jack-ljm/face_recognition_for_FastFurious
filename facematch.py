import face_recognition
#Compare faces by there index
image_of_Ocanar = face_recognition.load_image_file('./img/known/Ocanar_RIP.jpg')

ocanar_face_encoding = face_recognition.face_encodings(image_of_Ocanar)[0]

unknwon_img= face_recognition.load_image_file('./img/unknown/Ocanar.jpg')

unknown_face_encoding = face_recognition.face_encodings(unknwon_img)[0]

# results will eigher be TRUE or FALSE
results = face_recognition.compare_faces([ocanar_face_encoding],unknown_face_encoding)


if results[0]:
    print('This is Ocanar')
else:
    print('This is not Ocanar')