# Deprem Yardım Metadata Bilgileri .tif ve .jpg Dosyaları İçin

Deprem yardım projesinin bir geliştiricisi olarak drone görüntülerinde .tif veya .jpg dosya formatlarında bulunan önemli metadata verilerini çeken ve KML dosyasına aktaran çalışmadır.

## KURULUM
```bash
pip install Pillow
pip install simplekml
pip install gmplot
pip install ExifRead
```
## KULLANIM
Dosya türü .jpg ise `jpg_file_detect > jpg_coordinate_analysis.py` kodu çalıştırılmalıdır. Kod içerisinde `img = PIL.Image.open(".../.../***.jpg")` bulunan yere fotoğrafın konumu yazılır. Kod çalıştırıldıktan sonra metadata içerisinde bulunan önemli verileri getirecektir.

![image](https://user-images.githubusercontent.com/74931027/219063344-23dc07ca-5732-46fe-a75f-e314f30e61e6.png)

Kod çalıştıktan sonra koordinat verileri `jpg_coordinates.kml` adlı dosyaya eklenir ve konum tespitinin yapılması için `jpg_location.html` adlı Google Maps klasörü oluşturulur.

Dosya türü .tif ise `tif_file_detect > tif_coordinate_analysis.py` kodu çalıştırılmalıdır. Kod içerisinde `with open('.../.../***.tif', 'rb') as f:` bulunan yere fotoğrafın konumu yazılır. Kod çalıştırıldıktan sonra metadata içerisinde bulunan önemli verileri getirecektir.

![image](https://user-images.githubusercontent.com/74931027/219064369-32f171c7-7b17-40b3-8ca9-4b421689477a.png)

Kod çalıştıktan sonra koordinat verileri `tif_coordinates.kml` adlı dosyaya eklenir ve konum tespitinin yapılması için `tif_location.html` adlı Google Maps klasörü oluşturulur.

## VERİ TİPLERİ [TAGS]
Metadata üzerinden çekilen veriler çok daha fazladır. Bu projede ihtiyaç dahilinde bahsi geçen veriler alınmıştır. Farklı verileri çekmek isteyenler için `jpg_coordinate_analysis.py` burada `print(exif)` yazıp çalıştırırsanız hangi tag 'ın hangi veriye karşılık geldiğini görebilir ve o veriyi `variable = exif['Tag']` şeklinde çekebilirsiniz. 

`tif_coordinate_analysis.py` kodunda ise hangi tag 'ların hangi veriye karşılık geldiğini görmek için şu kodu deneyin,
```bash
import exifread
# Open image file for reading (must be in binary mode)
f = open('.../.../***.tif', 'rb')
tags = exifread.process_file(f)

for tag in tags.keys():
    if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
        print("Key: %s, value %s" % (tag, tags[tag]))
```
Kod çıktısı size tag'ları verecektir. İlgili veriyi `variable = exif_tags.get('Tag')` şeklinde çekebilirsiniz.

## DESTEK
Proje konusunda farklı fikirleriniz varsa ve geliştirmek istiyorsanız `Issue` açabilir veya benimle iletişime geçebilirsiniz.

### 🤝🏻 &nbsp;İletişim & Sosyal Medya

<p align="center">
<a href="mailto:cinarismailselcuk@gmail.com"><img src="https://img.shields.io/badge/-Mail-D14836?style=flat&logo=Gmail&logoColor=white"/></a>
<a href="https://www.linkedin.com/in/ismailselcukcinar/"><img src="https://img.shields.io/badge/-LinkedIn-0077B5?style=flat&logo=Linkedin&logoColor=white%22"/</a>
<a href="https://instagram.com/ismail_selcuks"><img src="https://img.shields.io/badge/-Instagram_-E4405F?style=flat&logo=Instagram&logoColor=white"/></a>
<a href="https://twitter.com/ismail_selcuks"><img src="https://img.shields.io/badge/-Twitter_-1976c2?style=flat&logo=Twitter&logoColor=white"/></a>
<a href="https://www.youtube.com/channel/UCSt6rE5y6iklyFBpm-0xOYA"><img src="https://img.shields.io/badge/-YouTube_-c4302b?style=flat&logo=YouTube&logoColor=white"/></a>
<a href="https://discordapp.com/users/652243845790302239/"><img src="https://img.shields.io/badge/-Discord_-6A5ACD?style=flat&logo=Discord&logoColor=white"/></a>
</p>
