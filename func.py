from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import time

def find_job1(search_skill,unfamiliar_skill):
    print(f"Fetching the results for {search_skill}...")
    url = f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={search_skill}&txtLocation='
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")
    
    print(f"Filtering the results for unfamiliar skills...")
    for job in jobs:
        published_date = job.find('span', class_ = "sim-posted").span.text
        if 'few' in published_date:
             company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','').strip()
             skills = list(job.find('span', class_ = "srp-skills").text.replace(' ','').strip().split(','))
             more_info = job.header.h2.a['href']
             if(all(x not in skills for x in unfamiliar_skill)): 
                 with open('jobs_list.txt','a') as f:
                    f.write(f'Company Name: {company_name}\n')
                    f.write(f'Skills: {skills}\n')
                    f.write(f'More info: {more_info}\n')
                    f.write('\n\n')
    print(f"Successfully fetched results without filter...")
    
    
def find_job2(known,unknown):
    driver = webdriver.Chrome("/Users/sham/chromedriver/chrome_driver") #Enter the path to chromedrive in your local system
    url = f"https://www.naukri.com/{known}-jobs?"
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source,'lxml')
    print(soup.prettify())
    driver.close()
    # job = soup.find('article', class_ = "jobTuple")
    
    
    
def find_job3(known,unknown):
    driver = webdriver.Chrome("/Users/sham/chromedriver/chrome_driver") #Enter the path to chromedrive in your local system
    url = f"https://in.indeed.com/jobs?q={known}&l=&from=searchOnHP"
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source,'lxml')
    print(soup.prettify())
    driver.close()
    
