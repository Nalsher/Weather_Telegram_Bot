import requests as rq
import json


def Get_W_Api(Cityname: str) -> dict :
    Weather_info = rq.get(f'https://api.openweathermap.org/data/2.5/weather?q={Cityname}&appid=30a5757fefcf337a0188a9403227b799&units=metric&lang=ru')
    return Weather_info.json()


class Parse_data():
    def __init__(self,Weather_inf):
        self.Weather_inf = Weather_inf

    def check(self):
        if self.Weather_inf['cod'] == '404':
            return False
        else:
            return True
    def Get_Weather_temperature(self) -> float:
        temp = self.Weather_inf['main']['temp']
        return temp
    def Get_Weather_descrip(self) -> str:
        descrip = self.Weather_inf['weather']
        descrip = descrip[0]

        return descrip['description']

