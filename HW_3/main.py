import pyowm
from tools import logger
TOKEN = '9d62e57ada18b760c296d39a1deea438'
@logger
def get_temp(sity,TOKEN):
    """1 аргумент город формат 'london,GB
        2 аргумент токен вашего ОВМ, оставляю для вас свой.'"""
    owm = pyowm.OWM(TOKEN)
    mgr = owm.weather_manager()
    sity = mgr.weather_at_place(sity)
    w = sity.weather
    temp = w.temperature('celsius')
    return(f'температура в перми: {temp["temp"]}')




if __name__ == '__main__':
    print(get_temp('Perm,RU',TOKEN))


