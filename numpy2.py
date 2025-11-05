import numpy as np

#Data Set Creation
#Generate Sales data:10, employees, 7 days
sales_data = np.random.randint(50,500, size = (10,7))
print("\nSales Data:\n", sales_data)

#Step 2 : Total Sales of Each Employee
total_sales=np.sum(sales_data,axis=1)
print("\n Total Sales per employee : ", total_sales)

# Step 3: Average Daily Sales
average_daily_sales = np.mean(sales_data,axis=0)
print("\nAverage Sales per Day:",average_daily_sales)

#Step 4: Increase sales by 10%
increased_sales = sales_data*1.10
print("\nSales After 10% Increase:\n", increased_sales)

#Step 5:Data Manupilation
first_five_employee=sales_data[: 5, :] 
print('\n Sales data for First Five Employee:\n',first_five_employee)

#Step 6 : Employee with Total Sales > 2000
high_performers = total_sales>2000
print("\n High Performer ( Total Sales > 2000) : ", np.where(high_performers)[0])

#Step 6 : Statistical analysis
mean_sales = np.mean(sales_data)
median_sales=np.median(sales_data)
std_dev_sales = np.std(sales_data)
print("\n Overall Mean Sales:", mean_sales)
print(" Overall Median Sales:", median_sales)
print(" Overall Standard Deviation of Sales:", std_dev_sales)

#Step 7 : Identify Employee with Highest Sales in a day
max_sales_day = np.max(sales_data, axis=1)
print("\n Highest Sales in a Day per Employee:", max_sales_day)
best_employee = np.argmax(max_sales_day)
print(" Employee with Highest Sales in a Day: Employee", best_employee)
