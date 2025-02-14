from tkinter import *
from tkinter import ttk
import requests

API_KEY = "5e1ab75e94b4a0013d9d2be78bee793e"
city_name = "Bengaluru"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&UNITS=metric"
data = requests.get(url).json()

print(data)