#Point Class
class Point:
  def __init__(self,row,col):
    self.row = row
    self.col = col

  def __repr__(self):
    return f"Point({self.row},{self.col})"

  def __add__(self,other):
    if isinstance(other,Point):
      return Point(self.row+other.row,self.col+other.col)
    else:
      raise Exception(f"{type(other)} is not a valid type to add to a point")

  def __sub__(self,other):
    if isinstance(other,Point):
      return Point(self.row-other.row,self.col-other.col)
    else:
      raise Exception(f"{type(other)} is not a valid type to subract from a point")
      
  def __mul__(self,other):
    if isinstance(other,Point):
      return Point(self.row*other.row,self.col*other.col)
    elif isinstance(other,int):
      return Point(self.row*other,self.col*other)
    else:
      raise Exception(f"{type(other)} is not a valid type to multiply to a point")

  def __mod__(self,other): #Can be used when "board wrapping" is allowed
    if isinstance(other,int):
      return Point(self.row%other,self.col%other)
    elif isinstance(other,Point):
      return Point(self.row%other.row,self.col%other.col)
    else:
      raise Exception(f"{type(other)} is not a valid type to multiply to a point")
      
  def __hash__(self):
    return hash((self.row, self.col))

  def __eq__(self,otherPoint):
    return self.row == otherPoint.row and self.col == otherPoint.col
