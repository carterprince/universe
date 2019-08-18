from random import choice
from ast import literal_eval

def medievalName():
    namesJSON = open("data/medievalNames",'r').read()
    names = literal_eval(namesJSON)
    return choice(names)

def medievalNationName():
    namesJSON = open("data/medievalNationNames",'r').read()
    names = literal_eval(namesJSON)
    return "The Nation of "+choice(names)

def medievalThought():
    namesJSON = open("data/medievalThoughts",'r').read()
    names = namesJSON.split("\n")
    return choice(names)

def modernName():
    namesJSON = open("data/modernNames",'r').read()
    names = literal_eval(namesJSON)
    return choice(names)
