# Classic Snake game Challenge

- ## 1. Snake body:
  - [x] Snake head should be one move ahead checknextmove(d1)
  - [x] Snake body can grow in legnth
  - [x] Snake can body move
  - [x] Numerical array ?/ pop push ? / tupples

- ## 2. Move Snake:
  - [x]Snake moves forward automatically
  - [x]Snake must continue on same trajectory if not controlled
  - [x]Snake body coords must appear and disappaer from arr
  - [x]Dont allow snake to reverse direction on itself
  - [] Extend turtle to allow for movement actions within class
-
- ## 3. Control Snake:
  - [x] Move using arrows
  - [x] Snake must continue on same trajectory if not controlled
  - [x] Grow Snake

- ## 4. Detect Colision with food
  - [x] Detect pos
  - [x] New food
  - [ ] Remove old food

- ## 5. Create Score board:
  - [x] Display Total of foods eaten

- ## 6. Detect collision with wall:
  - [x] Handle stop game

- ## 7. Detect collision with tail:
  - [x] Handle stop game

- ## 9. Bug:
  - [x] init bug splitting lines to draw snake
  - [] last food not not disapearing
  - [] fix issue with precision movement 
    - likely solved using correct measurements
  - [] fix issue with segments tweening off

- ## 9. Code Review (based on solution):
  - [] Use tracer (supposedly affects animation)  given, only each n-th regular screen update is really performed.
  - [] Use screen.update
  - Update screen only after snake has moved forwards
  - x / y could save a few extra lines and is easier to understand
  - [] Extend turtle to snake / food / perform movement here
  - [] Look closely at logic to display turtle (object likely better init in the loop itself) based of start positions
  - [] Init the snake class itself with snake creation saves visual debt
    - [] Pop append works just fine for snake body pieces. An improvment might be **slice** but could unneccessary (slice here is avoid use forward)
  - [] Appears we will need usernanes for high score in future
  - Board currently requires passing in arrays etc just to check the position of the square.. could this go into snake and food classes to do our checks ?
  - [] Tutor has defined consts iinn  snake.py for postions size 
  - [] Food(Turtle) and  super.__init__ is how we do child
  - [] Food is refreshed  
  - [] Tutor has added a method to calculate distance < to object allowing snake head to be inprecise
  - Use turtle write method 
  - [] Game rules appear to just be coded main loop
  - [] Use .writemethod
  - [] You can splice tupples [:5] (get up to pos 5) [start:end:inc]