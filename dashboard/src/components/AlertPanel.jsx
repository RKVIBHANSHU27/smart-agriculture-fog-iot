function AlertPanel({ alerts }) {


    const sortedAlerts = [...alerts].sort(
        (a, b) =>
            new Date(b.processed_at) -
            new Date(a.processed_at)
    );


    return (

        <div className="alert-section">


            <h2>
                🚨 Active Alerts
            </h2>



            <div className="alert-table">


                <div className="alert-header">

                    <span>Severity</span>
                    <span>Device</span>
                    <span>Sensor</span>
                    <span>Value</span>
                    <span>Time</span>

                </div>



                {
                    sortedAlerts.length === 0 ?

                    (
                        <p>
                            No active alerts
                        </p>
                    )

                    :

                    (

                    sortedAlerts.map((item,index)=>(


                        <div
                            key={
                                item.alert_id || index
                            }
                            className={
                                item.alert === "CRITICAL"
                                ?
                                "alert-row critical-row"
                                :
                                "alert-row warning-row"
                            }
                        >


                            <span>

                                {
                                    item.alert === "CRITICAL"
                                    ?
                                    "🔴 CRITICAL"
                                    :
                                    "🟡 WARNING"
                                }

                            </span>



                            <span>
                                {item.device_id}
                            </span>



                            <span>
                                {item.sensor_type}
                            </span>



                            <span>
                                {item.average} {item.unit}
                            </span>



                            <span>
{
new Date(item.processed_at)
.toLocaleString(
    "en-IE",
    {
        day:"2-digit",
        month:"short",
        year:"numeric",
        hour:"2-digit",
        minute:"2-digit",
        second:"2-digit"
    }
)
}
</span>


                        </div>


                    ))

                    )

                }


            </div>


        </div>

    )

}


export default AlertPanel;