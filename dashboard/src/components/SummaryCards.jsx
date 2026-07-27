function SummaryCards({data}) {

return (

<div style={{
display:"flex",
gap:"20px",
marginTop:"30px"
}}>


<div className="card">
<h3>Devices</h3>
<h1>{data.total_devices}</h1>
</div>


<div className="card">
<h3>Sensor Types</h3>
<h1>{data.total_sensor_types}</h1>
</div>


<div className="card">
<h3>Latest Readings</h3>
<h1>{data.total_latest_readings}</h1>
</div>


<div className="card">
<h3>Status</h3>
<h1>ONLINE 🟢</h1>
</div>


</div>

)

}

export default SummaryCards;