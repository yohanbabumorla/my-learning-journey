# 📅 Day 6 – Introduction to Pandas: Series & DataFrames

## 🔁 Recap

You've already covered:
- ✅ NumPy fundamentals: array math, reshaping, broadcasting
- ✅ Random data generation and manipulation

Now, it's time to organize and explore real-world datasets using **Pandas** — think of it as Excel for Python, but way more powerful.

---

## 🎯 Learning Objectives

By the end of this module, you’ll be able to:
- Understand Pandas Series and DataFrames
- Create and explore labeled data structures
- Access, modify, and summarize data efficiently

---

## 🧠 What is Pandas?

**Pandas** is a Python library for data analysis.

```bash
pip install pandas


import pandas as pd


Core Structures:
- Series: 1D labeled array (like a single column)
- DataFrame: 2D labeled table (like an Excel sheet)

📊 Series – One-Dimensional Data
marks = pd.Series([85, 90, 75, 60, 95],
                  index=['Yohan', 'Ravi', 'Anu', 'Teja', 'Kiran'])


Accessing Data:
marks['Yohan']
marks[1:3]


Use Series for single features like marks, salary, or age.

🧾 DataFrame – Two-Dimensional Data
data = {
    'Name': ['Yohan', 'Ravi', 'Anu', 'Teja'],
    'Age': [20, 21, 19, 22],
    'Marks': [85, 90, 75, 60]
}

df = pd.DataFrame(data)


Accessing Columns & Rows:
df['Name']
df[['Name', 'Marks']]
df.iloc[0]     # First row
df.loc[2]      # Row with label 2



✏️ Column Operations
df['Grade'] = ['A', 'A+', 'B', 'C']         # Add new column
df['Marks'] = df['Marks'] + 5              # Modify values



📈 Descriptive Statistics
df.describe()   # Summary of numeric columns
df.info()       # Data types and null info
df.shape        # (rows, columns)
df.columns      # Column names



📂 Reading External Data
df = pd.read_csv('students.csv')
df.head()       # First 5 rows
df.tail()       # Last 5 rows



🧩 Practice Task
data = {
    'Product': ['Phone', 'Laptop', 'Tablet', 'Watch'],
    'Price': [50000, 70000, 30000, 15000],
    'Quantity': [5, 3, 7, 10]
}

df = pd.DataFrame(data)

# 1. Add TotalValue column
df['TotalValue'] = df['Price'] * df['Quantity']

# 2. Average price
print(df['Price'].mean())

# 3. First and last 2 rows
print(df.head(2))
print(df.tail(2))

# 4. Update Watch price
df.loc[df['Product'] == 'Watch', 'Price'] = 12000

# 5. Info and summary
df.info()
df.describe()



❓ Reflection Prompts
- What’s the difference between a Series and a DataFrame?
- How do you access the first three rows of a DataFrame?
- What method gives a quick statistical summary?
- How do you add a new column to a DataFrame?
