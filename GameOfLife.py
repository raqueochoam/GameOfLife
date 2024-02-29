import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import copy

class Entity:
    def __init__(self, name, grid):
        self.name = name
        self.grid = grid
        self.cellsOn = []
        self.getCellsOn()
        
    def getCellsOn(self):
        self.cellsOn = []
        rows = len(grid)
        cols = len(grid[0])
        for row in range(0, rows):
            for col in range(0, cols):
                cell = (row, col)
                if grid[row][col] == 255:
                    self.cellsOn.append(cell)

def simulation(currentGrid, nextGrid, width, height, entities, entitiesCount):
    checkedCells = []
    cellsOn = []
    for row in range(1, height+1):
        for column in range(1, width+1):
            cell = (row, column)
            if cell not in checkedCells:
                checkedCells += checkEntities(currentGrid, row, column, entities, entitiesCount)
            neighbours = getOnNeighbours(cell, currentGrid)
            state = currentGrid[row][column]
            applyRules(nextGrid, row, column, state, neighbours)
            if state == ON:
                cellsOn.append(cell)
    otherEntities = checkOtherEntities(currentGrid, checkedCells, cellsOn)
    entitiesCount["other"] = otherEntities
            

def createBlockEntity():
    name = "block"
    grids = {}
    grid = [
            [0,   0,   0, 0], 
            [0, 255, 255, 0],
            [0, 255, 255, 0],
            [0,   0,   0, 0]
            ]
    grids[1] = grid
    return Entity(name, grids)

def createBeehiveEntity():
    name = "beehive"
    grids = {}
    grid = [
            [0,   0,   0,   0,   0, 0], 
            [0,   0, 255, 255,   0, 0],
            [0, 255,   0,   0, 255, 0],
            [0,   0, 255, 255,   0, 0],
            [0,   0,   0,   0,   0, 0]
            ]
    grids[1] = grid
    return Entity(name, grids)

def createLoafEntity():
    name = "loaf"
    grids = {}
    grid = [
            [0,   0,   0,   0,   0, 0], 
            [0,   0, 255, 255,   0, 0],
            [0, 255,   0,   0, 255, 0],
            [0,   0, 255,   0, 255, 0],
            [0,   0,   0, 255,   0, 0],
            [0,   0,   0,   0,   0, 0]
            ]
    grids[1] = grid
    return Entity(name, grids)
 
def createBoatEntity():
    name = "boat"
    grids = {}
    grid = [
            [0,   0,   0,   0, 0], 
            [0, 255, 255,   0, 0],
            [0, 255,   0, 255, 0],
            [0,   0, 255,   0, 0],
            [0,   0,   0,   0, 0]
            ]
    grids[1] = grid
    return Entity(name, grids)

def createTubEntity():
    name = "tub"
    grids = {}
    grid = [
            [0,   0,   0,   0, 0], 
            [0,   0, 255,   0, 0],
            [0, 255,   0, 255, 0],
            [0,   0, 255,   0, 0],
            [0,   0,   0,   0, 0]
            ]
    grids[1] = grid
    return Entity(name, grids)

def createBlinkerEntity():
    name = "blinker"
    grids = {}
    grid1 = [
            [0,   0, 0], 
            [0, 255, 0],
            [0, 255, 0],
            [0, 255, 0],
            [0,   0, 0]
            ]
    grid2 = [
            [0,   0,   0,   0, 0],
            [0, 255, 255, 255, 0],
            [0,   0,   0,   0, 0],
            ]
    grids[1] = grid1
    grids[2] = grid2
    return Entity(name, grids)

def createToadEntity():
    name = "toad"
    grids = {}
    grid1 = [
            [0,   0,   0,   0,   0, 0], 
            [0,   0,   0, 255,   0, 0],
            [0, 255,   0,   0, 255, 0],
            [0, 255,   0,   0, 255, 0],
            [0,   0, 255,   0,   0, 0],
            [0,   0,   0,   0,   0, 0]
            ]
    grid2 = [
            [0,   0,   0,   0,   0, 0], 
            [0,   0,   0,   0,   0, 0],
            [0,   0, 255, 255, 255, 0],
            [0, 255, 255, 255,   0, 0],
            [0,   0,   0,   0,   0, 0],
            [0,   0,   0,   0,   0, 0]
            ]
    grids[1] = grid1
    grids[2] = grid2
    return Entity(name, grids)

def createBeaconEntity():
    name = "beacon"
    grids = {}
    grid1 = [
            [0,   0,   0,   0,   0, 0], 
            [0, 255, 255,   0,   0, 0],
            [0, 255, 255,   0,   0, 0],
            [0,   0,   0, 255, 255, 0],
            [0,   0,   0, 255, 255, 0],
            [0,   0,   0,   0,   0, 0]
            ]
    grid2 = [
            [0,   0,   0,   0,   0, 0], 
            [0, 255, 255,   0,   0, 0],
            [0, 255,   0,   0,   0, 0],
            [0,   0,   0,   0, 255, 0],
            [0,   0,   0, 255, 255, 0],
            [0,   0,   0,   0,   0, 0]
            ]
    grids[1] = grid1
    grids[2] = grid2
    return Entity(name, grids)

def createGliderEntity():
    name = "glider"
    grids = {}
    grid1 = [
            [0,   0,   0,   0, 0], 
            [0,   0, 255,   0, 0],
            [0,   0,   0, 255, 0],
            [0, 255, 255, 255, 0],
            [0,   0,   0,   0, 0]
            ]
    grid2 = [
            [0,   0,   0,   0, 0], 
            [0, 255,   0, 255, 0],
            [0,   0, 255, 255, 0],
            [0,   0, 255,   0, 0],
            [0,   0,   0,   0, 0]
            ]
    grid3 = [
            [0,   0,   0,   0, 0], 
            [0,   0,   0, 255, 0],
            [0, 255,   0, 255, 0],
            [0,   0, 255, 255, 0],
            [0,   0,   0,   0, 0]
            ]
    grid4 = [
            [0,   0,   0,   0, 0], 
            [0, 255,   0,   0, 0],
            [0,   0, 255, 255, 0],
            [0, 255, 255,   0, 0],
            [0,   0,   0,   0, 0]
            ]
    grids[1] = grid1
    grids[2] = grid2
    grids[3] = grid3
    grids[4] = grid4
    return Entity(name, grids)

def createLightWeightSpaceshipEntity():
    name = "lightWeightSpaceship"
    grids = {}
    grid1 = [
            [0,   0,   0,   0,   0,   0, 0], 
            [0, 255,   0,   0, 255,   0, 0],
            [0,   0,   0,   0,   0, 255, 0],
            [0, 255,   0,   0,   0, 255, 0],
            [0,   0, 255, 255, 255, 255, 0],
            [0,   0,   0,   0,   0,   0, 0]
            ]
    grid2 = [
            [0,   0,   0,   0,   0,   0, 0], 
            [0,   0,   0, 255, 255,   0, 0],
            [0, 255, 255,   0, 255, 255, 0],
            [0, 255, 255, 255, 255,   0, 0],
            [0,   0, 255, 255,   0,   0, 0],
            [0,   0,   0,   0,   0,   0, 0]
            ]
    grid3 = [
            [0,   0,   0,   0,   0,   0, 0], 
            [0,   0, 255, 255, 255, 255, 0],
            [0, 255,   0,   0,   0, 255, 0],
            [0,   0,   0,   0,   0, 255, 0],
            [0, 255,   0,   0, 255,   0, 0],
            [0,   0,   0,   0,   0,   0, 0]
            ]
    grid4 = [
            [0,   0,   0,   0,   0,   0, 0], 
            [0,   0, 255, 255,   0,   0, 0],
            [0, 255, 255, 255, 255,   0, 0],
            [0, 255, 255,   0, 255, 255, 0],
            [0,   0,   0, 255, 255,   0, 0],
            [0,   0,   0,   0,   0,   0, 0]
            ]
    grids[1] = grid1
    grids[2] = grid2
    grids[3] = grid3
    grids[4] = grid4
    return Entity(name, grids)

def isNeighbour(cell1, cell2):
    cell1Row = cell1[0]
    cell1Column = cell1[1]
    cell2Row = cell2[0]
    cell2Column = cell2[1]
    
    if abs(cell1Row - cell2Row) not in [0,1] or abs(cell1Column - cell2Column) not in [0,1]:
        return False
    return True
    
def getNeighbours(cell):
    neighbours = []
    row = cell[0]
    column = cell[1]
    for rowOffset in range(-1, 2):
        for colOffset in range(-1, 2):
            if rowOffset != 0 or colOffset != 0:
                neighbours.append((row+rowOffset, column+colOffset))
    return neighbours
    
def getOnNeighbours(cell, grid):
    neighbours = 0
    row = cell[0]
    column = cell[1]
    for rowOffset in range(-1, 2):
        for colOffset in range(-1, 2):
            if rowOffset != 0 or colOffset != 0:
                neighbours += (grid[row+rowOffset][column+colOffset] == 255)
    return neighbours      

def applyRules(grid, row, column, state, neighbours):
    if state == ON:
        if neighbours not in [2,3]:
            grid[row][column] = OFF
    else:
        if neighbours == 3:
            grid[row][column] = ON
            
def checkEntities(grid, row, column, entites, entitiesCount):
    cellsChecked = []
    entityFound = False
    for entity in entites:
        if entityFound:
            break
        for entityMode in entity.grid:
            if entity.grid[entityMode] == ([col[column-1:column+(len(entity.grid[entityMode][0])-1)] for col in grid[row-1:row+(len(entity.grid[entityMode])-1)]]):
                entitiesCount[entity.name] += 1
                for i in range(0, len(entity.grid[entityMode])-2):
                    for j in range(0, len(entity.grid[entityMode][0])-2):
                        cell = (row+i, column+j)
                        cellsChecked.append(cell)
                entityFound = True
                break
    return cellsChecked

def checkOtherEntities(grid, checkedCells, cellsOn):
    entities = 0
    cells = set()
    for cell in cellsOn:
        if cell not in checkedCells:
            if cell not in cells:
                entities += 1
            cells.add(cell)
            cells.update(getNeighbours(cell))
    return entities
    
#def update(frame):
#    ax.clear()
#    ax.imshow(grid, cmap='binary', vmin=0, vmax=255)
#    ax.set_title(f"Frame {frame}")

#fig, ax = plt.subplots()
            
ON = 255
OFF = 0

width = 50
height = 10

grid = [[OFF for i in range(0,width+2)] for j in range(0,height+2) ] 

initialCells = [(0,1),(1,2),(2,0),(2,1),(2,2)]

for cell in initialCells:
    cellRow = cell[0] + 1
    cellColumn = cell[1] + 1
    grid[cellRow][cellColumn] = ON
    
generations = 20

entities = []

entities.append(createBlockEntity())
entities.append(createBeehiveEntity())
entities.append(createLoafEntity())
entities.append(createBoatEntity())
entities.append(createTubEntity())
entities.append(createBlinkerEntity())
entities.append(createToadEntity())
entities.append(createBeaconEntity())
entities.append(createGliderEntity())
entities.append(createLightWeightSpaceshipEntity())

entitiesCount = {"block": 0,
            "beehive": 0,
            "loaf": 0,
            "boat": 0,
            "tub": 0,
            "blinker": 0,
            "toad": 0,
            "beacon": 0,
            "glider": 0,
            "lightWeightSpaceship": 0,
            "other": 0}

for currentGen in range(0, generations):
    nextGrid = copy.deepcopy(grid)
    entitiesCount = {entity: 0 for entity in entitiesCount}
    simulation(grid, nextGrid, width, height, entities, entitiesCount)
    print(entitiesCount,  "\n")
    grid = copy.deepcopy(nextGrid)


plt.show() 
            