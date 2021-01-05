import requests
import pprint

headers = {
    'X-Naver-Client-Id': 'TVcdGN3l5f8ZIswuZ4tX',
    'X-Naver-Client-Secret': '4F9aWQDSdZ',
}

payload = {
    'query': '파이썬',
    'display': 100
}

url = 'https://openapi.naver.com/v1/search/blog'

res = requests.get(url, headers=headers, params=payload)
res_json = res.json()

#pprint.pprint(res_json)

#print(res_json['items'][0]['bloggername'])

items_list = list()
item_list = []
for item in res_json['items']:
    #print(item)
    item_list.append(item['title'])
    item_list.append(item['bloggername'])
    item_list.append(item['description'])
    item_list.append(item['bloggerlink'])
    item_list.append(item['link'])

    items_list.append(item_list)
    item_list = []

print(items_list)