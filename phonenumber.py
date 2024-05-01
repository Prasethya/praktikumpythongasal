import phonenumbers
from phonenumbers import carrier, geocoder, timezone
mobileNo = input("masukan nomor : ")
mobileNo = phonenumbers.parse(mobileNo, "ID")

#mendapatkan lokasi
print(timezone.time_zones_for_number(mobileNo))

#mendapatkan privider
print(carrier.name_for_number(mobileNo, "en"))

#mendapatkan negara
print(geocoder.description_for_number(mobileNo, "en"))


#volidating a phone number 
print("valid Mobile Number : ", phonenumbers.is_valid_number(mobileNo))

#chekking possibility a number
print("checking possibility of number : ", phonenumbers.is_possible_number(mobileNo))