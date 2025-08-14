import requests
from bs4 import BeautifulSoup as bs


url = "https://www.timeanddate.com/weather/@z-us-77954/hourly"
page = requests.get(url)
soup = bs(page.content, 'html.parser')
#print(soup.prettify())

graph = soup.find(id="wt-hbh")
times = graph.find_all("tr")

dateTime = times[2].find("th").get_text(" on ")  #date and time
data = times[2].find_all("td")  #breaks current data into chunks

temp = data[1].get_text()   #gets temp

weather = data[2].get_text()    #gets weather
weather = weather.removesuffix('.') 

feels = data[3].get_text()  #what it feels like outside

wind = data[4].get_text()   #wind

humid = data[6].get_text()  #humiidity

rain = data[7].get_text() #rain chance

chance = data[8]

print()
print('date: '+dateTime)
print('temp: '+temp)
print('weather: '+ weather)
print('feels like: '+feels)
print('wind: '+wind)
print('humidity: '+ humid)
print('chance of rain: ' + rain)
print()



