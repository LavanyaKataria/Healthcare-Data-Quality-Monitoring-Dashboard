<div align="center">

# 🩺 Healthcare Data Quality Monitoring Dashboard

**A browser-based analytics application that converts raw healthcare validation audit logs into structured, interactive, decision-ready intelligence.**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-%E2%89%A51.35-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-%E2%89%A55.20-3F4F75?style=flat-square&logo=plotly&logoColor=white)](https://plotly.com/)
[![Pandas](https://img.shields.io/badge/Pandas-%E2%89%A52.0-150458?style=flat-square&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Status](https://img.shields.io/badge/Status-Complete-2E7D32?style=flat-square)](#)
[![License](https://img.shields.io/badge/License-Academic-6c757d?style=flat-square)](#license)

Developed during a Data Analyst internship at **Aithent Technologies Pvt. Ltd.**, Gurugram

</div>

---

### 📑 Contents

[Overview](#overview) · [Key Features](#key-features) · [Tech Stack](#tech-stack) · [Architecture](#architecture) · [Engineering Challenges](#engineering-challenges) · [Getting Started](#getting-started) · [Data Schema](#data-schema) · [Sidebar Controls](#sidebar-controls) · [Troubleshooting](#troubleshooting) · [Results](#results)

---

<a id="overview"></a>
## Overview

Healthcare validation scripts generate large volumes of audit logs that are hard to interpret in their raw form. This dashboard automates ingestion, cleaning, and visualization of those logs — replacing a manual, Excel-based review process with a self-service, browser-based tool for non-technical users. It scales to any volume of validation records and adapts to varying validation-rule and table counts across source systems.

## ✨ Key Features

- **Automated file ingestion** — CSV, XLSX, and XLS uploads with UTF-8/Latin-1 encoding fallback
- **Column normalization engine** — resolves 30+ naming variants (case, spacing, typos) via an alias-lookup system, so the pipeline never breaks on inconsistent headers
- **KPI summary cards** — total checks, issues found, clean checks, and total affected records
- **Trend analysis** — daily pass/fail activity and cumulative affected records over time (bar/line/area, WebGL-rendered)
- **Issue breakdown** — categorical analysis by validation type and affected table (bar, horizontal bar, pie, donut, scatter)
- **Drill-down popups** — click any chart element to inspect the underlying records in a paginated, sortable, searchable table
- **Dark/light theme system** — a single CSS custom-property token system drives Streamlit components, Plotly charts, and iframe-embedded tables in sync
- **Hierarchical filters** — year, month, and custom date-range filtering

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| Web Framework | Streamlit ≥ 1.35 |
| Visualization | Plotly ≥ 5.20 (WebGL) |
| Data Processing | Pandas ≥ 2.0, NumPy ≥ 1.26 |
| Excel Support | openpyxl, xlrd |
| Styling | CSS3 custom properties |
| Client Logic | JavaScript (ES6), MutationObserver |

## 🏗️ Architecture

The application follows a layered, modular architecture — refactored from an initial monolithic prototype into a 13-file package with zero functional regression:

```
medical-dashboard/
├── app.py                      # Entry point: config, sidebar, tab routing
├── requirements.txt
├── Data_to_Transform.csv
│
├── assets/
│   ├── css/
│   │   └── dashboardfonts.css   # Font definitions
│   └── js/
│       └── table.js              # Paginated JS table engine
│
├── charts/
│   ├── tab_trend.py              # Trend Analysis tab
│   ├── tab_breakdown.py          # Issue Breakdown tab
│   ├── tab_rawdata.py            # Raw Records tab
│   ├── utils.py                  # Shared chart helpers
│   └── __init__.py
│
├── config/
│   ├── theme.py                  # Dark/light palettes, Plotly layout builders
│   └── __init__.py
│
├── data/
│   ├── loader.py                 # Ingestion, column normalization, date parsing
│   └── __init__.py
│
└── ui/
    ├── components.py             # KPI cards, chart type selectors
    ├── popup.py                  # Drill-down popup modal
    ├── styles.py                 # CSS injection / theme tokens
    └── __init__.py
```

**Data flow:** upload → `loader.py` normalizes columns and parses dates → sidebar filters applied in `app.py` → active tab module renders Plotly charts from the filtered DataFrame → chart click events trigger record-level drill-down popups.

## ⚙️ Notable Engineering Challenges

| Challenge | Solution |
|---|---|
| Inconsistent column naming across exports (`AFFTECTED` vs `AFFECTED`, mixed case/spacing) | Alias-lookup normalization engine handling 30+ known variants |
| Non-standard `DD-MMM-YY` date format not handled by default Pandas inference | Explicit `strptime` parsing with year expansion and `NaT` fallback |
| Sort dropdown clipped inside an iframe-embedded table | JS `MutationObserver` to detect dropdown state and dynamically resize the iframe |
| Streamlit's native theme switcher conflicting with the custom CSS token system | Targeted `!important` overrides to neutralize native theming |
| Monolithic-to-modular refactor without breaking functionality | Incremental, module-by-module extraction with regression testing after each step |

## 🚀 Getting Started

### 1. Clone or copy the project files

Ensure `app.py` and `dashboardfonts.css` stay in their existing relative locations within the project folder.

### 2. Install dependencies

**Consolidated (recommended)**
```bash
pip install streamlit pandas plotly numpy openpyxl xlrd
```

**Or from `requirements.txt`**
```bash
pip install -r requirements.txt
```

<details>
<summary>Individual install commands</summary>

```bash
pip install streamlit
pip install pandas
pip install plotly
pip install numpy
pip install openpyxl
pip install xlrd
```
</details>

### 3. Run the application

```bash
streamlit run app.py
```

Streamlit prints a local URL (default `http://localhost:8501`) — open it in any browser.

### 4. Upload data

On the landing page, upload a CSV or Excel (`.xlsx` / `.xls`) file. The file must contain the seven required columns listed below — column names are matched **case-insensitively**, and underscore/space variants are accepted. Any additional columns are silently ignored.

## 📋 Data Schema

### Required columns

The dashboard resolves column names through an alias map, so exact casing and delimiter style don't matter.

| Canonical Name | Accepted alias examples |
|---|---|
| `Unique Key` | `PK_ISBT_LABELS_MONITOR_AUDIT`, `unique_key` |
| `Validation Type` | `VALIDATION_TYPE`, `validationtype` |
| `Record Count` | `RECORD_COUNT`, `recordcount` |
| `Is issue found` | `IS_ISSUE_FOUND`, `isissuefound` |
| `Affected Table Name` | `AFFTECTED_TABLE_NAME`, `affected_table_name` |
| `Verified Date` | `VERIFIED_DATETIME`, `verified_date` |
| `Created On` | `CREATED_ON`, `createdon` |

Files with extra columns (e.g. `Department`, `Owner`, `Comments`, `Batch ID`) are accepted without error. Validation fails only when one or more required columns are absent — the resulting error message lists exactly which canonical names couldn't be resolved.

### Date format

`Verified Date` and `Created On` are expected in **`DD-Mon-YY`** format (e.g. `18-May-25`, `05-Sep-24`), but the parser also accepts general date strings as a fallback (e.g. `2025-05-18`, `05/18/2025`, `May 18, 2025`). Rows with dates that still can't be parsed are coerced to `NaT` and excluded from date-based filters.

## 🎛️ Sidebar Controls

| Control | Description |
|---|---|
| 🌙 Dark Mode | Toggle between dark and light themes |
| 📂 Change File | Return to the upload screen |
| 📅 Year / 🗓 Month | Scope data to a specific year or month |
| ⏱ Timeline | Preset date ranges or custom range picker |
| Affected Tables | Multi-select filter by table name |
| Validation Types | Multi-select filter by validation type |
| Issues only | Show only rows flagged with issues |

## 🩹 Troubleshooting

| Issue | Fix |
|---|---|
| `FileNotFoundError: dashboardfonts.css` | Run `streamlit run app.py` from the directory containing both files, not a parent directory |
| Columns not recognised | Check that your file contains all seven required column names (or valid aliases) — the error message lists which canonical names were not resolved |
| Date parsing warnings | Rows with dates that don't match `DD-Mon-YY` or a common fallback format are silently dropped from charts; verify date formatting in the source file |
| Excel file not loading | `.xlsx` requires `openpyxl`; `.xls` requires `xlrd` — both are included in the install command above |

## 📈 Results

- Delivered a production-ready, 13-module Streamlit application (~2,000+ lines) within a small timeline
- Identified the highest-impact validation rule as responsible for a disproportionate share of affected records relative to its check volume, directly informing remediation priority
- Reduced quality-review effort from manual, per-file Excel inspection to real-time, filterable, drill-down analysis

---

<div align="center">

## 👤 Author

**Lavanya Kataria**



