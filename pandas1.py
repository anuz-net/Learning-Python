import pandas as pd
    
stdata = {
    'Name' : ['Prabin', 'Sujan', 'Ramesh', 'Suresh', 'Gopal'],
    'Age' : [23, 25, 22, 24, 26],
    'City' : ['Kathmandu', 'Lalitpur', 'Bhaktapur', 'Pokhara', 'Biratnagar']
}

print("Original DataFrame: \n", pd.DataFrame(stdata)[["Name", "Age"]])

#Selecting Row By Index
first_row = pd.DataFrame(stdata).iloc[0]
print("\nFirst Row: \n", first_row)
    