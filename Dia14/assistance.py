import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# create database
route = 'Employees'
my_images = []
employees_names = []
employees_list = os.listdir(route)

for name in employees_list:
    actual_image = cv2.imread(f'{route}\\{name}')
    my_images.append(actual_image)
    employees_names.append(os.path.splitext(name)[0])


# codify images
def codify(images):

    # create new images list
    codified_list = []

    # pass all images to rgb
    for image in images:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # codify
        codified = fr.face_encodings(image)[0]

        # append to list
        codified_list.append(codified)

    # return codified list
    return codified_list


# register check-ins
def register(person):
    f = open('register.csv', 'r+')
    data_list = f.readlines()
    register_names = []
    for lane in data_list:
        entry = lane.split(',')
        register_names.append(entry[0])

    if person not in register_names:
        now = datetime.now()
        string_now = now.strftime('%H:%M:%S')
        f.writelines(f'\n{person}, {string_now}')


codified_employees_list = codify(my_images)

# take a picture from webcam
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# reed image from webcam
exito, image = capture.read()

if not exito:
    print("Unable to capture photo")
else:
    # recognize face in capture
    face_captured = fr.face_locations(image)

    # codified face captured
    face_catpure_codified = fr.face_encodings(image, face_captured)

    # search coincidences
    for facecodif, faceubic in zip(face_catpure_codified, face_captured):
        coincidences = fr.compare_faces(codified_employees_list, facecodif)
        distances = fr.face_distance(codified_employees_list, facecodif)

        coincidence_index = numpy.argmin(distances)

        # show coincidences if there are
        if distances[coincidence_index] > 0.5:
            print("No coincidence")
        else:
            # search employee name found
            name = employees_names[coincidence_index]

            y1, x2, y2, x1 = faceubic
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(image, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(image, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 255, 255), 2)

            register(name)

            # show image gotten
            cv2.imshow('Image Web', image)

            # keep window open
            cv2.waitKey(0)
