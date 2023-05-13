import os
from osgeo import ogr, osr
# Get the shapefile name without extension
shp_name = os.path.splitext('grid.shp')[0]

# Convert the extent to UTM coordinates (meters)
source_srs = osr.SpatialReference()
source_srs.ImportFromEPSG(4326)  # WGS84
target_srs = osr.SpatialReference()
target_srs.ImportFromEPSG(32631)  # UTM zone 31N
transform = osr.CoordinateTransformation(source_srs, target_srs)
xmin_utm, ymin_utm, _ = transform.TransformPoint(xmin, ymin)
xmax_utm, ymax_utm, _ = transform.TransformPoint(xmax, ymax)
xres_m, yres_m = transform.TransformPoint(xmin + xres, ymin + yres)[:2]

# Create the .prj file
with open(f"{shp_name}.prj", 'w') as prj_file:
    prj_file.write(srs.ExportToWkt())

# Close the shapefile
ds = None