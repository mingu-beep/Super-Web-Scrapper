import requests
from bs4 import BeautifulSoup

def extract_job(html):
    title = html.find("span", class_= "title").get_text()
    company = html.find("span", class_= "company").get_text()
    location = html.find("span", class_="region").get_text()
    link = html.find_all("a")[1]["href"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": link
    }

def extract_jobs(url):
    jobs = []
    
    print(f"Scrapping WEWORK Page: page")
    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("li", class_= "feature")
    for result in results:
        job = extract_job(result)
        jobs.append(job)
    return jobs

def get_wework_jobs(word):
    url = f"https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term={word}"
    jobs = extract_jobs(url)
    return jobs
