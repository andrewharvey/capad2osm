download:
        mkdir -p source_data
        curl 'http://www.environment.gov.au/fed/catalog/search/resource/downloadData.page' -H 'Referer: http://www.environment.gov.au/fed/catalog/search/resource/downloadData.page?uuid=%7B4448CACD-9DA8-43D1-A48F-48149FD5FCFD%7D' --data 'downloadFilesTable%3A0%3Aj_id_jsp_1490667900_4pc7=downloadFilesTable%3A0%3Aj_id_jsp_1490667900_4pc7&javax.faces.ViewState=-8750847866103299363%3A6810764797291798559&downloadFilesTable%3A0%3Aj_id_jsp_1490667900_4pc7%3Aj_id_jsp_1490667900_5pc7=downloadFilesTable%3A0%3Aj_id_jsp_1490667900_4pc7%3Aj_id_jsp_1490667900_5pc7&filename=CAPAD_2014_terrestrial.zip&fileIdentifier=9984a9fd-3dd0-4e38-bfbd-7e788fa851a1&uuid=4448CACD-9DA8-43D1-A48F-48149FD5FCFD' --compressed > 'source_data/CAPAD_2014_terrestrial.zip'
        unzip -d source_data/ source_data/CAPAD_2014_terrestrial.zip

osm:
        ogr2osm.py --no-memory-copy -t capad2osm -o capad.osm source_data/CAPAD_2014_terrestrial.shp