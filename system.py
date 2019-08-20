from thing import Thing

universe = Thing("universe")
universe.generateChildren()

from colorama import init
init()

from os import system
from data import things
path = [universe]
command = ""

while command.lower() != "q":
    universe.view()

    command = input("\nCommand: ")

    try:
        try:
            nextIndex = int(command)
            if nextIndex == 0:
                print("WARNING: No such thing of index "+str(nextIndex)+". ", end="")
            else:
                nextNode = universe.Contains[nextIndex-1]
                if nextNode.Type in things.cannotEnter:
                    print("WARNING: You cannot enter that. ",end="")
                    continue
                elif nextNode.Type.endswith("-thought"):
                    print("WARNING: You cannot enter that. ",end="")
                    continue
                else:
                    universe = nextNode
                    universe.generateChildren()
                    path.append(universe)

        except IndexError:
            print("WARNING: No such thing of index "+str(nextIndex)+". ",end="")
    except ValueError:
        if command.lower() == "b":
            try:
                universe = path[-2]
                del path[-1]
            except:
                print("WARNING: Cannot go back, this is the top node. ", end="")
        if command.lower() == "h" or command.lower() == "help":
            system("cls")
            print("\nHELP:\n(#) to enter a node.\n(B) to go back to the previous node.\n(Q) to quit.\n(r) to return to top node.\n(R) to reset simulation.", end="")
            input("\n\nEnter to exit...")
            system("cls")
        if command == 'R':
            universe = Thing("universe")
            universe.generateChildren()
            path = [universe]
            command = ""
            continue
        if command == 'r':
            universe = path[0]
            path = path[1:]
            print(path)
            command = ""
            continue