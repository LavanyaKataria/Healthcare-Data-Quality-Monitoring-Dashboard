# # import streamlit as st
# # import pandas as pd
# # import io


# # def render_tab_rawdata(df, display_labels: dict, T: dict, font_css: str, TABLE_JS: str) -> None:
# #     # ── Stats row using native metrics ──────────────────────────────────────
# #     total_rows = len(df)
# #     issue_rows = int(df["Has Issue"].sum())
# #     clean_rows = total_rows - issue_rows
# #     total_recs = int(df["Record Count"].sum())

# #     c1, c2, c3, c4 = st.columns(4)
# #     with c1:
# #         st.metric("Total Checks", f"{total_rows:,}")
# #     with c2:
# #         st.metric("With Issues", f"{issue_rows:,}", delta=f"{issue_rows} checks" if issue_rows else None, delta_color="inverse")
# #     with c3:
# #         st.metric("Clean Checks", f"{clean_rows:,}")
# #     with c4:
# #         st.metric("Affected Records", f"{total_recs:,}")

# #     st.markdown('<div style="height:12px"></div>', unsafe_allow_html=True)

# #     # ── Prepare display dataframe ──────────────────────────────────────────
# #     display = df.copy()
# #     display["Status"] = display["Has Issue"].map({True: "⚠️ Issue", False: "✅ Clean"})
    
# #     # Columns to show
# #     display_cols = [
# #         "Unique Key", "Validation Type", "Record Count", "Status",
# #         "Affected Table Name", "Verified Date", "Created On"
# #     ]
    
# #     # Select and format date fields
# #     display["Verified Date"] = display["Verified Date"].dt.strftime("%d %b %Y")
# #     display["Created On"]    = display["Created On"].dt.strftime("%d %b %Y")
# #     display["Record Count"]  = display["Record Count"].fillna(0).astype(int)
    
# #     # Subset
# #     display_subset = display[display_cols].copy()
    
# #     # Map to original file headers for presentation, preserving upload terms
# #     rename_map = {c: display_labels.get(c, c) for c in display_cols}
# #     # Update rename map for custom Status column
# #     rename_map["Status"] = "Status"
    
# #     display_subset = display_subset.rename(columns=rename_map)

# #     # ── Render native Streamlit Dataframe ───────────────────────────────────
# #     st.dataframe(
# #         display_subset,
# #         use_container_width=True,
# #         hide_index=True,
# #         column_config={
# #             display_labels.get("Unique Key", "Unique Key"): st.column_config.TextColumn(width="medium"),
# #             display_labels.get("Validation Type", "Validation Type"): st.column_config.TextColumn(width="medium"),
# #             display_labels.get("Record Count", "Record Count"): st.column_config.NumberColumn(format="%d", width="small"),
# #             "Status": st.column_config.TextColumn(width="small"),
# #             display_labels.get("Affected Table Name", "Affected Table Name"): st.column_config.TextColumn(width="medium"),
# #             display_labels.get("Verified Date", "Verified Date"): st.column_config.TextColumn(width="small"),
# #             display_labels.get("Created On", "Created On"): st.column_config.TextColumn(width="small"),
# #         }
# #     )

# #     st.markdown('<div style="height:8px"></div>', unsafe_allow_html=True)

# #     # ── Clean native CSV export button ──────────────────────────────────────
# #     buf = io.BytesIO()
# #     df.to_csv(buf, index=False)
# #     buf.seek(0)
# #     st.download_button(
# #         "⬇ Export Data to CSV",
# #         data=buf,
# #         file_name="raw_records.csv",
# #         mime="text/csv",
# #         key="rawdata_dl",
# #         use_container_width=True
# #     )















# import streamlit as st
# import streamlit.components.v1 as components
# import pandas as pd
# import io
# import json

# from ui.styles import table_base_css
# from ui.components import build_th_html

# import math

# def _safe_cell(v):
#     """Convert any cell value to a JSON-safe, display-safe Python object.
#     Handles None, NaN, int, float, and non-string types gracefully."""
#     if v is None:
#         return ""
#     if isinstance(v, float) and math.isnan(v):
#         return ""
#     if isinstance(v, (int, float)):
#         # Display integers without decimal point (123 not 123.0)
#         return int(v) if isinstance(v, float) and v == int(v) else v
#     return v


# def open_popup(f: dict, title: str) -> None:
#     st.session_state.popup_filter = f
#     st.session_state.popup_title  = title
#     st.session_state.popup_sort_col = "Record Count"
#     st.session_state.popup_sort_asc = False
#     st.rerun()


# def close_popup() -> None:
#     st.session_state.popup_filter = None
#     st.session_state.popup_title  = ""
#     st.rerun()


# def apply_popup_filter(dataframe, f: dict):
#     ddf = dataframe.copy()
#     if "Validation Type" in f: ddf = ddf[ddf["Validation Short"] == f["Validation Type"]]
#     if "Table"           in f: ddf = ddf[ddf["Affected Table Name"] == f["Table"]]
#     if "Date"            in f:
#         try: ddf = ddf[ddf["Verified Date"] == pd.Timestamp(f["Date"])]
#         except: pass
#     if "Status" in f:
#         if f["Status"] == "Issues": ddf = ddf[ddf["Has Issue"]]
#         elif f["Status"] == "Pass": ddf = ddf[~ddf["Has Issue"]]
#     if "kpi" in f:
#         if f["kpi"] == "issues": ddf = ddf[ddf["Has Issue"]]
#         elif f["kpi"] == "clean": ddf = ddf[~ddf["Has Issue"]]
#     return ddf


# def render_popup(base_df, display_labels: dict, T: dict, font_css: str, TABLE_JS: str) -> None:
#     f     = st.session_state.popup_filter
#     title = st.session_state.popup_title
#     if f is None: return

#     filtered    = apply_popup_filter(base_df, f)
#     total_rows  = len(filtered)
#     issue_rows  = int(filtered["Has Issue"].sum())
#     clean_rows  = total_rows - issue_rows
#     total_recs  = int(filtered["Record Count"].sum())

#     col_title, col_close = st.columns([11, 1])
#     with col_title:
#         st.markdown(f"<div style='padding:6px 0;font-family:Syne,sans-serif;font-size:1rem;font-weight:700;color:{T['accent']}'>🔍 {title}</div>", unsafe_allow_html=True)
#     with col_close:
#         if st.button("✕ Close", key="close_popup_btn", use_container_width=False):
#             close_popup()
#         components.html("""
# <script>
# (function() {
#     function styleCloseBtn() {
#         var btns = window.parent.document.querySelectorAll('button');
#         btns.forEach(function(btn) {
#             if (btn.innerText.trim() === '\u2715 Close') {
#                 btn.style.setProperty('background', '#dc2626', 'important');
#                 btn.style.setProperty('border', '2px solid #dc2626', 'important');
#                 btn.style.setProperty('color', '#ffffff', 'important');
#                 btn.style.setProperty('border-radius', '7px', 'important');
#                 btn.style.setProperty('font-weight', '700', 'important');
#                 btn.style.setProperty('box-shadow', '0 0 12px rgba(255,91,107,0.5)', 'important');
#                 btn.onmouseenter = function() { btn.style.setProperty('background', '#ff3347', 'important'); };
#                 btn.onmouseleave = function() { btn.style.setProperty('background', '#dc2626', 'important'); };
#             }
#         });
#     }
#     styleCloseBtn();
#     setTimeout(styleCloseBtn, 300);
#     setTimeout(styleCloseBtn, 800);
# })();
# </script>
# """, height=0)

#     display = filtered[["Unique Key","Validation Type","Record Count","Is issue found",
#                          "Affected Table Name","Verified Date","Created On"]].copy()
#     display["Verified Date"] = display["Verified Date"].dt.strftime("%d %b %Y")
#     display["Created On"]    = display["Created On"].dt.strftime("%d %b %Y")
#     display["Record Count"]  = display["Record Count"].fillna(0).astype(int)
#     # Coerce Affected Table Name to safe display values (handles int/float/None/NaN)
#     display["Affected Table Name"] = display["Affected Table Name"].apply(_safe_cell)
#     rows_json = json.dumps(display.values.tolist(), default=str)

#     # Use original column names from the uploaded file for display
#     lbl_unique_key   = display_labels.get("Unique Key",          "Unique Key")
#     lbl_val_type     = display_labels.get("Validation Type",     "Validation Type")
#     lbl_rec_count    = display_labels.get("Record Count",        "Record Count")
#     lbl_issue_found  = display_labels.get("Is issue found",      "Is issue found")
#     lbl_table_name   = display_labels.get("Affected Table Name", "Affected Table Name")
#     lbl_verified     = display_labels.get("Verified Date",       "Verified Date")
#     lbl_created      = display_labels.get("Created On",          "Created On")

#     COLS_DEF = [
#         (lbl_unique_key,  0, "str"),
#         (lbl_val_type,    1, "str"),
#         (lbl_rec_count,   2, "num"),
#         (lbl_issue_found, 3, "str"),
#         (lbl_table_name,  4, "str"),
#         (lbl_verified,    5, "str"),
#         (lbl_created,     6, "str"),
#     ]
#     th_html = build_th_html(COLS_DEF)
#     css     = table_base_css(T)

#     full_html = f"""<!DOCTYPE html>
# <html><head><meta charset="utf-8">
# <style>{font_css}
# {css}</style>
# </head>
# <body>
# <div class="box"><div class="body">
# <div class="stats">
#   <div class="stat"><div class="stat-val">{total_rows:,}</div><div class="stat-lbl">Total Rows</div></div>
#   <div class="stat"><div class="stat-val" style="color:var(--red)">{issue_rows:,}</div><div class="stat-lbl">With Issues</div></div>
#   <div class="stat"><div class="stat-val" style="color:var(--green)">{clean_rows:,}</div><div class="stat-lbl">Clean</div></div>
#   <div class="stat"><div class="stat-val" style="color:var(--amber)">{total_recs:,}</div><div class="stat-lbl">Affected Records</div></div>
# </div>
# <div class="controls">
#   <div class="perpage">Show <select id="perPageSel" onchange="changePerPage(this.value)"><option value="10">10</option><option value="25">25</option><option value="50">50</option><option value="100">100</option></select> entries per page</div>
#   <div class="srchwrap">Search: <input id="searchBox" type="text" placeholder="Filter records…" oninput="doSearch(this.value)"></div>
# </div>
# <div class="tbl-wrap"><table><thead><tr>{th_html}</tr></thead><tbody id="tbody"></tbody></table></div>
# <div class="pg-row"><div class="pg-info" id="pgInfo"></div><div class="pg-btns" id="pgBtns"></div></div>
# </div></div>
# <script>
# const RAW={rows_json};
# {TABLE_JS}
# </script></body></html>"""

#     components.html(full_html, height=620, scrolling=False)
#     buf = io.BytesIO(); filtered.to_csv(buf, index=False); buf.seek(0)
#     st.download_button("⬇ Export CSV", data=buf, file_name="drilldown.csv", mime="text/csv", key="popup_dl")












import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import io
import json

from ui.styles import table_base_css
from ui.components import build_th_html

import math

def _safe_cell(v):
    """Convert any cell value to a JSON-safe, display-safe Python object.
    Handles None, NaN, int, float, and non-string types gracefully."""
    if v is None:
        return ""
    if isinstance(v, float) and math.isnan(v):
        return ""
    if isinstance(v, (int, float)):
        # Display integers without decimal point (123 not 123.0)
        return int(v) if isinstance(v, float) and v == int(v) else v
    return v


def render_tab_rawdata(df, display_labels: dict, T: dict, font_css: str, TABLE_JS: str) -> None:
    # ── Stats row ─────────────────────────────────────────────────────────
    total_rows = len(df)
    issue_rows = int(df["Has Issue"].sum())
    clean_rows = total_rows - issue_rows
    total_recs = int(df["Record Count"].sum())

    # ── Prepare display dataframe ──────────────────────────────────────────
    display = df[[
        "Unique Key", "Validation Type", "Record Count", "Is issue found",
        "Affected Table Name", "Verified Date", "Created On"
    ]].copy()
    display["Verified Date"] = display["Verified Date"].dt.strftime("%d %b %Y")
    display["Created On"]    = display["Created On"].dt.strftime("%d %b %Y")
    display["Record Count"]  = display["Record Count"].fillna(0).astype(int)
    # Coerce Affected Table Name to safe display values (handles int/float/None/NaN)
    display["Affected Table Name"] = display["Affected Table Name"].apply(_safe_cell)

    rows_json = json.dumps(display.values.tolist(), default=str)

    # ── Column labels (use original file headers when available) ──────────
    lbl_unique_key  = display_labels.get("Unique Key",          "Unique Key")
    lbl_val_type    = display_labels.get("Validation Type",     "Validation Type")
    lbl_rec_count   = display_labels.get("Record Count",        "Record Count")
    lbl_issue_found = display_labels.get("Is issue found",      "Is issue found")
    lbl_table_name  = display_labels.get("Affected Table Name", "Affected Table Name")
    lbl_verified    = display_labels.get("Verified Date",       "Verified Date")
    lbl_created     = display_labels.get("Created On",          "Created On")

    COLS_DEF = [
        (lbl_unique_key,  0, "str"),
        (lbl_val_type,    1, "str"),
        (lbl_rec_count,   2, "num"),
        (lbl_issue_found, 3, "str"),
        (lbl_table_name,  4, "str"),
        (lbl_verified,    5, "str"),
        (lbl_created,     6, "str"),
    ]
    th_html = build_th_html(COLS_DEF)
    css     = table_base_css(T)

    full_html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8">
<style>{font_css}
{css}</style>
</head>
<body>
<div class="box"><div class="body">
<div class="stats">
  <div class="stat"><div class="stat-val">{total_rows:,}</div><div class="stat-lbl">Total Rows</div></div>
  <div class="stat"><div class="stat-val" style="color:var(--red)">{issue_rows:,}</div><div class="stat-lbl">With Issues</div></div>
  <div class="stat"><div class="stat-val" style="color:var(--green)">{clean_rows:,}</div><div class="stat-lbl">Clean</div></div>
  <div class="stat"><div class="stat-val" style="color:var(--amber)">{total_recs:,}</div><div class="stat-lbl">Affected Records</div></div>
</div>
<div class="controls">
  <div class="perpage">Show <select id="perPageSel" onchange="changePerPage(this.value)"><option value="10">10</option><option value="25">25</option><option value="50">50</option><option value="100">100</option></select> entries per page</div>
  <div class="srchwrap">Search: <input id="searchBox" type="text" placeholder="Filter records…" oninput="doSearch(this.value)"></div>
</div>
<div class="tbl-wrap"><table><thead><tr>{th_html}</tr></thead><tbody id="tbody"></tbody></table></div>
<div class="pg-row"><div class="pg-info" id="pgInfo"></div><div class="pg-btns" id="pgBtns"></div></div>
</div></div>
<script>
const RAW={rows_json};
{TABLE_JS}
</script></body></html>"""

    components.html(full_html, height=620, scrolling=False)

    # ── Export button ──────────────────────────────────────────────────────
    buf = io.BytesIO()
    df.to_csv(buf, index=False)
    buf.seek(0)
    st.download_button(
        "⬇ Export CSV",
        data=buf,
        file_name="raw_records.csv",
        mime="text/csv",
        key="rawdata_dl"
    )