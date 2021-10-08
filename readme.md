# Infinite Progression Mod Docs

## API Classes

### BigNumber

```python
import BigNumber

BigNumber(number)
# returns a BigNumber object with the value number
```

### SeededRand

```python
import SeededRand

Perlin(at)
# returns a random number from the seed, at position at

Word(num)
# gets a random word from rng at num
```

### GameController

```python
import GameController

GetRandOf(kind, defaultId, before)
# gets a random module of kind
# before the module id before
# defaults to defaultId if tries more than 100 times
# returns a GenericController object

GetSlider(id)
# gets a SliderController from the object id

GetData(id)
# gets the data from the module with id id
```

## Json

### info.json

the fields are:

```text
"name": the name of the module displayed in game
"description": the description of the module displayed in game
"main_file": the python file containing the data class and functions
"ui_file": the ui.json file name
"requires": a list of mods required by this one
"chance": the chance for the module to show, the actual chance is chance / total_chance, slider chance is always 10 total chance is the sum of all chances
```

### ui.json

the fields are:

```text
"buttons": a list of buttons each surrounded in {}
"slider": a list of sliders each surrounded in {}
```

### ui.json button

the fields are:

```text
"x", "y", "w", "h": the position of the button
"onClick": the name of the function to be called when the button is clicked, in python
"enable": the name of the function in python that returns wether the button is enabled
```

### ui.json slider

the fields are:

```text
"x", "y", "w", "h": the position of the slider
"variable": the name of the variable that shows progress between 0 and 1 of the bar
```

### ui.json text

the fields are:

```text
"x", "y", "w", "h": the position of the text
"dynamic_text": a name of a function that returns a string containing the text
"static_text": the text the text shows, overwrites dynamic_text
```
