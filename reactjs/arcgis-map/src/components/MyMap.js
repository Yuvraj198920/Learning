import React, { useRef, useEffect } from 'react';
import EsriMap from 'arcgis-js-api/Map';
import MapView from 'arcgis-js-api/views/MapView';
import "./myMap.css"

const MyMap = () => {
    const mapDiv = useRef(null);

    useEffect(() => {
        const map = new EsriMap({
            basemap: 'streets'
        });
    
        new MapView({
            container: mapDiv.current,
            map: map,
            zoom:4,
            center: [15, 65]
        })
    }, []);

    return <div className='mapDiv' ref={mapDiv}></div>
    
}

export default MyMap;