import requests

json_data = requests.get('http://www.floatrates.com/daily/idr.json')

# print(json_data.json())

# for data in json_data.json():
#     print(data)

for data in json_data.json().values():
    # print(data)
    print(data['code'])
    print(data['name'])
    print(data['date'])
    print(data['inverseRate'])