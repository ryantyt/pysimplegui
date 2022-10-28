import PySimpleGUI as sg

layout = [[]]

window = sg.Window('Graphing', layout)

while True:
    event, value = window.read()

    if event == sg.WIN_CLOSED: break

window.close()
