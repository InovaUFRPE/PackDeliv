def printError():
    error = sys.exc_info()
    type = error[0]#tipo do erro
    print(type.__name__)
    value = error[1] # valor do erro
    print(error[1])
    traceback=error[2]#aprender a usar esse objeto