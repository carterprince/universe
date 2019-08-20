import inspect
from random import random
from os import system
import nameGen
from data import things
from colorama import Fore

thingsDict = things.thingsDict

# every function in nameGen
nameGenFunctions = [
    x[0]
    for x in inspect.getmembers(nameGen, inspect.isfunction)
    if x[0] != "literal_eval" and x[0] != "getName"
]

# This class describes an object, its type, its display name, and its children.
class Thing:
    def __init__(self, thingType):
        self.Contains = []
        self.Type = thingType

        # if we have created a thing for it yet
        if self.Type in thingsDict:
            # if it has an alias/name gen
            if type(thingsDict[self.Type][0]) is str:
                # if the alias has a function in the nameGen module
                if thingsDict[self.Type][0] in nameGenFunctions:
                    # run the function, set the name to the output
                    self.Name = eval("nameGen." + thingsDict[self.Type][0] + "()")  #
                else:
                    # regular alias, just rename it to what's in things.json
                    self.Name = thingsDict[self.Type][0]
            else:  # if it does not have an alias or name generator, just use the thing's type
                self.Name = thingType
        else:
            self.Name = thingType

    def generateChildren(self):
        if (
            self.Contains == [] or self.Name == "universe"
        ):  # only generate if there's nothing in the object
            try:
                for potentialChild in thingsDict[
                    self.Type
                ]:  # for every contituient of a thing
                    if (
                        type(potentialChild) is tuple
                    ):  # if the element is not for naming purposes (is an actual thing)
                        for i in range(
                            potentialChild[1]
                        ):  # run potentialChild[1] times
                            if random() < potentialChild[2]:
                                self.Contains.append(
                                    Thing(potentialChild[0])
                                )  # add the thing to its parent
            except KeyError:
                self.Contains.append(Thing("wip"))

    def view(self):
        system("cls")
        print("Enter (H) for help.\n- " + self.Name)
        for i, child in enumerate(self.Contains):  # for every child of this node
            if child.Type in things.cannotEnter:  # if the child cannot be entered
                lines = child.Name.split("\n")
                if len(lines) > 1:  # if the line count is more than 1
                    for x, line in enumerate(lines):
                        if x == 0:  # if it's the first line
                            print("       - " + line)  # print with dash
                        else:
                            print("         " + line)  # print without dash
                else:
                    print("       - " + child.Name)
            elif child.Type.endswith("-thought"):
                print("       - " + Fore.GREEN + child.Name + Fore.WHITE)
            else:
                print(
                    "   "
                    + Fore.GREEN
                    + "+"
                    + Fore.WHITE
                    + " "
                    + Fore.CYAN
                    + str(i + 1)
                    + Fore.WHITE
                    + " - "
                    + child.Name
                )
