import face_recognition
image = face_recognition.load_image_file('./img/grp/ff2.jpg')
face_locations = face_recognition.face_locations(image)



#First to indicate how many ppl showing up in the given photo

num_ppl = len(face_locations)
sentence = 'There are {} people in the given photo'.format(num_ppl)
print(sentence)



