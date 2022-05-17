# Author:Shirley
# Date:2022-05-16
import jsonpath
import requests

url = 'https://netease-cloud-music-api-shirley.vercel.app/search/suggest'
data = {
    "keywords": "海阔天空"
}
response = requests.post(url=url, json=data)
# print(response.text)
# print(type(response.text))
# print(response.json())
# result = response.json()
# msg_value = result['result']['albums']['name']
# print(msg_value)
# assert "true" == msg_value
value = jsonpath.jsonpath(response.json(), '$.result.albums')
# value = jsonpath.jsonpath(response.json(), '$..name')
print(value)
a=value[0][0]
print(a)
