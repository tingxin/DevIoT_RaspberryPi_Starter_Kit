__author__ = 'tingxxu'

from DevIoTGateway.config import config
from DevIoTGatewayPi.pigateway import PiGateway

from logic.defaultsensorlogic import DefaultSensorLogic

if __name__ == '__main__':

    devIot_address = config.get_string("address", "10.140.92.22:9000")
    mqtt_address = config.get_string("mqtthost", "10.140.92.22:1883")
    app_name = config.get_string("appname", "raspberry")
    devIot_account = config.get_info("account", "")

    app = PiGateway(app_name, devIot_address, mqtt_address, devIot_account)
    app.default_sensor_logic = DefaultSensorLogic
    app.run()

