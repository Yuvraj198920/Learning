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