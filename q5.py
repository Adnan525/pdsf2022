import pandas as pd

df = pd.read_csv("mycsv.csv",
                 usecols=["SIS User ID", "Submit Assignment 1 (57584)", "Submit Assignment 2 (57585)",
                          "Submit Assignment 3 (57473)"])
# filter the id column prefix to check if it starts with u or s
df = df[df["SIS User ID"].str.startswith("u") | df["SIS User ID"].str.startswith("s")]

# rename the column names
df = df.rename(columns={
    "SIS User ID": "StudentID",
    "Submit Assignment 1 (57584)": "Ass1",
    "Submit Assignment 2 (57585)": "Ass2",
    "Submit Assignment 3 (57473)": "FE"
})

# rearranging columns
df = df[["StudentID", "Ass1", "Ass2", "FE"]]

# creating 2 groups
dfS = df[df["StudentID"].str.startswith("s")]
dfU = df[df["StudentID"].str.startswith("u")]

# change to numeric before sorting
dfS["Ass2"] = pd.to_numeric(dfS["Ass2"])
# dfU["FE"] = pd.to_numeric(dfS["FE"], errors="coerce")

# order
# dfs works without an issue after to_numeric conversion
dfS = dfS.sort_values(by = "Ass2", ascending= False)

# dfU does not work just by converting to numeric
# I need to convert the values to int and add as a column
# once I sort the value it works
temp = dfU["FE"]
myList = []
for i in temp:
    myList.append(int(i))
dfU["FE"] = myList
dfU = dfU.sort_values(by = "FE", ascending= True)

# save the file
with pd.ExcelWriter('myexcel.xls') as writer :
    dfS.to_excel(writer, sheet_name='SID')
    dfU.to_excel(writer, sheet_name='UID')
