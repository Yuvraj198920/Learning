import React, { useState } from "react";
import axios from "axios";

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
        <div>
            <input type="text" onChange={(e) => setCity(e.target.value)} />
            <button onClick={getWeather}>Get Weather</button>
            {weather && (
                <div>
                    <h3>{weather.data.name}</h3>
                    <p>{weather.data.main.temp}</p>
                    <p>{weather.data.weather[0].description}</p>
                </div>
            )}
        </div>
    )
}

export default Weather