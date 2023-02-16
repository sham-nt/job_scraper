# Job listings Web-scrapper 
                  using Python, BeautifulSoup4
---
## About
The internet is filled with sites with many job hunting sites, and many of them contain a lot of fluff which is not relevant to the average job-seeker
... so, I am building this project to scrape few popular job listing sites to get their combined jobs 

Initially i will be scrapping the 3 sites
* TimesJobs.com
* Naukri.com
* Indeed.com

![Screenshot 2023-02-15 at 9 26 19 PM](https://user-images.githubusercontent.com/90405823/219273531-83212fef-3b30-4c40-85a7-416e2412def5.jpg)
![Screenshot 2023-02-15 at 9 42 07 PM](https://user-images.githubusercontent.com/90405823/219273536-b5dd6c10-0789-47db-9af8-8bebb86f25f6.jpg)
![times_jobs](https://user-images.githubusercontent.com/90405823/219273537-6a1ed751-a8bc-4cbd-a087-05b062493388.jpg)

---
## Dependancies

If u want to setup this project in your local system

1) Install or update the following libraries

                      pip install beautifulsoup4
                      pip install lxml
                      pip install requests
                      pip install selenium
                      
2) Download the chrome driver specific to your system at https://chromedriver.chromium.org/ , and store it in a easily accessable path
3) replace the chrome_drive path in the func.py 
4) execute **main.py**
5) Enjoy 😁

---
## Roadmap to project

1) Build initial implementation for **Timesjobs.com**  ✅
2) complete the implementation of **Naukri.com** and **indeed.com**
3) Store the scrapped data in a database
4) build a front end for viewing the data 
5) fetch the data to the front end in realtime
 
---
