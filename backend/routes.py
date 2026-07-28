from fastapi import APIRouter
from backend.database import table
from config.config import MAX_HISTORY


router = APIRouter()


def get_all_items():

    items = []

    response = table.scan()

    items.extend(
        response.get("Items", [])
    )


    while "LastEvaluatedKey" in response:

        response = table.scan(
            ExclusiveStartKey=response["LastEvaluatedKey"]
        )

        items.extend(
            response.get("Items", [])
        )


    return items



@router.get("/telemetry")
def get_telemetry():

    items = get_all_items()


    items = sorted(
        items,
        key=lambda x: x["processed_at"],
        reverse=True
    )


    return items[:MAX_HISTORY]



@router.get("/latest")
def latest():

    items = get_all_items()


    items = sorted(
        items,
        key=lambda x: x["processed_at"],
        reverse=True
    )


    return items[:25]



@router.get("/dashboard")
def get_dashboard():

    items = get_all_items()


    items = sorted(
        items,
        key=lambda x: x["processed_at"],
        reverse=True
    )


    latest = {}


    for item in items:

        key = (
            item["device_id"],
            item["sensor_type"]
        )


        if key not in latest:
            latest[key] = item



    latest_items = list(latest.values())


    all_devices = set(
        item["device_id"]
        for item in items
    )


    all_sensors = set(
        item["sensor_type"]
        for item in items
    )


    normal = 0
    warning = 0
    critical = 0


    for item in latest_items:

        alert = item["alert"]


        if alert == "NORMAL":
            normal += 1


        elif alert in [
            "WARNING",
            "HIGH_CO2",
            "HIGH_TEMPERATURE",
            "LOW_HUMIDITY",
            "LOW_SOIL_MOISTURE"
        ]:
            warning += 1


        elif alert in [
            "CRITICAL",
            "EMERGENCY"
        ]:
            critical += 1



    return {

        "total_devices": len(all_devices),


        "total_sensor_types": len(all_sensors),


        "total_latest_readings": len(latest_items),


        "alerts": {

            "NORMAL": normal,

            "WARNING": warning,

            "CRITICAL": critical

        },


        "last_update":
            latest_items[0]["processed_at"]
            if latest_items
            else None

    }





@router.get("/alerts")
def get_alerts():

    items = get_all_items()


    items = sorted(
        items,
        key=lambda x: x["processed_at"],
        reverse=True
    )


    alerts = [

        item

        for item in items

        if item["alert"] != "NORMAL"

    ]


    return alerts[:50]





@router.get("/devices")
def get_devices():

    items = get_all_items()


    items = sorted(
        items,
        key=lambda x: x["processed_at"],
        reverse=True
    )


    latest = {}


    for item in items:

        key = (
            item["device_id"],
            item["sensor_type"]
        )


        if key not in latest:

            latest[key] = item



    devices = {}


    for item in latest.values():

        device = item["device_id"]


        if device not in devices:

            devices[device] = []


        devices[device].append(item)



    return devices