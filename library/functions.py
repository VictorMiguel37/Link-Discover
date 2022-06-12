def showArray(array):
    for i in range(0, len(array)):
        print(array[i])

def show(what, array, firstMessage, finalMessage):  
    print(firstMessage)

    if what:
        if len(array) == 0:
            print('Nenhum.')
        else:
            showArray(array)

    print(finalMessage)

def switchBool(value):
    match value:
        case True:
            return False
        case False:
            return True
        case _:
            return None
