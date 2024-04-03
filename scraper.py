import requests
from bs4 import BeautifulSoup

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser", )

jobs = soup.find("section", id="category-2").find_all("li")[1:-1]

all_jobs = []

for job in jobs:
    title = job.find("span", class_="title").text
    url = job.find("a")["href"]

    company, position, region = job.find_all("span", class_="company")

    jobs = {
        "title": title,
        "company": company.text,
        "position": position.text,
        "region": region.text,
        "url": url
    }

    all_jobs.append(jobs)

print(all_jobs)
