import React, { useEffect } from "react";
import Direction from "arcgis-js-api/widgets/Directions";
import RouteLayer from "arcgis-js-api/layers/RouteLayer";

const DirectionWidget = ({ view }) => {
    useEffect(() => {
        if (!view) return;

        // check if widget already created
        const existingWidget = view.ui.find("DirectionWidget")
        if (existingWidget) {
            return;
        }
        const apiKey = "AAPK9250e700411749c9b0f45c5c54662f24eGi6gpLH6WTEpI4rw0r6VT0MBuAEWhFUpHonLTRzLQfho48WPf4vBRkm0QFyErIP";
        const routLayer = new RouteLayer("https://route-api.arcgis.com/arcgis/rest/services/World/Route/NAServer/Route_World");
        const directionWidget = new Direction({
            layer: routLayer,
            apiKey,
            view
        })
        directionWidget.id = "DirectionWidget"
        view.ui.add(directionWidget, "top-left")
    },[view])

    return null;
}

export default DirectionWidget;