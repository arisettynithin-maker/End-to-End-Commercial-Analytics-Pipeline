# End-to-End Commercial Analytics Pipeline

An end-to-end **commercial & vendor performance analytics project** that demonstrates how raw transactional data can be ingested, transformed, analysed, and converted into **decision-ready insights** using Python, SQL-style logic, Jupyter Notebooks, and Power BI.

This repository is designed to mirror **real-world analytics workflows** used in large organisations (e.g. supply chain, fintech-adjacent commercial teams), with a strong focus on **data quality, metric integrity, and business decisioning**.

---

## 🔍 Business Objective

The goal of this project is to answer **commercial decision questions** such as:

* Which vendors and brands drive the majority of sales and profit?
* Where is capital locked in unsold inventory?
* Which partners should be **scaled, optimised, renegotiated, or exited**?
* How concentrated is procurement risk across top vendors?
* Are high sales always correlated with high margins?

The output is a **single source of truth commercial dataset**, analytical notebooks, and an **executive-ready Power BI dashboard**.

---

## 🗂 Repository Structure

```
End-to-End-Commercial-Analytics-Pipeline/
│
├── notebooks/
│   ├── 01_Commercial_Partner_Summary.ipynb
│   └── 02_Commercial_Partner_Decision_Analysis.ipynb
│
├── get_partner_summary.py
├── Ingestion_db.py
├── README.md
```
---

## Repository Structure
- notebooks/: Exploratory and decision-focused analysis
- outputs/figures/: Key visual outputs used in reporting
- outputs/tables/: Final analytical datasets
- powerbi/: Interactive dashboard and snapshots
- report/: Executive-ready PDF report and PPT Presentation
- src/: Reusable data processing and utility scripts

---

## ⚙️ Data Pipeline Overview

### 1️⃣ Data Ingestion (`Ingestion_db.py`)

* Handles ingestion of cleaned Pandas DataFrames into a SQLite database
* Abstracts database write logic using reusable functions
* Mimics how analytical datasets are materialised into warehouse tables

**Key Concepts Demonstrated:**

* Reusable ingestion utilities
* Separation of data engineering and analysis layers
* Logging-ready, production-style Python scripts

---

### 2️⃣ Commercial Partner Summary (`get_partner_summary.py`)

This script creates the **core analytical dataset** used across notebooks and dashboards.

It:

* Merges purchases, sales, pricing, freight, and inventory tables
* Computes business-critical metrics such as:

  * Total Sales & Purchases
  * Gross Profit & Profit Margin
  * Unsold Inventory Value (locked capital)
  * Sales-to-Purchase Ratios
  * Vendor & Brand-level aggregations

**Why this matters:**
This file represents **metric governance** — ensuring every downstream analysis uses consistent, validated commercial logic.

---

## 📊 Analytical Notebooks

### 📘 01 – Commercial Partner Summary

Focus: **Data validation, KPI creation, and descriptive analytics**

Key steps:

* Data loading from the curated summary table
* Summary statistics & sanity checks
* Vendor and brand-level aggregations
* Contribution analysis (Top vendors / brands)
* Identification of concentration risk

This notebook ensures the dataset is **analysis-ready and decision-safe**.

---

### 📕 02 – Commercial Partner Decision Analysis

Focus: **Insight generation & decision framing**

Key analyses:

* Low vs high performing vendor identification
* Margin vs sales behaviour analysis
* Unsold capital risk assessment
* Correlation analysis between key commercial metrics
* Rule-based vendor action tagging (Scale / Optimise / Review / Exit)

This notebook moves beyond charts into **business recommendations**.

---

## 📈 Power BI Dashboard

The Power BI dashboard brings all insights together into an **executive-friendly view**.

### Key Highlights:

* **Total Sales:** $441.41M
* **Total Purchases:** $307.34M
* **Gross Profit:** $134.07M
* **Profit Margin:** 38.7%
* **Unsold Capital:** $2.71M

### Visuals Include:

* Vendor purchase contribution (% concentration)
* Top vendors and brands by sales
* Low-performing vendors and brands
* Margin vs sales scatter for risk/opportunity detection

This dashboard is designed for **commercial leaders, category managers, and finance stakeholders**.

---

## 🧠 Key Insights Generated

* A small group of vendors contributes **~65% of total purchases**, highlighting procurement concentration risk
* High sales do not always translate to high margins
* Several vendors lock significant capital in unsold inventory despite reasonable sales
* Clear segmentation emerges between vendors to **scale vs optimise vs exit**

---

## 🛠 Tools & Skills Demonstrated

* **Python:** Pandas, NumPy, logging, modular scripting
* **SQL-style Analytics:** CTEs, joins, aggregations, metric engineering
* **Data Quality:** sanity checks, filtering, consistency validation
* **Jupyter Notebooks:** structured EDA and decision storytelling
* **Power BI:** executive dashboards, KPIs, commercial visuals
* **Analytics Thinking:** translating data into business actions

---

## 🚀 Why This Project Matters

This project is intentionally built to reflect **real commercial analytics work**, not just academic EDA:

* End-to-end pipeline (ingestion → metrics → insights → dashboard)
* Strong emphasis on **decision usability**, not just visuals
* Clear separation between engineering, analysis, and reporting layers

It is suitable for roles such as:

* Data Analyst / Senior Data Analyst
* Commercial Analytics Analyst
* Business Intelligence Analyst
* Product / Operations Analytics

---

**Author:** Nithin Arisetty
**Focus:** Commercial Analytics | Data Quality | Decision Intelligence
