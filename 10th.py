import PySimpleGUI as sg
from bs4 import BeautifulSoup as bs
import requests

def get_weather(location):
    url = f"https://www.google.com/search?q=weather+{ location.replace(' ', '') }"
    session = requests.Session()
    session.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.28 Safari/537.36'
    html = session.get(url)

    soup = bs(html.text, 'html.parser')
    name = soup.find('div', attrs={'id': 'wob_loc'}).text
    time = soup.find('div', attrs={'id': 'wob_dts'}).text
    weather = soup.find('span', attrs={'id': 'wob_dc'}).text
    temp = soup.find('span', attrs={'id': 'wob_tm'}).text
    return name, time, weather, temp

sg.theme('reddit')

img_col = sg.Column([
    [
        sg.Image(key='IMAGE', background_color='#FFFFFF')
    ]
])
info_col = sg.Column([
    [sg.Text('', key='LOCATION', font='Calibri 30', background_color='#FF0000', text_color='#FFFFFF', pad=0, visible=False)],
    [sg.Text('', key='TIME', font='Calibri 16', background_color='#000000', text_color='#FFFFFF', pad=0, visible=False)],
    [sg.Text('', key='TEMP', font='Calibri 16', background_color='#FFFFFF', text_color='#000000', pad=(0, 10), visible=False, justification='center')]
])
layout = [
    [
        sg.Input(expand_x=True, key='INPUT'), sg.Button('Enter', key='ENTER', border_width=0)
    ],
    [
        img_col, info_col
    ]

]

window = sg.Window('Weather App', layout, return_keyboard_events=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Escape:889192475': break
    # if event != '__TIMEOUT__': 
    #     print(event)

    if event == 'ENTER' or event == 'Return:603979789':
        name, time, weather, temp = get_weather(values['INPUT'])
        window['LOCATION'].update(name, visible=True)
        window['TIME'].update(time.split(' ')[0], visible=True)
        window['TEMP'].update(f'{temp} \u2103 ({weather})', visible=True)
        window['IMAGE'].update('passport.png')

    

window.close()