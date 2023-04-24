from turtle import Turtle,Screen

class Board(Turtle):

    def __init__(self):
      
      super().__init__()
      self.score = 0
      self.penup()
    
    def add_board(self,text,position):
      
      self.setpos(0,-position)
      style = ('System', 20, 'italic')
      self.color("white")
      self.write(text, font=style, align='center')

   
    def add_score(self,points = 1):
      self.score += points
      self.clear()

      # self.clear()
         
    # def in_game(self):
    #   return True
    
    # def reset(self,points = 1):
    #     time.sleep(1)
        
   
    

