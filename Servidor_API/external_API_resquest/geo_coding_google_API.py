import requests

class External_api_request_googleGeocode :

    googleGeocodeUrlBaseAPI = "https://maps.google.com/maps/api/geocode/"
    
    def __init__(self, outputFormat = "json", api_key = "AIzaSyD8b3UyPssRS9CwgWuW-788UFaZYS1oi9Q"):
        self.formated_url = self.googleGeocodeUrlBaseAPI + outputFormat + "?%s&key=" +api_key

    def localizationAddress(self, postal_code):
        parameters = "address=%s"%(str(postal_code))
        response = requests.get(self.formated_url%(parameters))
        response = response.json()
        if response['status'] == 'OK':
            localization = response['results'][0]['geometry']['location']
            return localization['lat'], localization['lng']
        return response['status']
