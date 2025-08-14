import requests
from bs4 import BeautifulSoup as bs


url = "https://www.timeanddate.com/weather/@z-us-77954/hourly"
page = requests.get(url)
soup = bs(page.content, 'html.parser')
#print(soup.prettify())

graph = soup.find(id="wt-hbh")
times = graph.find_all("tr")
data = times[2].find("th").get_text("\n")



for slice in times:
    print(slice.text)
    print()

print('\n\n\n')
print(data)
print('\n\n\n')

