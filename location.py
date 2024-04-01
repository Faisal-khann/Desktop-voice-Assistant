import requests


def find_loc():
    # use the request module to get the public IP address of the machine using the ipify API
    # ipadd = requests.get("https://api.ipify.org").text
    ipadd = requests.get("https://api.ipify.org").text
    # Construct the url for obtaining geographical information based on the Ip address using the geojs.io API
    url = "https://get.geojs.io/v1/ip/geo/" + ipadd + ".json"

    # use 'request to send a GET request to the geojs.io.API and get the geographic information in JSON format
    geo = requests.get(url)
    geo_data = geo.json()

    print(geo_data)  # print the obtained geographic in json format

    # Extract relevant information from the JSON response
    city = geo_data["city"]
    country = geo_data["country"]
    # state = geo_data["state"]
    latitude = geo_data["latitude"]
    longitude = geo_data["longitude"]
    timezone = geo_data["timezone"]
    internet = geo_data["organization"]

    # print the extracted information in a formatted manner
    print(
        f"city = {city}\ncountry = {country}\n\nlatitude = {latitude}\nlongitude = {longitude}\ntimezone = {timezone}\ninternet = {internet}"
    )

    return f"city = {city}\ncountry = {country}\n\nlatitude = {latitude}\nlongitude = {longitude}\ntimezone = {timezone}\ninternet = {internet}"

find_loc()
