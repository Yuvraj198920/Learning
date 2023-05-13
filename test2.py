from osgeo import gdal

tiff = r"Data\Extract_basin.tif"

step1 = gdal.Open(tiff, gdal.GA_ReadOnly)
GT_Input = step1.GetGeoTransform()

step2 = step1.GetRasterBand(1)

image_as_array = step2.ReadAsArray()
size1, size2 = image_as_array.shape
print(size1, size2)

print("Size is {} x {} x {}".format(step1.RasterXSize, step1.RasterYSize,
                                step1.RasterCount))

geotransform = step1.GetGeoTransform()
if GT_Input:
    print("Origin = ({}, {})".format(GT_Input[0], GT_Input[3]))
    print("Pixel Size = ({}, {})".format(GT_Input[1], GT_Input[5]))

band = step1.GetRasterBand(1)
print("Band Type={}".format(gdal.GetDataTypeName(band.DataType)))

min = band.GetMinimum()
max = band.GetMaximum()
if not min or not max:
    (min,max) = band.ComputeRasterMinMax(True)
print("Min={:.3f}, Max={:.3f}".format(min,max))

if band.GetOverviewCount() > 0:
    print("Band has {} overviews".format(band.GetOverviewCount()))

if band.GetRasterColorTable():
    print("Band has a color table with {} entries".format(band.GetRasterColorTable().GetCount()))