import rasterio as rio
from pyproj import Transformer

fp = '.\Data\Extract_basin.tif'

# Open the DEM file
with rio.open(fp) as src:

    # Get the raster dimensions
    width = src.width
    height = src.height

    # Get the spatial resolution of the raster
    x_res, y_res = src.res

    # Calculate the width and height in meters
    width_m = width * x_res
    height_m = height * y_res

    # Print the results
    print("Raster dimensions (in pixels): ", width, " x ", height)
    print("Raster dimensions (in meters): ", width_m, " x ", height_m)
     # Define the size of the grid cells
    # x_size = width_m # Replace with the desired cell size in meters
    # y_size = height_m # Replace

    transformer = Transformer.from_crs(src.crs, 'epsg:32631') # Replace 32631 with the UTM zone for your area
    width_m, height_m = transformer.transform(src.width*src.res[0], src.height*src.res[1])
    print("UTM height and width")
    print(width_m, height_m)
    # Define the extent of the fishnet
    xmin, ymin, xmax, ymax = transformer.transform(src.bounds.left, src.bounds.bottom, src.bounds.right, src.bounds.top)
    print("Print xmin, ymin, xmax, ymax")
    print(xmin, ymin, xmax, ymax)

# Generate the fishnet
rows = int((ymax-ymin)/width_m)
cols = int((xmax-xmin)/height_m)
polygons = []
print(rows, cols)