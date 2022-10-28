import PySimpleGUI as sg
from pathlib import Path

smileys = [
    'happy',[':)','xD',':D','<3'],
    'sad',[':(','T_T'],
    'other',[':3']
]
smiley_events = smileys[1] + smileys[3] + smileys[5]

menu_layout = [
    ['File', ['Open', 'Save', '---', 'Exit']],
    ['Tools', ['Word Count']],
    ['Others', [smileys]]
]

layout = [
    [sg.Menu(menu_layout)],
    [sg.Text('Untitled', key='-DOCNAME-'), sg.Push(), sg.Text('X', enable_events=True, key='-CLOSE-')],
    [sg.Multiline(no_scrollbar=True, size = (40, 30), key='-TEXT-')]
]

def createWindow():
    window = sg.Window('Text Editor', layout)
    return window

window = createWindow()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break

    if event == 'Open':
        FILE_PATH = sg.popup_get_file('open', no_window=True)
        if FILE_PATH:
            file = Path(FILE_PATH)
            window['-TEXT-'].update(file.read_text())
            window['-DOCNAME-'].update(FILE_PATH.split('/')[-1])

    if event == 'Save':
        FILE_PATH = sg.popup_get_file('Save as', no_window=True, save_as=True)
        file = Path(FILE_PATH)
        file.write_text(values['-TEXT-'])
        window['-DOCNAME-'].update(FILE_PATH.split('/')[-1])

    if event == '-CLOSE-':
        window.close()

    if event == 'Word Count':
        full_text = values['-TEXT-']
        cleaned_text = ' '.join(values['-TEXT-'].split()).replace('\n', ' ').split(' ')
        
        word_count = len(cleaned_text)
        char_count = len(''.join(full_text))

        sg.popup(f'Word Count: {word_count}\nCharacter Count: {char_count}')
    
    if event in smiley_events:
        current_text = values['-TEXT-']
        new_text = current_text + ' ' + event
        window['-TEXT-'].update(new_text)


        


window.close()