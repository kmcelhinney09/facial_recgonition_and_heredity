from picamera import PiCamera
from PIL import Image
from time import sleep
import os
from itertools import cycle

def picture_encoding(user_id):
    student_id = user_id
    os.chdir('/home/pi/attendancesystem/Attendance_Pictures')
    #cwd = os.getcwd()
    #dataset = os.path.join(cwd,"dataset")

    try:
        cwd = os.getcwd()
        dataset = os.path.join(cwd,"dataset")
        if os.path.isdir(os.path.join(dataset,student_id)):
            photopath = os.path.join(dataset,student_id)
            print("User Folder exists....")
            pass
        else:
            photopath = os.path.join(dataset,student_id)
            print("User Folder made")
            os.makedirs(photopath)
    except:
        print("There was an error making/finding Dir")

    # create object for PiCamera class
    #camera = PiCamera()
    #set resolution
    camera.resolution = (1024, 768)

    numbers = ['1.png','2.png','3.png']
    numbers_overlay = cycle(numbers)

    take = input("Are you ready to take the picture (y,n): ")

    def padding(resolution, width=32, height=16):
       return (
            ((resolution[0] + (width - 1)) // width) * width,
            ((resolution[1] + (height - 1)) // height) * height,
        )

    if take.lower()== 'y':

        for x in range(0,7):
            camera.start_preview()
            for y in range (3):
                overlay = next(numbers_overlay)
                image_file = os.path.join('/home/pi/overlay_test',overlay)
                img = Image.open(image_file)
                pad = Image.new('RGB', padding(camera.resolution))
            # Paste the original image into the padded one
                pad.paste(img, (300, 100))

                camera.add_overlay(pad.tobytes(), alpha=100, layer=3)
                sleep(1)
                for o in camera.overlays:
                    camera.remove_overlay(o)

            #store imagecallable
            #camera.start_preview(fullscreen=False, window = (100, 20, 640, 480))
            img2 = Image.open('/home/pi/overlay_test/picture.png')
            pad = Image.new('RGB', padding(camera.resolution))
            # Paste the original image into the padded one
            pad.paste(img2, (300, 100))

            camera.add_overlay(pad.tobytes(), alpha=100, layer=3)

            camera.capture(os.path.join(photopath,'{!s}.jpeg'.format(x)))
            sleep(2)
            for o in camera.overlays:
                camera.remove_overlay(o)
            camera.stop_preview()
    else:
        quit()