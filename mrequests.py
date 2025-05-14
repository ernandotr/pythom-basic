import requests

github_url = 'https://api.github.com'
httpbin_url = 'https://httpbin.org/ip'

response = requests.get(httpbin_url)

if response.status_code == 200:
    print("API is up!")
else:
    print("API is down!")
    
print("Status Code: " + str(response.status_code))
print("Response: " + response.text)
print("Response Headers: " + str(response.headers))
print("Response Content: " + response.content.decode('utf-8'))
print("Response JSON: " + str(response.json()))
print("Response Encoding: " + response.encoding)
print("Response URL: " + response.url)
print("Response History: " + str(response.history))
print("Response Cookies: " + str(response.cookies))
print("Response Elapsed: " + str(response.elapsed))
print("Response Request: " + str(response.request))
print("Response Reason: " + response.reason)