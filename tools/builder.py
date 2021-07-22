from requests_html import HTMLSession
#import requests
#from bs4 import BeautifulSoup

url = "https://dict.naver.com/linedict/#/cnen/search?query=%E8%87%B3%E5%B0%91"

""" page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

result = soup.find_all("a", class_="srchword")

for job_element in result:
    print(job_element) """


session = HTMLSession()
r = session.get(url)

r.html.render()

print(r.html.links)
