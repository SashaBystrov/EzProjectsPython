import requests
url = 'https://youtu.be/bCazNDPcCWI'
r = requests.get(url)
with open('/Users/De1pl/Downloads/cat3.wmv', 'wb') as f:
    f.write(r.content)
print(r.status_code)
print(r.headers['content-type'])
print(r.encoding)

