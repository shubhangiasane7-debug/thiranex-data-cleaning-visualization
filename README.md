Data Cleaning and Visualization of Student Performance Dataset

📌 Project Overview

This project focuses on cleaning, analyzing, and visualizing a student performance dataset using Python.

The main objective is to understand the data, check for data-quality issues, identify relationships between variables, and present meaningful insights through visualizations.

🎯 Objectives

- Inspect the dataset structure and data types
- Check and handle missing values
- Check and remove duplicate records
- Detect potential outliers using the IQR method
- Perform basic statistical analysis
- Create meaningful data visualizations
- Identify important patterns and relationships in the data

🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

📂 Dataset

The dataset contains 100 student records with the following attributes:

- Student ID
- Gender
- Study Hours
- Attendance
- Math Score
- Reading Score
- Writing Score

🧹 Data Cleaning

The dataset was checked for:

- Missing values
- Duplicate records
- Data types
- Statistical distribution
- Math score outliers using the IQR method

Data Cleaning Results

- Total records: 100
- Missing values: 0
- Duplicate records: 0
- Math score outliers: 0

Since no missing values, duplicates, or Math Score outliers were found, no records needed to be removed or imputed.

📊 Visualizations

The project generates the following visualizations:

1. Math Score Distribution

"Math Score Distribution" (math_score_distribution.png)

2. Study Hours vs Math Score

"Study Hours vs Math Score" (study_hours_vs_math.png)

3. Math Score by Gender

"Math Score by Gender" (math_score_by_gender.png)

4. Average Score by Subject

"Average Score by Subject" (average_subject_scores.png)

5. Correlation Heatmap

"Correlation Heatmap" (correlation_heatmap.png)

All visualizations are included in the repository.

🔍 Key Insights

- The average Math Score is 80.88.
- The average Reading Score is 82.24.
- The average Writing Score is 81.96.
- The average study time is 4.51 hours.
- The average attendance is 85.27%.
- The correlation between Study Hours and Math Score is 0.98, showing a very strong positive association in this dataset.
- The highest Math Score recorded is 98.

📈 Conclusion

This project demonstrates the basic workflow of data analysis: understanding the dataset, validating and cleaning the data, performing statistical analysis, creating visualizations, and extracting meaningful insights.

The analysis shows that the dataset is already relatively clean, with no missing values, duplicate records, or detected Math Score outliers. The visualizations help communicate important patterns in student performance.

🚀 Future Improvements

- Add an interactive dashboard using Streamlit
- Analyze outliers across all numerical variables
- Include more student attributes
- Apply machine learning models for performance prediction
- Add interactive filters and charts

👩‍💻 Author

Shubhangi Asane

Data Science Internship Project — Thiranex
