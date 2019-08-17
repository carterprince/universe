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

associations = {
    "medieval-wet-planet": "wet planet with life",
    "medieval-continent": "inhabited continent",
    "medieval-head": "head",
    "medieval-attire": "clothing",
    "medieval-building": "building",
    "medieval-civilization": "civilization",
    "medieval-capital": "capital city",
    "medieval-town": "town",
    "medieval-city": "city",
    "medieval-government-building": "government building",
    "medieval-house": "house",
    "medieval-farm": "farm",
    "medieval-person": medievalName,
    "medieval-nation": medievalNationName,
    "medieval-thought": medievalThought
}

#Main function:
def getName(thingType):
    try:
        if type(associations[thingType]) is str:
            return associations[thingType]
        else:
            return associations[thingType]()
    except KeyError:
        return thingType
