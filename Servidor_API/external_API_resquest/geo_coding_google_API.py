import requests

class External_api_request_googleGeocode :

    #endereço basse para acesso a Geocode api do google
    googleGeocodeUrlBaseAPI = "https://maps.google.com/maps/api/geocode/"

    # para acesso a api passar o formato e a api_key, como padrão o retorno é por json e api key está definida
    #obs: uma free key só possui 2500 requisições, e essa é uma free key
    def __init__(self, outputFormat = "json", api_key = "AIzaSyD8b3UyPssRS9CwgWuW-788UFaZYS1oi9Q"):
        self.formated_url = self.googleGeocodeUrlBaseAPI + outputFormat + "?%s&key=" +api_key

    def localizationAddress(self, postal_code = None, route = None, locality = None, administrative_area_state = None, administrative_area_city = None, country = "BR"):
        #codigo postal, bairro, estado, cidade, país
        if any( i == None for i in [postal_code]):
            raise ValueError('any parameters Null, provide all parameters : postal_code, route, administrative_area_state, administrative_area_city, country(default : BR)')
        
        formated_parameters = ""
        
        if (postal_code):
            formated_parameters+= "postal_code:"+str(postal_code)+"|"
            
        if (route):
            formated_parameters+= "route:"+str(route)+"|"
        
        if (locality):
            formated_parameters+= "locality:"+locality+"|"
            
        if (administrative_area_state):
            formated_parameters+= "administrative_area:"+administrative_area_state+"|"
            
        if (administrative_area_city):
            formated_parameters+= "administrative_area:"+administrative_area_city+"|"
            
        if (country):
            formated_parameters+= "country:"+country
        

        components = "components=%s"%(formated_parameters)
        
        requestUrl = self.formated_url%(components)
        print(requestUrl)
        response = requests.get(requestUrl)

        response = response.json()
        
        if response['status'] == 'OK':
            
            localization = response['results'][0]['geometry']['location']
            print(localization)
            return localization['lat'], localization['lng']
        print(response['status'])
        return response['status']
