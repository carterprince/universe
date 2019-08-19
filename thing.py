import inspect
import random
import nameGen
from data import things

thingsDict = things.thingsDict

#every function in nameGen
nameGenFunctions = [x[0] for x in inspect.getmembers(nameGen, inspect.isfunction) if x[0] != "literal_eval" and x[0] != "getName"]

#This class describes an object, its type, its display name, and its children.
class Thing:
    def __init__(self, thingType):
        self.Contains = []
        self.Type = thingType

        if self.Type in thingsDict: #if we have created a thing for it yet
            if type(thingsDict[self.Type][0]) is str: #if it has an alias/name gen
                if thingsDict[self.Type][0] in nameGenFunctions: #if the alias has a function in the nameGen module
                    self.Name = eval("nameGen."+thingsDict[self.Type][0]+"()") #run the function, set the name to the output
                else:
                    self.Name = thingsDict[self.Type][0] #regular alias, just rename it to what's in things.json
            else: # if it does not have an alias or name generator, just use the thing's type
                self.Name = thingType
        else:
            self.Name = thingType
    def generateChildren(self):
        if self.Contains == [] or self.Name == "universe": # only generate if there's nothing in the object
            try:
                for potentialChild in thingsDict[self.Type]: #for every contituient of a thing
                    if type(potentialChild) is tuple: #if the element is not for naming purposes (is an actual thing)
                        for i in range(potentialChild[1]): # run potentialChild[1] times
                            if random.random() < potentialChild[2]:
                                self.Contains.append(Thing(potentialChild[0])) #add the thing to its parent
            except KeyError:
                self.Contains.append(Thing("wip"))
    def view(self):
        print("\n- "+self.Name)
        for i, child in enumerate(self.Contains):
            if child.Type.endswith("-thought"):
                print("       - "+child.Name)
            else:
                print("   + "+str(i+1)+" - "+child.Name)