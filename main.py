from picamera import PiCamera
import datetime as dt
import time
import csv
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

data_file = dir_path + "/data.csv"

with open(data_file, "w") as f:
    writer = csv.writer(f)
    header = ("photo", "date / time", "location")
    writer.writerow(header)

"""The following piece of code is going to set the camera settings"""
camera = PiCamera()
camera.resolution = (2592, 1944)


#taking the photos
for a in range(10): #the variable a is going to be the serial number of photos
    try:
        location = "fjdksfjsdlfd"
        filename = (dir_path + "/" + str(a) + "_" + dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S") +".jpg") #the variable filename is going to be the name of the following photo
        camera.annotate_text = str(a) + dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        camera.capture(filename)
        with open(data_file, "a") as f:
            writer = csv.writer(f)
            row = a, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), location
            writer.writerow(row)
    except Exception as e: #If this part fails, the code will not end.
        print(e)
    time.sleep(1)
