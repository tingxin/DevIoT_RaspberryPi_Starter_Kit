__author__ = 'tingxxu'

from DevIoTGateway.sensor import *
from DevIoTGateway.config import config
from DevIoTGatewayPi.sensorlogic import SensorLogic
from logic.grovepioperator import GrovePiOperator


light = Sensor("light", "light_1", "RLight")

value_property = SProperty("level", 0, [0, 100], 0)

light.add_property(value_property)


class LightLogic(SensorLogic):

    @staticmethod
    def update(sensor, data):
        pin = config["sensors"][sensor.id]['pin']
        new_value = GrovePiOperator.read(pin)
        if new_value is not None:
            updated_properties = {"level": new_value}
            sensor.update_properties(updated_properties)