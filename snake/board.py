
from random import randint
from dotenv import load_dotenv

# Rules annd
class Board:

    def __init__(self,head = '',pieces = ''):

        self.width = 600
        self.height = 600
        self.head = ()
        self.walls = (self.width -1,self.height -1)
        # self.food = (randint(-abs(self.width % 2),299),randint(-299,299))
        self.score = 0
        self.pieces = pieces
        self.in_game = True
        self.size = 20
        self.food = (60,00)

    def is_wall(self,head):
      #  or head[0] > -abs(self.walls[1])
       if head[0] > (self.width -self.size) or head[0] < -abs(self.width +self.size):
         return True

    def is_food(self,head):
     if head == self.food:
       return True

    def is_back(self,head):

       if head in self.pieces:
         print(f"ilegal from {self.pieces[-1]} to {head}")
         return True

    def is_pieces(self,head):
       if head in self.pieces:
         return True
    
    def in_game(self):
       return True

    def generate_food(self):
      self.food = (self.size * randint(1,3), -self.size * randint(1,3) )
    
    def reset(self,object):
        self.in_game = False
        object.reset()

