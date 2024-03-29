import pandas as pd
data = {"Box": ["Box1","Box1","Box1","Box2","Box2","Box2"], "Dimension": ["Length","Width","Height", "Length","Width","Height"], "Value": [6,4,2,5,3,4]}
box = pd.DataFrame(data, columns = ["Box", "Dimension", "Value"])
tidy_box = box.pivot_table(index = ["Box"], columns = "Dimension", values = "Value").reset_index().rename_axis(None, axis=1)
addNewColumn = tidy_box.assign(Volume = tidy_box.Length*tidy_box.Width*tidy_box.Height)
print("The messy dataframe: \n", box)
print(" \n")
print("The tidy dataframe: \n", tidy_box)
print(" \n")
print("The resulting dataframe after adding a column: \n", addNewColumn)