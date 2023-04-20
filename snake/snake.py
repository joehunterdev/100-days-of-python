from dotenv import load_dotenv

class Snake:

    def __init__(self):

      self.body = [(0, 0),(10, 0),(20, 0),(30, 0),(40, 0),(50, 0)]
      self.legnth = len(self.body)
    #    the next square
      self.head = ()
      self.speed = 1
      self.direction = "Right"
      self.directions = ["Right"]
      self.size = 10

    def move(self,key):
 
        match key:

            case "Up":

                head = (self.body[-1][0],self.body[-1][1]+self.size)

            case "Down":

                head = (self.body[-1][0],self.body[-1][1]-self.size)

            case "Left":

                head = (self.body[-1][0]-self.size,self.body[-1][1])

            case "Right":

                head = (self.body[-1][0] + self.size,self.body[-1][1])       
        
        self.body.append(head)
        self.body.pop(0)

    def grow(self,head):
        
        self.body.append(head)
        # self.move(direction)


    def set_direction(self,key):
       
       self.direction = key
       self.directions.append(key)
    
    def get_next(self,key):
 
        match key:

            case "Up":

                head = (self.body[-1][0],self.body[-1][1]+10)

            case "Down":

                head = (self.body[-1][0],self.body[-1][1]-10)

            case "Left":

                head = (self.body[-1][0]-10,self.body[-1][1])

            case "Right":

                head = (self.body[-1][0] + 10,self.body[-1][1])       
        
        self.head = head
        return head
       
    #    if key == "Up"  and self.direction == "Down":
    #      self.direction = "Down"
    #    else:
    #      self.direction = "Up"
    #    #could use previous coords here
       
       
    def draw_snake(self):
        pass