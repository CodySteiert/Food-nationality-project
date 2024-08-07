# Food api
import requests

# Define the endpoint
endpoint = 'https://www.themealdb.com/api/json/v1/1/search.php?f=a'

# Make the request
response = requests.get(endpoint)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
