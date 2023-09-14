import arcpy

sde_file = "test.sde"
# Set workspace
arcpy.env.worksapce = sde_file

#List feature classes
fc_list = arcpy.ListFeatureClasses()

for fc in fc_list:
    print(fc)