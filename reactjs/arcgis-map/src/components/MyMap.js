import React, { useRef, useEffect, useState } from 'react';
import EsriMap from 'arcgis-js-api/Map';
import MapView from 'arcgis-js-api/views/MapView';
import "./myMap.css"

import BookmarkComponent from './BookmarkComponent';

const MyMap = () => {
    const mapDiv = useRef(null);
    const [view, setView] =  useState(null)

    const bookmarks = [
        { name: 'New York', location:[-74.006, 40.7128]},
        { name: 'Los Angeles', location:[-118.2437, 34.0522]}
    ]

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

    const handleBookmarkClick = (bookmark) =>{
        if(view) {
            view.goTo({
                target: bookmark.location,
                zoom:10
            })
        }
    }

    return (
        <div>
            <BookmarkComponent bookmarks={bookmarks} onBookmarkClick={handleBookmarkClick} />
            <div className='mapDiv' ref={mapDiv}></div>
        </div>
    ) 
    
}

export default MyMap;