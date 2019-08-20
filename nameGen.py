from random import choice
from random import randint

#This file generates names/sentences for people and things that are not generally one specific word. (Ex: Contries, People, Thoughts)

#Biology stuff

from colorama import Fore

def DNAContents():
    dna = ""
    for i in range(5):
        for j in range(10):
            dna += choice(['C', 'G', 'A', 'T'])
        dna += "\n"
    return Fore.RED+dna.strip("\n")+Fore.WHITE

#MEDIEVAL STUFF
def medievalName():
    fileContent = open("data/medieval/names",'r').read()
    fileList = fileContent.split("\n")
    return choice(fileList)

def medievalNationName():
    fileContent = open("data/medieval/nationNames",'r').read()
    fileList = fileContent.split("\n")
    return Fore.LIGHTRED_EX+choice(fileList)+Fore.WHITE

def medievalSerfThought():
    fileContent = open("data/medieval/serfThoughts",'r').read()
    fileList = fileContent.split("\n")
    return choice(fileList)

def medievalMerchantThought():
    fileContent = open("data/medieval/merchantThoughts",'r').read()
    fileList = fileContent.split("\n")
    return choice(fileList)

def medievalBureaucratThought():
    fileContent = open("data/medieval/bureaucratThoughts",'r').read()
    fileList = fileContent.split("\n")
    return choice(fileList)

def medievalFarmerThought():
    fileContent = open("data/medieval/farmerThoughts",'r').read()
    fileList = fileContent.split("\n")
    return choice(fileList)

def medievalNobleThought():
    fileContent = open("data/medieval/nobleThoughts",'r').read()
    fileList = fileContent.split("\n")
    return choice(fileList)

def medievalBureaucratThought():
    fileContent = open("data/medieval/bureaucratThoughts",'r').read()
    fileList = fileContent.split("\n")
    return choice(fileList)

def medievalKingThought():
    fileContent = open("data/medieval/kingThoughts",'r').read()
    fileList = fileContent.split("\n")
    return choice(fileList)

def medievalSerfName():
    return medievalName() + " (serf)"

def medievalMerchantName():
    return medievalName() + " (merchant)"

def medievalBureaucratName():
    return medievalName() + " (bureaucrat)"

def medievalFarmerName():
    return medievalName() + " (farmer)"

def medievalNobleName():
    return medievalName() + " (noble)"

def medievalKingName():
    fileContent = open("data/medieval/kingNames",'r').read()
    fileList = fileContent.split("\n")
    return "King "+choice(fileList)+" the "+str(randint(4,10))+"th"

#MODERN STUFF

def modernName():
    fileContent = open("data/modern/names",'r').read()
    fileList = fileContent.split("\n")
    return choice(fileList)
def modernNationName():
    fileContent = open("data/modern/nationNames",'r').read()
    fileList = fileContent.split("\n")
    return Fore.LIGHTRED_EX+"The Nation of "+choice(fileList)+Fore.WHITE

def modernHoboThought():
    fileContent = open("data/modern/hoboThoughts",'r').read()
    fileList = fileContent.split("\n")
    return choice(fileList)

def modernHoboName():
    return modernName() + " (hobo)"