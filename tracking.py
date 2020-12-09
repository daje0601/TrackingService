import json
import requests
from bs4 import BeautifulSoup

headers = {
	 "Content-Type" : "application / json" ,
	 "Trackingmore-Api-Key" : "2e6f4905-ab10-4abd-8a5f-b1636127c3ae"
}

url = "https://api.trackingmore.com/v2/carriers/"
res = requests.get(url, headers=headers)
tracker = BeautifulSoup(res.text, "lxml")

dict = tracker["json_object"]
print(dict)


