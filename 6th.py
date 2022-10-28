import PySimpleGUI as sg
from time import time
import random


FIELD_SIZE = 400
CELL_NUM = 20
CELL_SIZE = FIELD_SIZE / CELL_NUM

score = 0

apple_pos = random.randint(0, 19), random.randint(0, 19)
edges = [0, 20]
highscore = 0

DIRECTIONS = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
snake_body = [(10, 10), (9, 10), (8, 10)]
directions = DIRECTIONS['right']
pause = True

def pos_con(coords):
    t1 = coords[0] * CELL_SIZE, coords[1] * CELL_SIZE
    t2 = t1[0] + CELL_SIZE, t1[1] + CELL_SIZE
    return t1, t2

sg.theme='LightGray1'

field = sg.Graph(
    canvas_size = (FIELD_SIZE, FIELD_SIZE),
    graph_bottom_left = (0, 0),
    graph_top_right = (FIELD_SIZE, FIELD_SIZE),
    background_color='black'
)

layout = [
    [
        sg.Text(f'Score: {score}', key='-SCORE-', font='Calbri 20'), 
        sg.Button('START', key='-START-', visible=True),
        sg.Push(),
        sg.Text(f'Highscore: {highscore}', key='-HSCORE-', font='Calibri 20'),
        sg.Text('X', key='-CLOSE-', enable_events=True, font='Calibri 20', text_color='red')
    ],
    [field]
]

window = sg.Window('Snake', layout, return_keyboard_events=True)

start_time = time()
while True:
    event, values = window.read(timeout=1) 

    # Closing
    if event == sg.WIN_CLOSED: break
    if event == '-CLOSE-': window.close()

    # Controls
    if event == '-START-':
        pause = not pause
        if not pause:
            window['-START-'].update('STOP')
        else:
            window['-START-'].update('START')
    if event == 'Left:2063660802' and directions != DIRECTIONS['right']: directions = DIRECTIONS['left']
    if event == 'Up:2113992448' and directions != DIRECTIONS['down']: directions = DIRECTIONS['up']
    if event == 'Right:2080438019' and directions != DIRECTIONS['left']: directions = DIRECTIONS['right']
    if event == 'Down:2097215233' and directions != DIRECTIONS['up']: directions = DIRECTIONS['down']
    if event == 'Escape:889192475': 
        pause = not pause

    if not pause:
        time_ss = time() - start_time
        if time_ss >= 0.1:
            start_time = time()
            
            # Updating snake
            new_head = (snake_body[0][0] + directions[0], snake_body[0][1] + directions[1])
            snake_body.insert(0, new_head)
            snake_body.pop()

            # Scoring
            if snake_body[0] == apple_pos:
                score +=1  
                apple_pos = (random.randint(0, 19), random.randint(0, 19))
                window['-SCORE-'].update(score)
                snake_body.append((snake_body[-1][0] - directions[0], snake_body[-1][1] - directions[1]))

            # Refreshing Field
            field.DrawRectangle((0, 0), (FIELD_SIZE, FIELD_SIZE), 'black')

            # Drawing
            t1, t2 = pos_con(apple_pos)
            field.DrawRectangle(t1, t2, 'red')  

            for index, part in enumerate(snake_body):
                t1, t2 = pos_con(part)
                colour = 'yellow' if index == 0 else 'green'
                field.DrawRectangle(t1, t2, colour)

            # Losing
            if snake_body[0][0] in edges or snake_body[0][1] in edges:
                highscore = max(score, highscore)
                score = 0
                snake_body = [(10, 10), (9, 10), (8, 10)]
                direction = DIRECTIONS['right']
                pause = True
                window['-START-'].update('START')
                window['-SCORE-'].update(f'Score: {score}')
                window['-HSCORE-'].update(f'Highscore: {highscore}')
                apple_pos = (random.randint(0, 19), random.randint(0, 19))

            print(snake_body[0])


    if event != '__TIMEOUT__':
        print(event)
    
window.close()
