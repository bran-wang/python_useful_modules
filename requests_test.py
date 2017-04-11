import requests

GIT_URL="https://github.com"
HEADERS = {'content-type': "application/json"}

response = requests.request("GET", GIT_URL)
response.raise_for_status()
print response.status_code

response = requests.request("POST", GIT_URL,
                            data=json.dumps(PAYLOAD),
                            headers=HEADERS)


