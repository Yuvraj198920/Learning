import React, { useEffect } from 'react';
import Bookmarks from 'arcgis-js-api/widgets/Bookmarks';

const EsriBookmark = ({ view }) => {
    useEffect(() => {
        if (!view) return;
        const existingWidget = view.ui.find("bookmarksWidget");
        if (existingWidget) {
            return;
        }
        // create the bookmark widget
        const bookmarkwidget = new Bookmarks({
            view: view,
            editingEnabled: true
        });
        bookmarkwidget.id = "bookmarksWidget"
        //Add the bookmarks widget to the top-rght corner of view
        view.ui.add(bookmarkwidget, 'top-right')
    }, [view]);

    return null;
}

export default EsriBookmark;