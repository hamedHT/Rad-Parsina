import requests

r = requests.get("http://api.navasan.tech/latest/?api_key=freez49EqZxOFruGQJWKAyJp1VO298tX")
print(r.status_code)
data = r.json()

print(data['sekkeh']['value'])


#freez49EqZxOFruGQJWKAyJp1VO298tX 