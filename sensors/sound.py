__author__ = 'tingxxu'

from DevIoTGateway.sensor import *
from DevIoTGatewayPi.config import config
from DevIoTGatewayPi.sensorlogic import SensorLogic
from logic.grovepioperator import GrovePiOperator


sound = Sensor('sound', 'sound_1', 'RSound')

value_property = SProperty('volume', 0, [0, 100], 0)

sound.add_property(value_property)


class SoundLogic(SensorLogic):

    @staticmethod
    def update(sensor, data):
        pin = config['sensors'][sensor.id]['pin']
        new_value = GrovePiOperator.read(pin)
        if new_value is not None:
            updated_properties = {'volume': new_value}
        else:
            updated_properties = {}
        SensorLogic.update_properties(sensor, updated_properties)
