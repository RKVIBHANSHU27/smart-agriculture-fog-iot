function TelemetryTable({data}){


return(

<div className="card">

<h2>
Latest Telemetry
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

<td>{item.device_id}</td>

<td>{item.sensor_type}</td>

<td>
{item.average}
{item.unit}
</td>

<td>
{item.minimum}
</td>

<td>
{item.maximum}
</td>

<td>
🟢 {item.alert}
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