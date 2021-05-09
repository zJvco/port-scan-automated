import PySimpleGUI as sg
import defs
    
layout = [
    [sg.Text(text="DIGITE A URL ABAIXO", background_color="#2C2C2C", pad=(170, 5))],
    [sg.Input(key="-INPUT-", size=(100, 10), justification="center")],
    [sg.Button(button_text="VERIFICAR", key="button1", pad=(200, 10))],
    [sg.Output(size=(100, 100), background_color='#1A1A1A', text_color='#1ABC9C', key="-OUTPUT-")]
]

window = sg.Window("Cherub Scanner", layout, size=(500, 500), background_color="#2C2C2C", font="Helvetica, 10")

defs.main(window, sg)