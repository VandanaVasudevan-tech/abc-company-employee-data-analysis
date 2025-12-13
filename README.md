# abc-company-employee-data-analysis
📊 ABC Company Employee Data Analysis
📌 Project Overview

This project involves analyzing an employee dataset from ABC Company containing 458 records and 9 attributes. The goal is to preprocess the data, perform exploratory data analysis (EDA), and visualize key insights related to employee distribution, salary trends, and demographics across various teams.


📂 Dataset Description

The dataset includes the following information:
Employee Name
Team
Position
Age
Height
Weight
College
Salary
The data required preprocessing due to missing values and inconsistent formatting.

🛠️ Tools & Technologies Used
Python
Pandas – data manipulation and cleaning
Matplotlib – data visualization
Seaborn – statistical visualizations

🔄 Data Preprocessing Steps

The following preprocessing steps were performed:

Identified and handled missing values:
Filled missing College values with "Unknown"
Filled missing Salary values using the median
Resolved Excel auto-formatting issues in the Height column
Converted height values stored as dates into numeric inches
Checked for duplicate records
Ensured correct data types for all columns

📊 Exploratory Data Analysis (EDA)

Key analyses performed include:
Employee distribution across teams
Average salary by position
Salary distribution among employees
Relationship between age and salary


Each visualization is accompanied by clear observations to support insights.

🔍 Key Insights

Employee distribution across teams is fairly balanced
Centers have the highest average salary among positions
Salary distribution is right-skewed, with a few high earners
Salary tends to increase with age, though variations exist



📈 Visualizations

<img width="1746" height="743" alt="image" src="https://github.com/user-attachments/assets/e8d261d9-5188-4251-a8f9-8cc30a8f469d" />

<img width="792" height="600" alt="image" src="https://github.com/user-attachments/assets/99721611-c838-4352-885b-25c8b87611a6" />

<img width="992" height="627" alt="image" src="https://github.com/user-attachments/assets/388ff30d-ba9d-4f77-8643-084ff0b24638" />

<img width="992" height="626" alt="image" src="https://github.com/user-attachments/assets/2fdb8fc0-677b-4c1d-9fee-bfa2a4cc418a" />



✅ Conclusion

The project successfully demonstrates the use of Python for real-world data preprocessing, analysis, and visualization. The insights derived can help organizations better understand workforce structure and compensation trends.

▶️ How to Run the Project
Clone the repository
git clone https://github.com/your-username/abc-company-employee-data-analysis.git
Install required libraries
pip install pandas  matplotlib seaborn
Run the Python script or Jupyter Notebook

