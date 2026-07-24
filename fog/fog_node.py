from collections import defaultdict

from config.config import READINGS_PER_BATCH
from fog.validator import DataValidator
from fog.aggregator import DataAggregator
from fog.alert_manager import AlertManager
from aws.sqs.dispatcher import SQSDispatcher


class FogNode:

    def __init__(self):

        # Buffer readings by (device_id, sensor_type)
        self.buffer = defaultdict(list)

         # SQS dispatcher
        self.dispatcher = SQSDispatcher()

    def receive_reading(self, reading):

        # Step 1: Validate
        if not DataValidator.validate(reading):
            print(f"Invalid reading discarded: {reading}")
            return

        key = (
            reading["device_id"],
            reading["sensor_type"]
        )

        # Step 2: Store reading
        self.buffer[key].append(reading)

        # Step 3: Wait until enough readings arrive
        if len(self.buffer[key]) < READINGS_PER_BATCH:
            return

        readings = self.buffer[key]

        # Step 4: Aggregate
        statistics = DataAggregator.aggregate(readings)

        # Step 5: Check alerts
        alert = AlertManager.check_alert(
            reading["sensor_type"],
            statistics["average"]
        )

        # Step 6: Create processed record
        processed_data = {
            "device_id": reading["device_id"],
            "sensor_type": reading["sensor_type"],
            "reading_count": statistics["reading_count"],
            "minimum": statistics["minimum"],
            "maximum": statistics["maximum"],
            "average": statistics["average"],
            "alert": alert,
            "processed_at": reading["sensor_generated_at"]
        }

        print("\n========== FOG PROCESSED ==========")
        print(processed_data)
        print("===================================\n")

        self.dispatcher.send(processed_data)    

        
        self.buffer[key].clear()