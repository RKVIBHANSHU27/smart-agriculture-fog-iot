from fastapi import APIRouter
from backend.database import table

router = APIRouter()

@router.get("/telemetry")
def get_telemetry():
    response = table.scan()

    items = response.get("Items", [])

    items = sorted(
        items,
        key=lambda x: x["processed_at"],
        reverse=True
    )

    return items
    
@router.get("/latest")
def get_latest():

    response = table.scan()
    items = response.get("Items", [])

    items = sorted(
        items,
        key=lambda x: x["processed_at"],
        reverse=True
    )

    latest = {}
    results = []

    for item in items:

        key = (item["device_id"], item["sensor_type"])

        if key not in latest:
            latest[key] = True
            results.append(item)

    return results
    
@router.get("/dashboard")
def get_dashboard():

    response = table.scan()
    items = response.get("Items", [])

    items = sorted(
        items,
        key=lambda x: x["processed_at"],
        reverse=True
    )

    latest = {}

    for item in items:

        key = (item["device_id"], item["sensor_type"])

        if key not in latest:
            latest[key] = item

    latest_items = list(latest.values())

    normal = 0
    warning = 0
    critical = 0

    for item in latest_items:

        if item["alert"] == "NORMAL":
            normal += 1

        elif item["alert"] == "WARNING":
            warning += 1

        elif item["alert"] == "CRITICAL":
            critical += 1

    return {
        "total_devices": len(set(item["device_id"] for item in latest_items)),
        "total_sensor_types": len(set(item["sensor_type"] for item in latest_items)),
        "total_latest_readings": len(latest_items),

        "alerts": {
            "NORMAL": normal,
            "WARNING": warning,
            "CRITICAL": critical
        },

        "last_update": latest_items[0]["processed_at"] if latest_items else None
    }    
    
    
    @router.get("/alerts")
def get_alerts():

    response = table.scan()
    items = response.get("Items", [])

    items = sorted(
        items,
        key=lambda x: x["processed_at"],
        reverse=True
    )

    latest = {}

    for item in items:

        key = (item["device_id"], item["sensor_type"])

        if key not in latest:
            latest[key] = item

    alerts = [
        item
        for item in latest.values()
        if item["alert"] != "NORMAL"
    ]

    return alerts
    
    
    @router.get("/devices")
def get_devices():

    response = table.scan()
    items = response.get("Items", [])

    items = sorted(
        items,
        key=lambda x: x["processed_at"],
        reverse=True
    )

    latest = {}

    for item in items:

        key = (item["device_id"], item["sensor_type"])

        if key not in latest:
            latest[key] = item

    devices = {}

    for item in latest.values():

        device = item["device_id"]

        if device not in devices:
            devices[device] = []

        devices[device].append(item)

    return devices