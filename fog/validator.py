class DataValidator:
    

    VALID_RANGES = {
        "temperature": (-20, 60),
        "humidity": (0, 100),
        "soil_moisture": (0, 100),
        "light": (0, 120000),
        "co2": (0, 5000),
    }

    @classmethod
    def validate(cls, reading):

        sensor_type = reading["sensor_type"]
        value = reading["value"]

        if sensor_type not in cls.VALID_RANGES:
            return False

        minimum, maximum = cls.VALID_RANGES[sensor_type]

        return minimum <= value <= maximum