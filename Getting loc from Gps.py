import requests
import time

def fetch_location():
    while True:
        # Replace with your own concox GT 06 N API URL
        url = "http://example.com/api/v1/concox_gt06n"
        response = requests.get(url)
        data = response.json()

        # Print the location data
        print(f"Latitude: {data['latitude']}, Longitude: {data['longitude']}")

        # Sleep for a while before fetching the location again
        time.sleep(60) # 60 seconds

if __name__ == "__main__":
    fetch_location()