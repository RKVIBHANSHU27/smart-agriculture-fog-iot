function DeviceHealth(){

const devices = [
{
id:"DEVICE01",
battery:92,
temperature:27.5,
fog:"FOG_NODE_01"
},
{
id:"DEVICE02",
battery:86,
temperature:26.8,
fog:"FOG_NODE_01"
},
{
id:"DEVICE03",
battery:78,
temperature:28.1,
fog:"FOG_NODE_01"
},
{
id:"DEVICE04",
battery:88,
temperature:25.9,
fog:"FOG_NODE_02"
},
{
id:"DEVICE05",
battery:95,
temperature:24.7,
fog:"FOG_NODE_02"
}
];


return (

<div>

<h1>
Device Health Monitoring
</h1>


<div className="fog-container">

{
devices.map(device=>(

<div className="fog-card" key={device.id}>


<h2>
🟢 {device.id}
</h2>


<p>
Status:
<span className="active">
 ONLINE
</span>
</p>


<p>
Battery:
{device.battery}%
</p>


<p>
Temperature:
{device.temperature}°C
</p>


<p>
Fog Node:
{device.fog}
</p>


</div>

))
}


</div>


</div>

)

}


export default DeviceHealth;