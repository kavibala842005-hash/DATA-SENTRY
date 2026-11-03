# 🔎 DataSentry – Explainable Data Quality & Decision Assistant

**DataSentry** is a Python-based data quality assistant built using Streamlit. It helps users upload CSV and Excel datasets, identify common data quality issues, preview cleaned data, and download quality reports.

## 🚀 Features

- 📂 **Dataset Upload:** Upload CSV and Excel files.
- 📊 **Dataset Preview:** View uploaded dataset records.
- 🔍 **Missing Value Detection:** Identify missing values in datasets.
- 🔁 **Duplicate Detection:** Find duplicate records.
- ⚠️ **Suspicious Value Detection:** Identify suspicious age values.
- 📈 **Data Quality Dashboard:** Display dataset statistics and a basic quality score.
- 🧹 **Data Cleaning:** Preview cleaned datasets by removing duplicates and missing-value rows.
- 📋 **Column Data Profiling:** View data types, missing counts, missing percentages, and unique values.
- 📥 **Report Download:** Download data quality reports and cleaned CSV files.

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- OpenPyXL

## 📁 Project Structure

```text
DATA-SENTRY/
│
├── app.py
├── SAMPLE_DATA.csv
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/kavibala842005-hash/DATA-SENTRY.git
```

### 2. Navigate to the Project Folder

```bash
cd DATA-SENTRY
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Required Libraries

```bash
pip install pandas openpyxl streamlit
```

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📊 How It Works

1. Upload a CSV or Excel dataset.
2. Preview the uploaded data.
3. Check missing values and duplicate records.
4. Identify suspicious age values.
5. Review the data quality dashboard.
6. Preview cleaning operations.
7. Download the cleaned dataset and quality report.

## 🎯 Project Objective

The objective of DataSentry is to simplify dataset quality inspection and help users identify common data issues before performing data analysis or making data-driven decisions.

## 👩‍💻 Developed By

**Kavibala S**

GitHub: https://github.com/kavibala842005-hash

---

*DataSentry – Making Data Quality Inspection Simpler.*

