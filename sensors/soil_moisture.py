import random

from sensors.base_sensor import BaseSensor


class SoilMoistureSensor(BaseSensor):
    """
    Simulates a soil moisture sensor.
    """

    def __init__(
        self,
        sensor_id,
        generation_interval=2,
        dispatch_interval=5
    ):
        super().__init__(
            sensor_id=sensor_id,
            sensor_type="soil_moisture",
            unit="%",
            generation_interval=generation_interval,
            dispatch_interval=dispatch_interval
        )

    def generate_value(self):
        return random.uniform(20.0, 80.0)