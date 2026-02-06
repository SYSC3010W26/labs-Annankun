# camera.py

from picamera2 import Picamera2
import time

def get_camera():
    """
    Returns camera instance
    """
    picam2 = Picamera2()
    config = picam2.create_still_configuration(main={"size": (640, 480)})
    picam2.configure(config)
    return picam2


def camera_preview(camera, preview_time):
    """
    Takes in camera instance and preview time
    Displays camera preview for the indicated amount of time
    """
    camera.start()
    time.sleep(preview_time)
    camera.stop()


def capture_image(camera, image_out_location, countdown_time=0, preview=False):
    """
    Takes in camera instance, output image location, countdown time and preview Boolean
    If preview is true, preview is started
    The code waits the indicated countdown time before the image is taken and stored in the indicated location
    The preview is stopped if it was started
    """
    if preview:
        camera.start()
    
    if countdown_time > 0:
        print(f"Countdown: {countdown_time} seconds...")
        for i in range(countdown_time, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        print("Capturing image!")
    
    if not preview:
        camera.start()
    
    camera.capture_file(image_out_location)
    camera.stop()


def capture_video(camera, video_out_location, video_length, countdown_time=0, preview=False):
    """
    Takes in camera instance, output video location, video length, countdown time and preview Boolean
    If preview is true, preview is started
    The code waits the indicated countdown time before the video is taken for the indicated amount of time 
    and stored in the indicated location
    The preview is stopped if it was started
    """
    if preview:
        camera.start_preview()
    
    if countdown_time > 0:
        print(f"Countdown: {countdown_time} seconds...")
        for i in range(countdown_time, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        print("Recording video!")
    
    camera.start_recording(video_out_location)
    time.sleep(video_length)
    camera.stop_recording()
    
    if preview:
        camera.stop_preview()