import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import Tk, filedialog
import streamlit as st

# Step 1: Let user upload Excel file
Tk().withdraw()  # hide tkinter root window
file_path = filedialog.askopenfilename(
    title="Select an Excel file", 
    filetypes=[("Excel files", "*.xlsx *.xls")]
)

# Step 2: Read the Excel file
df = pd.read_excel(file_path)
print("\nPreview of the data:")
print(df.head())

# Step 3: Basic insights
print("\n--- Insights ---")
print(f"Number of rows: {df.shape[0]}")
print(f"Number of columns: {df.shape[1]}")
print("\nColumn Data Types:")
print(df.dtypes)
print("\nMissing Values per Column:")
print(df.isnull().sum())
print("\nBasic Statistics:")
print(df.describe())

# Step 4: Automatically generate some graphs
# Numeric columns → histograms + correlation
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
if len(numeric_cols) > 0:
    st.subheader("📈 Numeric Column Distributions")
    cols = st.columns(2)  # show 2 graphs side by side
    for i, col in enumerate(numeric_cols):
        with cols[i % 2]:
            fig, ax = plt.subplots(figsize=(5, 3))
            sns.histplot(df[col].dropna(), kde=True, ax=ax)
            ax.set_title(f"{col} Distribution")
            st.pyplot(fig)

    with st.expander("🔗 Correlation Heatmap"):
        fig, ax = plt.subplots(figsize=(7, 5))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

# Categorical columns → bar charts
categorical_cols = df.select_dtypes(include=['object']).columns
if len(categorical_cols) > 0:
    st.subheader("📊 Categorical Column Distributions")
    cols = st.columns(2)  # 2 per row
    for i, col in enumerate(categorical_cols):
        with cols[i % 2]:
            fig, ax = plt.subplots(figsize=(5, 3))
            df[col].value_counts().head(10).plot(kind="bar", ax=ax)  # top 10
            ax.set_title(f"{col} (Top 10)")
            st.pyplot(fig)

