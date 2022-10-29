import PySimpleGUI as sg
from io import BytesIO
from  PIL import Image
import base64
from pygame import mixer, time
mixer.init()
clock = time.Clock()

IMG_PATH = 'passport.png'
FILE_PATH = sg.popup_get_file('Open', no_window=True)
song_name = FILE_PATH.split('/')[-1].split('.')[0]
song = mixer.Sound(FILE_PATH)
playing = False

song_len = int(song.get_length())
time_ss = 0
pause_amount = 0


def b64_imgimport(path):
    image = Image.open(path)
    image = image.resize((round(image.size[0]*0.05), round(image.size[1]*0.05)))
    buffer = BytesIO()
    image.save(buffer, format='PNG')
    b64 = base64.b64encode(buffer.getvalue())
    return b64

sg.theme('reddit')

play_layout = [
    [
        sg.Text(song_name, key='SONGNAME', font='Calibri 20'), 
        sg.Push(), 
        sg.Button(image_data=b64_imgimport('passport.png'), key='PLAY', border_width=0)
        ],
    [sg.Progress(song_len, size=(80, 20), key='PROGRESS')]
]
vol_layout = [
    [sg.VPush()],
    [sg.Push(), sg.Slider(range=(0, 100), key='VOLUME', default_value=100, orientation='h'), sg.Push()],
    [sg.VPush()]
]
layout = [
    [sg.TabGroup([[
        sg.Tab('Play', play_layout), 
        sg.Tab('Volume', vol_layout)
        ]])]
]

window = sg.Window('Music Player', layout)

while True:
    event, values = window.read(timeout=1)

    if playing:
        time_ss = time.get_ticks()
        window['PROGRESS'].update((time_ss - pause_amount) // 1000)

    if event == sg.WIN_CLOSED or event == 'Escape:889192475': break

    if event == 'PLAY':
        if not playing:
            if mixer.get_busy() == False:
                song.play()
            else:
                mixer.unpause()
            playing = True
        else:
            mixer.pause()
            pause_amount += time.get_ticks() - time_ss
            playing = False

    song.set_volume(values['VOLUME']/100)


window.close()