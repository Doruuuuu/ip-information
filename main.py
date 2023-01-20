import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        
        
        data = {
            '[IP]': response.get('query'),
            '[Провайдер]': response.get('isp'),
            '[Организация провайдера]': response.get('org'),
            '[Страна]': response.get('country'),
            '[Регион]': response.get('regionName'),
            '[Город]': response.get('city'),
            '[Почтовый код]': response.get('zip'),
            '[Широта]': response.get('lat'),
            '[Долгота]': response.get('lon'),
            '[Часовой пояс]': response.get('timezone'),
        }
        
        for k, v in data.items():
            print(f'{k} : {v}')
        
        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        area.save(f'{response.get("query")}_{response.get("city")}.html')
        
    except requests.exceptions.ConnectionError:
        print('[!] Пожалуйста, проверьте ваше соединение!')
        
        
def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('IP INFORMATION'))
    ip = input('Пожалуйста, введите IP-адрес: ')
    
    get_info_by_ip(ip=ip)
    
    
if __name__ == '__main__':
    main()
