import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel('ABC Company.xlsx')
# print(df.isnull().sum())
# observation: Upon inspecting missing values in the dataset, it was found that the College column contains 84 missing
# entries, and the Salary column contains 11 missing entries. All other columns have complete data.
df['College'] = df['College'].fillna('Unknown')
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
# print(df.isnull().sum())

df['Height'] = np.random.randint(150, 181, size=len(df))
# Observation: the Height column contained inconsistent and non-numerical values, making it unsuitable for analysis
# therefore it was corrected by replacing all values with randomly generated integers between 150
# and 180 cm to ensure numerical consistency and data integrity before further analysis.
# * Verify data integrity
print(df['Height'].dtype)
print(df['Height'].min(), df['Height'].max())
# print(df['Height'].head(50))
print(df.isnull().sum())

# Question_1: Determine the distribution of employees across each team and calculate
# the percentage split relative to the total number of employees.
team_count = df['Team'].value_counts()
team_percentage = (team_count / len(df)) * 100
team_distribution = pd.DataFrame({
    'Employee_count': team_count,
    'Percentage(%)': team_percentage.round(2)
})
print(team_distribution)
# Observation: The dataset shows that employees are unevenly distributed across teams. Some teams have a higher
# concentration of employees, indicating larger team sizes, while others have fewer employees.
team_distribution['Employee_count'].plot(kind='bar', figsize=(14, 6))
plt.ylabel('Number of Employees')
plt.xlabel('Teams')
plt.title('Employee Distribution Across Teams')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
print("""The employee distribution across teams appears largely uniform, with most teams having a similar number 
of employees, typically around 14–16 members. A few teams, such as the New Orleans Pelicans and Memphis Grizzlies, 
show slightly higher employee counts, while teams like the Minnesota Timberwolves and Orlando Magic have marginally 
lower representation. Overall, the visualization indicates a balanced workforce allocation across teams, with no 
extreme disparities in team sizes """)

# Question_2:Segregate employees based on their positions within the company.
position_distribution = df['Position'].value_counts()
plt.figure(figsize=(6, 4))
position_distribution.plot(kind='bar', color='purple')
plt.xlabel('Position')
plt.ylabel('Number of Employees')
plt.title('Employee Segregation by Position')
plt.tight_layout()
plt.show()
print("""The visualization shows that employees are distributed across different positions such as PG, SG, SF, PF,
 and C. The number of employees in each position is fairly similar, indicating a balanced workforce. 
 No single position is significantly over-represented or under-represented within the organization.""")

# Question_3: Identify the predominant age group among employees.
age_bins = [18, 25, 30, 35, 40, 50]
age_labels = ['18-25', '26-30', '31-35', '36-40', '40+']
df['Age_Group'] = pd.cut(df['Age'], bins=age_bins, labels=age_labels)
age_group_distribution = df['Age_Group'].value_counts()
print(age_group_distribution)
# Observation: The predominant age group among employees is 18–25, as this group has the highest representation with
# 200 employees, indicating that the workforce largely consists of young professionals.
plt.figure(figsize=(6, 4))
age_group_distribution.plot(kind='bar', color='orange')
plt.xlabel('Age Group')
plt.ylabel('Number of Employees')
plt.title('Distribution of Employees by Age Group')
plt.tight_layout()
plt.show()
print("""The visualization shows that the 18–25 age group has the highest number of employees,
 making it the predominant age group. This indicates that the workforce is mainly composed of 
 young professionals, while older age groups have comparatively fewer employees.""")


# Question_4: Discover which team and position have the highest salary expenditure.
team_salary = df.groupby('Team')['Salary'].sum().sort_values(ascending=False)
print(team_salary.head(1))
plt.figure(figsize=(12, 5))
team_salary.plot(kind='bar', color='green')
plt.xlabel('Team')
plt.ylabel('Total Salary')
plt.title('Total Salary Expenditure by Team')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

# ----------------------------------------------------------------------------------------------------------------------
position_salary = df.groupby('Position')['Salary'].sum().sort_values(ascending=False)
print(position_salary.head(1))
plt.figure(figsize=(12, 5))
position_salary.plot(kind='bar')
plt.xlabel('Position')
plt.ylabel('Total Salary')
plt.title('Total Salary Expenditure by Position')
plt.tight_layout()
plt.show()
print(""" The salary expenditure analysis shows that Cleveland Cavaliers accounts for the highest total salary cost compared to
 other teams. Similarly, among positions, 'C' has the highest salary expenditure, indicating higher 
 compensation associated with that position.""")

# Question_5: Investigate if there's any correlation between age and salary, and
# represent it visually.
correlation = df['Age'].corr(df['Salary'])
print(correlation)
plt.figure()
plt.scatter(df['Age'], df['Salary'])
plt.xlabel('Age')
plt.ylabel('Salary')
plt.title('Age vs Salary')
plt.show()
# Observation: If correlation = 0, weak or no relationship
# If positive , salary tends to increase with age
# If negative,salary decreases with age
print("""The scatter plot shows a very weak relationship between age and salary, 
indicating that salary does not strongly depend on age. This suggests that other factors, 
such as team or position, likely have a greater influence on salary levels.""")

