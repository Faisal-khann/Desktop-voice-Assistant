import requests


def find_loc():
    try:
        # use the request module to get the public IP address of the machine using the ipify API
        ipadd = requests.get("https://api.ipify.org").text
        # Construct the url for obtaining geographical information based on the IP address using the geojs.io API
        url = "https://get.geojs.io/v1/ip/geo/" + ipadd + ".json"

        # use 'requests' to send a GET request to the geojs.io API and get the geographic information in JSON format
        geo = requests.get(url)
        geo.raise_for_status()  # Raise an exception for HTTP errors

        geo_data = geo.json()

        print(geo_data)  # print the obtained geographic in JSON format

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

    except requests.RequestException as e:
        print("Error occurred during HTTP request:", e)
        return "Error occurred during HTTP request. Please try again."
    except KeyError as e:
        print("KeyError occurred while parsing JSON response:", e)
        return "Error occurred while parsing JSON response. Please try again."


find_loc()
