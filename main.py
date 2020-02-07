from picamera import PiCamera, Color
import datetime as dt
import time
import csv
import os
import ephem

#we are going to use a "start_time" variable to run our experiment for 3 hours 
start_time = dt.datetime.now()


def take_photo(name, path, sublat, sublong):
    camera.start_preview()
    camera.annotate_text = dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S") + "\n"+ sublat + sublong + "\n"+ str(name) #push text to the photo:time, sublat, sublong, photoname
    time.sleep(2)
    camera.capture(path + "/" + str(name) + ".jpg")
    camera.stop_preview()

"""The following piece of code is going to set the camera settings"""
camera = PiCamera()
camera.resolution = (2592, 1944)
camera.annotate_background = Color('black')
camera.annotate_foreground = Color('white')


dir_path = os.path.dirname(os.path.realpath(__file__))
data_file = dir_path + "/data.csv"

with open(data_file, "w") as f:
    writer = csv.writer(f)
    header = ("photo", "date / time", "location_sublat", "location_sublong")
    writer.writerow(header)

def find_iss():
    name = "ISS (ZARYA)"
    line1 = "1 25544U 98067A   20038.28263115  .00000317  00000-0  13894-4 0  9991"
    line2 = "2 25544  51.6444 276.1694 0005150 236.7373 230.7998 15.49143331211728"

    iss = ephem.readtle(name, line1, line2)

    iss.compute()

    return [iss.sublat, iss.sublong]



now_time = dt.datetime.now() # we are going to compare "now_time" with start_time. We can  
serial_number = 0            # the variable a is going to be the serial number of photos
    
# taking the photos
while (now_time < start_time + dt.timedelta(seconds = 10)):
    try:
        location = find_iss()
        
        take_photo(serial_number, dir_path, str(location[0]), str(location[1]))
        with open(data_file, "a") as f:
            writer = csv.writer(f)
            row = serial_number, dt.datetime.now().strftime("%d/%m/%Y %H:%M:%S"), str(location[0]), str(location[1])
            writer.writerow(row)
    except Exception as e:
        print(e)
    serial_number = serial_number + 1
    time.sleep(1)
    now_time = dt.datetime.now()
camera.stop_preview()