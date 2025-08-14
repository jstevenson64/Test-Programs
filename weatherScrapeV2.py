import requests
from bs4 import BeautifulSoup as bs


url = "https://www.timeanddate.com/weather/@z-us-77954"
page = requests.get(url)
soup = bs(page.content, 'html.parser')
#print(soup.prettify())
waag = soup.find(id="qlook")
cast = soup.find("div", class_="eight columns")
#print(waag.prettify())

temp= waag.find("div",class_="h2")
para = waag.find_all("p")
feels = para[1].find_all()
like = feels

print("The weather in Cuero today is: ")
print(temp.text)
print(feels[1].text.strip())
print(para[0].text.strip())


