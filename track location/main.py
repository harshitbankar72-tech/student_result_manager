import phonenumbers
from phonenumbers import geocoder as phone_geocoder
from opencage.geocoder import OpenCageGeocode, NotAuthorizedError
import webbrowser

API_KEY = "94ba9e3a7dc84debbdefa03548a94df4"
geocoder_oc = OpenCageGeocode(API_KEY)

number = input("Enter phone number (with +91): ")

# Parse number (IMPORTANT)
parsed = phonenumbers.parse(number, "IN")

if not phonenumbers.is_valid_number(parsed):
    print("❌ Invalid phone number")
    exit()

# Get state / circle
region = phone_geocoder.description_for_number(parsed, "en")
print("📍 State / Circle:", region)

if not region:
    print("❌ Region not found")
    exit()

# Approximate map (state center)
try:
    results = geocoder_oc.geocode(f"{region}, India")
except NotAuthorizedError:
    print("❌ Invalid OpenCage API key")
    exit()
except Exception as e:
    print("❌ OpenCage error:", e)
    exit()

if not results:
    print("❌ No geocoding results")
    exit()

loc = results[0]
lat = loc['geometry']['lat']
lng = loc['geometry']['lng']

print("🌍 Latitude:", lat)
print("🌍 Longitude:", lng)
print("⚠️ Location is approximate, not live GPS")

maps_link = f"https://www.google.com/maps?q={lat},{lng}"
print("🗺 Google Maps:", maps_link)

webbrowser.open(maps_link)

