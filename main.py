from picamera import PiCamera
import datetime as dt
import time


"""The following piece of code is going to set the camera settings"""
camera = PiCamera()
camera.resolution = (2592, 1944)


#taking photos
for a in range(10): #the variable a is going to be a serial number of photos
    try:
        filename = (str(a) + "_" + dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S") +".jpg") #the variable filename is going to be name of the following photo
        camera.annotate_text = filename + dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        camera.capture(filename)
    except Exception as e: #If this part fails, the code will not end.
        print(e)
    time.sleep(1)
with open("log.txt", mode="w", encoding="utf-8") as file:
    print(text, file=file)
