# Infinite Progression Mod Template

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
