import React, { useEffect } from 'react';
import BasemapGallery from 'arcgis-js-api/widgets/BasemapGallery';

const BasemapGalleryWidget = ({ view }) => {
    useEffect(() => {
        if(!view) return
        const searchExisting = view.ui.find("basemapGalleryWidget")
        if (searchExisting) {
            return
        }

        const basemapGalleryWidget = new BasemapGallery({
            view: view
        })
        basemapGalleryWidget.id = "basemapGalleryWidget";
        view.ui.add(basemapGalleryWidget, 'top-right')
    }, [view])
}

export default BasemapGalleryWidget;