#!/bin/sh

rm -f id-name.csv
ls -1 geojson/*.geojson | parallel -j 4 --workdir $PWD ./name-id-mapping.sh {}
