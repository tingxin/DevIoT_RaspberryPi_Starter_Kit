__author__ = 'tingxxu'

from DevIoTGateway.sensor import *
from DevIoTGateway.config import config
from DevIoTGatewayPi.sensorlogic import SensorLogic
from logic.grovepioperator import GrovePiOperator


button = Sensor('button', 'button_r', 'RButton')

value_property = SProperty('pressed', 0, None, 0)

button.add_property(value_property)


class ButtonLogic(SensorLogic):

    @staticmethod
    def update(sensor, data):
        pin = config['sensors'][sensor.id]['pin']

        new_value = GrovePiOperator.read(pin)

        if 0 < new_value:
            updated_properties = {'pressed': 1}
        else:
            updated_properties = {'pressed': 0}
        sensor.update_properties(updated_properties)
