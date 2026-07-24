import random

from sensors.base_sensor import BaseSensor


class TemperatureSensor(BaseSensor):
    """
    Simulates an agriculture temperature sensor.
    """

    def __init__(
        self,
        sensor_id="TEMP001",
        generation_interval=2,
        dispatch_interval=5
    ):
        super().__init__(
            sensor_id=sensor_id,
            sensor_type="temperature",
            unit="°C",
            generation_interval=generation_interval,
            dispatch_interval=dispatch_interval
        )

    def generate_value(self):
        """
        Generate a realistic agriculture temperature.
        """
        return random.uniform(18.0, 35.0)