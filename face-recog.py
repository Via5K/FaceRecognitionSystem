import cv2
import numpy as np
import face_recognition as fr
import os
from datetime import datetime


#Process
#1. Getting images
#2. Finding the faces, their Locations
#3. Then encode the imageElon
#4. Display the detected face using a rectangle color
#5. Comparing the faces! To the database



def markAttendance(name):
    with open('Attendance.csv', 'r', encoding='utf8') as f:
        myDataList = f.readlines()
        nameList = []
        #print(myDataList)
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList: #if not then add.
            now = datetime.now()
            dateString = now.strftime('%d:%m:%y')
            final.append(f'{name},{dateString}') #appending name as well as date, so that at one day only one time attendance is taken.
        f.close()            

#Encoding Function.
def findImageEncodings(images):
    encodeList = []
    for image in images:
        #convert to rgb
        image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
        encode = fr.face_encodings(image)[0]
        encodeList.append(encode) #encodeList contains encoded for all images.
    return encodeList


folderPath = 'sample images' #folder name
images = [] #contains the images
names = [] #contains the name fo each image that is in the folder 
myList = os.listdir(folderPath) #stores all the names of the images in this list


#Concludes the naming.
for name in myList:
    currentImag = cv2.imread(f'{folderPath}/{name}')
    images.append(currentImag)
    names.append(os.path.splitext(name)[0])

final  = []

encodeListKnown = findImageEncodings(images)
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    success,img = cap.read()
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)
    facesCurrentFrame = fr.face_locations(imgS)
    encodesCurrentFrame = fr.face_encodings(imgS,facesCurrentFrame)
    #finding the matches

    attendancePresent = [] #to display how many students are present

    for encodeFace,faceLocation in zip(encodesCurrentFrame,facesCurrentFrame):
        
        matches = fr.compare_faces(encodeListKnown,encodeFace)
        faceDistance = fr.face_distance(encodeListKnown,encodeFace)
        matchIndex = np.argmin(faceDistance)
        
        if matches[matchIndex]:
            name = names[matchIndex].upper()
            print(name) #displaying name so that one can see their attendance has been marked correctly.
            y1,x2,y2,x1 = faceLocation
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,255),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,255),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markAttendance(name)
            set(final) #this removes duplicate entries
            
            #opeing the file again to write the entries
            with open('attendance.csv', 'w', encoding ='utf8') as f:
                for i in range(0, len(final)):
                    #print(final[i])
                    f.writelines(f'\n{final[i]}')
                    #attendancePresent.append(final[i]) #stores the result of present students to display in terminal
                f.close()
                
    cv2.imshow('Recognise Face',img)
    cv2.waitKey(1)