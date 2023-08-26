import React, { useState } from "react";
import axios from "axios";
import { TextField, Button, Card, CardContent, Typography } from "@mui/material";

import LeafletMap from "./LeaftletMap";
import ErrorDialog from "./common/ErrorDialog";

const Weather = () => {
    const [city, setCity] = useState('');
    const [weather, setWeather] = useState(null)
    const [err, setErr] = useState(null);
    const [open, setOpen] =  useState(false);

    const getWeather = async () => {
        try {
            // eslint-disable-next-line no-template-curly-in-string
            const response = await axios.get(`http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=923a06e8e1aed432d545415d3cf17a94`)
            setWeather(response)
            setErr(null)
        } catch (error) {
            if (error.response && error.response.data) {
                setErr(error.response.data.message);
              } else {
                setErr("An error occurred");
              }
              setWeather(null); 
              setOpen(true)
        }
    };

    const handleClose = () => {
        setOpen(false)
    }

    return (
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center', height: '100vh', backgroundColor: '#f5f5f5' }}>
            <TextField label="City" variant="outlined" onChange={(e) => setCity(e.target.value)} style={{ marginBottom: '20px' }} />
            <Button variant="contained" color="primary" onClick={getWeather}>Get Weather</Button>

            <ErrorDialog open={open} handleClose={handleClose} error={err}/>

            {weather && (
                <div>
                    <Card style={{ marginTop: '20px' }}>
                        <CardContent>
                            <Typography variant="h5" component="h2">{weather.data.name}</Typography>
                            <Typography color="textSecondary">{(weather.data.main.temp - 273.15).toFixed(2)}°C</Typography>
                            <Typography variant="body2" component="p">{weather.data.weather[0].description}</Typography>
                        </CardContent>
                    </Card>

                    <div style={{height: '300px', marginTop: '20px'}}>
                        <LeafletMap lat={weather.data.coord.lat} lon={weather.data.coord.lon}/>
                    </div>

                </div>
            )}
        </div>
    )
}

export default Weather