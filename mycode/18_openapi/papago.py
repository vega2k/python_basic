
import os
import sys
import urllib.request

client_id = "tUWdL7TJkF_3BiyMxvzL"
client_secret = "pIfZknRbul"
myText = str(input("번역할 글을 입력하세요"))
print(myText)
encText = urllib.parse.quote(myText)

data = "source=ko&target=en&text=" + encText
//url = "https://openapi.naver.com/v1/language/translate"
url = "https://openapi.naver.com/v1/papago/n2mt"
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request, data=data.encode("utf-8"))
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)