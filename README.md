# abs-population-etl
End-to-end ETL pipeline using Australian Bureau of Statistics population data
# ABS Population Data ETL Pipeline

## Overview
This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using real-world population data from the Australian Bureau of Statistics (ABS).
The pipeline converts raw Excel datasets into clean, analysis-ready relational tables stored in PostgreSQL.

The project focuses on data quality, reproducibility, and auditability, following industry-aligned data engineering best practices.

---

## Objectives
- Ingest raw population datasets without modifying source files
- Clean and standardise SA2-level population data
- Apply data validation and integrity checks
- Load structured data into PostgreSQL for analysis
- Maintain a reproducible and auditable project structure

---

## Project Structure

project/
├── raw_data/
│ └── population_by_region.xlsx
│
├── cleaned_data/
│ └── nsw_sa2_population_2023_24.csv
│
├── scripts/
│ ├── 01_extract_clean_nsw.ipynb
│ └── 02_analysis_postgres.ipynb


---

## ETL Process

### Extract
- Source data extracted from ABS Excel files
- Raw files preserved unchanged for traceability

### Transform
- Cleaned headers, missing values, and inconsistent formats using Pandas
- Standardised SA2 identifiers and year fields
- Applied validation checks including row counts and duplicate detection

### Load
- Loaded cleaned datasets into PostgreSQL
- Used SQL queries to validate data integrity and support analysis

---

## Data Validation
- Row count comparison before and after transformation
- Duplicate and null value checks
- Cross-validation against published ABS totals

---

## Tools & Technologies
- Python (Pandas)
- PostgreSQL
- SQL
- Jupyter Notebook
- Git & GitHub

---

## Future Improvements
- Convert notebooks into production-ready Python scripts
- Add incremental load logic
- Parameterise state and year selection
- Introduce scheduling (cron / Airflow-style design)
