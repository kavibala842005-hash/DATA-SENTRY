import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="DataSentry",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 DataSentry")
st.subheader("Explainable Data Quality & Decision Assistant")

st.write(
    "Upload your dataset to identify data quality issues "
    "and understand what needs attention."
)

st.info("DataSentry helps you inspect your data before making decisions.")

uploaded_file = st.file_uploader(
    "Upload your CSV or Excel file",
    type=["csv", "xlsx"]
)

if uploaded_file is not None:
    try:
        if uploaded_file.name.lower().endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            st.success("File uploaded successfully!")

        ## DATA QUALITY DASHBOARD ##
        st.subheader("📈 Data Quality Dashboard")
        total_rows = len(df)
        total_columns = len(df.columns)
        total_missing = int(df.isnull().sum().sum())
        total_duplicates = int(df.duplicated().sum())

        total_cells = df.shape[0] * df.shape[1]

        if total_cells > 0:
            missing_score = (total_missing / total_cells) * 100
            duplicate_score = (
                total_duplicates / total_rows * 100
                if total_rows > 0 else 0
            )

            quality_score = max(
                0,
                round(100 - missing_score - duplicate_score, 2)
            )
        else:
            quality_score = 0

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Total Rows", total_rows)
        col2.metric("Total Columns", total_columns)
        col3.metric("Missing Values", total_missing)
        col4.metric("Duplicate Rows", total_duplicates)

        ##DATASET PREVIEW
        st.subheader("📊 Dataset Preview")

        ##MISSING VALUES REPORT
        st.subheader("🔍 Missing Values Report")

        missing_values = df.isnull().sum()

        missing_report = missing_values[missing_values > 0]

        if not missing_report.empty:
            st.warning("Missing values detected!")

            st.dataframe(
                missing_report.rename("Missing Count").reset_index().rename(
                    columns={"index": "Column"}
                ),
                use_container_width=True
            )
        else:
            st.success("No missing values found!")


        ##DUPLICATE ROWS REPORT
        st.subheader("🔁 Duplicate Rows Report")

        duplicate_count = df.duplicated().sum()

        if duplicate_count > 0:
            st.warning(f"{duplicate_count} duplicate row(s) detected!")

            duplicate_rows = df[df.duplicated(keep=False)]

            st.dataframe(
                duplicate_rows,
                use_container_width=True
            )
        else:
            st.success("No duplicate rows found!")

        ##SUSPICIOUS VALUES REPORT    
        st.subheader("⚠️ Suspicious Values Report")

        if "Age" in df.columns:
            age_numeric = pd.to_numeric(df["Age"], errors="coerce")

            suspicious_ages = df[
                age_numeric.notna() & ((age_numeric < 0) | (age_numeric > 100))
            ]

            if not suspicious_ages.empty:
                st.warning("Suspicious age values detected!")
                st.dataframe(suspicious_ages, use_container_width=True)
            else:
                st.success("No suspicious age values found!")
        else:
            st.info("No Age column found. Age validation was skipped.")
        st.dataframe(df.head(10), use_container_width=True)

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Rows", df.shape[0])

        with col2:
            st.metric("Total Columns", df.shape[1])


        ##SAFE DATA CLEANING PREVIEW
        st.subheader("🧹 Safe Data Cleaning Preview")

        st.write(
            "Choose cleaning actions below. "
            "Your original uploaded dataset will remain unchanged."
        )

        cleaned_df = df.copy()

        remove_duplicates = st.checkbox("Remove duplicate rows")
        remove_missing = st.checkbox("Remove rows containing missing values")

        if remove_duplicates:
            cleaned_df = cleaned_df.drop_duplicates()

        if remove_missing:
            cleaned_df = cleaned_df.dropna()

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Original Rows", len(df))

        with col2:
            st.metric("Cleaned Rows", len(cleaned_df))


        ##PREVIEW OF CLEANED DATASET
        st.write("Preview of cleaned dataset:")
        st.dataframe(cleaned_df, use_container_width=True)

        st.download_button(
            label="Download Cleaned CSV",
            data=cleaned_df.to_csv(index=False).encode("utf-8"),
            file_name="datasentry_cleaned_data.csv",
            mime="text/csv"
        )


        ##COLUMN DATA PROFILE
        st.subheader("📋 Column Data Profile")

        profile = pd.DataFrame({
            "Column": df.columns,
            "Data Type": [str(dtype) for dtype in df.dtypes],
            "Missing Count": df.isnull().sum().values,
            "Missing Percentage (%)": (
                df.isnull().mean() * 100
            ).round(2).values,
            "Unique Values": df.nunique().values
        })

        st.dataframe(profile, use_container_width=True)

        ##DOWNLOAD DATA QUALITY REPORT
        st.subheader("📥 Download Data Quality Report")

        issue_report = pd.DataFrame([
            {
                "Issue": "Missing Values",
                "Count": int(df.isnull().sum().sum()),
                "Description": "Empty cells found in the dataset"
            },
            {
                "Issue": "Duplicate Rows",
                "Count": int(df.duplicated().sum()),
                "Description": "Repeated records found in the dataset"
            }
        ])

        st.dataframe(issue_report, use_container_width=True)

        st.download_button(
            label="Download Quality Report",
            data=issue_report.to_csv(index=False).encode("utf-8"),
            file_name="datasentry_quality_report.csv",
            mime="text/csv"
        )


    except Exception as e:
        st.error(f"Unable to read file: {e}")