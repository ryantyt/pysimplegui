import PySimpleGUI as sg
import cv2

layout = [
    [sg.Image(key='IMAGE')],
    [sg.Text('People: 0', key='TEXT', expand_x=True, justification='c', font='Calibri 20')]
]

window = sg.Window('Face detection', layout, return_keyboard_events=True)

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



while True:
    event, values = window.read(timeout=0)
    if event == sg.WIN_CLOSED or event == 'Escape:889192475': break

    if event != '__TIMEOUT__':
        print(event)

    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(grey, scaleFactor=1.3, minNeighbors=7, minSize=(50 ,50))

    for (x, y, w, h) in face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (251,72,196), 10)

    img = cv2.imencode('.png', frame)[1].tobytes()
    window['IMAGE'].update(data=img)
    window['TEXT'].update(f'People: {len(face)}')

window.close()
cv2.destroyAllWindows()