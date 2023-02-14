'''
Simple webscraper for fetching jobs 
with user inputs

Created by : @sham-nt (Shamanth Kashyap)

'''
from bs4 import BeautifulSoup
import requests
import time

def find_job(search_skill,unfamiliar_skill):
    print(f"Fetching the results for {search_skill}...")
    html_text = requests.get(f'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={search_skill}&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")
    
    print(f"Filtering the results for {unfamiliar_skill}...")
    for i,job in enumarate(jobs):
        published_date = job.find('span', class_ = "sim-posted").span.text
        if 'few' in published_date:
             company_name = job.find('h3', class_ = "joblist-comp-name").text.replace(' ','').strip()
             skills = list(job.find('span', class_ = "srp-skills").text.replace(' ','').strip().split(','))
             more_info = job.header.h2.a['href']
             if unfamiliar_skill not in skills:
                 with open('jobs_list.txt','a') as f:
                    f.write(f'Company Name: {company_name}\n')
                    f.write(f'Skills: {skills}\n')
                    f.write(f'More info: {more_info}\n')
                    f.write('\n\n')
    print(f"Successfully fetched {i} results without filter...")
         
def main():
    print("Enter the Programming language or skill you are familiar with: ")
    search_skill = input('>')
    print("Enter a language or skill you are unfamiliar with to filter out: ")
    unfamiliar_skill = input('>')
    print('\n\n')
    while True:
        find_job(search_skill, unfamiliar_skill)
        time_wait = 10
        print(f"Waiting every {time_wait} minutes...")
        time.sleep(time_wait * 60)
        
        
if __name__ == '__main__':
    main()