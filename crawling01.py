import requests 
page = requests.get("https://info.cern.ch")
print(page.text)
print(page.content)

