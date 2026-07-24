from abc import ABC, abstractmethod
from datetime import datetime, timezone
import uuid


class BaseSensor(ABC):
    """
    Abstract base class for all agriculture sensors.
    """

    def __init__(
        self,
        sensor_id: str,
        sensor_type: str,
        unit: str,
        generation_interval: int = 2,
        dispatch_interval: int = 5
    ):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.unit = unit
        self.generation_interval = generation_interval
        self.dispatch_interval = dispatch_interval

    @abstractmethod
    def generate_value(self):
        """
        Generated a sensor reading.
        Must be implemented by child classes.
        """
        pass

    def generate_payload(self):
        """
        Created a standardized sensor payload.
        """

        return {
            "message_id": str(uuid.uuid4()),

            "sensor_id": self.sensor_id,

            "sensor_type": self.sensor_type,

            "value": round(self.generate_value(), 2),

            "unit": self.unit,

            "generation_interval": self.generation_interval,

            "dispatch_interval": self.dispatch_interval,

            "sensor_generated_at": datetime.now(
                timezone.utc
            ).isoformat()
        }