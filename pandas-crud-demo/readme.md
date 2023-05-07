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
  - [] Column handling
  - [] Saving 
    - [] Resource close ?
    - [] Use of a nd w flags

```
   ## Paths
    print(image_path("spain"))
    print(csv_path("spain"))

    # Read

    ## All
    # csv = pandas.read_csv(csv_path("spain"))
    # print(f"Type: {type(print(csv))}" )
    # df = pandas.DataFrame(data = csv)

    ## Single Row
    result = df.iloc[[0]]
    print(f"Result: {result}" )


    ## Get Id where row
    row = results_where
    index = row.index.tolist()

    print(f"Index from row: {index}")

    ## Create row as list


    # df = pandas.concat([new_row_obj,df.loc[:]]).reset_index(drop=True)

    ##,ignore_index = True
    print(f"Updated: {df}" )
    test_csv_path = csv_path("spain").replace("coords", "coords-2")


    Likely you will not need to store the index=False
    df.to_csv(csv_path("spain"), encoding='utf-8', index=False)
    
```
 