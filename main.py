from picamera import PiCamera, Color
import datetime as dt
import time
import csv
import os
#import ephem

start_time = dt.datetime.now()

def take_photo(name, path, location):
    #filename = (str(a) + "_" + dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S") +".jpg") #the variable filename is going to be the name of the following photo
    camera.start_preview()
    camera.annotate_text = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n"+ location + "\n"+ str(name)
    time.sleep(2)
    camera.capture(path + "/" + str(name) + ".jpg")
    camera.stop_preview()

"""The following piece of code is going to set the camera settings"""
camera = PiCamera()
camera.resolution = (2592, 1944)
camera.annotate_background = Color('black')
camera.annotate_foreground = Color('white')



#def paths
dir_path = os.path.dirname(os.path.realpath(__file__))
data_file = dir_path + "/data.csv"

with open(data_file, "w") as f:
    writer = csv.writer(f)
    header = ("photo", "date / time", "location")
    writer.writerow(header)

"""def find_iss():
    

    name = "ISS (ZARYA)"
    line1 = "1 25544U 98067A   18032.92935684  .00002966  00000-0  52197-4 0  99911 25544U 98067A   18032.92935684  .00002966  00000-0  52197-4 0  9991"
    line2 = "2 25544  51.6438 332.9972 0003094  62.2964  46.0975 15.54039537 97480"

    iss = ephem.readtle(name, line1, line2)

    iss.compute()

    return (iss.sublat, iss.sublong)
"""

#taking the photos
now_time = dt.datetime.now()
serial_number = 0 #the variable a is going to be the serial number of photos
while (now_time < start_time + dt.timedelta(minutes = 10)):
    try:
        location = "fjdksfjsdlfd"
        
        take_photo(serial_number, dir_path, location)
        with open(data_file, "a") as f:
            writer = csv.writer(f)
            row = serial_number, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), location
            writer.writerow(row)
    except Exception as e: #If this part fails, the code will not end.
        print(e)
    serial_number = seria
    l_number + 1
    time.sleep(1)
    now_time = dt.datetime.now()
camera.stop_preview()