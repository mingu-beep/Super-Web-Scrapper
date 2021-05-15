import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_job(html):
  job_href = html.find("a", class_="no-border tooltip")
  if job_href :
    title = html.find("h2", itemprop="title").get_text()
    company = html.find("h3", itemprop="name").get_text()
    location = html.find("div", class_="location").get_text()
    job_href = job_href["href"]

    return {
        "title": title,
        "company": company,
        "location": location,
        "link": f"https://remoteok.io/{job_href}"
    }

def extract_jobs(url):
    jobs = []
    print("Scrapping REMOTE Page")
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("tr", class_="job")
    for result in results:
      job_href = result.find("a", class_="no-border tooltip")
      if job_href :
        title = result.find("h2", itemprop="title").get_text()
        company = result.find("h3", itemprop="name").get_text()
        location = result.find("div", class_="location").get_text()
        job_href = job_href["href"]

        job = {
            "title": title,
            "company": company,
            "location": location,
            "link": f"https://remoteok.io/{job_href}"
        }
        jobs.append(job)
    return jobs

def get_remote_jobs(word):
    url = f"https://remoteok.io/remote-{word}-jobs"
    jobs = extract_jobs(url)
    return jobs
