import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}

def extract_jobs(url):
    jobs = []
    print("Scrapping REMOTE Page")
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.text, "html.parser")
    results = soup.find_all("tr", class_="job")
    for result in results:
      job_href = result.find("a", class_="no-border tooltip")
      if job_href :
        title = result.find("h2", itemprop="title")
        if title == None:
          title = "None"
        else :
          title = title.get_text(strip=True)
        
        company = result.find("h3", itemprop="name")
        if company == None:
          company = "None"
        else:
          company = company.get_text(strip=True)
        
        location = result.find("div", class_="location")
        if location == None:
          location = "None"
        else:
          location = location.get_text(strip=True)
        
        job_href = job_href["href"]

        job = {
            "site" : "remoteok",
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
