from osgeo import gdal
from osgeo import ogr, osr
import math
import os

raster = r"pythonenv\Learning\Data\Extract_basin.tif"

open_raster = gdal.Open(raster, gdal.GA_ReadOnly)

# Get Raster size and extent
cols = open_raster.RasterXSize
rows = open_raster.RasterYSize
transform = open_raster.GetGeoTransform()
xmin = transform[0]
ymax = transform[3]
xmax = xmin + transform[1] * cols
ymin = ymax + transform[5] * rows
# print(xmin, ymax, xmax, ymin)
# Get pixel in meters
# Get pixel size in meters
srs = osr.SpatialReference()
srs.ImportFromWkt(open_raster.GetProjection())
utm_zone = int((math.floor((xmin + 180) / 6) % 60) + 1)
print(utm_zone)
srs.SetUTM(utm_zone, int(ymax > 0))
srs_geo = srs.CloneGeogCS()
ct = osr.CoordinateTransformation(srs_geo, srs)
xmin_m, ymin_m, _ = ct.TransformPoint(xmin, ymin)
xmax_m, ymax_m, _ = ct.TransformPoint(xmax, ymax)
xres_deg = transform[1]
yres_deg = abs(transform[5])
xres_m = (111320 * math.cos(math.radians((ymax+ymin)/2)) * xres_deg)
yres_m = (111320 * yres_deg)

print(f"Extent: {xmin}, {ymin}, {xmax}, {ymax}")
print(f"Pixel size: {xres_m} meters, {yres_m} meters")

# Convert the extent to UTM coordinates (meters)
source_srs = osr.SpatialReference()
source_srs.ImportFromEPSG(4326)  # WGS84
target_srs = osr.SpatialReference()
target_srs.ImportFromEPSG(32631)  # UTM zone 31N
transform = osr.CoordinateTransformation(source_srs, target_srs)
xmin_utm, ymin_utm, _ = transform.TransformPoint(xmin, ymin)
xmax_utm, ymax_utm, _ = transform.TransformPoint(xmax, ymax)

# Now we create grid using above cell size
driver = ogr.GetDriverByName('ESRI Shapefile')
ds = driver.CreateDataSource('grid.shp')
layer = ds.CreateLayer('grid', geom_type=ogr.wkbPolygon)
field_defn = ogr.FieldDefn('id', ogr.OFTInteger)
layer.CreateField(field_defn)

# Add grid cells to the layer
for i in range(int(xmin_m), int(xmax_m), int(xres_m)):
    for j in range(int(ymin_m), int(ymax_m), int(yres_m)):
        ring = ogr.Geometry(ogr.wkbLinearRing)
        ring.AddPoint(i, j)
        ring.AddPoint(i + xres_m, j)
        ring.AddPoint(i + xres_m, j + yres_m)
        ring.AddPoint(i, j + yres_m)
        ring.AddPoint(i, j)
        poly = ogr.Geometry(ogr.wkbPolygon)
        poly.AddGeometry(ring)
        feature = ogr.Feature(layer.GetLayerDefn())
        feature.SetGeometry(poly)
        feature.SetField('id', 1)
        layer.CreateFeature(feature)
        feature = None

# Create the .prj file
shp_name = os.path.splitext("grid.shp")[0]
with open(f"{shp_name}.prj", 'w') as prj_file:
    prj_file.write(target_srs.ExportToWkt())

# Close vector file
ds = None

# Close raster file
raster = None