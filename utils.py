def generate_maps_link(location):
    base_url = "https://www.google.com/maps/search/"
    return base_url + location.replace(" ", "+")