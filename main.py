import phonenumbers
from phone import number

from phonenumbers import carrier
from phonenumbers import geocoder

thenumber = phonenumbers.parse(number)
location = geocoder.description_for_number(thenumber, "en")
user = carrier.name_for_number(thenumber, "en")

print (location)
print (user)