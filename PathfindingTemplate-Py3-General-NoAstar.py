#Look for H's for where to change

class Game:
    def __init__(self,grid):
        #H: May be differently formatted
        grid = grid.split("\n")
        self.height = len(grid)
        self.width = len(grid[0])
        self.grid = [[Tile(grid[row][col],row,col) for col in range(self.width)] for row in range(self.height)]   #H: May need some editing
        #self.grid[0][0].visited = 1 #Corner is starting Point
        self.dirs = [Point(0,1),Point(0,-1),Point(-1,0),Point(1,0)]
        self.diagonals = [Point(1,1),Point(1,-1),Point(-1,-1),Point(-1,1)]
    
    def __repr__(self):
        ret = ""
        for row in self.grid:
            for tile in row:
                ret += str(tile.visited)
            ret+="\n"
        return ret[:-1]
    
    def isValid(self,point):
        return 0 <= point.row < self.height and 0 <= point.col < self.width
    
    def get_tile(self,point):
        return self.grid[point.row][point.col]
    
    def get_search_tile(self):
        for row in self.grid:
            for tile in row:
                if tile.visited == 1:
                    return tile
        return False
    
    def logic(self):
        while(True):
            tile = self.get_search_tile()
            if tile:
                for dir in self.dirs:
                    newPoint = tile.pos+dir
                    if self.isValid(newPoint):
                        searchTile = self.get_tile(newPoint)
                        tile.search(searchTile)
                tile.visited = 2
            else:
                print(self)
                return self.answer()
            
    def answer(self):
        #H: Needs how the answer is achieved
        #return self.grid[-1][-1].visited != 0 #Corner is ending point
        for row in self.grid:
            for tile in row:
                if tile.letter == "E":
                    return tile.score
    
class Tile:
    def __init__(self,letter,row,col):
        self.letter = letter
        self.wall = False
        self.visited = 0
        if letter == "S": #Start Letter
            self.visited = 1
        elif letter == "W": #Wall Letter
            self.wall = True #H: Could need more types 
        self.score = 0 #This could be many different things
        self.row = row
        self.col = col
        self.pos = Point(row,col) #row, then column
        
    def search(self,otherTile):
        #H: Needs the logic of a search
        if otherTile.wall: return
        if otherTile.visited == 0:
            otherTile.visited = 1
            otherTile.score = self.score+1

class Point:
    def __init__(self,row,col):
        self.row = row
        self.col = col
    
    def __repr__(self):
        return f"Point({self.row},{self.col})"
    
    def __add__(self,otherPoint):
        return Point(self.row+otherPoint.row,self.col+otherPoint.col)
    
    def __eq__(self,otherPoint):
        return self.row == otherPoint.row and self.col == otherPoint.col
        


inpt = ".WWWW\n.WWWW\n.....\nWWWW.\nWWWW."
game = Game(inpt)
print(game.logic())
