import React, { useRef, useEffect, useState } from 'react';
import EsriMap from 'arcgis-js-api/Map';
import MapView from 'arcgis-js-api/views/MapView';
import "./myMap.css"
import EsriBookmark from './EsriBookmark';
import SearchAddress from './SearchAddress';
import BasemapGalleryWidget from './BasemapGalleryWidget';
import DirectionWidget from './Directions';

const MyMap = () => {
    const mapDiv = useRef(null);
    const [view, setView] =  useState(null);

    useEffect(() => {
        const map = new EsriMap({
            basemap: 'streets'
        });
    
        const mapview = new MapView({
            container: mapDiv.current,
            map: map,
            zoom:4,
            center: [15, 65]
        })

        setView(mapview)
    }, []);

    return (
        <div>
            <div className='mapDiv' ref={mapDiv}></div>
            {view && < EsriBookmark view={view}/>}
            {view && < SearchAddress view={view}/>}
            {view && < BasemapGalleryWidget view={view}/>}
            {view && < DirectionWidget view={view}/>}
        </div>
    ) 
    
}

export default MyMap;