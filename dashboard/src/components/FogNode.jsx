function FogNode(){

const fogNodes = [
    {
        id:"FOG_NODE_01",
        status:"ACTIVE",
        devices:3,
        leader:"YES"
    },
    {
        id:"FOG_NODE_02",
        status:"ACTIVE",
        devices:2,
        leader:"NO"
    }
];


return (

<div>

<h1>
Fog Node Monitoring
</h1>


<div className="fog-container">

{
fogNodes.map((node)=>(

<div className="fog-card" key={node.id}>

<h2>
🟢 {node.id}
</h2>


<p>
Status:
<strong className="active">
 {node.status}
</strong>
</p>


<p>
Connected Devices:
{node.devices}
</p>


<p>
Leader:
{node.leader}
</p>


<p>
Processing:
Edge Analytics
</p>


</div>

))
}


</div>

</div>

);


}


export default FogNode;