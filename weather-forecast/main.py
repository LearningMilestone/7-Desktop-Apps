import tkinter
from tkinter import BOTH,IntVar
import requests

#define root
root=tkinter.Tk()
root.title("weather forecast")
root.geometry("400x400")
root.resizable(0,0)

#Define fonts and colors
sky_color = "#76c3ef"
grass_color = "#aad207"
output_color = "#dcf0fb"
input_color = "#ecf2ae"
large_font = ('SimSun', 14)
small_font = ('Simsun', 10)

#Define functions
def search():
    '''Use open weather api to look up current weather given a city'''
    global response
    #Get API response
    #URL and my api key.
    #https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
    url="https://api.openweathermap.org/data/2.5/weather"
    api_key="839466faa5bab3be19b3f4c98c62432c"

    #Search by approprite quety, by city name or zip code
    if search_method.get()==1:
        queryString={"q":city_entry.get(),"appid":api_key}
    elif search_method.get()==2:
        queryString={"zip":city_entry.get(),"appid":api_key}
    #call api
    response=requests.request("GET",url=url,params=queryString)
    response=response.json()
    print(response)
    #sample response
    '''{'coord': {'lon': 55.3047, 'lat': 25.2582}, 'weather': [{'id': 800, 'main': 'Clear', 'description': 'clear sky', 'icon': '01d'}], 'base': 'stations', 
    'main': {'temp': 309.38, 'feels_like': 306.71, 'temp_min': 308.31, 'temp_max': 310.29, 'pressure': 1008, 'humidity': 12}, 
    'visibility': 10000, 'wind': {'speed': 2.57, 'deg': 120}, 
    'clouds': {'all': 0}, 'dt': 1650529076, 
    'sys': {'type': 1, 'id': 7537, 'country': 'AE', 'sunrise': 1650505858, 'sunset': 1650552224}, 
    'timezone': 14400, 'id': 292223, 'name': 'Dubai', 'cod': 200}'''

    #call get_weather function
    get_weather()

def get_weather():
    '''get data from api response and update weather label '''
    #gather the data to be used from api response
    city_name=response['name']
    city_lat=str(response['coord']['lat'])
    city_lon=str(response['coord']['lon'])
    main_weather=response['weather'][0]['main']
    description=response['weather'][0]['description']
    temp=str(response['main']['temp'])
    feels_like=str(response['main']['feels_like'])
    temp_min=str(response['main']['temp_min'])
    temp_max=str(response['main']['temp_max'])
    humidity=str(response['main']['humidity'])

    #Update output labels
    city_info_label.config(text=city_name + "(" + city_lat + ", " + city_lon + ")",
                           font=large_font, bg=output_color)
    weather_label.config(text="Weather: " + main_weather + ", " + description,
                         font=small_font, bg=output_color)
    temp_label.config(text='Temperature: ' + temp + " F", font=small_font,
                      bg=output_color)
    feels_label.config(text="Feels Like: " + feels_like + " F", font=small_font,
                       bg=output_color)
    temp_min_label.config(text="Min Temperature: " + temp_min + " F", font=small_font,
                          bg=output_color)
    temp_max_label.config(text="Max Temperature: " + temp_max + " F", font=small_font,
                          bg=output_color)
    humidity_label.config(text="Humidity: " + humidity, font=small_font, bg=output_color)



#Define layout
#create frames
sky_frame=tkinter.Frame(root,bg=sky_color,height=250)
grass_frame=tkinter.Frame(root,bg=grass_color)
sky_frame.pack(fill=BOTH,expand=True)
grass_frame.pack(fill=BOTH,expand=True)

output_frame=tkinter.LabelFrame(sky_frame,bg=output_color,width=325,height=225)
input_frame=tkinter.LabelFrame(grass_frame,bg=input_color,width=325)
output_frame.pack(pady=30)
output_frame.pack_propagate(0)
input_frame.pack(pady=15)

#output frame layout
city_info_label=tkinter.Label(output_frame,bg=output_color,text="Test")
weather_label=tkinter.Label(output_frame,bg=output_color,text="Testing")
temp_label=tkinter.Label(output_frame,bg=output_color,text="Testing")
feels_label=tkinter.Label(output_frame,bg=output_color,text="Testing")
temp_min_label=tkinter.Label(output_frame,bg=output_color,text="Testing")
temp_max_label=tkinter.Label(output_frame,bg=output_color,text="Testing")
humidity_label=tkinter.Label(output_frame,bg=output_color,text="Testing")
photo_label=tkinter.Label(output_frame,bg=output_color,text="Testing")


city_info_label.pack()
weather_label.pack()
temp_label.pack()
feels_label.pack()
temp_min_label.pack()
temp_max_label.pack()
humidity_label.pack()
photo_label.pack()

#input_frame layout
search_method=IntVar()
search_method.set(1)

city_entry=tkinter.Entry(input_frame,width=20,font=large_font)
submit_btn=tkinter.Button(input_frame,text="Submit",font=small_font,command=search)
search_by_city=tkinter.Radiobutton(input_frame,text="Search by city name",variable=search_method,value=1,font=small_font)
search_by_zip=tkinter.Radiobutton(input_frame,text="Search by zip code",variable=search_method,value=2,font=small_font)

city_entry.grid(row=0,column=0,padx=10,pady=(10,0))
submit_btn.grid(row=0,column=1,pady=(10,0))
search_by_city.grid(row=1,column=0,pady=2)
search_by_zip.grid(row=1,column=1,pady=5,padx=(0,5))

#API - Key -Weather forecast -839466faa5bab3be19b3f4c98c62432c (from - https://home.openweathermap.or)


#main loop
root.mainloop()

