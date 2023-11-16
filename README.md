# Face Detection with OpenCV
## Dependencies
- Python 3.7
- opencv-python 4.8.1.78

## Approach

To establish a basic face detection system employing a pre-trained Haar Cascade classifier, the initial step involves the installation and configuration of OpenCV. For this, we used the pre-trained `haarcascade_frontalface_default` cascade file.

To create structure in the test data, a json file was written which contained both the filnames of the test data as well as how many faces there are in a given image. The json file is loaded into the python script and the inside a loop, the program runs the code responsible for facial detection for every image in the json file. This was done to streamline the testing process instead of having to load inividual images to test and check for facial recognition accuracy.

The facial detection code section reads an image provided and converts it to grayscale to be compatible with the openCV facial detection toolset. To display the faces detected by open cv, a rectangle is drawn around the approximate coordinates of each face. Finally to check the accuracy of the Haar Cascade classifier, a comparison between each photos' given number of faces and detected number of faces is calculated as a percentage. 

Initially this was tested with a single image. After the program was proven to be working, a dataset was created using multiple images with and without faces to evaluate the performance of the system.

## Limitations

There are false positives which affect accuracy percentage. Typically this is when an algorithm gives a positive detection of a face where there is no face. When using the metric of "number of faces detected" false positives have an outsized effect on the perceived accuracy as a false positive can lead to the number of faces that is detected is the same as the number of faces given, leading us to believe that it has detected all the faces if we are only using this metric. As a solution to this, the system can be changed where instead of detecting the number of faces, the `groundTruth` can have correctly identified bounding boxes for each face and the facial detection system will only consider detected faces whose bounding boxes intersect with the `groundTruth` bounding boxes. The intersected boxes will count as a positive and the other boxes are correctly flagged as false positives.
