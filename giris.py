from multiprocessing.connection import wait
from time import sleep
from turtle import speed
import cv2
from simple_facerec import SimpleFacerec
from datetime import datetime
from datetime import date




def main():
    today = date.today()
    day = today.strftime("%b-%d-%Y")
    day_str = "Giriş " + day + ".txt"
    print(day_str)

    dosya = open(day_str, "a+")
    dosya.write("\n\n--------------------  Ad, Saat, Tarih  --------------------\n")
    dosya.close()

    print(day_str)

    #exitString = "Çıkış " + day + ".txt"
    #exitCSV = open(exitString, "a+")
    #exitCSV.write("\n\n--------------------  Ad, Saat, Tarih  --------------------\n")
    #exitCSV.close()

    enteredPerson = []
    leftPerson = []

    def yoklamayaYaz(name):
        #with open('yoklama.csv','a+') as f:
        with open(day_str, 'a+') as f:
            myDataList = f.readlines()
            nameList = []

            for line in myDataList:
                entry = line.split(',')
                nameList.append(entry[0])

        #  if (name in enteredPerson):
        #     writeToExit(name)





            if (name not in enteredPerson):
                now = datetime.now()
                dtString = now.strftime('  %H:%M:%S')
                adtString = now.strftime('  %D')
                if not (name == "Bilinmiyor"):
                    f.writelines(f'\n{name}{dtString}{adtString}')
                    enteredPerson.append(name)


    # def writeToExit(name):
    # if (name not in leftPerson):
        #     with open(exitString, 'a+') as f:
        #         now = datetime.now()
        #         dtString = now.strftime('  %H:%M:%S')
        #         adtString = now.strftime('  %D')
        #         f.writelines(f'\n{name}{dtString}{adtString}')
        #         leftPerson.append(name)




    # Encode faces from a folder
    sfr = SimpleFacerec()
    sfr.load_encoding_images("FaceID-Data/")

    # Load Camera
    cap = cv2.VideoCapture(0)


    while True:
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

            cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

            yoklamayaYaz(name)

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key == 27:
            break

    cap.release()
    cv2.destroyAllWindows()
