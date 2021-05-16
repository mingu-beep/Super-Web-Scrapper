import requests
from bs4 import BeautifulSoup

def extract_job(html):
    title = html.find("span", class_= "title")
    if title == None:
      title = "None"
    else :
      title = title.get_text(strip=True)
      
    company = html.find("span", class_= "company")
    if company == None:
      company = "None"
    else :
      company = company.get_text(strip=True)

    location = html.find("span", class_="region")
    if location == None:
      location = "None"
    else :
      location = location.get_text(strip=True)

    link = html.find_all("a")[1]["href"]

    return {
        "site": "wework",
        "title": title,
        "company": company,
        "location": location,
        "link": link
    }

def extract_jobs(url):
    jobs = []
    
    print(f"Scrapping WEWORK Page")
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
