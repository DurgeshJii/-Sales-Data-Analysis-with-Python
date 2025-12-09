# -Sales-Data-Analysis-with-Python
This repository contains a complete end-to-end Sales Data Analysis workflow performed on a restaurant’s sales dataset. The objective is to clean raw data, perform exploratory analysis, extract insights, and visualize trends.


📁 Project Structure
├── Sales Dataset.csv  
├── Day 9 Project.pdf  (Complete analysis notes)
├── notebook.ipynb     (Python code)
└── README.md

🧹 1. Data Cleaning Performed

Removed unwanted columns

Renamed incorrect column headers

Removed first row containing metadata

Stripped and normalized Manager name inconsistencies

Converted data types:

Order ID → int

Price → float

Quantity → float → rounded → int

Date → datetime

Removed duplicate rows

📈 2. Exploratory Data Analysis
✔ Payment Method Analysis

Credit Card – 120 transactions

Cash – 76

Gift Card – 58

✔ Product Performance

Most sold product (quantity): Beverages (34,988)

Highest revenue product: Burgers (₹376,943.82)

✔ City & Manager Performance

Top city: Lisbon

Top manager: Joao Silva

✔ Revenue Trends

Calculated date-wise revenue

Compared monthly performance (Nov vs Dec)

December revenue was significantly higher

📊 3. Statistical Analysis

Avg revenue: ₹3028.73

Standard deviation:

Quantity: 214.97

Revenue: 2419.93

Variance calculated for both fields

Computed average quantity & revenue per product

📉 4. Visualizations

Bar plots for:

Payment method distribution

Product sales by quantity

Product revenue comparison

Line plot for date-wise revenue trend

🛠 Tech Stack

Python

Pandas

Matplotlib

Seaborn

NumPy

🎯 Outcome

This project demonstrates a complete real-world data analysis pipeline — from raw data cleaning to business insight generation, suitable for roles in Data Analytics and Business Intelligence.
