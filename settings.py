def getSettings():
    f = open("settings.txt", "r")
    list_of_lines = f.readlines()
    try:
        cameraSetting = list_of_lines[0]
        userID = list_of_lines[1]
        authKey = list_of_lines[2]
    except IndexError:
        f = open("settings.txt", "w")

        # default settings values
        defaultSettings = ['1\n', 'Spotify User ID\n', 'Spotify Authorization Token\n']

        f.writelines(defaultSettings)
        f.close()

        f = open("settings.txt", "r")
        list_of_lines = f.readlines()
        cameraSetting = list_of_lines[0]
        userID = list_of_lines[1]
        authKey = list_of_lines[2]

    return cameraSetting, userID, authKey


def changeSettings(newCameraValue, newUserID, newAuthKey):
    f = open("settings.txt", "r")
    list_of_lines = f.readlines()

    if list_of_lines[0] != newCameraValue:
        list_of_lines[0] = newCameraValue + '\n'
    if list_of_lines[1] != newUserID:
        list_of_lines[1] = newUserID + '\n'
    if list_of_lines[2] != newAuthKey:
        list_of_lines[2] = newAuthKey + '\n'

    f = open("settings.txt", "w")
    f.writelines(list_of_lines)
    f.close()