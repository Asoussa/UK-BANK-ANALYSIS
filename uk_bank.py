import pandas as pd
import matplotlib.pyplot as matpolt







 
# STARTUP =PANDES AND THE FILE THAT CONTAIN THE DATA
startup=pd.read_excel(r"d:\My-project\uk-bankk.xlsx")


print(startup.head(10))  # display first 10 rows

# display first 10 rows
pd.set_option('display.max_rows',None) 
print(startup)

#DESCRIBE THE MEAN AND COUNT,......
print(startup[['Marketing Spend','Revenue']].describe().round(1))
#GIVE U ALL THE DETAILS ABOUT THE DATA TYPE
startup.info()


print(startup['City'].nunique()) #NUMBER THE CITY 
print(startup['City'].unique())  #NAME OF THE CITY 
print(startup['City'].value_counts()) #NUMBER OF EACH CITY 
 




print(startup['State'].nunique()) #NUMBER THE STATE
print(startup['State'].unique())  #NAME OF THE STATE
print(startup['State'].value_counts()) #NUMBER OF EACH CIT STATE

print(startup['Sales Region'].unique())
print(startup['Sales Region'].value_counts())


print(startup['New Expansion'].unique())
print(startup['New Expansion'].value_counts())


print(startup.isnull().sum()) # IS THERE ARE ANY NULL CELL
print(startup.duplicated().sum()) # IS THERE ARE ANY DUBLICATED ROW


print(len(startup)) #LENGHT OF THE DATA SET
print(len(startup["Store ID"].value_counts()))  #LENGHT OF THE DATA SET ("Store ID")


print(startup.sample(5)) #RONDOM SAMPLE

startup['Sales Region'].value_counts().plot.bar(color='red', edgecolor='black') #BAR_CHART
matpolt.xlabel("Sales Region")
matpolt.ylabel("Count")
matpolt.show()


# Pie chart to visualize the distribution of sales regions
startup['New Expansion'].value_counts().plot.pie()
matpolt.title('Sales Region Distribution')
matpolt.ylabel('')  # Removes default ylabel
matpolt.show()


# Group by 'State' and sum the 'Revenue' for each state
state_revenue_sum = startup.groupby('State')['Revenue'].sum()

state_revenue_sum.plot.hist(bins=20, alpha=0.7, color='skyblue', edgecolor='black', figsize=(8, 6))
matpolt.title('Histogram of Revenue Sum by State')
matpolt.xlabel('Total Revenue')
matpolt.ylabel('Frequency')
matpolt.show()

top_states_revenue = startup.groupby('State')['Revenue'].sum().nlargest(10)
top_states_revenue.plot.bar(
    color='orange', figsize=(10, 6), edgecolor='black', alpha=0.8
)
matpolt.title('Top 10 States by Revenue')
matpolt.xlabel('State')
matpolt.ylabel('Total Revenue')
matpolt.xticks(rotation=45)
matpolt.show()

# Group by 'New Expansion' and count the number of occurrences for each group
print(startup.groupby('New Expansion').size())
# Group by 'Revenue' and display the maximum values for other columns in each group
print(startup.groupby('Revenue').max())


 # Analyze revenue for 'Old' and 'New' expansions grouped by state
print(startup[startup['New Expansion']=="Old"].groupby("State")["Revenue"].sum().nlargest(10))
print(startup[startup['New Expansion']=="New"].groupby("State")["Revenue"].sum().nlargest(10))


# Calculate profit as Revenue - Marketing Spend
profit=(startup['Revenue']-startup['Marketing Spend']).round(1) 
print(profit)
# Display the maximum profit value
print(profit.max())

# Add 'profit' column to the DataFrame
startup['profit'] =(startup['Revenue']-startup['Marketing Spend']).round(1) 
# Calculate ROMS (Return on Marketing Spend) as (profit / marketing spend) * 100
startup['ROMS'] = (startup['profit'] / startup['Marketing Spend']* 100).round(2)
# Add a column 'ROMS %' by dividing 'ROMS' by 100 and rounding the result
startup['ROMS %'] = (startup['ROMS'] / 100). round()
# Display the updated DataFrame
print(startup)



# Save the modified DataFrame to a CSV file
startup.to_csv(r'D:\My-project\uk_bank_modified.csv')

