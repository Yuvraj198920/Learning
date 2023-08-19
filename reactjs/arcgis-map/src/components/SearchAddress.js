import React, { useEffect } from "react";
import Search from "arcgis-js-api/widgets/Search";

const SearchAddress = ({ view }) => {
    useEffect(() => {
        if (!view) return;

        // check if widget already created
        const existingWidget = view.ui.find("searchWidget")
        if (existingWidget) {
            return;
        }
        const searchWidget = new Search({
            view:view
        });
        searchWidget.id = "searchWidget"
        view.ui.add(searchWidget, "top-left")
    },[view])

    return null;
}

export default SearchAddress;