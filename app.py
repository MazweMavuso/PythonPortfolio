import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Excel Data Insights", layout="wide")

st.title("📊 Excel Data Insights App")

# Upload file
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx", "xls"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.subheader("Preview of Data")
    st.dataframe(df.head())

    # Insights
    st.subheader("🔍 Basic Insights")
    st.write(f"**Rows:** {df.shape[0]}")
    st.write(f"**Columns:** {df.shape[1]}")
    st.write("**Column Data Types:**")
    st.write(df.dtypes)
    st.write("**Missing Values per Column:**")
    st.write(df.isnull().sum())
    st.write("**Basic Statistics:**")
    st.write(df.describe())

    # Numeric columns → histograms + correlation
    numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
    if len(numeric_cols) > 0:
        st.subheader("📈 Numeric Column Distributions")
        for col in numeric_cols:
            fig, ax = plt.subplots()
            sns.histplot(df[col].dropna(), kde=True, ax=ax)
            ax.set_title(f"Distribution of {col}")
            st.pyplot(fig)

        st.subheader("🔗 Correlation Heatmap")
        fig, ax = plt.subplots(figsize=(8, 6))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

    # Categorical columns → bar charts
    categorical_cols = df.select_dtypes(include=['object']).columns
    if len(categorical_cols) > 0:
        st.subheader("📊 Categorical Column Distributions")
        for col in categorical_cols:
            fig, ax = plt.subplots()
            df[col].value_counts().plot(kind="bar", ax=ax)
            ax.set_title(f"Count of {col}")
            st.pyplot(fig)
