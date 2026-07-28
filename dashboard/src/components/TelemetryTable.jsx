function TelemetryTable({data}){


return(

<div className="card">

<h2>
Latest Fog Processed Telemetry (25)
</h2>


<table>

<thead>

<tr>
<th>Device</th>
<th>Sensor</th>
<th>Average</th>
<th>Minimum</th>
<th>Maximum</th>
<th>Status</th>
</tr>

</thead>



<tbody>

{
data.map((item,index)=>(

<tr key={index}>


<td>
{item.device_id}
</td>


<td>

{
item.sensor_type === "soil_moisture"
?
"Soil Moisture"
:
item.sensor_type === "co2"
?
"CO₂"
:
item.sensor_type
}

</td>



<td>
{item.average} {item.unit}
</td>



<td>
{item.minimum}
</td>



<td>
{item.maximum}
</td>



<td>

<span

className={
 item.alert === "NORMAL"
 ?
 "status-normal"
 :
 item.alert === "WARNING"
 ?
 "status-warning"
 :
 "status-critical"
}

>

{
 item.alert === "NORMAL"
 ?
 "🟢 NORMAL"
 :
 item.alert === "WARNING"
 ?
 "🟡 WARNING"
 :
 "🔴 CRITICAL"
}

</span>


</td>


</tr>

))

}


</tbody>


</table>


</div>

)

}


export default TelemetryTable;