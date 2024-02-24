import requests

API_KEY = "41ebe2232d376d644cec5b22de14328a"


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    # Data Processing!
    filterdata = data['list'][:days * 8]
    return filterdata
    # if view == 'Temperature':
    #     temperatures = [item['main']['temp'] for item in filterdata]
    #     return temperatures
    # if view == 'Sky':
    #     sky = [item['weather'][0]['main'] for item in filterdata]
    #     return sky

if __name__ == "__main__":
    print(get_data('Tokyo', 1, 'Sky'))
