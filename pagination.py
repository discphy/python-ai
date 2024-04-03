import requests
from bs4 import BeautifulSoup

all_jobs = []

def scrape_page(url):
    print(f"Scraping url : {url}")
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser", )

    jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

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

def get_pages(url):
    response = requests.get("https://weworkremotely.com/remote-full-time-jobs?page=1")
    soup = BeautifulSoup(response.content, "html.parser")

    return len(soup.find("div", class_="pagination").find_all("span", class_="page"))

total_pages = get_pages("https://weworkremotely.com/categories/remote-full-stack-programming-jobs")

for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

print(all_jobs)