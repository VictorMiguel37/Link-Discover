def showArray(array):
    for i in range(0, len(array)):
        print(array[i])

def switchBool(value):
    match value:
        case True:
            return False
        case False:
            return True
        case _:
            return None
