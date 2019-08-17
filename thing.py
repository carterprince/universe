from ast import literal_eval
thingsJSON = open("things.json",'r').read()
thingsDict = literal_eval(thingsJSON)

import random
import nameGen

class Thing:
    def __init__(self, type):
        self.Contains = []
        self.Type = type

        self.Name = nameGen.getName(type)
    def generateChildren(self):
        if self.Contains == [] or self.Name == "universe":
            try:
                for potentialChild in thingsDict[self.Type]:
                    for i in range(potentialChild[1]):
                        if random.random() < potentialChild[2]:
                            self.Contains.append(Thing(potentialChild[0]))
            except KeyError:
                self.Contains.append(Thing("WORK IN PROGRESS"))
    def view(self):
        print("\n- "+self.Name)
        for i, child in enumerate(self.Contains):
            if child.Type == "medieval-thought":
                print("       - "+child.Name)
            else:
                print("   + "+str(i+1)+" - "+child.Name)
