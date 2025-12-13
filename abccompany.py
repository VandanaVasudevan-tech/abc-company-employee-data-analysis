import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import datetime

df = pd.read_excel('ABC Company.xlsx')
# Observation: In college there are 84 missing values, dropping 84 rows removes a lot of useful data so filled it with
# "Unknown".
df['College'].fillna('Unknown', inplace=True)

# Observation: Salary is filled with median as median is safer than mean because salary usually has outliers.
df['Salary'].fillna(df['Salary'].median(), inplace=True)

# print(df.dtypes)


# Observation: Due to Excel’s automatic formatting, height values were incorrectly stored as date objects.
# These were identified and converted into numerical height values (in inches) using a custom transformation
# to maintain data consistency.
def fix_height(val):
    if pd.isna(val):
        return None

    # Handle Excel date (datetime or Timestamp)
    if isinstance(val, (pd.Timestamp, datetime.datetime)):
        feet = val.day      # 6
        inches = val.month  # 2 (Feb)
        return feet * 12 + inches

    val = str(val)

    # Handle normal height like '7-0'
    if '-' in val:
        parts = val.split('-')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            feet = int(parts[0])
            inches = int(parts[1])
            return feet * 12 + inches

    return None


df['Height_inches'] = df['Height'].apply(fix_height)
# print(df[['Height', 'Height_inches']].head(15))
# Old column has been dropped
df.drop(columns=['Height'], inplace=True)
# print(df.isnull().sum())

# Employee distribution by Team
team_count = df['Team'].value_counts()
print(team_count)

# Employee distribution by Position
print(df['Position'].value_counts())


plt.figure(figsize=(14, 6))
sns.countplot(x='Team', data=df)
plt.xticks(rotation=90)
plt.title("Employee Distribution by Team")
plt.tight_layout()
plt.show()
# Observation : The employee distribution across teams is fairly uniform, with most teams having approximately
# 14 to 16 employees. A few teams have slightly higher employee counts, but no extreme imbalance is observed.
# This indicates that the company maintains a balanced workforce structure across different teams.

plt.figure()
sns.barplot(x='Position', y='Salary', data=df)
plt.xticks(rotation=90)
plt.title("Average Salary by Position")
plt.show()
# Observation: The average salary varies significantly across positions.
# Centers receive the highest average salary, while Shooting Guards earn the lowest.
# Point Guards and Small Forwards have comparable salary levels, indicating that player
# position plays a key role in determining compensation.


plt.figure(figsize=(8, 5))
sns.histplot(df['Salary'], kde=True)
plt.title("Salary Distribution of Employees")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()
# Observation: The salary distribution is right-skewed, indicating that most employees earn salaries in the lower
# to midrange, while a small number of employees receive significantly higher salaries.


plt.figure(figsize=(8, 5))
sns.scatterplot(x='Age', y='Salary', data=df)
plt.title("Age vs Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
plt.tight_layout()
plt.show()
# Observation: The scatter plot shows a general trend where salary tends to increase with age,
# suggesting that experience may positively influence employee compensation.
# However, there is noticeable variation, indicating that age alone does not determine salary.


