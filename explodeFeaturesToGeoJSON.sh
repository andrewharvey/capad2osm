#!/bin/sh

rm -fR geojson
mkdir -p geojson

# get all PA_IDs from source SHP file
# then using parallel processing convert each PA_ID feature into a simplified GeoJSON file with a subset of fields
ogrinfo -al -geom=NO source_data/CAPAD_2014_terrestrial.shp | grep 'PA_ID ' | cut -d'=' -f2 | sed 's/ //g' | \
    parallel -j 4 --workdir $PWD nice ogr2ogr -f GeoJSON -simplify 0.001 -select 'NAME,TYPE,GAZ_DATE,AUTHORITY,DATASOURCE,GOVERNANCE'  -where \"PA_ID=\'{}\'\" 'geojson/{}.geojson' source_data/CAPAD_2014_terrestrial.shp
