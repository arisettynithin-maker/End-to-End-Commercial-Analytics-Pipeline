# End-to-End Commercial Analytics Pipeline

Commercial and vendor performance analytics project that transforms raw transaction data into decision-ready reporting for partner review, performance analysis, and commercial action.

## Project Overview

This repository is structured as an end-to-end analytics workflow rather than a single notebook exercise. It shows how commercial data can be ingested, standardised, analysed, and presented in a way that supports business decisions around vendor performance, margin quality, inventory risk, and concentration exposure.

The implementation combines Python, notebook analysis, and Power BI output to reflect a realistic BI and analytics workflow.

## Business Problem

Commercial teams often work with fragmented raw data that makes it difficult to answer questions such as:

- which vendors actually drive profitable growth
- where inventory value is getting stuck
- where procurement or partner concentration creates risk
- which partners should be scaled, reviewed, optimised, or exited

Without a clean analytical layer, those decisions are slower and less reliable.

## Solution / Approach

This project builds a commercial analytics pipeline that:

- ingests and structures raw transactional inputs
- creates consistent summary tables for downstream use
- defines core commercial KPIs and margin logic
- supports notebook-based analysis for partner decisioning
- presents results in Power BI and executive-ready report outputs

The emphasis is on metric integrity, analytical clarity, and decision support.

## Tech Stack

- Python
- Jupyter Notebooks
- SQL-style business logic
- Power BI

## Key Features

- Data ingestion layer for curated analysis-ready datasets
- Vendor and brand-level summary generation
- KPI development across sales, purchases, profit, margin, and unsold inventory
- Decision-oriented notebook analysis
- Dashboard and report outputs for stakeholder review

## Outputs / Dashboard / Documents

This repository includes:

- analytical notebooks in `notebooks/`
- reusable scripts in `src/`
- Power BI assets in `powerbi/`
- executive materials in `report/`

Key output files:

- `powerbi/partner_performance.pbix`
- `powerbi/Dashboard Snip.jpeg`
- `report/Final Analysis Report.pdf`

## Business Impact / Insights

This project is useful because it mirrors the kind of analytical work that supports commercial decisions in real operating environments:

- improves visibility into vendor and brand performance
- highlights margin quality, not just top-line sales
- surfaces inventory and capital lock-up issues
- supports structured partner review and action recommendations

It positions analytics as part of commercial governance, not just reporting.

## Repository Structure

```text
.
├── README.md
├── notebooks/
│   ├── 01_Commercial_Partner_Summary.ipynb
│   └── 02_Commercial_Patner_Decision_Analysis.ipynb
├── powerbi/
│   ├── Dashboard Snip.jpeg
│   └── partner_performance.pbix
├── report/
│   ├── Final Analysis Report.pdf
│   └── Vendor Performance & Commercial Efficiency Analysis.pptx
└── src/
    ├── Ingestion_db.py
    └── get_partner_summary.py
```

## How to Run

```bash
jupyter notebook
```

Open the notebooks in sequence, then review the Power BI and report outputs for the presentation layer of the project.

## Future Improvements

- add a `requirements.txt` file for faster local setup
- add sample input data or a documented synthetic dataset
- package KPI logic into a more reusable pipeline module
- add more README screenshots from the Power BI layer
