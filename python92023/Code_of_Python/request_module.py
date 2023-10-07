import requests
from bs4 import BeautifulSoup
respose=requests.get("https://www.codewithharry.com/tutorial/python/")
# print(respose.text) 
'''url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": 'ajay',
    "body": 'bhai',
    "userId": 102,
}

headers = {
    "Content-type": "application/json; charset=UTF-8",
}

response = requests.post(url, headers=headers, json=data)

print(response.text)'''
soup=BeautifulSoup(respose.text,"html.parser")

# print(soup.prettify())
for heading in soup.find_all("div"):
    print(heading.text)