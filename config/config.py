"""
Application Configuration
"""

# Number of IoT Devices
TOTAL_DEVICES = 5

# Sensors available on every device
SENSOR_TYPES = [
    "temperature",
    "humidity",
    "soil_moisture",
    "light",
    "co2"
]

# Timing
GENERATION_INTERVAL = 2        # Seconds
READINGS_PER_BATCH = 5         # Fog processes after 5 readings

# AWS
AWS_REGION = "eu-west-1"

# Dashboard
MAX_HISTORY = 5