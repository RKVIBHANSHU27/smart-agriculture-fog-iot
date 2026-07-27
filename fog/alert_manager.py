class AlertManager:


    THRESHOLDS = {

        "temperature": {
            "warning": 30,
            "critical": 35
        },

        "humidity": {
            "warning_low": 35,
            "critical_low": 25
        },

        "soil_moisture": {
            "warning_low": 30,
            "critical_low": 20
        },

        "light": {
            "warning_low": 5000,
            "critical_low": 2000
        },

        "co2": {
            "warning": 1000,
            "critical": 1500
        },
    }


    @classmethod
    def check_alert(cls, sensor_type, average_value):

        if sensor_type not in cls.THRESHOLDS:
            return "NORMAL"


        limits = cls.THRESHOLDS[sensor_type]


        # HIGH values

        if "critical" in limits:
            if average_value >= limits["critical"]:
                return "CRITICAL"


        if "warning" in limits:
            if average_value >= limits["warning"]:
                return "WARNING"



        # LOW values

        if "critical_low" in limits:
            if average_value <= limits["critical_low"]:
                return "CRITICAL"


        if "warning_low" in limits:
            if average_value <= limits["warning_low"]:
                return "WARNING"



        return "NORMAL"