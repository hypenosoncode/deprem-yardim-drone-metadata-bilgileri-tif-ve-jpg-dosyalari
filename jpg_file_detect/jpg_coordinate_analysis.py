"""
--- Python v3.10.0 ---
"""

import simplekml
import PIL.Image
import PIL.ExifTags
from gmplot import gmplot

img = PIL.Image.open("Sample/JPG/DJI_0458.jpg")
exif = {PIL.ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in PIL.ExifTags.TAGS}

marka = exif['Make']
model = exif['Model']
tarih_saat = exif['DateTime'].split(" ")
tarih = tarih_saat[0].split(":")
tarih_format = tarih[2] + "." + tarih[1] + "." + tarih[0]

kuzey = exif['GPSInfo'][2]
dogu = exif['GPSInfo'][4]
yukseklik = exif['GPSInfo'][6]

enlem = ((((kuzey[0] * 60) + kuzey[1]) * 60) + kuzey[2]) / 3600
boylam = ((((dogu[0] * 60) + dogu[1]) * 60) + dogu[2]) / 3600

print("MARKA: ", marka)
print("MODEL: ", model)
print("TARİH: ", tarih_format)
print("SAAT: ", tarih_saat[1])
print("ENLEM: ", float(enlem))
print("BOYLAM: ", float(boylam))
print("YÜKSEKLİK: ", float(yukseklik))

# KML File Writing
kml_list = [['description', float(enlem), float(boylam)]]
kml = simplekml.Kml()
for row in kml_list:
    kml.newpoint(description=row[0],
        coords=[(row[2], row[1])])  # lon, lat, optional height
kml.save("jpg_file_detect/jpg_coordinates.kml")

# Google Maps View HTML File  
gmap = gmplot.GoogleMapPlotter(enlem, boylam, 12)
gmap.marker(enlem, boylam, "cornlowerblue")
gmap.draw("jpg_file_detect/jpg_location.html")
