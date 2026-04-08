[![](https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=200&section=header&text=European+Bank+Churn+Analysis&fontSize=42&fontColor=ffffff&fontAlignY=38&desc=End-to-End+Data+Analysis+%7C+Streamlit+Dashboard&descAlignY=58&descSize=16&animation=fadeIn)](https://dataanlysisproject01-europeanbank.streamlit.app/)

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&size=22&pause=1000&color=00D4FF&center=true&vCenter=true&width=600&lines=🚀+European+Bank+Churn+Analysis;📊+Interactive+Streamlit+Dashboard;🐍+Python+%7C+Pandas+%7C+Plotly+%7C+Seaborn;📈+EDA+%7C+KPIs+%7C+Business+Insights)](https://dataanlysisproject01-europeanbank.streamlit.app/)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Live%20App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://dataanlysisproject01-europeanbank.streamlit.app/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org)
[![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Charts-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](https://github.com/Techwithabhi/data_anlysis_project_01/blob/main/LICENSE)

> **🚀 A comprehensive data analysis project on European Bank customer churn — uncovering churn patterns, high-risk segments, geographic trends, and key retention insights through interactive visualizations and a live Streamlit dashboard.**

---

## 🌊 Live Dashboard

[![🚀 Launch Dashboard](https://img.shields.io/badge/🚀%20Launch%20Live%20Dashboard-Click%20Here-00D4FF?style=for-the-badge&labelColor=0f2027)](https://dataanlysisproject01-europeanbank.streamlit.app/)

> **Fully interactive** • **No installation required** • **Real-time exploration**

---

## 📌 Table of Contents

- [🎯 Project Overview](#-project-overview)
- [📂 Repository Structure](#-repository-structure)
- [📊 Dataset Overview](#-dataset-overview)
- [🔍 Key Metrics & KPIs](#-key-metrics--kpis)
- [📈 Analysis & Charts](#-analysis--charts)
- [🛠️ Tech Stack](#%EF%B8%8F-tech-stack)
- [⚡ Quick Start](#-quick-start)
- [🖥️ Dashboard Features](#%EF%B8%8F-dashboard-features)
- [💡 Key Insights](#-key-insights)
- [👤 Connect With Me](#-connect-with-me)

---

## 🎯 Project Overview

[![](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,2,5,30&height=3&section=header)](https://dataanlysisproject01-europeanbank.streamlit.app/)

The **European Bank Customer Churn Analysis** project is an end-to-end data analysis solution that dives deep into customer behavior and churn patterns across a European bank. Using Python's powerful data science ecosystem, this project transforms raw customer records into actionable business intelligence through:

- 🔍 **Exploratory Data Analysis (EDA)** — Uncovering hidden churn patterns in customer data
- 📊 **Statistical Summaries** — Descriptive statistics, correlations, and distributions
- 🗺️ **Visual Storytelling** — Rich charts and graphs for every key metric
- 🌐 **Interactive Dashboard** — A deployed Streamlit app for live data exploration
- 💡 **Business Insights** — Actionable recommendations to improve customer retention

---

## 📂 Repository Structure

```
📦 data_anlysis_project_01/
├── 📁 dashboard/                           # Streamlit Dashboard Application
├── 📁 data/                                # Raw & Processed Datasets
├── 📁 notebooks/                           # Jupyter Notebooks (EDA + Analysis)
├── 📁 reports/                             # Analysis Reports & Summaries
├── 📁 research/                            # Research Notes & References
├── 📁 sql/                                 # SQL Queries (optional analysis)
├── 📁 src/                                 # Source Python Scripts
├── 📄 requirements.txt                     # Python Dependencies
├── 📄 runtime.txt                          # Python Runtime Version
├── 📄 run_command.txt                      # Run Instructions
└── 📄 README.md                            # Project Documentation
```

---

## 📊 Dataset Overview

The dataset captures detailed customer records from a European bank with 10,000 rows of banking activity and demographics.

| Feature | Description | Type |
|---|---|---|
| `CustomerId` | Unique customer identifier | `int` |
| `Surname` | Customer surname | `string` |
| `CreditScore` | Customer credit score | `int` |
| `Geography` | Country (France / Germany / Spain) | `categorical` |
| `Gender` | Male / Female | `categorical` |
| `Age` | Customer age | `int` |
| `Tenure` | Years with the bank | `int` |
| `Balance` | Account balance | `float` |
| `NumOfProducts` | Number of bank products used | `int` |
| `HasCrCard` | Has credit card (0/1) | `binary` |
| `IsActiveMember` | Active member status (0/1) | `binary` |
| `EstimatedSalary` | Estimated annual salary | `float` |
| `Exited` | Churned (1) or Retained (0) | `binary` |

---

## 🔍 Key Metrics & KPIs

| 📦 Metric | 📈 Value | 🔎 Description |
|---|---|---|
| **Total Customers** | 10,000 records | Full dataset volume analyzed |
| **Overall Churn Rate** | ~20% | Percentage of customers who exited |
| **Highest Churn Geography** | Germany (~32%) | Country with most churn |
| **Most At-Risk Segment** | Senior customers (~49%) | Age group with highest churn rate |
| **Inactive vs Active Churn** | 2x higher for inactive | Engagement-based churn multiplier |
| **High-Value Customer Churn** | ~25% | Churn rate among premium customers |
| **Avg. Account Balance** | Computed across segments | Mean balance per churned vs retained |
| **Top Retention Risk Factor** | Low activity + Germany | Combined churn risk signal |

---

## 📈 Analysis & Charts

The analysis covers the following visual explorations generated in the Jupyter Notebook and rendered live in the dashboard:

### 📊 Distribution Analysis

```
✅ Age distribution of churned vs retained customers (histogram + KDE)
✅ Credit score distribution by churn status
✅ Account balance spread across geographies
✅ Salary distribution across customer segments
```

### 🔗 Correlation & Relationships

```
✅ Heatmap — Correlation matrix of numeric features
✅ Scatter plot — Balance vs. credit score by churn label
✅ Box plot — Age distribution per churn category
✅ Pair plot — Multi-variable relationship matrix
```

### 🌍 Geographic & Demographic Intelligence

```
✅ Bar chart — Churn rate by country (France, Germany, Spain)
✅ Grouped bar — Churn by gender across geographies
✅ Donut chart — Customer distribution by geography
✅ Stacked bar — Product usage vs. churn behavior
```

### 📅 Behavioral & Engagement Trends

```
✅ Tenure vs. churn rate trend line
✅ Active vs. inactive member churn comparison
✅ Number of products vs. churn rate analysis
✅ Credit card ownership impact on churn
```

### 🚦 Operational & Risk Metrics

```
✅ High-value customer churn breakdown (pie chart)
✅ Churn rate by age group (horizontal bar)
✅ Risk segment classification (stacked bar)
✅ Retention opportunity matrix per segment
```

---

## 🛠️ Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Language** | ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white) | Core programming language |
| **Notebook** | ![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white) | Interactive EDA environment |
| **Data Wrangling** | ![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white) | Data manipulation & analysis |
| **Numerical** | ![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat-square&logo=numpy&logoColor=white) | Numerical computations |
| **Visualization** | ![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat-square) | Static charting library |
| **Visualization** | ![Seaborn](https://img.shields.io/badge/-Seaborn-4C9BE8?style=flat-square) | Statistical visualizations |
| **Interactive Charts** | ![Plotly](https://img.shields.io/badge/-Plotly-3F4F75?style=flat-square&logo=plotly&logoColor=white) | Interactive chart rendering |
| **Dashboard** | ![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) | Web app & dashboard framework |
| **Deployment** | ![Streamlit Cloud](https://img.shields.io/badge/-Streamlit%20Cloud-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) | Live cloud deployment |

---

## ⚡ Quick Start

Follow these steps to run the project locally:

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Techwithabhi/data_anlysis_project_01.git
cd data_anlysis_project_01
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # On macOS/Linux
venv\Scripts\activate           # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Jupyter Notebook

```bash
cd notebooks
jupyter notebook
```

### 5️⃣ Launch the Streamlit Dashboard Locally

```bash
streamlit run dashboard/app.py
```

> 🌐 Or simply visit the **[Live Dashboard](https://dataanlysisproject01-europeanbank.streamlit.app/)** — no setup required!

---

## 🖥️ Dashboard Features

The live Streamlit app offers:

- 🎛️ **Interactive Filters** — Filter by geography, gender, age group, and activity status
- 📊 **Dynamic Charts** — All plots update in real-time based on filter selections
- 📋 **Raw Data View** — Explore the underlying dataset with search & sort
- 📥 **Download Options** — Export filtered data as CSV
- 📱 **Responsive Layout** — Works seamlessly across desktop and mobile
- 🌙 **Dark/Light Mode** — Adapts to system theme preference

---

## 💡 Key Insights

> Derived from the European Bank Customer Churn Analysis:

```
📌 INSIGHT 1 — Overall churn rate stands at ~20%
   → 1 in 5 customers exits, representing significant revenue loss potential

📌 INSIGHT 2 — Germany has the highest churn rate (~32%)
   → Geographic targeting essential for region-specific retention strategies

📌 INSIGHT 3 — Senior customers (50+) show ~49% churn rate
   → Age-targeted programs needed to retain this high-risk demographic

📌 INSIGHT 4 — Inactive members are ~2x more likely to churn
   → Engagement campaigns could cut churn rate significantly

📌 INSIGHT 5 — High-value customers (high balance) still churn at ~25%
   → Premium retention plans required for top-tier customer segments
```

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

---

## 👤 Connect With Me

[![](https://capsule-render.vercel.app/api?type=rect&color=gradient&customColorList=0,2,2,5,30&height=3)](https://techwithabhi.github.io/)

**Abhi Sarkar** — *Data Analyst | Python Developer | Tech Enthusiast*

[![Portfolio](https://img.shields.io/badge/🌐%20Portfolio-techwithabhi.github.io-00D4FF?style=for-the-badge&labelColor=0f2027)](https://techwithabhi.github.io/)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-techwithabhi-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/techwithabhi/)
[![Instagram](https://img.shields.io/badge/Instagram-i__am__abhi__sarkar-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/i_am_abhi_sarkar/)
[![Dashboard](https://img.shields.io/badge/🚀%20Live%20App-European%20Bank%20Dashboard-FF4B4B?style=for-the-badge)](https://dataanlysisproject01-europeanbank.streamlit.app/)

[![](https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=120&section=footer&animation=fadeIn)](https://techwithabhi.github.io/)

*"Turning raw data into meaningful stories — one analysis at a time."*