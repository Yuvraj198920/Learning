import React, { useEffect } from 'react';
import Bookmarks from 'arcgis-js-api/widgets/Bookmarks';

const EsriBookmark = ({ view }) => {
    useEffect(() => {
        if (!view) return;

        const bookmarkList = [
            {
              name: 'New York',
              extent: {
                spatialReference: {
                  wkid: 4326
                },
                xmin: -74.5,
                ymin: 40.5,
                xmax: -73.5,
                ymax: 41
              }
            },
            {
              name: 'Los Angeles',
              extent: {
                spatialReference: {
                  wkid: 4326
                },
                xmin: -118.8,
                ymin: 33.8,
                xmax: -117.8,
                ymax: 34.2
              }
            }
          ];

          // create the bookmark widget
          const bookmarkwidget = new Bookmarks({
            view: view,
            bookmarks: bookmarkList
          });

          //Add the bookmarks widget to the top-rght corner of view
          view.ui.add(bookmarkwidget, 'top-right')
    }, [view]);

    return null;
}

export default EsriBookmark;