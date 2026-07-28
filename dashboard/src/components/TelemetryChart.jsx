import {
 LineChart,
 Line,
 XAxis,
 YAxis,
 Tooltip,
 CartesianGrid,
 ResponsiveContainer
} from "recharts";


function TelemetryChart({data, sensor}){


const chartData = data
.filter(
    item => item.sensor_type === sensor
)
.map(item => ({

    time: new Date(
        item.processed_at
    ).toLocaleTimeString(
        "en-IE",
        {
            hour:"2-digit",
            minute:"2-digit",
            second:"2-digit"
        }
    ),

    value:Number(
        item.average
    ),

    device:item.device_id,

    unit:item.unit

}));



return (

<div className="card chart-card">


<h2>

{
sensor === "temperature"
?
"Temperature (°C)"
:
sensor === "humidity"
?
"Humidity (%)"
:
sensor === "soil_moisture"
?
"Soil Moisture (%)"
:
sensor === "co2"
?
"CO₂ (ppm)"
:
"Light (lux)"
}

</h2>



<ResponsiveContainer
 width="100%"
 height={220}
>


<LineChart data={chartData}>


<CartesianGrid />


<XAxis
dataKey="time"
/>


<YAxis />


<Tooltip
formatter={
(value)=>
[
 value,
 sensor === "temperature"
 ? "°C"
 :
 sensor === "humidity"
 ? "%"
 :
 sensor === "soil_moisture"
 ? "%"
 :
 sensor === "co2"
 ? "ppm"
 :
 "lux"
]
}
/>



<Line
type="monotone"
dataKey="value"
strokeWidth={3}
/>


</LineChart>


</ResponsiveContainer>


</div>

);

}

export default TelemetryChart;