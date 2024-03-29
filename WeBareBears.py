import pandas as pd
data1 = {"Student": ["Ice Bear", "Panda", "Grizzly"], "Math": [80,95,79]}
data2 = {"Student": ["Ice Bear", "Panda", "Grizzly"], "Electronics": [85,81,83]}
data3 = {"Student": ["Ice Bear", "Panda", "Grizzly"], "GEAS": [90,79,93]}
data4 = {"Student": ["Ice Bear", "Panda", "Grizzly"], "ESAT": [93,89,88]}
M = pd.DataFrame(data1, columns = ["Student","Math"])
El = pd.DataFrame(data2, columns = ["Student","Electronics"])
G = pd.DataFrame(data3, columns = ["Student","GEAS"])
Es = pd.DataFrame(data4, columns = ["Student","ESAT"])
j1 = pd.merge(M,El, how="outer", on="Student")
j2 = pd.merge(j1,G, how="outer", on="Student")
j = pd.merge(j2,Es, how="outer", on="Student")
print("The four dataframes which contain the scores of We Bare Bears cast: \n", M)
print(" \n", El)
print(" \n", G)
print(" \n", Es)
print("and then the resulting dataframe after joining them using pd.merge: \n", j)
print(" \n")
print("To convert to long format, type longformat(j), Thank you!!! \n")

def longformat(j):
    lf1 = pd.melt(j, id_vars = "Student", value_vars = ["Math", "Electronics", "GEAS", "ESAT"])
    lf2 = lf1.rename(columns = {"variable": "Subject", "value": "Grades"})
    lf3 = lf2.sort_values("Student").reset_index().drop(columns = ["index"])
    lf = print("The converted dataframe is: \n", lf3)
    return lf