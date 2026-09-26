# 🚀 TrendPulse — Live Trend Data Pipeline

> **Collect • Clean • Analyse • Visualise • Discover Trends 📊**

TrendPulse is a Python-based data pipeline project that transforms live trending data into meaningful insights and visualizations.

The project follows a complete data workflow:

**🌐 Data Collection → 🧹 Data Processing → 🔍 Data Analysis → 📊 Visualization**

---

## 🎯 Project Overview

TrendPulse demonstrates how raw trend data can be collected from an online source, cleaned and processed using Python, analysed to identify patterns, and finally transformed into easy-to-understand visualizations.

The project is divided into four independent tasks, with each Python script representing one stage of the pipeline.

---

## 🧩 Project Tasks

### 1️⃣ Data Collection

**File: [task1_data_collection.py](https://github.com/sangarikumar/trendpulse-Sangari/blob/main/task1_data_collection.py)**

Collects trending data from an online source using Python and stores the raw data in CSV format.

#### Key Activities:
- Connect to the trend data source
- Define topics to monitor
- Collect recent trend information
- Store the collected data
- Export the raw dataset to CSV

**Output: trends_20260926.json**

### 2️⃣ Data Processing

**File: [task2_data_processing.py](https://github.com/sangarikumar/trendpulse-Sangari/blob/main/task2_data_processing.py)**

Cleans and prepares the collected data for analysis.

#### Key Activities:
- Load the raw CSV dataset
- Convert date values
- Remove duplicate records
- Handle missing values
- Sort the dataset
- Export the cleaned dataset

**Output: trends_clean.csv**

### 3️⃣ Data Analysis

**File: [task3_analysis.py](https://github.com/sangarikumar/trendpulse-Sangari/blob/main/task3_analysis.py)**

Analyses the processed data to identify important trends and patterns.

#### Key Activities:
- Calculate average trend interest
- Calculate maximum trend interest
- Identify the most popular topic
- Generate analysis results
- Export the results to CSV

**Output: trends_analysed.csv**

### 4️⃣ Data Visualization

***File: [task4_visualization.py](https://github.com/sangarikumar/trendpulse-Sangari/blob/main/task4_visualization.py)**

Converts the analysed data into visual insights using charts.

#### Key Activities:
- Load processed data
- Plot trend changes over time
- Compare different topics
- Add chart titles and labels
- Generate a visual trend report

**Outputs:** 
1. chart1_top_stories.png
2. chart2_categories.png
3. chart3_scatter.png
4. dashboard.png

---

### 📊 Pipeline Outputs
| **File** | **Description** |
|----------|-----------------|
| trends_20260926.json |	Raw collected trend data |
| trends_clean.csv	| Processed and cleaned data |
| trends_analysed.csv | Analytical results |
| chart1_top_stories.png, chart2_categories.png, chart3_scatter.png, dashboard.png | Trend visualization |

---

### 📈 Visualization

The visualization stage presents the trend data in an easy-to-understand graphical format.

The chart can be used to identify:

1. 📈 Changes in interest over time
2. 🔥 Topics with higher interest
3. 📊 Differences between topics
4. 📉 Changes and fluctuations in trends

---

### 🛠️ Technologies Used

This project demonstrates the complete workflow of a Python data pipeline.

| **Technology** | **Purpose** |
|------------|---------|
| 🐍 Python	| Core programming language |
| 🐼 Pandas |	Data processing and analysis |
| 📈 Matplotlib |	Data visualization |
| 🔎 PyTrends |	Trend data collection |
| 🌐 GitHub |	Source code hosting |
| 💻 PyCharm | Development environment |

---

### 🔄 End-to-End Workflow

       LIVE DATA
           │
           ▼
    ┌─────────────┐
    │   COLLECT   │
    └──────┬──────┘
           │
           ▼
      RAW DATA
           │
           ▼
    ┌─────────────┐
    │   PROCESS   │
    └──────┬──────┘
           │
           ▼
     CLEAN DATA
           │
           ▼
    ┌─────────────┐
    │   ANALYSE   │
    └──────┬──────┘
           │
           ▼
      INSIGHTS
           │
           ▼
    ┌─────────────┐
    │ VISUALIZE   │
    └──────┬──────┘
           │
           ▼
       📊 CHARTS

---

### 🌟 Project Highlights

**🔹 Real-World Data**

Works with trend information collected from an online data source.

**🔹 Automated Pipeline**

The four Python scripts represent a complete data workflow from collection to visualization.

**🔹 Reproducible**

The project can be recreated by installing the dependencies and running the scripts in sequence.

**🔹 Beginner-Friendly**

The project demonstrates fundamental concepts of data science and Python without requiring a complex infrastructure.

---

### 🚀 Future Improvements

Possible future enhancements include:

- 📡 Add more live data sources
- 🤖 Apply machine learning for trend prediction
- 📊 Add interactive dashboards
- 🗄️ Store data in a database
- ⏰ Schedule automatic data collection
- 📧 Add automated trend alerts
- 🌐 Build a web dashboard

---

### ⭐ Final Takeaway

TrendPulse transforms raw trending data into clean datasets, meaningful analysis, and visual insights.

🌐 Collect → 🧹 Clean → 🔍 Analyse → 📊 Visualise

That's the TrendPulse journey. 🚀

---

### 👩‍💻 Author
Sivasangari Selvakumar

**GitHub:**
https://github.com/sangarikumar

---

### 📌 Repository

**🔗 TrendPulse GitHub Repository**

[https://github.com/sangarikumar/trendpulse-Sangari](https://github.com/sangarikumar/trendpulse-Sangari.git)

---
