import time
import picamera

def capture_pic(filename):
    with picamera.PiCamera() as camera:
        camera.start_preview()
        time.sleep(5)
        camera.capture(filename)
        camera.stop_preview

def capture_video(filename):
    with picamera.PiCamera() as camera:
        camera.start_preview()
        camera.start_recording(filename)
        time.sleep(10)
        camera.stop_recording()
        camera.stop_preview()

capture_video('/home/pi/video.h264')
