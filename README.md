# universe
Universe Observatory in Python 3 🌌

Lets you model and explore the entire universe. Based on [Orteil's Nested](http://orteil.dashnet.org/nested).

I want to rewrite this in a compiled language soon to make it easier to release binaries. Stay tuned.

# How to run

If you download universe-release-bundled.zip, extract the zip folder then run `startUniverse.bat`.

If you want to run the source version, make sure you have Colorama installed with `pip install colorama`.
Then, extract universe-release-source.zip, and run `python system.py` in that directory with Python 3 installed.

# Setting the seed

Run `system.py` with the `-s` or `--seed` option.

Example: `python system.py -s SeedyMcSeedFace`

Each seed generates the exact same, including nations' and individuals' names.

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
