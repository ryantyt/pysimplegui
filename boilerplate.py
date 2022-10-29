import PySimpleGUI as sg

layout = [
    []
]

window = sg.Window('Boilerplate', layout, return_keyboard_events=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Escape:889192475': break


    if event != '__TIMEOUT__':
        print(event)

window.close()

