# Classic Pong Game

## Todo:

  - 1. Create Screen
    - [x] 800 x 600
    - [x] Basic Cfg params
  - 2. Create & Move a bat
    - [x] Gist
    - [x] Bat Class & 
    - [x] Init Bat (Left||Right)
      - [x] Set Side ()
      - [0] Bug 1
        - [x] Screen handling in class
        - [x] Screen object init in main
        - ~~[] Keyboard btn init ("Left","w","s") ?~~
      - [x] Refactor logic in to main.py
  - 3. [x] Duplicate Paddle
  - 4. [x] Create ball and make it move
  - 5. [x] Detect colision with wall and bounce
  - 6. [x] Detect collision with paddle
  - 7. [x] Detect Net
  - 8. [x] Keep Score
  - 9. [x] Speed Up Ball

## Bugs
  - 1. [] Issue with key movements interrupting  each other
        - [] looks like this could be keypress event 
        - [x] Test alt go_up methods
 
## Outline 

    - [] Bat
      - bat 1 / 2
    - [] Board
      - xchor score
    - [] Ball
      - super()
      - speed
      - move
    - [] ~~Half Way line~~
      - super()

  - [] main loop conditionals
    - [] Wall
    - [] Net
    - [] ? Count bat hits ?

## Methods
    ~~Reset Ball~~
    rebound:
       invert y pos of wall
       invert x pos of bat
          
 
