import PySimpleGUI as sg

w, h = 6, 3
button_size = 6, 3

sg.set_options(font='Calibri 20', button_element_size=(w, h))

theme_menu = ['menu', ['LightGray1', 'dark', 'DarkGray8', 'random']]

def createWindow(theme):
    sg.theme(theme)

    layout = [
        [sg.Text('', font='Franklin 26', justification='right', expand_x=True, pad=(10,20), right_click_menu=theme_menu, key='-OUTPUT-')],
        [sg.Button('Clear', expand_x=True), sg.Button('Enter', expand_x=True)],
        [sg.Button(7, size=button_size), sg.Button(8, size=button_size), sg.Button(9, size=button_size), sg.Button('+', size=button_size)],
        [sg.Button(4, size=button_size), sg.Button(5, size=button_size), sg.Button(6, size=button_size), sg.Button('-', size=button_size)],
        [sg.Button(1, size=button_size), sg.Button(2, size=button_size), sg.Button(3, size=button_size), sg.Button('*', size=button_size)],
        [sg.Button('', size=button_size), sg.Button(0, size=button_size), sg.Button('**', size=button_size), sg.Button('/', size=button_size)]
    ]

    return sg.Window('Calculator', layout)

curNum = []
ope = []

window = createWindow(theme_menu[1][0])

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    if event in theme_menu[1]:
        window.close()
        window = createWindow(event)

    if event in ['0','1','2','3','4','5','6','7','8','9','.']:
        curNum.append(event)
        numstr = ''.join(curNum)
        window['-OUTPUT-'].update(numstr)

    if event in ['+','-','/','*', '**']:
        ope.append(''.join(curNum))
        curNum = []
        ope.append(event)
        window['-OUTPUT-'].update('')
        print(ope)

    if event == 'Enter':
        ope.append(''.join(curNum))
        result = eval(' '.join(ope))
        window['-OUTPUT-'].update(result)
        ope = []

    if event == 'Clear':
        curNum = []
        window['-OUTPUT-'].update('')

window.close()