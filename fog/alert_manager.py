class AlertManager:
   

    THRESHOLDS = {
        "temperature": {"high": 30},
        "humidity": {"low": 35},
        "soil_moisture": {"low": 30},
        "light": {"low": 5000},
        "co2": {"high": 1500},
    }

    @classmethod
    def check_alert(cls, sensor_type, average_value):

        if sensor_type not in cls.THRESHOLDS:
            return None

        limits = cls.THRESHOLDS[sensor_type]

        if "high" in limits and average_value > limits["high"]:
            return f"HIGH_{sensor_type.upper()}"

        if "low" in limits and average_value < limits["low"]:
            return f"LOW_{sensor_type.upper()}"

        return None