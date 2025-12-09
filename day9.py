# ------------------------------
# SALES DATA ANALYSIS PROJECT
# ------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
data = pd.read_csv("Sales Dataset.csv")
print(data.head())

# ------------------------------
# CLEANING THE DATA
# ------------------------------

# Remove unwanted column
data.drop(columns="Unnamed: 0", inplace=True)

# Replace column names with first row values
data.columns = data.loc[0]
data.drop(0, inplace=True)

# Clean Manager column formatting
data['Manager'] = data['Manager'].str.strip().str.replace(r"\s+", " ", regex=True)

# Remove duplicates
data.drop_duplicates(inplace=True)

# Convert datatype
data["Quantity"] = data["Quantity"].astype(float).round().astype(int)
data["Order ID"] = data["Order ID"].astype(int)
data["Price"] = data["Price"].astype(float)
data["Date"] = pd.to_datetime(data["Date"])

# Calculate Revenue
data["Revenue"] = data["Price"] * data["Quantity"]

print(data.info())
print(data.head())

# ------------------------------
# Q1. Most Preferred Payment Method
# ------------------------------

print(data["Payment Method"].value_counts())
data["Payment Method"].value_counts().plot(kind="bar")
plt.title("Most Preferred Payment Method")
plt.show()

# ------------------------------
# Q2. Most Selling Product (By Quantity)
# ------------------------------

qty = data.groupby("Product")["Quantity"].sum().sort_values(ascending=False)
print(qty)

qty_df = qty.reset_index()

plt.figure(figsize=(8,4))
plt.bar(qty_df["Product"], qty_df["Quantity"])
plt.title("Most Selling Product - Quantity")
plt.xticks(rotation=45)
plt.show()

# By Revenue
rev = data.groupby("Product")["Revenue"].sum().sort_values(ascending=False)
print(rev)

rev_df = rev.reset_index()

plt.figure(figsize=(8,4))
plt.bar(rev_df["Product"], rev_df["Revenue"])
plt.title("Most Selling Product - Revenue")
plt.xticks(rotation=45)
plt.show()

# ------------------------------
# Q3. City & Manager with Maximum Revenue
# ------------------------------

print(data.groupby("City")["Revenue"].sum().sort_values(ascending=False))
print(data.groupby("Manager")["Revenue"].sum().sort_values(ascending=False))

# ------------------------------
# Q4. Date-wise Revenue Trend
# ------------------------------

data.plot("Date", "Revenue", linewidth=2)
plt.title("Date-wise Revenue")
plt.show()

# ------------------------------
# Q5. Average Revenue
# ------------------------------

print("Average Revenue:", data["Revenue"].mean())

# ------------------------------
# Q6. Avg Revenue for Nov & Dec
# ------------------------------

data["Month"] = data["Date"].dt.month

m11 = data[data["Month"] == 11]
m12 = data[data["Month"] == 12]

print("Avg Revenue November:", m11["Revenue"].mean())
print("Avg Revenue December:", m12["Revenue"].mean())

# ------------------------------
# Q7. Standard Deviation
# ------------------------------

print("Std Dev - Quantity:", data["Quantity"].std())
print("Std Dev - Revenue:", data["Revenue"].std())

# ------------------------------
# Q8. Variance
# ------------------------------

print("Variance - Quantity:", data["Quantity"].var())
print("Variance - Revenue:", data["Revenue"].var())

# ------------------------------
# Q9. Is revenue increasing or decreasing?
# ------------------------------

print("Total Revenue November:", m11["Revenue"].sum())
print("Total Revenue December:", m12["Revenue"].sum())

# ------------------------------
# Q10. Avg Quantity & Revenue per Product
# ------------------------------

print(
    data.groupby("Product")[["Quantity", "Revenue"]]
    .agg({"Quantity": "mean", "Revenue": "mean"})
)
