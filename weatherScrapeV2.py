import requests
import tkinter as tk
from bs4 import BeautifulSoup as bs

root = tk.Tk()
root.geometry("600x450")
root.title("Weather Scraper")



zip = '77954'

url = "https://www.timeanddate.com/weather/@z-us-"+zip+"/hourly"
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

#print()
#print('date: '+dateTime.strip())
#print('temp: '+temp.strip())
#print('weather: '+ weather.strip())
#print('feels like: '+feels.strip())
#print('wind: '+wind.strip())
#print('humidity: '+ humid.strip())
#print('chance of rain: ' + rain.strip())
#print('\n')
#print('Link to forecast: ' + url)

zipLabel = tk.Label(root, text=dateTime + '\n' + temp + '\n' + weather + '\n' + feels + "\n" 
                    + wind + '\n' + humid + '\n' + rain)
zipLabel.pack(pady=40)
exitButton  = tk.Button(root, text="Exit", command=root.destroy)
exitButton.pack(pady=20)


root.mainloop()