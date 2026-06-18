# Data Quality Monitor

A Streamlit-based clinical data quality monitoring dashboard that processes CSV/Excel audit data and displays interactive Plotly visualisations across three analysis tabs: Trend Analysis, Issue Breakdown, and Raw Records.

---

## Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web application framework |
| `pandas` | Data loading and manipulation |
| `plotly` | Interactive charts and visualisations |
| `numpy` | Numerical operations |
| `openpyxl` | Read `.xlsx` Excel files |
| `xlrd` | Read legacy `.xls` Excel files |

All packages are pure Python and install via `pip`.

---

## Installation

### Consolidated (recommended)

```bash
pip install streamlit pandas plotly numpy openpyxl xlrd
```

### Individual commands

```bash
pip install streamlit
pip install pandas
pip install plotly
pip install numpy
pip install openpyxl
pip install xlrd
```

### From a `requirements.txt` file

Create `requirements.txt` in the project root:

```
streamlit>=1.35.0
pandas>=2.0.0
plotly>=5.20.0
numpy>=1.26.0
openpyxl>=3.1.0
xlrd>=2.0.1
```

Then install:

```bash
pip install -r requirements.txt
```

---

## Project Structure

```text
medical-dashboard/
├── app.py
├── requirements.txt
├── Data_to_Transform.csv
│
├── assets/
│   ├── css/
│   │   └── dashboardfonts.css
│   └── js/
│       └── table.js
│
├── charts/
│   ├── tab_breakdown.py
│   ├── tab_rawdata.py
│   ├── tab_trend.py
│   ├── utils.py
│   └── __init__.py
│
├── config/
│   ├── theme.py
│   └── __init__.py
│
├── data/
│   ├── loader.py
│   └── __init__.py
│
└── ui/
    ├── components.py
    ├── popup.py
    ├── styles.py
    └── __init__.py
```

---
## Setup & Execution

### 1. Clone or copy the project files

Ensure `app.py` and `dashboardfonts.css` are in the same folder.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Streamlit will print a local URL (default `http://localhost:8501`). Open it in any browser.

### 5. Upload data

On the landing page, upload a **CSV or Excel (`.xlsx` / `.xls`)** file. The file must contain the seven required columns listed below (column names are matched case-insensitively and underscore/space variants are accepted). Any additional columns in the file are silently ignored.

---

## Required Columns

The dashboard resolves column names through an alias map, so exact casing and delimiter style do not matter. The canonical names and their accepted aliases are:

| Canonical Name | Accepted aliases (examples) |
|---|---|
| `Unique Key` | `PK_ISBT_LABELS_MONITOR_AUDIT`, `unique_key` |
| `Validation Type` | `VALIDATION_TYPE`, `validationtype` |
| `Record Count` | `RECORD_COUNT`, `recordcount` |
| `Is issue found` | `IS_ISSUE_FOUND`, `isissuefound` |
| `Affected Table Name` | `AFFTECTED_TABLE_NAME`, `affected_table_name` |
| `Verified Date` | `VERIFIED_DATETIME`, `verified_date` |
| `Created On` | `CREATED_ON`, `createdon` |

Files with **extra columns** (e.g. `Department`, `Owner`, `Comments`, `Batch ID`) are accepted without error — extra columns are ignored entirely.

Validation fails **only** when one or more required columns are absent.

---

## Date Format

`Verified Date` and `Created On` must be in `DD-Mon-YY` format (e.g. `18-May-25`, `05-Sep-24`). Rows with unparseable dates are coerced to `NaT` and excluded from date-based filters.

---

## Sidebar Controls

| Control | Description |
|---|---|
| 🌙 Dark Mode | Toggle between dark and light themes |
| 📂 Change File | Return to the upload screen |
| 📅 Year / 🗓 Month | Scope data to a specific year or month |
| ⏱ Timeline | Preset date ranges or custom range picker |
| Affected Tables | Multi-select filter by table name |
| Validation Types | Multi-select filter by validation type |
| Issues only | Show only rows flagged with issues |

---

## Troubleshooting

**`FileNotFoundError: dashboardfonts.css`** — Run `streamlit run app.py` from the directory containing both files, not a parent directory.

**Columns not recognised** — Check that your file contains all seven required column names (or valid aliases). The error message lists which canonical names were not resolved.

**Date parsing warnings** — Rows with dates outside `DD-Mon-YY` format are silently dropped from charts. Verify date formatting in the source file.

**Excel file not loading** — `.xlsx` requires `openpyxl`; `.xls` requires `xlrd`. Both are included in the install command above.
