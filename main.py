import clr
clr.AddReference('IP.Lib')
clr.AddReference('IP.Game')

import BigNumber
import SeededRand
import GameController

class Data:
    def __init__(self, id):
        self.id = id

def onLoad():
    return  "Success Loading"

def onUnload():
    return "Success Unloading"

def createModule(id):
    data.result = "Created Template"
    return data

def tick(data):
    return data

def bulkTick(data, amount):
    return data

def destroyModule(data):
    return data

def prestige(data):
    pass

def loadSave(save, id):
    data = createModule(id)
    return data

def saveData(data):
    result = ""
    return result