# universe
Universe Observatory in Python 3 🌌

Lets you model and explore the entire universe. Based on [Orteil's Nested](http://orteil.dashnet.org/nested).

Work in progress, contributions and improvments welcome! :)


# How to run

Make sure you have Colorama installed with `pip install colorama`

Run the file `system.py` with Python 3.
Do this by running `py system.py` in the directory you installed the files to.

# Making your own things

The composition of everything is defined in `things.py` in the `data` folder.

The format for objects is as follows:

`"thing-type": ["Thing Alias/Name", Child, Child, Child]`

Children are formatted like this:

`("child-type", [possible instances], [chance of each instance occuring])`

Here's an example thing, a `medieval-house`:

`"medieval-house": ["house", ("desk",1,0.7), ("dinner table",1,1),("medieval-farmer", 7, 0.7)]`

In this case, a desk will appear in the house 70% of the time, on average there will be 5 famers in the house, and a dinner table will always appear no matter what.

For its children to be viewable, you would have to define them too. For example, the `dinner table`:

`"dinner table": [("plate",7,0.7),("chair",7,0.7)]`
