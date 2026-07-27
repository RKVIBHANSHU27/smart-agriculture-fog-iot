import {
  useEffect,
  useState
} from "react";

import {
  getDashboardData,
  getTelemetry
} from "./services/api";

import TelemetryChart from "./components/TelemetryChart";
import TelemetryTable from "./components/TelemetryTable";
import FogNode from "./components/FogNode";
import DeviceHealth from "./components/DeviceHealth";
import AlertPanel from "./components/AlertPanel";
import {getAlerts} from "./services/api";



function App(){
function formatDate(timestamp){
  
  const [alerts,setAlerts] = useState([]);

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
      minute:"2-digit"
    }
  );

}


  const [dashboard, setDashboard] = useState(null);
  const [telemetry, setTelemetry] = useState([]);
  const [alerts,setAlerts] = useState([]);

useEffect(()=>{

    getDashboardData()
      .then(data => {
        setDashboard(data);
      });


    getTelemetry()
      .then(data => {
        setTelemetry(data);
      });


}, []);



  if(!dashboard)
    return <h1>Loading...</h1>



  return(

    <div className="dashboard">

      <h1 className="title">
      🌱 Smart Agriculture Monitoring System
      <span className="live">
        ● LIVE
      </span>
      </h1>


      <div className="cards">


        <div className="card">
          <h3>Devices</h3>
          <div className="value">
            {dashboard.total_devices}
          </div>
        </div>


        <div className="card">
          <h3>Sensor Types</h3>
          <div className="value">
            {dashboard.total_sensor_types}
          </div>
        </div>


        <div className="card">
          <h3>Latest Readings</h3>
          <div className="value">
            {dashboard.total_latest_readings}
          </div>
        </div>


        <div className="card">
          <h3>Status</h3>
          <div className="status">
            🟢 ONLINE
          </div>
        </div>


      </div>



      <h2>Alert Monitoring</h2>


      <div className="alerts">


        <div className="alert green">
          <h3>Normal</h3>
          <h1>{dashboard.alerts.NORMAL}</h1>
        </div>


        <div className="alert yellow">
          <h3>Warning</h3>
          <h1>{dashboard.alerts.WARNING}</h1>
        </div>


        <div className="alert red">
          <h3>Critical</h3>
          <h1>{dashboard.alerts.CRITICAL}</h1>
        </div>


      </div>


      <FogNode />
      
      <DeviceHealth />
      
      <h1>
        Sensor Analytics
      </h1>


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