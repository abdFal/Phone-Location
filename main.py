import phonenumbers
import requests
import opencage
from opencage.geocoder import OpenCageGeocode
from phonenumbers import geocoder
from phone import number

# Ambil nomor telepon dari pengguna
num = number

# Parsing nomor telepon menggunakan library phonenumbers
thenumber = phonenumbers.parse(num)

# Ambil lokasi dari nomor telepon menggunakan library phonenumbers
location = geocoder.description_for_number(thenumber, "id")

key = 'your api key'
geocoder = OpenCageGeocode(key)
query = str(location)
result = geocoder.geocode(query)

lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']

# Tampilkan hasil
print("Lokasi: ", location)
print("Koordinat: ",lat,lng)
