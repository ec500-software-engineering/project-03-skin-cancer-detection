import googlemaps

KEY = "AIzaSyBhkOO1fkzFJfsEKHBKOjagBoJ195Ue-Kw"
gmaps_key = googlemaps.Client(key = KEY)

place_result = gmaps_key.find_place("24 Peabody Terrace, Cambridge, MA", "textquery",fields = [
    "formatted_address", "geometry", "name", "photos", "place_id"])
# print(place_result)
place_id = place_result["candidates"][0]["place_id"]
# print(place_id)
place_detail = gmaps_key.place(place_id)

LAT = place_result["candidates"][0]["geometry"]["location"]["lat"]
LON = place_result["candidates"][0]["geometry"]["location"]["lng"]
# print(LAT, LON)

# print(place_detail)

def get_position(address):
    if type(address) == str:
        geocode_result = gmaps_key.geocode(address)
        LAT = geocode_result[0]["geometry"]["location"]["lat"]
        LON = geocode_result[0]["geometry"]["location"]["lng"]
        return (LAT, LON)
    else:
        LAT = address["geometry"]["location"]["lat"]
        LON = address["geometry"]["location"]["lng"]
        return (LAT, LON)

position = get_position("24 Peabody Terrace, Cambridge, MA")


def get_nearby_results(position, searchRange, searchName):
    nearby_results = gmaps_key.places_nearby(position, searchRange, name = searchName)
    return nearby_results["results"]

def get_place_details(place_id):
    return gmaps_key.place(place_id)

def get_photo_html(result):
    try:
        ref = result["photos"][0]["photo_reference"]
        # ref = place_detail["result"]["photos"][0]["photo_reference"]
        html = "https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=" + ref + "&key=" + KEY
        return html
    except:
        return []

def get_phone_number(place_detail):
    try:
        num = place_detail["result"]["international_phone_number"]
        return num
    except:
        return "not available"
    
    
    
