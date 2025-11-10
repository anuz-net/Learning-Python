import pandas as pd

data = {
    'Name': ['Prabin', 'Sujan', 'Ramesh', 'Suresh', 'Gopal'],
    'Age': [23, 25, 22, 24, 26],
    'City': ['Kathmandu', 'Lalitpur', 'Bhaktapur', 'Pokhara', 'Biratnagar']
    
}
df =  pd.DataFrame(data)
# save data to csv file
df.to_csv('students.csv', index=False)
print("Data saved to 'students.csv'")

#read data from csv file
df2 = pd.read_csv('students.csv')
#show basic info
print("DataFrame Info:")
print(df2.info())

#Show Mean of Age
mean_age = df2['Age'].mean()
print(f"\nMean Age: {mean_age}")

#Filter dataframe for Rows where Age > 25 then save the records to a new csv file


