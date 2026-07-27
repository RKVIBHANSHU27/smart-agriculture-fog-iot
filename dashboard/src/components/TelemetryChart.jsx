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
.reduce((acc,item)=>{

const existing = acc.find(
 x => x.device === item.device_id
);


if(!existing){

acc.push({
 device:item.device_id,
 value:Number(item.average.toFixed(2))
});

}


return acc;

},[]);



return (

<div className="card chart-card">

<h2>
{sensor.replace("_"," ").toUpperCase()}
</h2>


<ResponsiveContainer
width="100%"
height={300}
>

<LineChart data={chartData}>

<CartesianGrid />

<XAxis
dataKey="device"
/>


<YAxis />


<Tooltip />


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