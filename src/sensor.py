import RPi.GPIO as GPIO
import time
import picamera
import datetime

def get_file_name():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H.%M.%S.h264")

SENSOR = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR, GPIO.IN, GPIO.PUD_DOWN)

previous_state = False
current_state = False

cam = picamera.PiCamera()
cam.led = False 
cam.resolution=(320,240)
cam.framerate = 12
# cam.annotate_background = piCamera.Color
while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(SENSOR)
    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        print ("GPIO pin %s is %s" % (SENSOR, new_state))
        if current_state:
            fileName = get_file_name()
            cam.start_preview()
            cam.start_recording(fileName)
            cam.annotate_text = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#        camera.wait_recording(0.2)
        else:
            cam.stop_recording()
            cam.stop_preview()
