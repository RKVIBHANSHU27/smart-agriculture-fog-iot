import random

from sensors.base_sensor import BaseSensor


class HumiditySensor(BaseSensor):
    """
    Simulates an agriculture humidity sensor.
    """

    def __init__(
        self,
        sensor_id,
        generation_interval=2,
        dispatch_interval=5
    ):
        super().__init__(
            sensor_id=sensor_id,
            sensor_type="humidity",
            unit="%",
            generation_interval=generation_interval,
            dispatch_interval=dispatch_interval
        )

    def generate_value(self):
        return random.uniform(30.0, 90.0)