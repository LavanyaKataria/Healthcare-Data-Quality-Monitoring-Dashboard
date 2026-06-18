# # import streamlit as st
# # import pandas as pd

# # _ALIASES = {
# #     "Unique Key": [
# #         "unique key",
# #         "pk isbt labels monitor audit",
# #         "unique_key",
# #         "pk_isbt_labels_monitor_audit",
# #     ],
# #     "Validation Type": [
# #         "validation type",
# #         "validation_type",
# #         "validationtype",
# #     ],
# #     "Record Count": [
# #         "record count",
# #         "record_count",
# #         "recordcount",
# #     ],
# #     "Is issue found": [
# #         "is issue found",
# #         "is_issue_found",
# #         "isissuefound",
# #     ],
# #     "Affected Table Name": [
# #         "affected table name",
# #         "afftected table name",
# #         "affected_table_name",
# #         "afftected_table_name",
# #         "affectedtablename",
# #         "afftectedtablename",
# #     ],
# #     "Verified Date": [
# #         "verified date",
# #         "verified_date",
# #         "verifieddate",
# #         "verified datetime",
# #         "verified_datetime",
# #         "verifieddatetime",
# #     ],
# #     "Created On": [
# #         "created on",
# #         "created_on",
# #         "createdon",
# #     ],
# # }

# # _REQUIRED_COLS = [
# #     "Unique Key",
# #     "Validation Type",
# #     "Record Count",
# #     "Is issue found",
# #     "Affected Table Name",
# #     "Verified Date",
# #     "Created On",
# # ]


# # def _build_rename_map() -> dict:
# #     lookup = {}
# #     for canonical, aliases in _ALIASES.items():
# #         for alias in aliases:
# #             key = " ".join(alias.strip().lower().replace("_", " ").split())
# #             lookup[key] = canonical
# #     return lookup


# # _RENAME_LOOKUP = _build_rename_map()


# # def _normalise_columns(df: pd.DataFrame) -> tuple:
# #     """
# #     Returns (normalised_df, display_labels) where display_labels is a dict
# #     mapping canonical column name -> original column name as it appeared in the file.
# #     """
# #     seen_canonical: dict = {}
# #     cols_to_drop: list = []
# #     rename_map: dict = {}
# #     display_labels: dict = {}   # canonical -> original name from file

# #     for raw_col in df.columns:
# #         key = " ".join(str(raw_col).strip().lower().replace("_", " ").split())
# #         canonical = _RENAME_LOOKUP.get(key)

# #         if canonical is None:
# #             continue

# #         if canonical in seen_canonical:
# #             cols_to_drop.append(raw_col)
# #         else:
# #             seen_canonical[canonical] = raw_col
# #             rename_map[raw_col] = canonical
# #             # Store the original name (stripped) for display
# #             display_labels[canonical] = canonical

# #     if cols_to_drop:
# #         df = df.drop(columns=cols_to_drop)

# #     df = df.rename(columns=rename_map)

# #     missing = [c for c in _REQUIRED_COLS if c not in df.columns]
# #     if missing:
# #         raise ValueError(
# #             f"Missing required columns after normalisation:\n  {missing}\n\n"
# #             f"Columns found in file:\n  {df.columns.tolist()}"
# #         )

# #     return df, display_labels


# # @st.cache_data
# # def load_data(file):
# #     name = file.name.lower()
# #     if name.endswith(".xlsx") or name.endswith(".xls"):
# #         df = pd.read_excel(
# #             file,
# #             engine="openpyxl" if name.endswith(".xlsx") else "xlrd",
# #         )
# #     else:
# #         df = pd.read_csv(file)

# #     df.columns = df.columns.str.strip()
# #     df, display_labels = _normalise_columns(df)

# #     df["Verified Date"] = pd.to_datetime(df["Verified Date"], format="%d-%b-%y", errors="coerce")
# #     df["Created On"]    = pd.to_datetime(df["Created On"],    format="%d-%b-%y", errors="coerce")
# #     df["Is issue found"]  = df["Is issue found"].str.strip().str.upper()
# #     df["Has Issue"]        = df["Is issue found"] == "N"
# #     df["Validation Short"] = df["Validation Type"].str.replace("VALIDATE_", "", regex=False)
# #     df["Year"] = df["Verified Date"].dt.year
# #     return df, display_labels








# # import streamlit as st
# # import pandas as pd
# # import io


# # _ALIASES = {
# #     "Unique Key": [
# #         "unique key",
# #         "pk isbt labels monitor audit",
# #         "unique_key",
# #         "pk_isbt_labels_monitor_audit",
# #     ],
# #     "Validation Type": [
# #         "validation type",
# #         "validation_type",
# #         "validationtype",
# #     ],
# #     "Record Count": [
# #         "record count",
# #         "record_count",
# #         "recordcount",
# #     ],
# #     "Is issue found": [
# #         "is issue found",
# #         "is_issue_found",
# #         "isissuefound",
# #     ],
# #     "Affected Table Name": [
# #         "affected table name",
# #         "afftected table name",
# #         "affected_table_name",
# #         "afftected_table_name",
# #         "affectedtablename",
# #         "afftectedtablename",
# #     ],
# #     "Verified Date": [
# #         "verified date",
# #         "verified_date",
# #         "verifieddate",
# #         "verified datetime",
# #         "verified_datetime",
# #         "verifieddatetime",
# #     ],
# #     "Created On": [
# #         "created on",
# #         "created_on",
# #         "createdon",
# #     ],
# # }

# # _REQUIRED_COLS = [
# #     "Unique Key",
# #     "Validation Type",
# #     "Record Count",
# #     "Is issue found",
# #     "Affected Table Name",
# #     "Verified Date",
# #     "Created On",
# # ]


# # def _build_rename_map() -> dict:
# #     lookup = {}
# #     for canonical, aliases in _ALIASES.items():
# #         for alias in aliases:
# #             key = " ".join(alias.strip().lower().replace("_", " ").split())
# #             lookup[key] = canonical
# #     return lookup


# # _RENAME_LOOKUP = _build_rename_map()


# # def _normalise_columns(df: pd.DataFrame) -> tuple:
# #     """
# #     Returns (normalised_df, display_labels) where display_labels maps
# #     canonical column name -> original column name as it appeared in the file.

# #     - Equivalent column names (e.g. PK_ISBT_LABELS_MONITOR_AUDIT, UNIQUE_KEY,
# #       Unique Key) are all recognised as the same field.
# #     - The displayed header is always the original name from the file.
# #     - Extra/unknown columns (e.g. VERIFIED_QUERY, AFFTECTED_PRIMARY_KEY) are
# #       silently ignored and never shown in the UI.
# #     """
# #     seen_canonical: dict = {}
# #     cols_to_drop: list = []
# #     rename_map: dict = {}
# #     display_labels: dict = {}

# #     for raw_col in df.columns:
# #         key = " ".join(str(raw_col).strip().lower().replace("_", " ").split())
# #         canonical = _RENAME_LOOKUP.get(key)

# #         if canonical is None:
# #             continue  # unknown / extra column — skip silently

# #         if canonical in seen_canonical:
# #             cols_to_drop.append(raw_col)  # duplicate — drop
# #         else:
# #             seen_canonical[canonical] = raw_col
# #             rename_map[raw_col] = canonical
# #             display_labels[canonical] = str(raw_col).strip()

# #     if cols_to_drop:
# #         df = df.drop(columns=cols_to_drop)

# #     df = df.rename(columns=rename_map)

# #     missing = [c for c in _REQUIRED_COLS if c not in df.columns]
# #     if missing:
# #         raise ValueError(
# #             f"Missing required columns after normalisation:\n  {missing}\n\n"
# #             f"Columns found in file:\n  {df.columns.tolist()}"
# #         )

# #     return df, display_labels


# # def _parse_dates(series: pd.Series) -> pd.Series:
# #     """
# #     Try common date formats in order, returning the first that parses cleanly.
# #     Handles both 2-digit years (17-May-25) and 4-digit years (17-MAY-2025),
# #     as well as ISO and slash-separated formats.
# #     """
# #     for fmt in ("%d-%b-%Y", "%d-%b-%y", "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"):
# #         parsed = pd.to_datetime(series, format=fmt, errors="coerce")
# #         if parsed.notna().sum() > 0:
# #             return parsed
# #     # Last resort: let pandas infer the format
# #     return pd.to_datetime(series, format="mixed", errors="coerce")


# # @st.cache_data
# # def load_data(file):
# #     name = file.name.lower()

# #     if name.endswith(".xlsx") or name.endswith(".xls"):
# #         df = pd.read_excel(
# #             file,
# #             engine="openpyxl" if name.endswith(".xlsx") else "xlrd",
# #         )
# #     else:
# #         # Try UTF-8 first; fall back to latin-1 for files that contain
# #         # non-UTF-8 bytes such as \xa0 (non-breaking space) in column names.
# #         raw = file.read()
# #         try:
# #             df = pd.read_csv(io.BytesIO(raw), encoding="utf-8")
# #         except UnicodeDecodeError:
# #             df = pd.read_csv(io.BytesIO(raw), encoding="latin-1")

# #     df.columns = df.columns.str.strip()
# #     df, display_labels = _normalise_columns(df)

# #     df["Verified Date"]    = _parse_dates(df["Verified Date"])
# #     df["Created On"]       = _parse_dates(df["Created On"])
# #     df["Is issue found"]   = df["Is issue found"].str.strip().str.upper()
# #     df["Has Issue"]        = df["Is issue found"] == "N"
# #     df["Validation Short"] = df["Validation Type"].str.replace("VALIDATE_", "", regex=False)
# #     df["Year"]             = df["Verified Date"].dt.year

# #     return df, display_labels










# import streamlit as st
# import pandas as pd
# import io


# _ALIASES = {
#     "Unique Key": [
#         "unique key",
#         "pk isbt labels monitor audit",
#         "unique_key",
#         "pk_isbt_labels_monitor_audit",
#     ],
#     "Validation Type": [
#         "validation type",
#         "validation_type",
#         "validationtype",
#     ],
#     "Record Count": [
#         "record count",
#         "record_count",
#         "recordcount",
#     ],
#     "Is issue found": [
#         "is issue found",
#         "is_issue_found",
#         "isissuefound",
#     ],
#     "Affected Table Name": [
#         "affected table name",
#         "afftected table name",
#         "affected_table_name",
#         "afftected_table_name",
#         "affectedtablename",
#         "afftectedtablename",
#     ],
#     "Verified Date": [
#         "verified date",
#         "verified_date",
#         "verifieddate",
#         "verified datetime",
#         "verified_datetime",
#         "verifieddatetime",
#     ],
#     "Created On": [
#         "created on",
#         "created_on",
#         "createdon",
#     ],
# }

# _REQUIRED_COLS = [
#     "Unique Key",
#     "Validation Type",
#     "Record Count",
#     "Is issue found",
#     "Affected Table Name",
#     "Verified Date",
#     "Created On",
# ]


# def _build_rename_map() -> dict:
#     lookup = {}
#     for canonical, aliases in _ALIASES.items():
#         for alias in aliases:
#             key = " ".join(alias.strip().lower().replace("_", " ").split())
#             lookup[key] = canonical
#     return lookup


# _RENAME_LOOKUP = _build_rename_map()


# def _normalise_columns(df: pd.DataFrame) -> tuple:
#     """
#     Returns (normalised_df, display_labels) where display_labels maps
#     canonical column name -> original column name as it appeared in the file.

#     - Equivalent column names (e.g. PK_ISBT_LABELS_MONITOR_AUDIT, UNIQUE_KEY,
#       Unique Key) are all recognised as the same field.
#     - The displayed header is always the original name from the file.
#     - Extra/unknown columns (e.g. VERIFIED_QUERY, AFFTECTED_PRIMARY_KEY) are
#       silently ignored and never shown in the UI.
#     """
#     seen_canonical: dict = {}
#     cols_to_drop: list = []
#     rename_map: dict = {}
#     display_labels: dict = {}

#     for raw_col in df.columns:
#         key = " ".join(str(raw_col).strip().lower().replace("_", " ").split())
#         canonical = _RENAME_LOOKUP.get(key)

#         if canonical is None:
#             continue  # unknown / extra column — skip silently

#         if canonical in seen_canonical:
#             cols_to_drop.append(raw_col)  # duplicate — drop
#         else:
#             seen_canonical[canonical] = raw_col
#             rename_map[raw_col] = canonical
#             display_labels[canonical] = str(raw_col).strip()

#     if cols_to_drop:
#         df = df.drop(columns=cols_to_drop)

#     df = df.rename(columns=rename_map)

#     missing = [c for c in _REQUIRED_COLS if c not in df.columns]
#     if missing:
#         raise ValueError(
#             f"Missing required columns after normalisation:\n  {missing}\n\n"
#             f"Columns found in file:\n  {df.columns.tolist()}"
#         )

#     return df, display_labels


# def _parse_dates(series: pd.Series) -> pd.Series:
#     """
#     Try common date formats in order, returning the first that parses cleanly.
#     Handles both 2-digit years (17-May-25) and 4-digit years (17-MAY-2025),
#     as well as ISO and slash-separated formats.
#     """
#     for fmt in ("%d-%b-%Y", "%d-%b-%y", "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"):
#         parsed = pd.to_datetime(series, format=fmt, errors="coerce")
#         if parsed.notna().sum() > 0:
#             return parsed
#     # Last resort: let pandas infer the format
#     return pd.to_datetime(series, format="mixed", errors="coerce")


# @st.cache_data
# def load_data(file):
#     name = file.name.lower()

#     if name.endswith(".xlsx") or name.endswith(".xls"):
#         df = pd.read_excel(
#             file,
#             engine="openpyxl" if name.endswith(".xlsx") else "xlrd",
#         )
#     else:
#         # Try UTF-8 first; fall back to latin-1 for files that contain
#         # non-UTF-8 bytes such as \xa0 (non-breaking space) in column names.
#         raw = file.read()
#         try:
#             df = pd.read_csv(io.BytesIO(raw), encoding="utf-8")
#         except UnicodeDecodeError:
#             df = pd.read_csv(io.BytesIO(raw), encoding="latin-1")

#     df.columns = df.columns.str.strip()
#     df, display_labels = _normalise_columns(df)

#     df["Verified Date"]    = _parse_dates(df["Verified Date"])
#     df["Created On"]       = _parse_dates(df["Created On"])
#     df["Is issue found"]   = df["Is issue found"].str.strip().str.upper()
#     df["Has Issue"]        = df["Is issue found"] == "N"
#     df["Validation Short"] = df["Validation Type"].str.replace("VALIDATE_", "", regex=False)
#     df["Year"]             = df["Verified Date"].dt.year

#     return df, display_labels



















import streamlit as st
import pandas as pd
import io


_ALIASES = {
    "Unique Key": [
        "unique key",
        "pk isbt labels monitor audit",
        "unique_key",
        "pk_isbt_labels_monitor_audit",
    ],
    "Validation Type": [
        "validation type",
        "validation_type",
        "validationtype",
    ],
    "Record Count": [
        "record count",
        "record_count",
        "recordcount",
    ],
    "Is issue found": [
        "is issue found",
        "is_issue_found",
        "isissuefound",
    ],
    "Affected Table Name": [
        "affected table name",
        "afftected table name",
        "affected_table_name",
        "afftected_table_name",
        "affectedtablename",
        "afftectedtablename",
    ],
    "Verified Date": [
        "verified date",
        "verified_date",
        "verifieddate",
        "verified datetime",
        "verified_datetime",
        "verifieddatetime",
    ],
    "Created On": [
        "created on",
        "created_on",
        "createdon",
    ],
}

_REQUIRED_COLS = [
    "Unique Key",
    "Validation Type",
    "Record Count",
    "Is issue found",
    "Affected Table Name",
    "Verified Date",
    "Created On",
]


def _build_rename_map() -> dict:
    lookup = {}
    for canonical, aliases in _ALIASES.items():
        for alias in aliases:
            key = " ".join(alias.strip().lower().replace("_", " ").split())
            lookup[key] = canonical
    return lookup


_RENAME_LOOKUP = _build_rename_map()


def _normalise_columns(df: pd.DataFrame) -> tuple:
    """
    Returns (normalised_df, display_labels) where display_labels maps
    canonical column name -> original column name as it appeared in the file.

    - Equivalent column names (e.g. PK_ISBT_LABELS_MONITOR_AUDIT, UNIQUE_KEY,
      Unique Key) are all recognised as the same field.
    - The displayed header is always the original name from the file.
    - Extra/unknown columns (e.g. VERIFIED_QUERY, AFFTECTED_PRIMARY_KEY) are
      silently ignored and never shown in the UI.
    """
    seen_canonical: dict = {}
    cols_to_drop: list = []
    rename_map: dict = {}
    display_labels: dict = {}

    for raw_col in df.columns:
        key = " ".join(str(raw_col).strip().lower().replace("_", " ").split())
        canonical = _RENAME_LOOKUP.get(key)

        if canonical is None:
            continue  # unknown / extra column — skip silently

        if canonical in seen_canonical:
            cols_to_drop.append(raw_col)  # duplicate — drop
        else:
            seen_canonical[canonical] = raw_col
            rename_map[raw_col] = canonical
            display_labels[canonical] = str(raw_col).strip()

    if cols_to_drop:
        df = df.drop(columns=cols_to_drop)

    df = df.rename(columns=rename_map)

    missing = [c for c in _REQUIRED_COLS if c not in df.columns]
    if missing:
        raise ValueError(
            f"Missing required columns after normalisation:\n  {missing}\n\n"
            f"Columns found in file:\n  {df.columns.tolist()}"
        )

    return df, display_labels


def _parse_dates(series: pd.Series) -> pd.Series:
    """
    Try common date formats in order, returning the first that parses cleanly.
    Handles both 2-digit years (17-May-25) and 4-digit years (17-MAY-2025),
    as well as ISO and slash-separated formats.
    """
    for fmt in ("%d-%b-%Y", "%d-%b-%y", "%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y"):
        parsed = pd.to_datetime(series, format=fmt, errors="coerce")
        if parsed.notna().sum() > 0:
            return parsed
    # Last resort: let pandas infer the format
    return pd.to_datetime(series, format="mixed", errors="coerce")


@st.cache_data
def load_data(file):
    name = file.name.lower()

    if name.endswith(".xlsx") or name.endswith(".xls"):
        df = pd.read_excel(
            file,
            engine="openpyxl" if name.endswith(".xlsx") else "xlrd",
        )
    else:
        # Try UTF-8 first; fall back to latin-1 for files that contain
        # non-UTF-8 bytes such as \xa0 (non-breaking space) in column names.
        raw = file.read()
        try:
            df = pd.read_csv(io.BytesIO(raw), encoding="utf-8")
        except UnicodeDecodeError:
            df = pd.read_csv(io.BytesIO(raw), encoding="latin-1")

    df.columns = df.columns.str.strip()
    df, display_labels = _normalise_columns(df)

    df["Verified Date"]    = _parse_dates(df["Verified Date"])
    df["Created On"]       = _parse_dates(df["Created On"])
    df["Is issue found"]   = df["Is issue found"].str.strip().str.upper()
    df["Has Issue"]        = df["Is issue found"] == "N"
    df["Validation Short"] = df["Validation Type"].str.replace("VALIDATE_", "", regex=False)
    df["Year"]             = df["Verified Date"].dt.year

    return df, display_labels