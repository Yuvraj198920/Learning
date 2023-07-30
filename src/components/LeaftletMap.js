import React from "react";
import { MapContainer, TileLayer, Marker, useMap } from "react-leaflet";

function ChangeView ({ center }) {
    const map = useMap()
    map.setView(center);
    return null
}

const LeafletMap = ({ lat, lon }) => {
    return (
        <MapContainer center={[lat, lon]} zoom={13} style={{ height: "100%", width: "100%" }}>
            <ChangeView center={[lat, lon]}/>
            <TileLayer
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            <Marker position={[lat, lon]} />
        </MapContainer>
    )
}

export default LeafletMap