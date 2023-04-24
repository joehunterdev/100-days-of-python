# Classic Snake game Challenge

- ## 9. Bugs:
  - [x] init bug splitting lines to draw snake
  - [x] last food not not disapearing
  - [x] fix issue with precision movement 
    - likely solved using correct measurements
  - [x] fix issue with segments tweening off
  - [] slow refresh
  
- ## 9. Code Review (based on solution):
  - [0] Use tracer given, only each n-th regular screen update is really performed.
  - [] Use screen.update
  - Update screen only after snake has moved forwards
-   - [x] Extend turtle to snake / food / perform movement here
  - [x] Look closely at logic to display turtle (object likely better init in the loop itself) based of start positions
  - [x] Init the snake class itself with snake creation saves visual debt
    - [x] Pop append works just fine for snake body pieces. An improvment might be **slice** but could unneccessary (slice here is avoid use forward)
  - ~~[] usernames for high score in future~~
  - Board currently requires passing in arrays etc just to check the position of the square.. could this go into snake and food classes to do our checks ?
  - [x] Defined consts in snake.py for postions size 
  - [x] Food(Turtle) and ```super().__init__```
  - [x] Food is refreshed  
  > Tutor has added a method to calculate distance < to object allowing snake head to be inprecise
  - [x] Use turtle write method 
  - [x] Game rules 
  - [x] Use .write() method
  - [] You can splice tupples [:5] (get up to pos 5) [start:end:inc]