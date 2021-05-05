def getCameraSetting():
    f = open("settings.txt", "r")
    list_of_lines = f.readlines()
    cameraSetting = list_of_lines[1].replace('Camera = ', '')

    return cameraSetting


def getAuthKey():
    f = open("settings.txt", "r")
    list_of_lines = f.readlines()
    authKey = list_of_lines[2].replace('Authorization Key = ', '')

    return authKey


def changeCamera(newCameraValue):
    f = open("settings.txt", "r")
    list_of_lines = f.readlines()
    list_of_lines[1] = "Camera = " + newCameraValue

    f = open("settings.txt", "w")
    f.writelines(list_of_lines)
    f.close()


def changeAuthKey(newAuthKey):
    f = open("settings.txt", "r")
    list_of_lines = f.readlines()
    list_of_lines[2] = "Authorization Key = " + newAuthKey

    f = open("settings.txt", "w")
    f.writelines(list_of_lines)
    f.close()
