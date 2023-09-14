import arcpy

sde_file = "test.sde"
# Set workspace
arcpy.env.worksapce = sde_file

#List feature classes
fc_list = arcpy.ListFeatureClasses()

for fc in fc_list:
    print(fc)

# table
table_name = "tablename"

# Check if the table exists in sde
if arcpy.Exists(table_name):
    print(f"{table_name} is present in sde")
else:
    print(f"{table_name} is not present inside sde")

# Search for feature
# Where clause
jobID = "rgrgrwgwrgwegw"
where_clause = f"OBJECTID = {jobID}"

with arcpy.da.SearchCursor(table_name, ["OBJECTID", "F3E_ID"], where_clause) as cursor:
    for row in cursor:
        xy = row[0].firstPoint
        x, y = xy.X, xy.Y
        