import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = input("Enter the phone number : ")
ch_number = phonenumbers.parse(number, 'CH')

print(geocoder.description_for_number(ch_number, "en"))

m_data = phonenumbers.PhoneMetadata.load_all()

s_num = phonenumbers.parse(number, 'RO')

print(carrier.name_for_number(s_num, "en"))
