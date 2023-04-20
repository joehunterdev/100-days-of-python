from dotenv import load_dotenv

class Snake:

    def __init__(self):

      self.pieces = [(0, 0),(20, 0),(40, 0)]
      self.legnth = len(self.pieces)
      self.head = ()
      self.speed = 1
      self.direction = "Right"
      self.directions = ["Right"]
      self.size = 10

    def move(self,key):
 
        match key:

            case "Up":

                head = (self.pieces[-1][0],self.pieces[-1][1]+self.size)

            case "Down":

                head = (self.pieces[-1][0],self.pieces[-1][1]-self.size)

            case "Left":

                head = (self.pieces[-1][0]-self.size,self.pieces[-1][1])

            case "Right":

                head = (self.pieces[-1][0] + self.size,self.pieces[-1][1])       
        
        self.pieces.append(head)
        self.pieces.pop(0)

    def grow(self,head):
        
        self.pieces.append(head)
        # self.move(direction)


    def set_direction(self,key):
       
       self.direction = key
       self.directions.append(key)
    
    def get_next(self,key):
 
        match key:

            case "Up":

                head = (self.pieces[-1][0],self.pieces[-1][1]+10)

            case "Down":

                head = (self.pieces[-1][0],self.pieces[-1][1]-10)

            case "Left":

                head = (self.pieces[-1][0]-10,self.pieces[-1][1])

            case "Right":

                head = (self.pieces[-1][0] + 10,self.pieces[-1][1])       
        
        self.head = head
        return head
       
    def draw_snake(self):
        pass