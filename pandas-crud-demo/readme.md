# States Game
-  [x] Takes as uppercase
-  [x] Count states correct
-  [x] Read From CSV
-  [x] Find Comparison
-  [x] Place text at x y
-  [x] Use mainloop() to avoid using click
>> Note: We have set a list of states to check in 
- [x] Store Guessed attempts

Notes

- **Initial approach was good, just missing `item`**
- **Dont use append, use `concat`**
- **ValueError: If using all scalar values, you must pass an index**
- **The error message says that if you're passing scalar values, you have to pass an index. So you can either not use scalar values for the columns -- e.g. use a list:**

--- 

## Pandas Crud
  > Interesting to setup a working Pandas csv db abstraction layer using oop
  
  - [] Create Row
  - [x] Read All
  - [x] Read Row 
    - [x] where index 
    - [x] where col => value
  - [] Update 
  - [] Update Row Where 
  - [] Delete Row
  - [] Helpers 
    - [] Load CSV, Save CSV, Get Difference, Paginate
    - [] Get row id