import sys
from traceback import print_tb, extract_tb, format_list

def printError():
    error = sys.exc_info()
    type = error[0]#tipo do erro
    print('\n'+'Type: \n'+type.__name__+'\n')
    value = error[1] # valor do erro
    print('Value: \n'+str(error[1])+'\n')
    tb=error[2]
    print('Traceback:')
    e_tb=extract_tb(tb)
    f_l=format_list(e_tb)#traceback em forma de lista para futuro usos
    print_tb(tb)

def checkType(nameType,object):
    n_o=object.__class__.__name__
    if n_o != nameType:
        raise TypeError('wrong DAO for class:'+n_o)

def changeEditedAttr(obj,editedObj):
    diEditedObj=editedObj.__dict__
    diEditedObj={key : diEditedObj[key] for key in  diEditedObj if key != '_sa_instance_state'}
    dicObj=obj.__dict__
    dicObj={key : dicObj[key] for key in  dicObj if key != '_sa_instance_state'}
    for i in dicObj:
        if (i in diEditedObj) and (dicObj[i] != diEditedObj[i]) and diEditedObj[i] != None:
            setattr(obj, i, diEditedObj[i])
    return obj
