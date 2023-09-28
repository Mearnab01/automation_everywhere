import phonenumbers
from phonenumbers import timezone, geocoder, carrier

try:
    country_code ="+91"
    user_input = input("Enter a phone number: ")
    
    full_phNo = f"{country_code}{user_input}"

    phone = phonenumbers.parse(full_phNo)

    # Get the country code and country name
    country_code = phonenumbers.region_code_for_number(phone)
    country_name = geocoder.country_name_for_number(phone, "en")

    # Get the timezone for the phone number
    time_zones = timezone.time_zones_for_number(phone)

    # Get the carrier (telecom operator) for the phone number
    carrier_name = carrier.name_for_number(phone, "en")

    # Get the localized description of the registration area (usually the city)
    registration_area = geocoder.description_for_number(phone, "en")

    print("Phone Number:", full_phNo)
    print("Country Code:", country_code)
    print("Country Name:", country_name)
    print("Time Zones:", time_zones)
    print("Carrier Name:", carrier_name)
    print("Registration Area:", registration_area)

except Exception as e:
    print(f"An error occurred: {str(e)}")
