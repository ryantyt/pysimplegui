import PySimpleGUI as sg
from time import time

sg.theme('black')

def createWindow():
    layout = [
        [sg.Push(), sg.Text('X', key='-CLOSE-', enable_events=True)],
        [sg.VPush()],
        [sg.Text('Time', key='-TIME-', font='Young 50')], 
        [
            sg.Button('Start', button_color=('#FFFFFF', '#FF0000'), border_width=0, key='-STARTSTOP-'), 
            sg.Button('Lap', button_color=('#FFFFFF', '#FF0000'), border_width=0, key='-LAP-', visible=False),
            sg.Button('Reset', button_color=('#FFFFFF', '#FF0000'), border_width=0, key='-RESET-')
            ],
        [sg.Text(key='-LAPS-')],
        [sg.VPush()]
        ]

    window = sg.Window(
        'Stopwatch', 
        layout, 
        size=(300, 300), 
        no_titlebar=True, 
        element_justification='center'
        )

    return window

window = createWindow()

stime = 0
active = False
tottime = 0
num = 1

while True:
    event, values = window.read(timeout=10)

    if event == sg.WIN_CLOSED:
        break

    if event == '-CLOSE-':
        window.close()

    if event == '-STARTSTOP-':
        if active:
            tottime += time() - stime
            active = False
            window['-LAP-'].update(visible=False)
        
        else:
            stime = time()
            active = True
            window['-LAP-'].update(visible=True)
            window['-STARTSTOP-'].update('Stop')

    if event == '-LAP-':
        window.extend_layout(window['-LAPS-'], [[sg.Text(num), sg.HSeparator(), sg.Text(round(time() - stime, 1))]])
        num += 1

    if event == '-RESET-':
        tottime = 0
        stime = 0
        num = 1
        active = False
        window.close()
        window = createWindow()

    if active:
        eltime = round(time() - stime + tottime, 1)
        window['-TIME-'].update(eltime)

window.close()