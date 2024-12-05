import cv2
import face_recognition as fr

# charge images
photo_control = fr.load_image_file('Employees/Dante.jpg')
test_photo = fr.load_image_file('FotoB.jpg')

# MAKE IMAGES TO RGB
photo_control = cv2.cvtColor(photo_control, cv2.COLOR_BGR2RGB)
test_photo = cv2.cvtColor(test_photo, cv2.COLOR_BGR2RGB)

# localize control face
place_face_A = fr.face_locations(photo_control)[0]
codified_face_A = fr.face_encodings(photo_control)[0]

# localize test face
place_face_B = fr.face_locations(test_photo)[0]
codified_face_B = fr.face_encodings(test_photo)[0]

# show faces rectangles
cv2.rectangle(photo_control,
              (place_face_A[3], place_face_A[0]),
              (place_face_A[1], place_face_A[2]),
              (0, 255, 0),
              2)

cv2.rectangle(test_photo,
              (place_face_B[3], place_face_B[0]),
              (place_face_B[1], place_face_B[2]),
              (0, 255, 0),
              2)

# compare images
result = fr.compare_faces([codified_face_A], codified_face_B)

# distance data
distance = fr.face_distance([codified_face_A], codified_face_B)

# show result
cv2.putText(photo_control,
            f'{result} {distance.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0, 255, 0))

# show images
cv2.imshow('Photo Control', photo_control)
cv2.imshow('Test Photo', test_photo)

# distance data
distance = fr.face_distance([codified_face_A], codified_face_B)

# keep open sotfware
cv2.waitKey(0)


