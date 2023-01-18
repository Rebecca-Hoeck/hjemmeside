from sense_hat import SenseHat
sense = SenseHat()
sense.clear

from orbit import ISS

from picamera import PiCamera
from time import sleep

import datetime
from pathlib import Path
from time import sleep

start_time = datetime.datetime.now()
now_time = datetime.datetime.now()
duration = datetime.timedelta(seconds=20)
print(start_time)

location = ISS.coordinates() # Equivalent to ISS.at(timescale.now()).subpoint()
print(location)

print(f"breddegrader: {location.latitude.degrees}")
print(f"længdegrader: {location.longitude.degrees}")

i=0
m=0


while now_time < start_time + duration:
    
    if location.latitude.degrees < 0 and location.latitude.degrees > -60 and location.longitude.degrees < 0 and location.longitude.degrees > -60:
        print('hav')
    
        with PiCamera() as camera:
            sleep(5)
            camera.capture('hav%d.jpg'%i)

        i+=1
        print("har taget billed af vand %s" %(i))
        print(f"breddegrader: {location.latitude.degrees}")
        print(f"længdegrader: {location.longitude.degrees}")

    
    if location.latitude.degrees > -15 and location.latitude.degrees < 40 and location.longitude.degrees > 5 and location.longitude.degrees < 35:
        print('jord')
        with PiCamera() as camera:
            sleep(5)
            camera.capture('jord%d.jpg'%m)
        m+=1
        print("har taget billed af jord %s" %(m))
        print(f"breddegrader: {location.latitude.degrees}")
        print(f"længdegrader: {location.longitude.degrees}")
    else:
        print('lokation ikke opfyldt')
    now_time= datetime.datetime.now()
            




