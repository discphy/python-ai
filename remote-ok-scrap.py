import requests
from bs4 import BeautifulSoup

keywords = ["flutter", "python", "golang"]

response = requests.get("https://remoteok.com/remote-flutter-jobs", headers={
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
})

print(response.status_code)

# TODO : code challenge OOP
