import emotion
import settings
import PySimpleGUI as sg

theme = {'BACKGROUND': '#a8c1b4',
         'TEXT': '#2c5042',
         'INPUT': '#ffffff',
         'TEXT_INPUT': '#1B1B1B',
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


def settingsMenu():
    cameraValue = settings.getCameraSetting()
    authKey = settings.getAuthKey()

    layout = [[sg.Text('Camera', font=layoutFont), sg.In(cameraValue, font=layoutFont)],
              [sg.Text('Authorization Key', font=layoutFont), sg.In(authKey, font=layoutFont)],
              [sg.Button('Save'), sg.Button('Exit')]
              ]

    window = sg.Window("Settings", layout, modal=True)

    while True:
        event, values = window.read()
        if event == 'Exit' or event == sg.WINDOW_CLOSED:
            break
        if event == 'Save':
            settings.changeCamera(values[0])
            settings.changeAuthKey(values[1])
            window.close()

    window.close()


def main():
    layout = [[sg.Text(' ')],
              [sg.Button('Create Playlist', font=layoutFont, size=(11, 1))],
              [sg.Button('Settings', font=layoutFont, size=(11, 1))],
              [sg.Button('Quit', font=layoutFont, size=(11, 1))],
              [sg.Text(' ')]
              ]

    # create window
    window = sg.Window("Music Player",
                       layout,
                       element_justification='c',
                       size=(250, 180),
                       )

    while True:
        event, values = window.read()
        if event == "Quit" or event == sg.WIN_CLOSED:
            break
        if event == "Create Playlist":
            emotion.main()
        if event == 'Settings':
            settingsMenu()

    window.close()


if __name__ == "__main__":
    main()
