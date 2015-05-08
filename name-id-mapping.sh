#!/bin/sh

name=`jq --raw-output '.features[].properties.NAME + " " + .features[].properties.TYPE' $1`
base=`basename $1 .geojson`
echo "$base\t$name" >> id-name.csv
