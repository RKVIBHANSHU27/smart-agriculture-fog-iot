import random

from sensors.base_sensor import BaseSensor


class CO2Sensor(BaseSensor):
    """
    Simulates a CO₂ sensor.
    """

    def __init__(
        self,
        sensor_id,
        generation_interval=2,
        dispatch_interval=5
    ):
        super().__init__(
            sensor_id=sensor_id,
            sensor_type="co2",
            unit="ppm",
            generation_interval=generation_interval,
            dispatch_interval=dispatch_interval
        )

    def generate_value(self):
        return random.uniform(350.0, 2000.0)