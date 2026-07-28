import {
  useEffect,
  useState
} from "react";


import {
  getDashboardData,
  getTelemetry,
  getAlerts
} from "./services/api";


import TelemetryChart from "./components/TelemetryChart";
import TelemetryTable from "./components/TelemetryTable";
import FogNode from "./components/FogNode";
import AlertPanel from "./components/AlertPanel";
import DeviceHealth from "./components/DeviceHealth";



function formatDate(timestamp){

  if(!timestamp)
    return "";

  const date = new Date(timestamp);

  return date.toLocaleString(
    "en-IE",
    {
      day:"2-digit",
      month:"long",
      year:"numeric",
      hour:"2-digit",
      minute:"2-digit",
      second:"2-digit"
    }
  );

}



function App(){


const [dashboard,setDashboard] = useState(null);

const [telemetry,setTelemetry] = useState([]);

const [alerts,setAlerts] = useState([]);




useEffect(()=>{


const loadData = () => {


    // Dashboard data
    getDashboardData()
    .then(data=>{
        setDashboard(data);
    });



    // Telemetry data
    getTelemetry()
    .then(data=>{
        setTelemetry(data);
    });



    // Alerts history
    getAlerts()
    .then(data=>{


        setAlerts(prevAlerts=>{


            const combined = [
                ...data,
                ...prevAlerts
            ];



            const unique = Array.from(

                new Map(

                    combined.map(
                        alert=>[
                            alert.alert_id,
                            alert
                        ]
                    )

                ).values()

            );



            return unique.slice(0,50);


        });


    });



};



// initial load
loadData();



// refresh every 5 seconds

const interval = setInterval(
    loadData,
    5000
);



return ()=>clearInterval(interval);



},[]);





if(!dashboard)

return <h1>Loading...</h1>;





return(


<div className="dashboard">



<h1 className="title">

🌱 Smart Agriculture Monitoring System

</h1>



<p>

🟢 Live Updates every 5 seconds

</p>





<div className="cards">



<div className="card">

<h3>
Devices
</h3>

<div className="value">

{dashboard.total_devices}

</div>

</div>





<div className="card">

<h3>
Sensor Types
</h3>

<div className="value">

{dashboard.total_sensor_types}

</div>

</div>





<div className="card">

<h3>
Latest Readings
</h3>

<div className="value">

{dashboard.total_latest_readings}

</div>

</div>





<div className="card">

<h3>
Status
</h3>

<div className="status">

🟢 ONLINE

</div>

</div>




</div>





<h2>
Monitoring Summary
</h2>





<div className="alerts">



<div className="alert green">

<h3>
Normal
</h3>

<h1>
{dashboard.alerts.NORMAL}
</h1>

</div>





<div className="alert yellow">

<h3>
Warning
</h3>

<h1>
{dashboard.alerts.WARNING}
</h1>

</div>





<div className="alert red">

<h3>
Critical
</h3>

<h1>
{dashboard.alerts.CRITICAL}
</h1>

</div>



</div>







<FogNode />



<DeviceHealth />



<AlertPanel alerts={alerts}/>







<h2>
📊 Sensor Analytics
</h2>


<div className="chart-grid">

<TelemetryChart
  data={telemetry}
  sensor="temperature"
/>


<TelemetryChart
  data={telemetry}
  sensor="humidity"
/>


<TelemetryChart
  data={telemetry}
  sensor="soil_moisture"
/>


<TelemetryChart
  data={telemetry}
  sensor="light"
/>


<div className="co2-chart">

<TelemetryChart
    data={telemetry}
    sensor="co2"
/>

</div>

</div>







<TelemetryTable

data={telemetry}

/>







<h2>

Last Telemetry Update

</h2>



<p>

{formatDate(dashboard.last_update)}

</p>





</div>


)

}



export default App;