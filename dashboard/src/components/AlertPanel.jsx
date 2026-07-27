function AlertPanel({alerts}){


return (

<div>

<h1>
🚨 Active Alerts
</h1>


{
alerts.length === 0 ?

<p>
No active alerts
</p>

:

alerts.map((alert,index)=>(


<div className="fog-card" key={index}>


<h2>
{
alert.alert === "CRITICAL"
?
"🔴 CRITICAL"
:
"🟡 WARNING"
}
</h2>


<p>
Device:
<strong>
{alert.device_id}
</strong>
</p>


<p>
Sensor:
{alert.sensor_type}
</p>


<p>
Average:
{alert.average} {alert.unit}
</p>


<p>
Time:
{alert.processed_at}
</p>


</div>


))

}


</div>

)

}


export default AlertPanel;