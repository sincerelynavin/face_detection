#Import opencv and json modules
import cv2
import json

#Load the cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Variable needed for path
test_data_path = 'testData' 

#Load JSON file
with open(f'./{test_data_path}/groundTruth.json') as configfile:
    test_configs = json.load(configfile)

#Variables needed to calculate accuracy%
total_images = len(test_configs)
accurate_face_count = 0

#Loop to iterate through all testData
for test_config in test_configs:

    img = cv2.imread(f"./{test_data_path}/{test_config['fileName']}")  #Fixing the access to the fileName
    print('\nTest Photo Name:', test_config['fileName'])  #Print name of the photo thats being examined
    print('Number of faces given:',test_config['faces'])  #Print number of faces of that photo pre-determined inside groundTruth.json
    

    #Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    #Print the number of faces detected from the program
    facesAmount = len(faces)
    print('Number of faces detected:',facesAmount)

    #Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    #Display the output and wait for keypress
    cv2.imshow('showcase', img)
    cv2.waitKey(0)
    
    #Alternatively to quickly determine the statistics of the program you can comment out waitKey(0) and implement destroyAllWindows() to quickly get the output numbers
    #cv2.destroyAllWindows() 

    #Check if faces are accurately detected
    if facesAmount == test_config['faces']:
        accurate_face_count += 1  #To calculate accuracy%
        print("Number of faces detected is accurate")
    else:
        print("Number of faces detected is inaccurate")

#Total Accuracy%
overall_accuracy = (accurate_face_count / total_images) * 100
print(f"\nOverall Accuracy: {overall_accuracy:.2f}%")

