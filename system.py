from thing import Thing

universe = Thing("universe")
universe.generateChildren()

import os

path = [universe]
command = ""
while command.lower() != "q":
    universe.view()

    command = input("\nCommand: ")
    os.system("cls")

    try:
        try:
            nextIndex = int(command)
            if nextIndex == 0:
                print("No such thing of index "+str(nextIndex)+".",end="")
            else:
                universe = universe.Contains[nextIndex-1]
                universe.generateChildren()
                path.append(universe)
        except IndexError:
            print("No such thing of index "+str(nextIndex)+".",end="")
    except ValueError:
        if command.lower() == "b":
            try:
                universe = path[-2]
                del path[-1]
            except:
                print("WARNING: Cannot go back, this is the top node.", end="")
        if command.lower() == "h" or command.lower() == "help":
            print("(B) to go back to the previous node. (Q) to quit.", end="")
