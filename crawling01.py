import requests 
page = requests.get("https://info.cern.ch")
print(page.text)
print(page.content)

with open("info.cern.ch.html", 'w') as f:
    f.write(page.text)
    