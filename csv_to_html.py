import pandas as pd 

# to read csv file named "samplee"
a = pd.read_csv("Resources/cities.csv")
 
# to save as html file
# named as "Table"
a.to_html("Table.html")
 
# assign it to a
# variable (string)
html_file = a.to_html()