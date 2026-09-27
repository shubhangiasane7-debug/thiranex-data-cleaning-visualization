import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("student_performance.csv")

# Display first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Display dataset information
print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

# Check missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Check duplicate records
print("\nNumber of duplicate records:")
print(df.duplicated().sum())

# Basic statistical summary
print("\nStatistical summary:")
print(df.describe())

# Check data types
print("\nData types:")
print(df.dtypes)

# -------------------------------
# DATA CLEANING
# -------------------------------

# Remove duplicate records
df = df.drop_duplicates()

print("\nDuplicates after cleaning:")
print(df.duplicated().sum())

# Check missing values
print("\nMissing values after cleaning:")
print(df.isnull().sum())

# -------------------------------
# OUTLIER DETECTION
# -------------------------------

# Detect outliers using IQR method
Q1 = df["Math_Score"].quantile(0.25)
Q3 = df["Math_Score"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nMath Score Outlier Limits:")
print("Lower Limit:", lower_limit)
print("Upper Limit:", upper_limit)

outliers = df[
    (df["Math_Score"] < lower_limit) |
    (df["Math_Score"] > upper_limit)
]

print("\nNumber of Math Score outliers:")
print(len(outliers))

# -------------------------------
# DATA VISUALIZATION
# -------------------------------


# Create visualization folder if it doesn't exist
os.makedirs("visualizations", exist_ok=True)

# 1. Math Score Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df["Math_Score"], bins=10, kde=True)
plt.title("Math Score Distribution")
plt.xlabel("Math Score")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("visualizations/math_score_distribution.png")
plt.show()


# 2. Study Hours vs Math Score
plt.figure(figsize=(8, 5))
sns.scatterplot(x="Study_Hours", y="Math_Score", data=df)
plt.title("Study Hours vs Math Score")
plt.xlabel("Study Hours")
plt.ylabel("Math Score")
plt.tight_layout()
plt.savefig("visualizations/study_hours_vs_math.png")
plt.show()


# 3. Gender-wise Math Performance
plt.figure(figsize=(8, 5))
sns.boxplot(x="Gender", y="Math_Score", data=df)
plt.title("Math Score by Gender")
plt.xlabel("Gender")
plt.ylabel("Math Score")
plt.tight_layout()
plt.savefig("visualizations/math_score_by_gender.png")
plt.show()


# 4. Average Subject Scores
subject_means = df[
    ["Math_Score", "Reading_Score", "Writing_Score"]
].mean()

plt.figure(figsize=(8, 5))
subject_means.plot(kind="bar")
plt.title("Average Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("visualizations/average_subject_scores.png")
plt.show()


# 5. Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(
    df[[
        "Study_Hours",
        "Attendance",
        "Math_Score",
        "Reading_Score",
        "Writing_Score"
    ]].corr(),
    annot=True,
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig("visualizations/correlation_heatmap.png")
plt.show()

print("\nAll visualizations created successfully!")

# -------------------------------
# DATA INSIGHTS
# -------------------------------

print("\n========== DATA INSIGHTS ==========")

# Average scores
print("\nAverage Scores:")
print("Math:", round(df["Math_Score"].mean(), 2))
print("Reading:", round(df["Reading_Score"].mean(), 2))
print("Writing:", round(df["Writing_Score"].mean(), 2))

# Average study hours
print("\nAverage Study Hours:")
print(round(df["Study_Hours"].mean(), 2))

# Average attendance
print("\nAverage Attendance:")
print(round(df["Attendance"].mean(), 2))

# Gender-wise average math score
print("\nGender-wise Average Math Score:")
print(df.groupby("Gender")["Math_Score"].mean().round(2))

# Correlation between study hours and math score
correlation = df["Study_Hours"].corr(df["Math_Score"])

print("\nCorrelation between Study Hours and Math Score:")
print(round(correlation, 2))

# Highest Math Score
highest_math = df.loc[df["Math_Score"].idxmax()]

print("\nHighest Math Score:")
print(highest_math[["Student_ID", "Gender", "Math_Score"]])

# -------------------------------
# FINAL DATA INSIGHTS
# -------------------------------

print("\n========== FINAL DATA INSIGHTS ==========")

# Average scores
print("\nAverage Scores:")
print("Math Score:", round(df["Math_Score"].mean(), 2))
print("Reading Score:", round(df["Reading_Score"].mean(), 2))
print("Writing Score:", round(df["Writing_Score"].mean(), 2))

# Average study hours and attendance
print("\nAverage Study Hours:", round(df["Study_Hours"].mean(), 2))
print("Average Attendance:", round(df["Attendance"].mean(), 2))

# Gender-wise average Math score
print("\nGender-wise Average Math Score:")
print(df.groupby("Gender")["Math_Score"].mean().round(2))

# Study Hours vs Math Score correlation
correlation = df["Study_Hours"].corr(df["Math_Score"])

print("\nStudy Hours vs Math Score Correlation:")
print(round(correlation, 2))

# Highest Math Score
highest_math = df.loc[df["Math_Score"].idxmax()]

print("\nHighest Math Score:")
print("Student ID:", highest_math["Student_ID"])
print("Gender:", highest_math["Gender"])
print("Math Score:", highest_math["Math_Score"])

print("\n========================================")