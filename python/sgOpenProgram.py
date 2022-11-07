import PySimpleGUI as sg

edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"


layout = [  
    [sg.Text('Text area', key='-TEXT-')],
    [sg.Input(key='-URL-')],
    [sg.Button('Edge'), sg.Button('Exit')]
]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Edge':
        sg.execute_command_subprocess(edge)

window.close()