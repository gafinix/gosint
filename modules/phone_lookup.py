import phonenumbers
from phonenumbers import geocoder, carrier

def lookup_phone(number):
    try:
        phone_data = phonenumbers.parse(number)
        country = geocoder.description_for_number(phone_data, "en")
        service_provider = carrier.name_for_number(phone_data, "en")
        return {
            "Country": country,
            "Service Provider": service_provider,
            "Valid": phonenumbers.is_valid_number(phone_data)
        }
    except Exception as e:
        return {"Error": str(e)}
