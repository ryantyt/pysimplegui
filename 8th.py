import PySimpleGUI as sg
from io import BytesIO
from PIL import Image, ImageFilter, ImageOps

# pil_img = Image.open('passport.jpg')
# pil_img.save('passport.png')

def update_img(original, blur, contrast, emboss, contour, flipx, flipy):
    global image
    image = original.filter(ImageFilter.GaussianBlur(blur))
    image = image.filter(ImageFilter.UnsharpMask(contrast))

    if emboss:
        image = image.filter(ImageFilter.EMBOSS())
    if contour:
        image.filter(ImageFilter.CONTOUR())
    if flipx:
        image = ImageOps.mirror(image)
    if flipy:
        image = ImageOps.mirror(image)

    bio = BytesIO()
    image.save(bio, format='PNG')
    window['-IMAGE-'].update(data=bio.getvalue())

IMG_PATH  = sg.popup_get_file('Open', no_window=True)

sg.theme('dark')

control_col = sg.Column([
    [
        sg.Frame('Blur', layout=[[sg.Slider(range=(-10, 10), orientation='h', key='-BLUR-', default_value=0)]])
        ],
    [
        sg.Frame('Contrast', layout=[[sg.Slider(range=(-10, 10), orientation='h', key='-CONTRAST-', default_value=0)]])
        ],
    [
        sg.Checkbox('Emboss', key='-EMBOSS-'), 
        sg.Checkbox('Contour', key='-CONTOUR-')
        ],
    [
        sg.Checkbox('Flip X', key='-FLIPX-'), 
        sg.Checkbox('Flip Y', key='-FLIPY-')
        ],
    [sg.Button('Save', key='-SAVE-')],    
])
img_col = sg.Column([[sg.Image(IMG_PATH, key='-IMAGE-')]])
layout = [
    [
        control_col,
        img_col
    ]
]

original = Image.open(IMG_PATH)
window = sg.Window('Editor', layout, return_keyboard_events=True)

while True:
    event, values = window.read(timeout=5)

    if event == sg.WIN_CLOSED or event == 'Escape:889192475':
        break

    if event != '__TIMEOUT__':
        print(event)

    if event == '-SAVE-':
        FILE_PATH = sg.popup_get_file('Save', save_as=True, no_window=True) + '.png'
        image.save(FILE_PATH, 'PNG')


    update_img(original, values['-BLUR-'], values['-CONTRAST-'], values['-EMBOSS-'], values['-CONTOUR-'], values['-FLIPX-'], values['-FLIPY-'])


window.close()