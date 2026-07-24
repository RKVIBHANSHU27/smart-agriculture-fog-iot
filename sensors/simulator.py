import time

from config.config import TOTAL_DEVICES, GENERATION_INTERVAL
from sensors.device import Device
from fog.fog_node import FogNode


class SensorSimulator:
  
    def __init__(self):
        self.devices = [
            Device(device_id)
            for device_id in range(1, TOTAL_DEVICES + 1)
        ]
        self.fog_node = FogNode()

    def start(self):

        print("=" * 70)
        print(f"Starting Smart Agriculture Sensor Simulator")
        print(f"Devices              : {TOTAL_DEVICES}")
        print(f"Sensors per Device   : 5")
        print(f"Generation Interval  : {GENERATION_INTERVAL} sec")
        print("=" * 70)

        try:

            while True:

                print("\nGenerating Sensor Readings...\n")

                for device in self.devices:

                    readings = device.generate_readings()

                    for reading in readings:
                        self.fog_node.receive_reading(reading)

                print("\nWaiting for next cycle...\n")

                time.sleep(GENERATION_INTERVAL)

        except KeyboardInterrupt:
            print("\nSensor Simulator stopped.")


if __name__ == "__main__":
    simulator = SensorSimulator()
    simulator.start()