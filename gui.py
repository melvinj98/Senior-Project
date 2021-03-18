import emotion
import PySimpleGUI as sg

theme = {'BACKGROUND': '#a8c1b4',
         'TEXT': '#2c5042',
         'INPUT': '#ffffff',
         'TEXT_INPUT': '#ffffff',
         'SCROLL': '#ffffff',
         'BUTTON': ('white', '#6d9f85'),
         'PROGRESS': ('#ffffff', '#ffffff'),
         'BORDER': '1',
         'SLIDER_DEPTH': '0',
         'PROGRESS_DEPTH': '0'
         }
sg.theme_add_new('Theme', theme)
sg.theme('Theme')
layoutFont = 'Helvetica'


def createPlaylist():
    layout = [[sg.Button("Quit")]
              ]

    window = sg.Window("Create Playlist",
                       layout,
                       element_justification='c',
                       size=(300, 200)
                       )

    while True:
        event, values = window.read()
        if event == "Quit" or event == sg.WIN_CLOSED:
            break

    window.close()


def main():
    layout = [[sg.Text("Music Player", font=(layoutFont, 14, 'bold'))],
              [sg.Button('Create Playlist', font=layoutFont)],
              [sg.Button("Settings", font=layoutFont)],
              [sg.Button("Quit", font=layoutFont)],
              ]

    # create window
    window = sg.Window("Music Player",
                       layout,
                       element_justification='c',
                       size=(1920, 1080)
                       )

    while True:
        event, values = window.read()
        if event == "Quit" or event == sg.WIN_CLOSED:
            break
        if event == "Create Playlist":
            # emotion.main()
            createPlaylist()

    window.close()


if __name__ == "__main__":
    main()

"""

import PySimpleGUI as sg


def open_window():
    layout = [[sg.Text("New Window", key="new")]]
    window = sg.Window("Second Window", layout, modal=True)
    choice = None
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()


def main():
    layout = [[sg.Button("Open Window", key="open")]]
    window = sg.Window("Main Window", layout)
    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event == "open":
            open_window()

    window.close()


if __name__ == "__main__":
    main()
"""
