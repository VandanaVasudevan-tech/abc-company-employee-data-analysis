# abc-company-employee-data-analysis
ABC Company Employee Data Analysis

📌 Project Overview

This project analyzes an employee dataset from ABC Company, consisting of 458 rows and 9 columns. The goal is to preprocess the dataset, perform exploratory data analysis (EDA), and present insights through visualizations. The analysis focuses on understanding workforce distribution, positions, age groups, salary expenditure, and correlations between employee attributes.

📌Dataset

Number of rows: 458
Number of columns: 9
Columns include: Name, Team, Number, Position, Age, Height, Weight, College, Salary

📌Preprocessing

The Height column contained inconsistent/non-numerical values. It was corrected by replacing all values with random numbers between 150–180 to ensure numerical consistency.

📌Missing values:

College (84 missing) → filled with "Unknown"
Salary (11 missing) → filled with median salary
Data integrity and consistency were verified before analysis.

📌Analysis Tasks & Visualizations

1. Employee Distribution Across Teams
   
Counted the number of employees in each team and calculated percentage contribution.

Visualization:
Bar chart showing number of employees per team.

Insight:
Most teams have a similar number of employees (around 14–16). Some teams like New Orleans Pelicans and Memphis Grizzlies have slightly higher counts, while teams like Minnesota Timberwolves and Orlando Magic have slightly lower counts. Overall, the workforce is fairly balanced across teams.


<img width="1737" height="790" alt="image" src="https://github.com/user-attachments/assets/8bff10d9-e048-4092-87b1-818c37020ab3" />



2. Employee Segregation by Position
   
Employees grouped by positions: PG, SG, SF, PF, C.

Visualization: Bar chart.

Insight:
The number of employees in each position is fairly similar, indicating a balanced workforce. No single position is significantly over- or under-represented.


<img width="743" height="527" alt="image" src="https://github.com/user-attachments/assets/0e096cf6-123c-4fdd-94d7-d79c0c55490f" />



4. Predominant Age Group
   
Employees grouped into age ranges: 18–25, 26–30, 31–35, 36–40, 40+.

Visualization: Bar chart.

Insight:

The 18–25 age group has the highest number of employees, indicating that the workforce is largely composed of young professionals.


<img width="745" height="536" alt="image" src="https://github.com/user-attachments/assets/708c435e-0811-4b14-8cd3-7ad5b3f394ab" />



6. Salary Expenditure by Team and Position
   
Calculated total salary for each team and position.

Visualization: 

Separate bar charts for teams and positions.

Insight:

Team:
Cleveland Cavaliers has the highest total salary expenditure.
Position: 
The C (Center) position has the highest salary expenditure, reflecting higher compensation for that role.


<img width="1491" height="660" alt="image" src="https://github.com/user-attachments/assets/1abd56e6-e00c-41d2-8ac7-2ce2a4a766d9" />

<img width="1500" height="658" alt="image" src="https://github.com/user-attachments/assets/5237c88f-ae3f-4aa6-99cb-5c7c8733b939" />



8. Correlation Between Age and Salary
   
Correlation calculated between Age and Salary.

Visualization: Scatter plot.
Insight:
The scatter plot shows a very weak relationship between age and salary. This indicates that salary is not strongly influenced by age and other factors, such as team or position, likely have a greater impact.


<img width="792" height="631" alt="image" src="https://github.com/user-attachments/assets/748cd78e-9ffe-4b27-a76f-b5d01f3f4a2a" />


📌Technologies Used

Python
Pandas
NumPy
Matplotlib

📌Key Takeaways

Workforce distribution is fairly balanced across teams and positions.
Majority of employees are young professionals (18–25 years).
Salary expenditure is concentrated in certain teams and positions.
Age alone does not strongly affect salary; other factors play a bigger role.

✅ Conclusion

The project successfully demonstrates the use of Python for real-world data preprocessing, analysis, and visualization. The insights derived can help organizations better understand workforce structure and compensation trends.

▶️ How to Run the Project
Clone the repository
git clone https://github.com/your-username/abc-company-employee-data-analysis.git
Install required libraries
pip install pandas  matplotlib numpy
Run the Python script or Jupyter Notebook

