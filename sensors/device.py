from sensors.temperature import TemperatureSensor
from sensors.humidity import HumiditySensor
from sensors.soil_moisture import SoilMoistureSensor
from sensors.light import LightSensor
from sensors.co2 import CO2Sensor


class Device:

    def __init__(self, device_id):

        self.device_id = device_id

        self.sensors = [
            TemperatureSensor(f"TEMP{device_id:02}"),
            HumiditySensor(f"HUM{device_id:02}"),
            SoilMoistureSensor(f"SOIL{device_id:02}"),
            LightSensor(f"LIGHT{device_id:02}"),
            CO2Sensor(f"CO2{device_id:02}")
        ]

    def generate_readings(self):

        readings = []

        for sensor in self.sensors:

            payload = sensor.generate_payload()

            payload["device_id"] = f"DEVICE{self.device_id:03}"

            readings.append(payload)

        return readings