import pandas as pd
import numpy as np

# TASK 1 Load the morg_d07_strings.csv data set into a "morg_df" variable here
# Note: The rest of the code in this file will not work until you've done this.

## YOUR CODE HERE ##


# TASKS 2-6
# For each of the tasks, print the value requested in the task.

## YOUR CODE HERE ##


### Task 7
### convert to categoricals
TO_CATEGORICALS = ["gender", "race", "ethnicity", "employment_status"]

## YOUR CODE HERE ##

# Example use of cut()
boundaries = range(16, 89, 8)
morg_df["age_bin"] = pd.cut(morg_df["age"], 
                            bins=boundaries,
                            labels=range(len(boundaries)-1),
                            include_lowest=True, right=False)

### Task 8

## YOUR CODE HERE ##

print("Morg columns types after Task 8")
print(morg_df.dtypes)


### Tasks 9-13



### Task 14

students = pd.read_csv("data/students.csv")   
extended_grades = pd.read_csv("data/extended_grades.csv")

