import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup as bs

app = Flask(__name__)

zip = "77954" #input("what zipcode?: ") 

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

info = {
    "dateTime" : dateTime.strip(),
    "temp" : temp.strip(),
    "weather" : weather.strip(),
    "feels" : feels.strip(),
    "wind" : wind.strip(),
    "humid":humid.strip(),
    "rain":rain.strip()
}
    

print()
print('date: '+dateTime.strip())
print('temp: '+temp.strip())
print('weather: '+ weather.strip())
print('feels like: '+feels.strip())
print('wind: '+wind.strip())
print('humidity: '+ humid.strip())
print('chance of rain: ' + rain.strip())
print('\n\n\n\n')
print(info)


@app.route("/", methods=["GET","POST"])
def index():
    return render_template("index.html", info = info)

if __name__ == "__main__":  
   app.run(debug=True)

