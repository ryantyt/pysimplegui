from os import get_blocking
import PySimpleGUI as sg

layout = [
        [
            sg.Input(key='-INPUT-'), 
            sg.Spin(['min to s', 'g to kg', 'degrees to fahrenheit'], key='-CHANGE-'), 
            sg.Button('Convert', key='-CONVERT-')
        ],
        [sg.Text('Output', key='-OUTPUT-')]
    ]

window = sg.Window('Converter', layout)

def stomin(n):
    return str(n * 60) + ' seconds'

def gtokg(n):
    return str(n/1000) + 'kg'

def degtof(n):
    return str((n*9/5)+32) + 'f'

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    
    if event == '-CONVERT-':
        inputval = values['-INPUT-']
        try: 
            inputval = int(inputval)
            match values['-CHANGE-']:
                case 'min to s':
                    window['-OUTPUT-'].update(stomin(inputval))
                case 'g to kg':
                    window['-OUTPUT-'].update(gtokg(inputval))
                case 'degrees to fahrenheit':
                    window['-OUTPUT-'].update(degtof(inputval))
        except ValueError:
            pass

    

window.close()