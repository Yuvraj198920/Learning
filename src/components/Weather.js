import React, { useState } from "react";
import axios from "axios";
import { TextField, Button, Card, CardContent, Typography } from "@mui/material";

const Weather = () => {
    const[city, setCity] = useState('');
    const[weather, setWeather] = useState(null)

    const getWeather = async () => {
        try{
            // eslint-disable-next-line no-template-curly-in-string
            const response = await axios.get(`http://api.openweathermap.org/data/2.5/weather?q=${city}&appid=923a06e8e1aed432d545415d3cf17a94`)
            setWeather(response)
        } catch(err) {
            console.error(err)
        }
    };

    return (
        <div style={{display: 'flex', flexDirection: 'column', alignItems:'center', justifyContent: 'center', height: '100vh', backgroundColor: '#f5f5f5'}}>
            <TextField label="City" variant="outlined" onChange={(e) => setCity(e.target.value)} style={{ marginBottom: '20px' }} />
            <Button variant="contained" color="primary" onClick={getWeather}>Get Weather</Button>
            {weather && (
                <Card style={{ marginTop: '20px', width: '300px' }}>
                    <CardContent>
                    <Typography variant="h5" component="h2">{weather.data.name}</Typography>
                    <Typography color="textSecondary">{(weather.data.main.temp - 273.15).toFixed(2)}°C</Typography>
                    <Typography variant="body2" component="p">{weather.data.weather[0].description}</Typography>
                    </CardContent>
                </Card>
            )}
        </div>
    )
}

export default Weather