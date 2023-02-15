import exifread
import simplekml
from gmplot import gmplot

with open('Sample/TIF/DJI_0153.tif', 'rb') as f:
    # EXIF data read
    exif_tags = exifread.process_file(f)
    # TAG Reading Area
    trademark = exif_tags.get('Image Make')
    model = exif_tags.get('Image Model')

    weather = exif_tags.get('EXIF LightSource')

    date_time = exif_tags.get('EXIF DateTimeOriginal')
    date_time_value_convert = str(date_time).split(" ")
    date = date_time_value_convert[0].split(":")
    date_format = date[2] + "." + date[1] + "." + date[0]
    time = date_time_value_convert[1]

    lat_tag = exif_tags.get('GPS GPSLatitude')
    lon_tag = exif_tags.get('GPS GPSLongitude')
    altitude = exif_tags.get('GPS GPSAltitude')
    altitude_ref = exif_tags.get('GPS GPSAltitudeRef')

    # GPS Converter
    if lat_tag and lon_tag:
        lat_convert = [float(x.num) / float(x.den) for x in lat_tag.values]
        lat_degree = lat_convert[0] + lat_convert[1] / 60 + lat_convert[2] / 3600

        lon_convert = [float(x.num) / float(x.den) for x in lon_tag.values]
        lon_degree = lon_convert[0] + lon_convert[1] / 60 + lon_convert[2] / 3600

    # Altitude variable is "Ratio", Ratio to Float converter process    
    if altitude and altitude_ref:
        altitude_value = altitude.values[0]
        altitude_float = float(altitude_value.num) / altitude_value.den
        # Set mark based on height reference
        if altitude_ref.values[0] == 1:
            altitude_float *= -1

    print("MARKA: ", trademark)
    print("MODEL: ", model)
    print("TARİH: ", date_format)
    print("SAAT : ", time)
    print("ENLEM: ", lat_degree)
    print("BOYLAM: ", lon_degree)
    print("YÜKSEKLİK: ", altitude_float)
    print("HAVA DURUMU: ", weather)

    # KML File Writing
    kml_list = [['description', float(lat_degree), float(lon_degree)]]
    kml = simplekml.Kml()
    for row in kml_list:
        kml.newpoint(description=row[0],
        coords=[(row[2], row[1])])  # lon, lat, optional height
    kml.save("tif_file_detect/tif_coordinates.kml")

    # Google Maps View HTML File        
    gmap = gmplot.GoogleMapPlotter(lat_degree, lon_degree, 12)
    gmap.marker(lat_degree, lon_degree, "cornlowerblue")
    gmap.draw("tif_file_detect/tif_location.html")
