from DevIoTGateway.sensor import *
from DevIoTGateway.config import config
from DevIoTGatewayPi.sensorlogic import SensorLogic
from picamera import PiCamera
import threading
import time

path = None
if "camera_images" in config:
    path = config["camera_images"]
else:
    import os
    current_folder = os.getcwd()
    path = current_folder + "/camera_images"

camera = Sensor('camera', 'camera_r', 'RCamera')

value_property = SProperty('CapturePath', 1, None, path)

camera.add_property(value_property)

on_action = SAction('start')
off_action = SAction('stop')

camera.add_action(on_action)
camera.add_action(off_action)


class CameraLogic(SensorLogic):
    camera_obj = None
    t = None

    busy = False
    index = 0

    @staticmethod
    def action(sensor, action):
        if action.name == 'start':
            CameraLogic.start()
        elif action.name == 'stop':
            CameraLogic.index = 0
        else:
            pass

    @staticmethod
    def start():
        if CameraLogic.index <= 0:
            CameraLogic.index += 5
            CameraLogic.t = threading.Thread(target=CameraLogic.capture)
            CameraLogic.t.daemon = True
            CameraLogic.t.start()

    @staticmethod
    def capture():
        if CameraLogic.camera_obj is not None:
            CameraLogic.camera_obj.start_preview()
            while CameraLogic.index > 0:
                CameraLogic.camera_obj.capture(path)
                time.sleep(2.5)
                CameraLogic.index -= 1
            CameraLogic.camera_obj.stop_preview()

try:
    CameraLogic.camera_obj = PiCamera()
except Exception as ex:
    print(ex.message)
    CameraLogic.camera_obj = None
