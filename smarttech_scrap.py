from bs4 import BeautifulSoup
import requests

user_agent = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
    ]

product_links = []
r= requests.get('https://smarttechnologies.hire.trakstar.com/')

soup = BeautifulSoup(r.content, 'lxml')
job_cards = soup.find_all('div', class_='js-card list-item list-item-clickable js-careers-page-job-list-item')
jobs_list = []

if job_cards:
    for job in job_cards:
        job_info = {}  
        
        title = job.find('h3', class_='rb-h3 js-job-list-opening-name cut-text rb-text-color-primary rb-space-on-bottom-2rbpx')
        if title:
            job_info['title'] = title.text.strip()  
            
        link_tag = job.find('a')  
        if link_tag and 'href' in link_tag.attrs:  
            job_info['link'] = link_tag['href'].strip()  

        country_tag = job.find('span', attrs={'class': 'meta-job-location-country'})
        if country_tag:
            job_info['country'] = country_tag.text.strip() 
        
        jobs_list.append(job_info)

for job in jobs_list:
    print(job)