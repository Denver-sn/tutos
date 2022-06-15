# > MODULE NEEDED: PySimpleGUI (pip install pysimplegui)

import PySimpleGUI as sg

sg.theme('DarkAmber') 


layout = [[sg.Text('Texte:        \n'), sg.Multiline(size=(25, 3), key='-INPUT-')],
          [sg.Text('Conversion:\n'), sg.Multiline(
              size=(25, 3), key='-OUTPUT-')],
          [sg.Button('Convertir'), sg.Button('Quitter', key='quit1')]]

layout2 = [[sg.Text('Binaire:      \n'), sg.Multiline(size=(25, 3), key='-INPUT-B')],
           [sg.Text('Conversion:\n'), sg.Multiline(
               size=(25, 3), key='-OUTPUT-B')],
           [sg.Button('Convertir', key="submit"), sg.Button('Quitter', key='quit2')]]
layout3 = [
    [sg.Text('\n\nBINARY CONVERTER\n\nDeveloper: DENVER\nVersion: 1.0 (BETA)')]
]
layout_group = [[sg.TabGroup([[sg.Tab('Texte en Binaire', layout), sg.Tab('Binaire en Texte', layout2), sg.Tab('About', layout3, element_justification='center')]])],
                ]

window = sg.Window('Binary Converter | v1.0', layout_group, icon="icon.ico")
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'quit1' or event == 'quit2':
        break
    if event == "submit":
        a_binary_string = values['-INPUT-B']
        binary_values = a_binary_string.split()
        ascii_string = ""
        for binary_value in binary_values:
            an_integer = int(binary_value, 2)
            ascii_character = chr(an_integer)
            ascii_string += ascii_character

        window['-OUTPUT-B'].update(ascii_string)
    window['-OUTPUT-'].update(' '.join(format(ord(x), 'b')
                              for x in values['-INPUT-']))


window.close()
