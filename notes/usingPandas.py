import pandas
# pandas = data analysis library


#       BUILDING DATAFRAMES
#   df = dataframe

# Build array        w/ lists or dictionaries
df1 = pandas.DataFrame([[2,4,6],[10,20,30]])
print (df1, "\n")

# Add column names
df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns = ["Price", "Weight", "Value"])
print (df1, "\n")

# Add row names
df1 = pandas.DataFrame([[2,4,6],[10,20,30]], index = ["First", "Second"])
print (df1, "\n")

# Combo
df1 = pandas.DataFrame([[2,4,6],[10,20,30]], columns = ["Price", "Weight", "Value"], index = ["First", "Second"])
print (df1, "\n")


# Using dictionaries
df2 = pandas.DataFrame([{"Name": "John"},{"Name": "Jack"}])
print (df2, "\n")

df2 = pandas.DataFrame([{"Name": "John", "Surname": "Johnson"},{"Name": "Jack"}])
print (df2, "\n")




#       GETTING DATA FROM DATAFRAMES

print (df1.mean())
print (df1.mean().mean())
print (df1.Price)
print (df1.Price.max())