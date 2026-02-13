Project Title

Weather Data Cleaning and Preprocessing using Python & Pandas

*Project Description

This project focuses on cleaning, preprocessing, and analyzing a structured weather dataset using Python.
The dataset contains weather-related parameters such as temperature, humidity, pressure, wind speed, rainfall, UV index, and visibility collected for multiple cities.

The goal of this project is to:

Load raw weather data from CSV files

Detect and handle missing values

Identify and remove duplicate records

Standardize timestamp formats

Sort and organize the dataset

Generate a cleaned dataset ready for analysis

This project demonstrates practical data cleaning skills used in real-world Data Science and Data Analytics workflows.

*Files

- Azure_Weather_2025_Extended.csv
- Azure_Weather_2025_Cleaned.csv
- clean_weather.py

*Technologies Used

Python 3.x
Pandas
NumPy
VS Code
Git & GitHub

 *Project Structure
Weather-data/
├── Azure_Weather_2025_Extended.csv     # Raw Dataset
├── Azure_Weather_2025_Cleaned.csv      # Cleaned Dataset
├── clean_weather.py                    # Data Cleaning Script
└── README.md                           # Project Documentation

 *Dataset Features

The dataset includes the following columns:

City

Date

Timestamp

Avg_Temperature_C

Avg_Humidity_Percent

Avg_Pressure_hPa

Avg_Wind_Speed_km_h

Total_Rain_mm

UV_Index

Visibility_km

*Data Cleaning Process
Step 1: Load Dataset
df = pd.read_csv("Azure_Weather_2025_Extended.csv")

Step 2: Convert Timestamp
df["Timestamp"] = pd.to_datetime(df["Timestamp"])

Step 3: Sort Data
df = df.sort_values(by="Timestamp")

Step 4: Find Duplicates
df[df.duplicated()]

Step 5: Remove Duplicates
df = df.drop_duplicates()

Step 6: Check Missing Values
df.isnull().sum()

Step 7: Save Cleaned File
df.to_csv("Azure_Weather_2025_Cleaned.csv", index=False)

*Learning Outcomes

Through this project, I learned:

Practical data preprocessing techniques

Handling structured datasets using Pandas

Managing CSV files in Python

Using Git for version control

Uploading projects to GitHub

Writing professional documentation


