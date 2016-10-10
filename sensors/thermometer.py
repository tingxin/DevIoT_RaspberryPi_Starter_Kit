__author__ = 'davigar'

from DevIoTGateway.sensor import *
from DevIoTGateway.config import config
from DevIoTGatewayPi.sensorlogic import SensorLogic
from logic.grovepioperator import GrovePiOperator


thermometer = Sensor('thermometer', 'thermometer_1', 'RThermometer')

temperature_property = SProperty('temperature', 0, [0, 100], 0)
humidity_property = SProperty('humidity', 0, [0, 100], 0)

temperature_property.unit = "Celsius"

thermometer.add_property(temperature_property)
thermometer.add_property(humidity_property)

class ThermometerLogic(SensorLogic):

    @staticmethod
    def update(sensor, data):
        pin = config['sensors'][sensor.id]['pin']
        new_temp, new_hum = GrovePiOperator.read(pin, mode='dht')
        updated_properties = {'temperature': new_temp, 'humidity': new_hum}
        sensor.update_properties(updated_properties)
