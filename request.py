import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Beds':3, 'Bath':2, 'Sqft':2000})

print(r.json())