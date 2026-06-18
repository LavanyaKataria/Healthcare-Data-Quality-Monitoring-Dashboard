# # # # import streamlit as st
# # # # import streamlit.components.v1 as components
# # # # from datetime import timedelta
# # # # import pandas as pd

# # # # # ── Page config (must be first Streamlit call) ─────────────────────────────
# # # # st.set_page_config(
# # # #     page_title="Data Quality Monitor",
# # # #     page_icon="🧬",
# # # #     layout="wide",
# # # #     initial_sidebar_state="expanded",
# # # # )

# # # # # ── Session state initialisation ──────────────────────────────────────────
# # # # def init_session():
# # # #     defaults = {
# # # #         "popup_filter": None, "popup_title": "",
# # # #         "active_tab": 0,
# # # #         "ct_trend": "Line", "ct_passbar": "Bar",
# # # #         "ct_cumulative": "Area", "ct_bytype": "Horizontal Bar", "ct_bytable": "Donut",
# # # #         "popup_sort_col": "Record Count", "popup_sort_asc": False,
# # # #         "close_popup_trigger": 0,
# # # #         "dark_mode": False,
# # # #     }
# # # #     for k, v in defaults.items():
# # # #         if k not in st.session_state:
# # # #             st.session_state[k] = v

# # # # init_session()

# # # # # ── Theme ──────────────────────────────────────────────────────────────────
# # # # from config.theme import get_theme, build_layout, build_hover, PLOTLY_CONFIG

# # # # DARK = st.session_state.dark_mode
# # # # T = get_theme(DARK)
# # # # LAYOUT = build_layout(T)
# # # # HOVER  = build_hover(T)

# # # # C_BLUE  = T["accent"]
# # # # C_GREEN = T["green"]
# # # # C_RED   = T["red"]
# # # # C_AMBER = T["amber"]
# # # # C_PURP  = T["purple"]
# # # # PALETTE = [C_BLUE, C_GREEN, C_AMBER, C_RED, C_PURP, "#0284c7", "#b91c1c", "#15803d"]

# # # # # ── Load fonts CSS ─────────────────────────────────────────────────────────
# # # # with open("assets/css/dashboardfonts.css", "r", encoding="utf-8") as _f:
# # # #     _font_css = _f.read()

# # # # # ── Load table JS ──────────────────────────────────────────────────────────
# # # # with open("assets/js/table.js", "r", encoding="utf-8") as _f:
# # # #     TABLE_JS = _f.read()

# # # # # ── Inject global styles ───────────────────────────────────────────────────
# # # # from ui.styles import inject_global_styles
# # # # inject_global_styles(T, _font_css)

# # # # # ── File upload gate ───────────────────────────────────────────────────────
# # # # if "uploaded_file" not in st.session_state:
# # # #     st.session_state.uploaded_file = None

# # # # if st.session_state.uploaded_file is None:
# # # #     st.markdown(f"""
# # # #     <style>
# # # #     section[data-testid="stSidebar"] {{ display: none !important; }}
# # # #     .upload-screen {{ display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 52vh; text-align: center; padding: 2rem 2rem 0; }}
# # # #     .upload-icon-ring {{ width: 110px; height: 110px; border-radius: 50%; background: linear-gradient(135deg, {T['accent_glow']}, {T['green_glow']}); border: 2px solid {T['accent']}; display: flex; align-items: center; justify-content: center; font-size: 3rem; margin: 0 auto 28px; box-shadow: 0 0 48px {T['accent_glow']}, 0 0 0 18px {T['accent_glow']}; animation: pulse-ring 2.8s ease-in-out infinite; }}
# # # #     @keyframes pulse-ring {{ 0%, 100% {{ box-shadow: 0 0 48px {T['accent_glow']}, 0 0 0 18px {T['accent_glow']}; }} 50% {{ box-shadow: 0 0 64px {T['accent_glow']}, 0 0 0 26px {T['accent_glow']}; }} }}
# # # #     .upload-title {{ font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; background: linear-gradient(135deg, {T['text_primary']} 30%, {T['accent']} 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 32px; letter-spacing: -0.02em; }}
# # # #     [data-testid="stFileUploaderDropzoneInstructions"] {{ display: none !important; }}
# # # #     [data-testid="stFileUploader"] small, [data-testid="stFileUploader"] span[class*="uploadInstructions"] {{ display: none !important; }}
# # # #     .center-uploader [data-testid="stFileUploader"] {{ background: {T['bg_card']} !important; border: 2px dashed {T['accent']} !important; border-radius: 16px !important; padding: 28px 32px !important; display: flex !important; justify-content: center !important; }}
# # # #     .center-uploader [data-testid="stFileUploaderDropzone"] {{ display: flex !important; justify-content: center !important; align-items: center !important; width: 100% !important; }}
# # # #     .center-uploader section[data-testid="stFileUploaderDropzone"] > div {{ display: flex !important; justify-content: center !important; width: 100% !important; }}
# # # #     .center-uploader [data-testid="stFileUploader"]:hover {{ border-color: {T['accent']} !important; background: {T['bg_hover']} !important; }}
# # # #     .center-uploader [data-testid="stFileUploaderDropzone"] {{ background: transparent !important; }}
# # # #     </style>
# # # #     <div class="upload-screen">
# # # #       <div class="upload-icon-ring">🧬</div>
# # # #       <div class="upload-title">Data Quality Monitor</div>
# # # #     </div>
# # # #     """, unsafe_allow_html=True)

# # # #     _, col_mid, _ = st.columns([1, 2, 1])
# # # #     with col_mid:
# # # #         st.markdown('<div class="center-uploader">', unsafe_allow_html=True)
# # # #         center_upload = st.file_uploader("Upload a CSV or Excel file to get started", type=["csv", "xlsx", "xls"], key="center_uploader")
# # # #         st.markdown('</div>', unsafe_allow_html=True)

# # # #     if center_upload is not None:
# # # #         st.session_state.uploaded_file = center_upload
# # # #         st.rerun()
# # # #     st.stop()


# # # # # ── Load data ──────────────────────────────────────────────────────────────
# # # # from data.loader import load_data

# # # # uploaded = st.session_state.uploaded_file
# # # # df_raw, display_labels = load_data(uploaded)

# # # # def dlbl(canonical: str) -> str:
# # # #     """Return the original uploaded column name for a given canonical name."""
# # # #     return display_labels.get(canonical, canonical)


# # # # # ── Sidebar ────────────────────────────────────────────────────────────────
# # # # from ui.popup import close_popup

# # # # with st.sidebar:
# # # #     st.markdown(f"""
# # # #     <div class="sidebar-brand">
# # # #       <div class="sidebar-brand-icon">🧬</div>
# # # #       <div>
# # # #         <div class="sidebar-brand-text">Data Quality Monitor</div>
# # # #         <div class="sidebar-brand-sub">Clinical Data Quality</div>
# # # #       </div>
# # # #     </div>
# # # #     """, unsafe_allow_html=True)

# # # #     new_dark = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode, key="dark_toggle")
# # # #     if new_dark != st.session_state.dark_mode:
# # # #         st.session_state.dark_mode = new_dark
# # # #         st.rerun()

# # # #     if st.button("📂 Change File", use_container_width=True):
# # # #         st.session_state.uploaded_file = None
# # # #         st.rerun()

# # # #     st.markdown('<div class="section-label">Filters</div>', unsafe_allow_html=True)
# # # #     available_years = sorted(df_raw["Year"].dropna().unique().astype(int).tolist())
# # # #     sel_year = st.selectbox("📅 Year", ["All Years"] + [str(y) for y in available_years], index=0)
# # # #     df_year_scoped = df_raw if sel_year == "All Years" else df_raw[df_raw["Year"] == int(sel_year)].copy()

# # # #     MONTH_NAMES = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
# # # #                    7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
# # # #     available_months = sorted(df_year_scoped["Verified Date"].dropna().dt.month.unique().astype(int).tolist())
# # # #     month_options = ["All Months"] + [MONTH_NAMES[m] for m in available_months]
# # # #     sel_month = st.selectbox("🗓 Month", month_options, index=0)
# # # #     if sel_month != "All Months":
# # # #         sel_month_num = [k for k, v in MONTH_NAMES.items() if v == sel_month][0]
# # # #         df_year_scoped = df_year_scoped[df_year_scoped["Verified Date"].dt.month == sel_month_num].copy()

# # # #     all_dates = sorted(df_year_scoped["Verified Date"].dropna().unique())
# # # #     if not all_dates:
# # # #         st.warning("No data for selected filters.")
# # # #         st.stop()
# # # #     date_min = pd.Timestamp(min(all_dates)); date_max = pd.Timestamp(max(all_dates))

# # # #     preset = st.selectbox("⏱ Timeline", [
# # # #         "Custom Range","Last 7 Days","Last 14 Days","Last 30 Days","Last 45 Days",
# # # #         "Last 60 Days","Last 3 Months","Last 6 Months","Last 12 Months","All Time"
# # # #     ], index=9)

# # # #     offsets = {
# # # #         "Last 7 Days":6,"Last 14 Days":13,"Last 30 Days":29,"Last 45 Days":44,
# # # #         "Last 60 Days":59,"Last 3 Months":89,"Last 6 Months":179,"Last 12 Months":364,
# # # #     }
# # # #     preset_start = (date_max - timedelta(days=offsets[preset])) if preset in offsets else date_min
# # # #     preset_end   = date_max

# # # #     if preset == "Custom Range":
# # # #         dr = st.date_input("Range", value=(preset_start.date(), preset_end.date()),
# # # #                            min_value=date_min.date(), max_value=date_max.date())
# # # #         d0, d1 = (pd.Timestamp(dr[0]), pd.Timestamp(dr[1])) if len(dr)==2 else (preset_start, preset_end)
# # # #     else:
# # # #         d0 = max(preset_start, date_min); d1 = min(preset_end, date_max)
# # # #         st.caption(f"📅 {d0.strftime('%d %b %Y')} → {d1.strftime('%d %b %Y')}")

# # # #     st.markdown('<div class="section-label">Scope</div>', unsafe_allow_html=True)
# # # #     all_tables = sorted(df_year_scoped["Affected Table Name"].unique())
# # # #     sel_tables = st.multiselect("Affected Tables", all_tables, default=all_tables)
# # # #     all_types  = sorted(df_year_scoped["Validation Short"].unique())
# # # #     sel_types  = st.multiselect("Validation Types", all_types, default=all_types)
# # # #     show_only_issues = st.toggle("Issues only", value=False)

# # # #     if st.session_state.popup_filter:
# # # #         st.markdown('<div class="section-label">Popup</div>', unsafe_allow_html=True)
# # # #         if st.button("✕ Close Drill-Down", use_container_width=True):
# # # #             close_popup()

# # # #     st.markdown("---")
# # # #     st.markdown(f'<span style="font-size:0.65rem;color:{T["text_dim"]};letter-spacing:0.1em;text-transform:uppercase">v5.6 · {"🌙 Dark" if DARK else "☀️ Light"} Mode</span>', unsafe_allow_html=True)


# # # # # ── Apply filters ──────────────────────────────────────────────────────────
# # # # df = df_year_scoped[
# # # #     (df_year_scoped["Verified Date"] >= d0) &
# # # #     (df_year_scoped["Verified Date"] <= d1) &
# # # #     (df_year_scoped["Affected Table Name"].isin(sel_tables)) &
# # # #     (df_year_scoped["Validation Short"].isin(sel_types))
# # # # ].copy()
# # # # if show_only_issues: df = df[df["Has Issue"]]

# # # # total       = len(df)
# # # # with_issues = int(df["Has Issue"].sum())
# # # # clean       = total - with_issues
# # # # total_recs  = int(df["Record Count"].sum())
# # # # pass_rate   = (clean / total * 100) if total else 0

# # # # days_sorted = sorted(df["Verified Date"].dropna().unique())
# # # # if len(days_sorted) >= 2:
# # # #     delta  = int(df[df["Verified Date"]==days_sorted[-1]]["Has Issue"].sum()) - int(df[df["Verified Date"]==days_sorted[-2]]["Has Issue"].sum())
# # # #     dlabel = f"{'▲' if delta>0 else '▼' if delta<0 else '='} {abs(delta)} vs prev"
# # # # else:
# # # #     dlabel = "—"

# # # # # ── Dashboard header ───────────────────────────────────────────────────────
# # # # st.markdown(f"""
# # # # <div class="dash-header">
# # # #   <div class="dash-title">Data Quality Monitor</div>
# # # #   <div class="dash-meta">
# # # #     <span class="dash-meta-chip">📅 {d0.strftime('%d %b %Y')} → {d1.strftime('%d %b %Y')}</span>
# # # #     <span class="dash-meta-chip">📋 {total:,} records</span>
# # # #     {"<span class='dash-meta-chip'>🗓 " + sel_year + "</span>" if sel_year != "All Years" else ""}
# # # #   </div>
# # # # </div>
# # # # """, unsafe_allow_html=True)

# # # # # ── KPI buttons ────────────────────────────────────────────────────────────
# # # # from ui.popup import open_popup
# # # # from ui.components import green_css, grey_css

# # # # active_kpi = st.session_state.popup_filter.get("kpi") if isinstance(st.session_state.popup_filter, dict) else None

# # # # kpi_labels = {
# # # #     "all":     "VALIDATION SUMMARY",
# # # #     "issues":  "ISSUE OVERVIEW",
# # # #     "clean":   f"VALIDATION SUCCESS RATE  {pass_rate:.1f}%",
# # # #     "records": "IMPACT ANALYSIS",
# # # # }

# # # # active_map = {
# # # #     "kpi_all":     active_kpi == "all",
# # # #     "kpi_issues":  active_kpi == "issues",
# # # #     "kpi_clean":   active_kpi == "clean",
# # # #     "kpi_records": active_kpi == "records",
# # # # }

# # # # base_css = f"""
# # # # <style>
# # # # div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button {{
# # # #     border-radius: 14px !important; font-family: 'Inter', sans-serif !important;
# # # #     font-size: 0.78rem !important; height: 70px !important; width: 100% !important;
# # # #     letter-spacing: 0.05em !important; transition: all 0.18s ease !important;
# # # #     cursor: pointer !important; color: {T['text_muted']} !important;
# # # # }}
# # # # """
# # # # col_map = [("kpi_all",1),("kpi_issues",2),("kpi_clean",3),("kpi_records",4)]
# # # # for bid, nth in col_map:
# # # #     base_css += green_css(nth, T) if active_map[bid] else grey_css(nth, T)
# # # # base_css += "</style>"
# # # # st.markdown(base_css, unsafe_allow_html=True)

# # # # c1, c2, c3, c4 = st.columns(4)
# # # # for col, ktype, bid in zip([c1,c2,c3,c4], ["all","issues","clean","records"],
# # # #                            ["kpi_all","kpi_issues","kpi_clean","kpi_records"]):
# # # #     with col:
# # # #         if st.button(kpi_labels[ktype], key=bid, use_container_width=True):
# # # #             open_popup({"kpi": ktype}, kpi_labels[ktype])

# # # # st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

# # # # # ── Popup ──────────────────────────────────────────────────────────────────
# # # # from ui.popup import render_popup
# # # # render_popup(df, display_labels, T, _font_css, TABLE_JS)

# # # # # ── Tab navigation ─────────────────────────────────────────────────────────
# # # # TAB_LABELS = ["📈  Trend Analysis", "🗂  Issue Breakdown", "📋  Raw Records"]
# # # # tab_selection = st.radio(
# # # #     "tabs", TAB_LABELS, index=st.session_state.active_tab,
# # # #     horizontal=True, label_visibility="collapsed", key="tab_radio"
# # # # )
# # # # active_tab = TAB_LABELS.index(tab_selection)
# # # # st.session_state.active_tab = active_tab
# # # # st.markdown(f'<div style="border-bottom:1px solid {T["border"]};margin:6px 0 22px"></div>', unsafe_allow_html=True)

# # # # # ── Tab content ────────────────────────────────────────────────────────────
# # # # if active_tab == 0:
# # # #     from charts.tab_trend import render_tab_trend
# # # #     render_tab_trend(df, T, LAYOUT, HOVER, PALETTE, PLOTLY_CONFIG, C_BLUE, C_GREEN, C_RED)

# # # # elif active_tab == 1:
# # # #     from charts.tab_breakdown import render_tab_breakdown
# # # #     render_tab_breakdown(df, T, LAYOUT, HOVER, PALETTE, PLOTLY_CONFIG, C_RED, C_AMBER)

# # # # elif active_tab == 2:
# # # #     from charts.tab_rawdata import render_tab_rawdata
# # # #     render_tab_rawdata(df, display_labels, T, _font_css, TABLE_JS)












# # # import streamlit as st
# # # import streamlit.components.v1 as components
# # # from datetime import timedelta
# # # import pandas as pd

# # # # ── Page config (must be first Streamlit call) ─────────────────────────────
# # # st.set_page_config(
# # #     page_title="Data Quality Monitor",
# # #     page_icon="🧬",
# # #     layout="wide",
# # #     initial_sidebar_state="expanded",
# # # )

# # # # ── Session state initialisation ──────────────────────────────────────────
# # # def init_session():
# # #     defaults = {
# # #         "popup_filter": None, "popup_title": "",
# # #         "active_tab": 0,
# # #         "ct_trend": "Line", "ct_passbar": "Bar",
# # #         "ct_cumulative": "Area", "ct_bytype": "Horizontal Bar", "ct_bytable": "Donut",
# # #         "popup_sort_col": "Record Count", "popup_sort_asc": False,
# # #         "close_popup_trigger": 0,
# # #         "dark_mode": False,
# # #     }
# # #     for k, v in defaults.items():
# # #         if k not in st.session_state:
# # #             st.session_state[k] = v

# # # init_session()

# # # # ── Theme ──────────────────────────────────────────────────────────────────
# # # from config.theme import get_theme, build_layout, build_hover, PLOTLY_CONFIG

# # # DARK = st.session_state.dark_mode
# # # T = get_theme(DARK)
# # # LAYOUT = build_layout(T)
# # # HOVER  = build_hover(T)

# # # C_BLUE  = T["accent"]
# # # C_GREEN = T["green"]
# # # C_RED   = T["red"]
# # # C_AMBER = T["amber"]
# # # C_PURP  = T["purple"]
# # # PALETTE = [C_BLUE, C_GREEN, C_AMBER, C_RED, C_PURP, "#0284c7", "#b91c1c", "#15803d"]

# # # # ── Load fonts CSS ─────────────────────────────────────────────────────────
# # # with open("assets/css/dashboardfonts.css", "r", encoding="utf-8") as _f:
# # #     _font_css = _f.read()

# # # # ── Load table JS ──────────────────────────────────────────────────────────
# # # with open("assets/js/table.js", "r", encoding="utf-8") as _f:
# # #     TABLE_JS = _f.read()

# # # # ── Inject global styles ───────────────────────────────────────────────────
# # # from ui.styles import inject_global_styles
# # # inject_global_styles(T, _font_css)

# # # # ── File upload gate ───────────────────────────────────────────────────────
# # # if "uploaded_file" not in st.session_state:
# # #     st.session_state.uploaded_file = None

# # # if st.session_state.uploaded_file is None:
# # #     st.markdown(f"""
# # #     <style>
# # #     section[data-testid="stSidebar"] {{ display: none !important; }}
# # #     .upload-screen {{ display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 52vh; text-align: center; padding: 2rem 2rem 0; }}
# # #     .upload-icon-ring {{ width: 110px; height: 110px; border-radius: 50%; background: linear-gradient(135deg, {T['accent_glow']}, {T['green_glow']}); border: 2px solid {T['accent']}; display: flex; align-items: center; justify-content: center; font-size: 3rem; margin: 0 auto 28px; box-shadow: 0 0 48px {T['accent_glow']}, 0 0 0 18px {T['accent_glow']}; animation: pulse-ring 2.8s ease-in-out infinite; }}
# # #     @keyframes pulse-ring {{ 0%, 100% {{ box-shadow: 0 0 48px {T['accent_glow']}, 0 0 0 18px {T['accent_glow']}; }} 50% {{ box-shadow: 0 0 64px {T['accent_glow']}, 0 0 0 26px {T['accent_glow']}; }} }}
# # #     .upload-title {{ font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; background: linear-gradient(135deg, {T['text_primary']} 30%, {T['accent']} 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 32px; letter-spacing: -0.02em; }}
# # #     [data-testid="stFileUploaderDropzoneInstructions"] {{ display: none !important; }}
# # #     [data-testid="stFileUploader"] small, [data-testid="stFileUploader"] span[class*="uploadInstructions"] {{ display: none !important; }}
# # #     .center-uploader [data-testid="stFileUploader"] {{ background: {T['bg_card']} !important; border: 2px dashed {T['accent']} !important; border-radius: 16px !important; padding: 28px 32px !important; display: flex !important; justify-content: center !important; }}
# # #     .center-uploader [data-testid="stFileUploaderDropzone"] {{ display: flex !important; justify-content: center !important; align-items: center !important; width: 100% !important; }}
# # #     .center-uploader section[data-testid="stFileUploaderDropzone"] > div {{ display: flex !important; justify-content: center !important; width: 100% !important; }}
# # #     .center-uploader [data-testid="stFileUploader"]:hover {{ border-color: {T['accent']} !important; background: {T['bg_hover']} !important; }}
# # #     .center-uploader [data-testid="stFileUploaderDropzone"] {{ background: transparent !important; }}
# # #     </style>
# # #     <div class="upload-screen">
# # #       <div class="upload-icon-ring">🧬</div>
# # #       <div class="upload-title">Data Quality Monitor</div>
# # #     </div>
# # #     """, unsafe_allow_html=True)

# # #     _, col_mid, _ = st.columns([1, 2, 1])
# # #     with col_mid:
# # #         st.markdown('<div class="center-uploader">', unsafe_allow_html=True)
# # #         center_upload = st.file_uploader("Upload a CSV or Excel file to get started", type=["csv", "xlsx", "xls"], key="center_uploader")
# # #         st.markdown('</div>', unsafe_allow_html=True)

# # #     if center_upload is not None:
# # #         st.session_state.uploaded_file = center_upload
# # #         st.rerun()
# # #     st.stop()


# # # # ── Load data ──────────────────────────────────────────────────────────────
# # # from data.loader import load_data

# # # uploaded = st.session_state.uploaded_file
# # # df_raw, display_labels = load_data(uploaded)

# # # def dlbl(canonical: str) -> str:
# # #     """Return the original uploaded column name for a given canonical name."""
# # #     return display_labels.get(canonical, canonical)


# # # # ── Sidebar ────────────────────────────────────────────────────────────────
# # # from ui.popup import close_popup

# # # with st.sidebar:
# # #     st.markdown(f"""
# # #     <div class="sidebar-brand">
# # #       <div class="sidebar-brand-icon">🧬</div>
# # #       <div>
# # #         <div class="sidebar-brand-text">Data Quality Monitor</div>
# # #         <div class="sidebar-brand-sub">Clinical Data Quality</div>
# # #       </div>
# # #     </div>
# # #     """, unsafe_allow_html=True)

# # #     new_dark = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode, key="dark_toggle")
# # #     if new_dark != st.session_state.dark_mode:
# # #         st.session_state.dark_mode = new_dark
# # #         st.rerun()

# # #     if st.button("📂 Change File", use_container_width=True):
# # #         st.session_state.uploaded_file = None
# # #         st.rerun()

# # #     st.markdown('<div class="section-label">Filters</div>', unsafe_allow_html=True)
# # #     available_years = sorted(df_raw["Year"].dropna().unique().astype(int).tolist())
# # #     sel_year = st.selectbox("📅 Year", ["All Years"] + [str(y) for y in available_years], index=0)
# # #     df_year_scoped = df_raw if sel_year == "All Years" else df_raw[df_raw["Year"] == int(sel_year)].copy()

# # #     MONTH_NAMES = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
# # #                    7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
# # #     available_months = sorted(df_year_scoped["Verified Date"].dropna().dt.month.unique().astype(int).tolist())
# # #     month_options = ["All Months"] + [MONTH_NAMES[m] for m in available_months]
# # #     sel_month = st.selectbox("🗓 Month", month_options, index=0)
# # #     if sel_month != "All Months":
# # #         sel_month_num = [k for k, v in MONTH_NAMES.items() if v == sel_month][0]
# # #         df_year_scoped = df_year_scoped[df_year_scoped["Verified Date"].dt.month == sel_month_num].copy()

# # #     all_dates = sorted(df_year_scoped["Verified Date"].dropna().unique())
# # #     if not all_dates:
# # #         st.warning("No data for selected filters.")
# # #         st.stop()
# # #     date_min = pd.Timestamp(min(all_dates)); date_max = pd.Timestamp(max(all_dates))

# # #     preset = st.selectbox("⏱ Timeline", [
# # #         "Custom Range","Last 7 Days","Last 14 Days","Last 30 Days","Last 45 Days",
# # #         "Last 60 Days","Last 3 Months","Last 6 Months","Last 12 Months","All Time"
# # #     ], index=9)

# # #     offsets = {
# # #         "Last 7 Days":6,"Last 14 Days":13,"Last 30 Days":29,"Last 45 Days":44,
# # #         "Last 60 Days":59,"Last 3 Months":89,"Last 6 Months":179,"Last 12 Months":364,
# # #     }
# # #     preset_start = (date_max - timedelta(days=offsets[preset])) if preset in offsets else date_min
# # #     preset_end   = date_max

# # #     if preset == "Custom Range":
# # #         dr = st.date_input("Range", value=(preset_start.date(), preset_end.date()),
# # #                            min_value=date_min.date(), max_value=date_max.date())
# # #         d0, d1 = (pd.Timestamp(dr[0]), pd.Timestamp(dr[1])) if len(dr)==2 else (preset_start, preset_end)
# # #     else:
# # #         d0 = max(preset_start, date_min); d1 = min(preset_end, date_max)
# # #         st.caption(f"📅 {d0.strftime('%d %b %Y')} → {d1.strftime('%d %b %Y')}")

# # #     st.markdown('<div class="section-label">Scope</div>', unsafe_allow_html=True)
# # #     all_tables = sorted([str(v) for v in df_year_scoped["Affected Table Name"].dropna().unique()])
# # #     sel_tables = st.multiselect("Affected Tables", all_tables, default=all_tables)
# # #     all_types  = sorted([str(v) for v in df_year_scoped["Validation Short"].dropna().unique()])
# # #     sel_types  = st.multiselect("Validation Types", all_types, default=all_types)
# # #     show_only_issues = st.toggle("Issues only", value=False)

# # #     if st.session_state.popup_filter:
# # #         st.markdown('<div class="section-label">Popup</div>', unsafe_allow_html=True)
# # #         if st.button("✕ Close Drill-Down", use_container_width=True):
# # #             close_popup()

# # #     st.markdown("---")
# # #     st.markdown(f'<span style="font-size:0.65rem;color:{T["text_dim"]};letter-spacing:0.1em;text-transform:uppercase">v5.6 · {"🌙 Dark" if DARK else "☀️ Light"} Mode</span>', unsafe_allow_html=True)


# # # # ── Apply filters ──────────────────────────────────────────────────────────
# # # df = df_year_scoped[
# # #     (df_year_scoped["Verified Date"] >= d0) &
# # #     (df_year_scoped["Verified Date"] <= d1) &
# # #     (df_year_scoped["Affected Table Name"].astype(str).isin(sel_tables)) &
# # #     (df_year_scoped["Validation Short"].isin(sel_types))
# # # ].copy()
# # # if show_only_issues: df = df[df["Has Issue"]]

# # # total       = len(df)
# # # with_issues = int(df["Has Issue"].sum())
# # # clean       = total - with_issues
# # # total_recs  = int(df["Record Count"].sum())
# # # pass_rate   = (clean / total * 100) if total else 0

# # # days_sorted = sorted(df["Verified Date"].dropna().unique())
# # # if len(days_sorted) >= 2:
# # #     delta  = int(df[df["Verified Date"]==days_sorted[-1]]["Has Issue"].sum()) - int(df[df["Verified Date"]==days_sorted[-2]]["Has Issue"].sum())
# # #     dlabel = f"{'▲' if delta>0 else '▼' if delta<0 else '='} {abs(delta)} vs prev"
# # # else:
# # #     dlabel = "—"

# # # # ── Dashboard header ───────────────────────────────────────────────────────
# # # st.markdown(f"""
# # # <div class="dash-header">
# # #   <div class="dash-title">Data Quality Monitor</div>
# # #   <div class="dash-meta">
# # #     <span class="dash-meta-chip">📅 {d0.strftime('%d %b %Y')} → {d1.strftime('%d %b %Y')}</span>
# # #     <span class="dash-meta-chip">📋 {total:,} records</span>
# # #     {"<span class='dash-meta-chip'>🗓 " + sel_year + "</span>" if sel_year != "All Years" else ""}
# # #   </div>
# # # </div>
# # # """, unsafe_allow_html=True)

# # # # ── KPI buttons ────────────────────────────────────────────────────────────
# # # from ui.popup import open_popup
# # # from ui.components import green_css, grey_css

# # # active_kpi = st.session_state.popup_filter.get("kpi") if isinstance(st.session_state.popup_filter, dict) else None

# # # kpi_labels = {
# # #     "all":     "VALIDATION SUMMARY",
# # #     "issues":  "ISSUE OVERVIEW",
# # #     "clean":   f"VALIDATION SUCCESS RATE  {pass_rate:.1f}%",
# # #     "records": "IMPACT ANALYSIS",
# # # }

# # # active_map = {
# # #     "kpi_all":     active_kpi == "all",
# # #     "kpi_issues":  active_kpi == "issues",
# # #     "kpi_clean":   active_kpi == "clean",
# # #     "kpi_records": active_kpi == "records",
# # # }

# # # base_css = f"""
# # # <style>
# # # div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button {{
# # #     border-radius: 14px !important; font-family: 'Inter', sans-serif !important;
# # #     font-size: 0.78rem !important; height: 70px !important; width: 100% !important;
# # #     letter-spacing: 0.05em !important; transition: all 0.18s ease !important;
# # #     cursor: pointer !important; color: {T['text_muted']} !important;
# # # }}
# # # """
# # # col_map = [("kpi_all",1),("kpi_issues",2),("kpi_clean",3),("kpi_records",4)]
# # # for bid, nth in col_map:
# # #     base_css += green_css(nth, T) if active_map[bid] else grey_css(nth, T)
# # # base_css += "</style>"
# # # st.markdown(base_css, unsafe_allow_html=True)

# # # c1, c2, c3, c4 = st.columns(4)
# # # for col, ktype, bid in zip([c1,c2,c3,c4], ["all","issues","clean","records"],
# # #                            ["kpi_all","kpi_issues","kpi_clean","kpi_records"]):
# # #     with col:
# # #         if st.button(kpi_labels[ktype], key=bid, use_container_width=True):
# # #             open_popup({"kpi": ktype}, kpi_labels[ktype])

# # # st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)

# # # # ── Popup ──────────────────────────────────────────────────────────────────
# # # from ui.popup import render_popup
# # # render_popup(df, display_labels, T, _font_css, TABLE_JS)

# # # # ── Tab navigation ─────────────────────────────────────────────────────────
# # # TAB_LABELS = ["📈  Trend Analysis", "🗂  Issue Breakdown", "📋  Raw Records"]
# # # tab_selection = st.radio(
# # #     "tabs", TAB_LABELS, index=st.session_state.active_tab,
# # #     horizontal=True, label_visibility="collapsed", key="tab_radio"
# # # )
# # # active_tab = TAB_LABELS.index(tab_selection)
# # # st.session_state.active_tab = active_tab
# # # st.markdown(f'<div style="border-bottom:1px solid {T["border"]};margin:6px 0 22px"></div>', unsafe_allow_html=True)

# # # # ── Tab content ────────────────────────────────────────────────────────────
# # # if active_tab == 0:
# # #     from charts.tab_trend import render_tab_trend
# # #     render_tab_trend(df, T, LAYOUT, HOVER, PALETTE, PLOTLY_CONFIG, C_BLUE, C_GREEN, C_RED)

# # # elif active_tab == 1:
# # #     from charts.tab_breakdown import render_tab_breakdown
# # #     render_tab_breakdown(df, T, LAYOUT, HOVER, PALETTE, PLOTLY_CONFIG, C_RED, C_AMBER)

# # # elif active_tab == 2:
# # #     from charts.tab_rawdata import render_tab_rawdata
# # #     render_tab_rawdata(df, display_labels, T, _font_css, TABLE_JS)






 
# # import streamlit as st
# # import streamlit.components.v1 as components
# # from datetime import timedelta
# # import pandas as pd
 
# # # ── Page config (must be first Streamlit call) ─────────────────────────────
# # st.set_page_config(
# #     page_title="Data Quality Monitor",
# #     page_icon="🧬",
# #     layout="wide",
# #     initial_sidebar_state="expanded",
# # )
 
# # # ── Session state initialisation ──────────────────────────────────────────
# # def init_session():
# #     defaults = {
# #         "popup_filter": None, "popup_title": "",
# #         "active_tab": 0,
# #         "ct_trend": "Line", "ct_passbar": "Bar",
# #         "ct_cumulative": "Area", "ct_bytype": "Horizontal Bar", "ct_bytable": "Donut",
# #         "popup_sort_col": "Record Count", "popup_sort_asc": False,
# #         "close_popup_trigger": 0,
# #         "dark_mode": False,
# #     }
# #     for k, v in defaults.items():
# #         if k not in st.session_state:
# #             st.session_state[k] = v
 
# # init_session()
 
# # # ── Theme ──────────────────────────────────────────────────────────────────
# # from config.theme import get_theme, build_layout, build_hover, PLOTLY_CONFIG
 
# # DARK = st.session_state.dark_mode
# # T = get_theme(DARK)
# # LAYOUT = build_layout(T)
# # HOVER  = build_hover(T)
 
# # C_BLUE  = T["accent"]
# # C_GREEN = T["green"]
# # C_RED   = T["red"]
# # C_AMBER = T["amber"]
# # C_PURP  = T["purple"]
# # PALETTE = [C_BLUE, C_GREEN, C_AMBER, C_RED, C_PURP, "#0284c7", "#b91c1c", "#15803d"]
 
# # # ── Load fonts CSS ─────────────────────────────────────────────────────────
# # with open("assets/css/dashboardfonts.css", "r", encoding="utf-8") as _f:
# #     _font_css = _f.read()
 
# # # ── Load table JS ──────────────────────────────────────────────────────────
# # with open("assets/js/table.js", "r", encoding="utf-8") as _f:
# #     TABLE_JS = _f.read()
 
# # # ── Inject global styles ───────────────────────────────────────────────────
# # from ui.styles import inject_global_styles
# # inject_global_styles(T, _font_css)
 
# # # ── File upload gate ───────────────────────────────────────────────────────
# # if "uploaded_file" not in st.session_state:
# #     st.session_state.uploaded_file = None
 
# # if st.session_state.uploaded_file is None:
# #     st.markdown(f"""
# #     <style>
# #     section[data-testid="stSidebar"] {{ display: none !important; }}
# #     .upload-screen {{ display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 52vh; text-align: center; padding: 2rem 2rem 0; }}
# #     .upload-icon-ring {{ width: 110px; height: 110px; border-radius: 50%; background: linear-gradient(135deg, {T['accent_glow']}, {T['green_glow']}); border: 2px solid {T['accent']}; display: flex; align-items: center; justify-content: center; font-size: 3rem; margin: 0 auto 28px; box-shadow: 0 0 48px {T['accent_glow']}, 0 0 0 18px {T['accent_glow']}; animation: pulse-ring 2.8s ease-in-out infinite; }}
# #     @keyframes pulse-ring {{ 0%, 100% {{ box-shadow: 0 0 48px {T['accent_glow']}, 0 0 0 18px {T['accent_glow']}; }} 50% {{ box-shadow: 0 0 64px {T['accent_glow']}, 0 0 0 26px {T['accent_glow']}; }} }}
# #     .upload-title {{ font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; background: linear-gradient(135deg, {T['text_primary']} 30%, {T['accent']} 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 32px; letter-spacing: -0.02em; }}
# #     [data-testid="stFileUploaderDropzoneInstructions"] {{ display: none !important; }}
# #     [data-testid="stFileUploader"] small, [data-testid="stFileUploader"] span[class*="uploadInstructions"] {{ display: none !important; }}
# #     .center-uploader [data-testid="stFileUploader"] {{ background: {T['bg_card']} !important; border: 2px dashed {T['accent']} !important; border-radius: 16px !important; padding: 28px 32px !important; display: flex !important; justify-content: center !important; }}
# #     .center-uploader [data-testid="stFileUploaderDropzone"] {{ display: flex !important; justify-content: center !important; align-items: center !important; width: 100% !important; }}
# #     .center-uploader section[data-testid="stFileUploaderDropzone"] > div {{ display: flex !important; justify-content: center !important; width: 100% !important; }}
# #     .center-uploader [data-testid="stFileUploader"]:hover {{ border-color: {T['accent']} !important; background: {T['bg_hover']} !important; }}
# #     .center-uploader [data-testid="stFileUploaderDropzone"] {{ background: transparent !important; }}
# #     </style>
# #     <div class="upload-screen">
# #       <div class="upload-icon-ring">🧬</div>
# #       <div class="upload-title">Data Quality Monitor</div>
# #     </div>
# #     """, unsafe_allow_html=True)
 
# #     _, col_mid, _ = st.columns([1, 2, 1])
# #     with col_mid:
# #         st.markdown('<div class="center-uploader">', unsafe_allow_html=True)
# #         center_upload = st.file_uploader("Upload a CSV or Excel file to get started", type=["csv", "xlsx", "xls"], key="center_uploader")
# #         st.markdown('</div>', unsafe_allow_html=True)
 
# #     if center_upload is not None:
# #         st.session_state.uploaded_file = center_upload
# #         st.rerun()
# #     st.stop()
 
 
# # # ── Load data ──────────────────────────────────────────────────────────────
# # from data.loader import load_data
 
# # uploaded = st.session_state.uploaded_file
# # df_raw, display_labels = load_data(uploaded)
 
# # def dlbl(canonical: str) -> str:
# #     """Return the original uploaded column name for a given canonical name."""
# #     return display_labels.get(canonical, canonical)
 
 
# # # ── Sidebar ────────────────────────────────────────────────────────────────
# # from ui.popup import close_popup
 
# # with st.sidebar:
# #     st.markdown(f"""
# #     <div class="sidebar-brand">
# #       <div class="sidebar-brand-icon">🧬</div>
# #       <div>
# #         <div class="sidebar-brand-text">Data Quality Monitor</div>
# #         <div class="sidebar-brand-sub">Clinical Data Quality</div>
# #       </div>
# #     </div>
# #     """, unsafe_allow_html=True)
 
# #     new_dark = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode, key="dark_toggle")
# #     if new_dark != st.session_state.dark_mode:
# #         st.session_state.dark_mode = new_dark
# #         st.rerun()
 
# #     if st.button("📂 Change File", use_container_width=True):
# #         st.session_state.uploaded_file = None
# #         st.rerun()
 
# #     st.markdown('<div class="section-label">Filters</div>', unsafe_allow_html=True)
# #     available_years = sorted(df_raw["Year"].dropna().unique().astype(int).tolist())
# #     sel_year = st.selectbox("📅 Year", ["All Years"] + [str(y) for y in available_years], index=0)
# #     df_year_scoped = df_raw if sel_year == "All Years" else df_raw[df_raw["Year"] == int(sel_year)].copy()
 
# #     MONTH_NAMES = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
# #                    7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
# #     available_months = sorted(df_year_scoped["Verified Date"].dropna().dt.month.unique().astype(int).tolist())
# #     month_options = ["All Months"] + [MONTH_NAMES[m] for m in available_months]
# #     sel_month = st.selectbox("🗓 Month", month_options, index=0)
# #     if sel_month != "All Months":
# #         sel_month_num = [k for k, v in MONTH_NAMES.items() if v == sel_month][0]
# #         df_year_scoped = df_year_scoped[df_year_scoped["Verified Date"].dt.month == sel_month_num].copy()
 
# #     all_dates = sorted(df_year_scoped["Verified Date"].dropna().unique())
# #     if not all_dates:
# #         st.warning("No data for selected filters.")
# #         st.stop()
# #     date_min = pd.Timestamp(min(all_dates)); date_max = pd.Timestamp(max(all_dates))
 
# #     preset = st.selectbox("⏱ Timeline", [
# #         "Custom Range","Last 7 Days","Last 14 Days","Last 30 Days","Last 45 Days",
# #         "Last 60 Days","Last 3 Months","Last 6 Months","Last 12 Months","Last Quarter","All Time"
# #     ], index=10)
 
# #     offsets = {
# #         "Last 7 Days":6,"Last 14 Days":13,"Last 30 Days":29,"Last 45 Days":44,
# #         "Last 60 Days":59,"Last 3 Months":89,"Last 6 Months":179,"Last 12 Months":364,
# #     }
 
# #     def _prev_completed_quarter(ref_date):
# #         # Previous fully-completed calendar quarter relative to ref_date
# #         # Jan-Mar -> Q1, Apr-Jun -> Q2, Jul-Sep -> Q3, Oct-Dec -> Q4
# #         q = (ref_date.month - 1) // 3 + 1
# #         cur_q_start = pd.Timestamp(year=ref_date.year, month=3 * (q - 1) + 1, day=1)
# #         prev_q_end = cur_q_start - timedelta(days=1)
# #         prev_q = (prev_q_end.month - 1) // 3 + 1
# #         prev_q_start = pd.Timestamp(year=prev_q_end.year, month=3 * (prev_q - 1) + 1, day=1)
# #         return prev_q_start, prev_q_end
 
# #     if preset == "Last Quarter":
# #         preset_start, preset_end = _prev_completed_quarter(date_max)
# #     elif preset in offsets:
# #         preset_start, preset_end = (date_max - timedelta(days=offsets[preset])), date_max
# #     else:
# #         preset_start, preset_end = date_min, date_max
 
# #     if preset == "Custom Range":
# #         dr = st.date_input("Range", value=(preset_start.date(), preset_end.date()),
# #                            min_value=date_min.date(), max_value=date_max.date())
# #         d0, d1 = (pd.Timestamp(dr[0]), pd.Timestamp(dr[1])) if len(dr)==2 else (preset_start, preset_end)
# #     else:
# #         d0 = max(preset_start, date_min); d1 = min(preset_end, date_max)
# #         st.caption(f"📅 {d0.strftime('%d %b %Y')} → {d1.strftime('%d %b %Y')}")
 
# #     st.markdown('<div class="section-label">Scope</div>', unsafe_allow_html=True)
# #     all_tables = sorted([str(v) for v in df_year_scoped["Affected Table Name"].dropna().unique()])
# #     sel_tables = st.multiselect("Affected Tables", all_tables, default=all_tables)
# #     all_types  = sorted([str(v) for v in df_year_scoped["Validation Short"].dropna().unique()])
# #     sel_types  = st.multiselect("Validation Types", all_types, default=all_types)
# #     show_only_issues = st.toggle("Issues only", value=False)
 
# #     if st.session_state.popup_filter:
# #         st.markdown('<div class="section-label">Popup</div>', unsafe_allow_html=True)
# #         if st.button("✕ Close Drill-Down", use_container_width=True):
# #             close_popup()
 
# #     st.markdown("---")
# #     st.markdown(f'<span style="font-size:0.65rem;color:{T["text_dim"]};letter-spacing:0.1em;text-transform:uppercase">v5.6 · {"🌙 Dark" if DARK else "☀️ Light"} Mode</span>', unsafe_allow_html=True)
 
 
# # # ── Apply filters ──────────────────────────────────────────────────────────
# # df = df_year_scoped[
# #     (df_year_scoped["Verified Date"] >= d0) &
# #     (df_year_scoped["Verified Date"] <= d1) &
# #     (df_year_scoped["Affected Table Name"].astype(str).isin(sel_tables)) &
# #     (df_year_scoped["Validation Short"].isin(sel_types))
# # ].copy()
# # if show_only_issues: df = df[df["Has Issue"]]
 
# # total       = len(df)
# # with_issues = int(df["Has Issue"].sum())
# # clean       = total - with_issues
# # total_recs  = int(df["Record Count"].sum())
# # pass_rate   = (clean / total * 100) if total else 0
 
# # days_sorted = sorted(df["Verified Date"].dropna().unique())
# # if len(days_sorted) >= 2:
# #     delta  = int(df[df["Verified Date"]==days_sorted[-1]]["Has Issue"].sum()) - int(df[df["Verified Date"]==days_sorted[-2]]["Has Issue"].sum())
# #     dlabel = f"{'▲' if delta>0 else '▼' if delta<0 else '='} {abs(delta)} vs prev"
# # else:
# #     dlabel = "—"
 
# # # ── Dashboard header ───────────────────────────────────────────────────────
# # st.markdown(f"""
# # <div class="dash-header">
# #   <div class="dash-title">Data Quality Monitor</div>
# #   <div class="dash-meta">
# #     <span class="dash-meta-chip">📅 {d0.strftime('%d %b %Y')} → {d1.strftime('%d %b %Y')}</span>
# #     <span class="dash-meta-chip">📋 {total:,} records</span>
# #     {"<span class='dash-meta-chip'>🗓 " + sel_year + "</span>" if sel_year != "All Years" else ""}
# #   </div>
# # </div>
# # """, unsafe_allow_html=True)
 
# # # ── KPI buttons ────────────────────────────────────────────────────────────
# # from ui.popup import open_popup
# # from ui.components import green_css, grey_css
 
# # active_kpi = st.session_state.popup_filter.get("kpi") if isinstance(st.session_state.popup_filter, dict) else None
 
# # kpi_labels = {
# #     "all":     "VALIDATION SUMMARY",
# #     "issues":  "ISSUE OVERVIEW",
# #     "clean":   f"VALIDATION SUCCESS RATE  {pass_rate:.1f}%",
# #     "records": "IMPACT ANALYSIS",
# # }
 
# # active_map = {
# #     "kpi_all":     active_kpi == "all",
# #     "kpi_issues":  active_kpi == "issues",
# #     "kpi_clean":   active_kpi == "clean",
# #     "kpi_records": active_kpi == "records",
# # }
 
# # base_css = f"""
# # <style>
# # div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button {{
# #     border-radius: 14px !important; font-family: 'Inter', sans-serif !important;
# #     font-size: 0.78rem !important; height: 70px !important; width: 100% !important;
# #     letter-spacing: 0.05em !important; transition: all 0.18s ease !important;
# #     cursor: pointer !important; color: {T['text_muted']} !important;
# # }}
# # """
# # col_map = [("kpi_all",1),("kpi_issues",2),("kpi_clean",3),("kpi_records",4)]
# # for bid, nth in col_map:
# #     base_css += green_css(nth, T) if active_map[bid] else grey_css(nth, T)
# # base_css += "</style>"
# # st.markdown(base_css, unsafe_allow_html=True)
 
# # c1, c2, c3, c4 = st.columns(4)
# # for col, ktype, bid in zip([c1,c2,c3,c4], ["all","issues","clean","records"],
# #                            ["kpi_all","kpi_issues","kpi_clean","kpi_records"]):
# #     with col:
# #         if st.button(kpi_labels[ktype], key=bid, use_container_width=True):
# #             open_popup({"kpi": ktype}, kpi_labels[ktype])
 
# # st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
 
# # # ── Popup ──────────────────────────────────────────────────────────────────
# # from ui.popup import render_popup
# # render_popup(df, display_labels, T, _font_css, TABLE_JS)
 
# # # ── Tab navigation ─────────────────────────────────────────────────────────
# # TAB_LABELS = ["📈  Trend Analysis", "🗂  Issue Breakdown", "📋  Raw Records"]
# # tab_selection = st.radio(
# #     "tabs", TAB_LABELS, index=st.session_state.active_tab,
# #     horizontal=True, label_visibility="collapsed", key="tab_radio"
# # )
# # active_tab = TAB_LABELS.index(tab_selection)
# # st.session_state.active_tab = active_tab
# # st.markdown(f'<div style="border-bottom:1px solid {T["border"]};margin:6px 0 22px"></div>', unsafe_allow_html=True)
 
# # # ── Tab content ────────────────────────────────────────────────────────────
# # if active_tab == 0:
# #     from charts.tab_trend import render_tab_trend
# #     render_tab_trend(df, T, LAYOUT, HOVER, PALETTE, PLOTLY_CONFIG, C_BLUE, C_GREEN, C_RED)
 
# # elif active_tab == 1:
# #     from charts.tab_breakdown import render_tab_breakdown
# #     render_tab_breakdown(df, T, LAYOUT, HOVER, PALETTE, PLOTLY_CONFIG, C_RED, C_AMBER)
 
# # elif active_tab == 2:
# #     from charts.tab_rawdata import render_tab_rawdata
# #     render_tab_rawdata(df, display_labels, T, _font_css, TABLE_JS)





# import streamlit as st
# import streamlit.components.v1 as components
# from datetime import timedelta
# import pandas as pd
 
# # ── Page config (must be first Streamlit call) ─────────────────────────────
# st.set_page_config(
#     page_title="Data Quality Monitor",
#     page_icon="🧬",
#     layout="wide",
#     initial_sidebar_state="expanded",
# )
 
# # ── Session state initialisation ──────────────────────────────────────────
# def init_session():
#     defaults = {
#         "popup_filter": None, "popup_title": "",
#         "active_tab": 0,
#         "ct_trend": "Line", "ct_passbar": "Bar",
#         "ct_cumulative": "Area", "ct_bytype": "Horizontal Bar", "ct_bytable": "Donut",
#         "popup_sort_col": "Record Count", "popup_sort_asc": False,
#         "close_popup_trigger": 0,
#         "dark_mode": False,
#     }
#     for k, v in defaults.items():
#         if k not in st.session_state:
#             st.session_state[k] = v
 
# init_session()
 
# # ── Theme ──────────────────────────────────────────────────────────────────
# from config.theme import get_theme, build_layout, build_hover, PLOTLY_CONFIG
 
# DARK = st.session_state.dark_mode
# T = get_theme(DARK)
# LAYOUT = build_layout(T)
# HOVER  = build_hover(T)
 
# C_BLUE  = T["accent"]
# C_GREEN = T["green"]
# C_RED   = T["red"]
# C_AMBER = T["amber"]
# C_PURP  = T["purple"]
# PALETTE = [C_BLUE, C_GREEN, C_AMBER, C_RED, C_PURP, "#0284c7", "#b91c1c", "#15803d"]
 
# # ── Load fonts CSS ─────────────────────────────────────────────────────────
# with open("assets/css/dashboardfonts.css", "r", encoding="utf-8") as _f:
#     _font_css = _f.read()
 
# # ── Load table JS ──────────────────────────────────────────────────────────
# with open("assets/js/table.js", "r", encoding="utf-8") as _f:
#     TABLE_JS = _f.read()
 
# # ── Inject global styles ───────────────────────────────────────────────────
# from ui.styles import inject_global_styles
# inject_global_styles(T, _font_css)
# from ui.components import inject_axis_rail_arrows
# inject_axis_rail_arrows()
 
# # ── File upload gate ───────────────────────────────────────────────────────
# if "uploaded_file" not in st.session_state:
#     st.session_state.uploaded_file = None
 
# if st.session_state.uploaded_file is None:
#     st.markdown(f"""
#     <style>
#     section[data-testid="stSidebar"] {{ display: none !important; }}
#     .upload-screen {{ display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 52vh; text-align: center; padding: 2rem 2rem 0; }}
#     .upload-icon-ring {{ width: 110px; height: 110px; border-radius: 50%; background: linear-gradient(135deg, {T['accent_glow']}, {T['green_glow']}); border: 2px solid {T['accent']}; display: flex; align-items: center; justify-content: center; font-size: 3rem; margin: 0 auto 28px; box-shadow: 0 0 48px {T['accent_glow']}, 0 0 0 18px {T['accent_glow']}; animation: pulse-ring 2.8s ease-in-out infinite; }}
#     @keyframes pulse-ring {{ 0%, 100% {{ box-shadow: 0 0 48px {T['accent_glow']}, 0 0 0 18px {T['accent_glow']}; }} 50% {{ box-shadow: 0 0 64px {T['accent_glow']}, 0 0 0 26px {T['accent_glow']}; }} }}
#     .upload-title {{ font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; background: linear-gradient(135deg, {T['text_primary']} 30%, {T['accent']} 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 32px; letter-spacing: -0.02em; }}
#     [data-testid="stFileUploaderDropzoneInstructions"] {{ display: none !important; }}
#     [data-testid="stFileUploader"] small, [data-testid="stFileUploader"] span[class*="uploadInstructions"] {{ display: none !important; }}
#     .center-uploader [data-testid="stFileUploader"] {{ background: {T['bg_card']} !important; border: 2px dashed {T['accent']} !important; border-radius: 16px !important; padding: 28px 32px !important; display: flex !important; justify-content: center !important; }}
#     .center-uploader [data-testid="stFileUploaderDropzone"] {{ display: flex !important; justify-content: center !important; align-items: center !important; width: 100% !important; }}
#     .center-uploader section[data-testid="stFileUploaderDropzone"] > div {{ display: flex !important; justify-content: center !important; width: 100% !important; }}
#     .center-uploader [data-testid="stFileUploader"]:hover {{ border-color: {T['accent']} !important; background: {T['bg_hover']} !important; }}
#     .center-uploader [data-testid="stFileUploaderDropzone"] {{ background: transparent !important; }}
#     </style>
#     <div class="upload-screen">
#       <div class="upload-icon-ring">🧬</div>
#       <div class="upload-title">Data Quality Monitor</div>
#     </div>
#     """, unsafe_allow_html=True)
 
#     _, col_mid, _ = st.columns([1, 2, 1])
#     with col_mid:
#         st.markdown('<div class="center-uploader">', unsafe_allow_html=True)
#         center_upload = st.file_uploader("Upload a CSV or Excel file to get started", type=["csv", "xlsx", "xls"], key="center_uploader")
#         st.markdown('</div>', unsafe_allow_html=True)
 
#     if center_upload is not None:
#         st.session_state.uploaded_file = center_upload
#         st.rerun()
#     st.stop()
 
 
# # ── Load data ──────────────────────────────────────────────────────────────
# from data.loader import load_data
 
# uploaded = st.session_state.uploaded_file
# df_raw, display_labels = load_data(uploaded)
 
# def dlbl(canonical: str) -> str:
#     """Return the original uploaded column name for a given canonical name."""
#     return display_labels.get(canonical, canonical)
 
 
# # ── Sidebar ────────────────────────────────────────────────────────────────
# from ui.popup import close_popup
 
# with st.sidebar:
#     st.markdown(f"""
#     <div class="sidebar-brand">
#       <div class="sidebar-brand-icon">🧬</div>
#       <div>
#         <div class="sidebar-brand-text">Data Quality Monitor</div>
#         <div class="sidebar-brand-sub">Clinical Data Quality</div>
#       </div>
#     </div>
#     """, unsafe_allow_html=True)
 
#     new_dark = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode, key="dark_toggle")
#     if new_dark != st.session_state.dark_mode:
#         st.session_state.dark_mode = new_dark
#         st.rerun()
 
#     if st.button("📂 Change File", use_container_width=True):
#         st.session_state.uploaded_file = None
#         st.rerun()
 
#     st.markdown('<div class="section-label">Filters</div>', unsafe_allow_html=True)
#     available_years = sorted(df_raw["Year"].dropna().unique().astype(int).tolist())
#     sel_year = st.selectbox("📅 Year", ["All Years"] + [str(y) for y in available_years], index=0)
#     df_year_scoped = df_raw if sel_year == "All Years" else df_raw[df_raw["Year"] == int(sel_year)].copy()
 
#     MONTH_NAMES = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
#                    7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
#     available_months = sorted(df_year_scoped["Verified Date"].dropna().dt.month.unique().astype(int).tolist())
#     month_options = ["All Months"] + [MONTH_NAMES[m] for m in available_months]
#     sel_month = st.selectbox("🗓 Month", month_options, index=0)
#     if sel_month != "All Months":
#         sel_month_num = [k for k, v in MONTH_NAMES.items() if v == sel_month][0]
#         df_year_scoped = df_year_scoped[df_year_scoped["Verified Date"].dt.month == sel_month_num].copy()
 
#     all_dates = sorted(df_year_scoped["Verified Date"].dropna().unique())
#     if not all_dates:
#         st.warning("No data for selected filters.")
#         st.stop()
#     date_min = pd.Timestamp(min(all_dates)); date_max = pd.Timestamp(max(all_dates))
 
#     preset = st.selectbox("⏱ Timeline", [
#         "Custom Range","Last 7 Days","Last 14 Days","Last 30 Days","Last 45 Days",
#         "Last 60 Days","Last 3 Months","Last 6 Months","Last 12 Months","Last Quarter","All Time"
#     ], index=10)
 
#     offsets = {
#         "Last 7 Days":6,"Last 14 Days":13,"Last 30 Days":29,"Last 45 Days":44,
#         "Last 60 Days":59,"Last 3 Months":89,"Last 6 Months":179,"Last 12 Months":364,
#     }
 
#     def _prev_completed_quarter(ref_date):
#         # Previous fully-completed calendar quarter relative to ref_date
#         # Jan-Mar -> Q1, Apr-Jun -> Q2, Jul-Sep -> Q3, Oct-Dec -> Q4
#         q = (ref_date.month - 1) // 3 + 1
#         cur_q_start = pd.Timestamp(year=ref_date.year, month=3 * (q - 1) + 1, day=1)
#         prev_q_end = cur_q_start - timedelta(days=1)
#         prev_q = (prev_q_end.month - 1) // 3 + 1
#         prev_q_start = pd.Timestamp(year=prev_q_end.year, month=3 * (prev_q - 1) + 1, day=1)
#         return prev_q_start, prev_q_end
 
#     if preset == "Last Quarter":
#         preset_start, preset_end = _prev_completed_quarter(date_max)
#     elif preset in offsets:
#         preset_start, preset_end = (date_max - timedelta(days=offsets[preset])), date_max
#     else:
#         preset_start, preset_end = date_min, date_max
 
#     if preset == "Custom Range":
#         dr = st.date_input("Range", value=(preset_start.date(), preset_end.date()),
#                            min_value=date_min.date(), max_value=date_max.date())
#         d0, d1 = (pd.Timestamp(dr[0]), pd.Timestamp(dr[1])) if len(dr)==2 else (preset_start, preset_end)
#     else:
#         d0 = max(preset_start, date_min); d1 = min(preset_end, date_max)
#         st.caption(f"📅 {d0.strftime('%d %b %Y')} → {d1.strftime('%d %b %Y')}")
 
#     st.markdown('<div class="section-label">Scope</div>', unsafe_allow_html=True)
#     all_tables = sorted([str(v) for v in df_year_scoped["Affected Table Name"].dropna().unique()])
#     sel_tables = st.multiselect("Affected Tables", all_tables, default=all_tables)
#     all_types  = sorted([str(v) for v in df_year_scoped["Validation Short"].dropna().unique()])
#     sel_types  = st.multiselect("Validation Types", all_types, default=all_types)
#     show_only_issues = st.toggle("Issues only", value=False)
 
#     if st.session_state.popup_filter:
#         st.markdown('<div class="section-label">Popup</div>', unsafe_allow_html=True)
#         if st.button("✕ Close Drill-Down", use_container_width=True):
#             close_popup()
 
#     st.markdown("---")
#     st.markdown(f'<span style="font-size:0.65rem;color:{T["text_dim"]};letter-spacing:0.1em;text-transform:uppercase">v5.6 · {"🌙 Dark" if DARK else "☀️ Light"} Mode</span>', unsafe_allow_html=True)
 
 
# # ── Apply filters ──────────────────────────────────────────────────────────
# df = df_year_scoped[
#     (df_year_scoped["Verified Date"] >= d0) &
#     (df_year_scoped["Verified Date"] <= d1) &
#     (df_year_scoped["Affected Table Name"].astype(str).isin(sel_tables)) &
#     (df_year_scoped["Validation Short"].isin(sel_types))
# ].copy()
# if show_only_issues: df = df[df["Has Issue"]]
 
# total       = len(df)
# with_issues = int(df["Has Issue"].sum())
# clean       = total - with_issues
# total_recs  = int(df["Record Count"].sum())
# pass_rate   = (clean / total * 100) if total else 0
 
# days_sorted = sorted(df["Verified Date"].dropna().unique())
# if len(days_sorted) >= 2:
#     delta  = int(df[df["Verified Date"]==days_sorted[-1]]["Has Issue"].sum()) - int(df[df["Verified Date"]==days_sorted[-2]]["Has Issue"].sum())
#     dlabel = f"{'▲' if delta>0 else '▼' if delta<0 else '='} {abs(delta)} vs prev"
# else:
#     dlabel = "—"
 
# # ── Dashboard header ───────────────────────────────────────────────────────
# st.markdown(f"""
# <div class="dash-header">
#   <div class="dash-title">Data Quality Monitor</div>
#   <div class="dash-meta">
#     <span class="dash-meta-chip">📅 {d0.strftime('%d %b %Y')} → {d1.strftime('%d %b %Y')}</span>
#     <span class="dash-meta-chip">📋 {total:,} records</span>
#     {"<span class='dash-meta-chip'>🗓 " + sel_year + "</span>" if sel_year != "All Years" else ""}
#   </div>
# </div>
# """, unsafe_allow_html=True)
 
# # ── KPI buttons ────────────────────────────────────────────────────────────
# from ui.popup import open_popup
# from ui.components import green_css, grey_css
 
# active_kpi = st.session_state.popup_filter.get("kpi") if isinstance(st.session_state.popup_filter, dict) else None
 
# kpi_labels = {
#     "all":     "VALIDATION SUMMARY",
#     "issues":  "ISSUE OVERVIEW",
#     "clean":   f"VALIDATION SUCCESS RATE  {pass_rate:.1f}%",
#     "records": "IMPACT ANALYSIS",
# }
 
# active_map = {
#     "kpi_all":     active_kpi == "all",
#     "kpi_issues":  active_kpi == "issues",
#     "kpi_clean":   active_kpi == "clean",
#     "kpi_records": active_kpi == "records",
# }
 
# base_css = f"""
# <style>
# div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button {{
#     border-radius: 14px !important; font-family: 'Inter', sans-serif !important;
#     font-size: 0.78rem !important; height: 70px !important; width: 100% !important;
#     letter-spacing: 0.05em !important; transition: all 0.18s ease !important;
#     cursor: pointer !important; color: {T['text_muted']} !important;
# }}
# """
# col_map = [("kpi_all",1),("kpi_issues",2),("kpi_clean",3),("kpi_records",4)]
# for bid, nth in col_map:
#     base_css += green_css(nth, T) if active_map[bid] else grey_css(nth, T)
# base_css += "</style>"
# st.markdown(base_css, unsafe_allow_html=True)
 
# c1, c2, c3, c4 = st.columns(4)
# for col, ktype, bid in zip([c1,c2,c3,c4], ["all","issues","clean","records"],
#                            ["kpi_all","kpi_issues","kpi_clean","kpi_records"]):
#     with col:
#         if st.button(kpi_labels[ktype], key=bid, use_container_width=True):
#             open_popup({"kpi": ktype}, kpi_labels[ktype])
 
# st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
 
# # ── Popup ──────────────────────────────────────────────────────────────────
# from ui.popup import render_popup
# render_popup(df, display_labels, T, _font_css, TABLE_JS)
 
# # ── Tab navigation ─────────────────────────────────────────────────────────
# TAB_LABELS = ["📈  Trend Analysis", "🗂  Issue Breakdown", "📋  Raw Records"]
# tab_selection = st.radio(
#     "tabs", TAB_LABELS, index=st.session_state.active_tab,
#     horizontal=True, label_visibility="collapsed", key="tab_radio"
# )
# active_tab = TAB_LABELS.index(tab_selection)
# st.session_state.active_tab = active_tab
# st.markdown(f'<div style="border-bottom:1px solid {T["border"]};margin:6px 0 22px"></div>', unsafe_allow_html=True)
 
# # ── Tab content ────────────────────────────────────────────────────────────
# if active_tab == 0:
#     from charts.tab_trend import render_tab_trend
#     render_tab_trend(df, T, LAYOUT, HOVER, PALETTE, PLOTLY_CONFIG, C_BLUE, C_GREEN, C_RED)
 
# elif active_tab == 1:
#     from charts.tab_breakdown import render_tab_breakdown
#     render_tab_breakdown(df, T, LAYOUT, HOVER, PALETTE, PLOTLY_CONFIG, C_RED, C_AMBER)
 
# elif active_tab == 2:
#     from charts.tab_rawdata import render_tab_rawdata
#     render_tab_rawdata(df, display_labels, T, _font_css, TABLE_JS)












 
import streamlit as st
import streamlit.components.v1 as components
from datetime import timedelta
import pandas as pd
 
# ── Page config (must be first Streamlit call) ─────────────────────────────
st.set_page_config(
    page_title="Data Quality Monitor",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded",
)
 
# ── Session state initialisation ──────────────────────────────────────────
def init_session():
    defaults = {
        "popup_filter": None, "popup_title": "",
        "active_tab": 0,
        "ct_trend": "Line", "ct_passbar": "Bar",
        "ct_cumulative": "Area", "ct_bytype": "Horizontal Bar", "ct_bytable": "Donut",
        "popup_sort_col": "Record Count", "popup_sort_asc": False,
        "close_popup_trigger": 0,
        "dark_mode": False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
 
init_session()
 
# ── Theme ──────────────────────────────────────────────────────────────────
from config.theme import get_theme, build_layout, build_hover, PLOTLY_CONFIG
 
DARK = st.session_state.dark_mode
T = get_theme(DARK)
LAYOUT = build_layout(T)
HOVER  = build_hover(T)
 
C_BLUE  = T["accent"]
C_GREEN = T["green"]
C_RED   = T["red"]
C_AMBER = T["amber"]
C_PURP  = T["purple"]
PALETTE = [C_BLUE, C_GREEN, C_AMBER, C_RED, C_PURP, "#0284c7", "#b91c1c", "#15803d"]
 
# ── Load fonts CSS ─────────────────────────────────────────────────────────
with open("assets/css/dashboardfonts.css", "r", encoding="utf-8") as _f:
    _font_css = _f.read()
 
# ── Load table JS ──────────────────────────────────────────────────────────
with open("assets/js/table.js", "r", encoding="utf-8") as _f:
    TABLE_JS = _f.read()
 
# ── Inject global styles ───────────────────────────────────────────────────
from ui.styles import inject_global_styles
inject_global_styles(T, _font_css)
from ui.components import inject_axis_rail_arrows
inject_axis_rail_arrows()
 
# ── File upload gate ───────────────────────────────────────────────────────
if "uploaded_file" not in st.session_state:
    st.session_state.uploaded_file = None
 
if st.session_state.uploaded_file is None:
    st.markdown(f"""
    <style>
    section[data-testid="stSidebar"] {{ display: none !important; }}
    .upload-screen {{ display: flex; flex-direction: column; align-items: center; justify-content: center; min-height: 52vh; text-align: center; padding: 2rem 2rem 0; }}
    .upload-icon-ring {{ width: 110px; height: 110px; border-radius: 50%; background: linear-gradient(135deg, {T['accent_glow']}, {T['green_glow']}); border: 2px solid {T['accent']}; display: flex; align-items: center; justify-content: center; font-size: 3rem; margin: 0 auto 28px; box-shadow: 0 0 48px {T['accent_glow']}, 0 0 0 18px {T['accent_glow']}; animation: pulse-ring 2.8s ease-in-out infinite; }}
    @keyframes pulse-ring {{ 0%, 100% {{ box-shadow: 0 0 48px {T['accent_glow']}, 0 0 0 18px {T['accent_glow']}; }} 50% {{ box-shadow: 0 0 64px {T['accent_glow']}, 0 0 0 26px {T['accent_glow']}; }} }}
    .upload-title {{ font-family: 'Syne', sans-serif; font-size: 2rem; font-weight: 800; background: linear-gradient(135deg, {T['text_primary']} 30%, {T['accent']} 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; margin-bottom: 32px; letter-spacing: -0.02em; }}
    [data-testid="stFileUploaderDropzoneInstructions"] {{ display: none !important; }}
    [data-testid="stFileUploader"] small, [data-testid="stFileUploader"] span[class*="uploadInstructions"] {{ display: none !important; }}
    .center-uploader [data-testid="stFileUploader"] {{ background: {T['bg_card']} !important; border: 2px dashed {T['accent']} !important; border-radius: 16px !important; padding: 28px 32px !important; display: flex !important; justify-content: center !important; }}
    .center-uploader [data-testid="stFileUploaderDropzone"] {{ display: flex !important; justify-content: center !important; align-items: center !important; width: 100% !important; }}
    .center-uploader section[data-testid="stFileUploaderDropzone"] > div {{ display: flex !important; justify-content: center !important; width: 100% !important; }}
    .center-uploader [data-testid="stFileUploader"]:hover {{ border-color: {T['accent']} !important; background: {T['bg_hover']} !important; }}
    .center-uploader [data-testid="stFileUploaderDropzone"] {{ background: transparent !important; }}
    </style>
    <div class="upload-screen">
      <div class="upload-icon-ring">🧬</div>
      <div class="upload-title">Data Quality Monitor</div>
    </div>
    """, unsafe_allow_html=True)
 
    _, col_mid, _ = st.columns([1, 2, 1])
    with col_mid:
        st.markdown('<div class="center-uploader">', unsafe_allow_html=True)
        center_upload = st.file_uploader("Upload a CSV or Excel file to get started", type=["csv", "xlsx", "xls"], key="center_uploader")
        st.markdown('</div>', unsafe_allow_html=True)
 
    if center_upload is not None:
        st.session_state.uploaded_file = center_upload
        st.rerun()
    st.stop()
 
 
# ── Load data ──────────────────────────────────────────────────────────────
from data.loader import load_data
 
uploaded = st.session_state.uploaded_file
df_raw, display_labels = load_data(uploaded)
 
def dlbl(canonical: str) -> str:
    """Return the original uploaded column name for a given canonical name."""
    return display_labels.get(canonical, canonical)
 
 
# ── Sidebar ────────────────────────────────────────────────────────────────
from ui.popup import close_popup
 
with st.sidebar:
    st.markdown(f"""
    <div class="sidebar-brand">
      <div class="sidebar-brand-icon">🧬</div>
      <div>
        <div class="sidebar-brand-text">Data Quality Monitor</div>
        <div class="sidebar-brand-sub">Clinical Data Quality</div>
      </div>
    </div>
    """, unsafe_allow_html=True)
 
    new_dark = st.toggle("🌙 Dark Mode", value=st.session_state.dark_mode, key="dark_toggle")
    if new_dark != st.session_state.dark_mode:
        st.session_state.dark_mode = new_dark
        st.rerun()
 
    if st.button("📂 Change File", use_container_width=True):
        st.session_state.uploaded_file = None
        st.rerun()
 
    st.markdown('<div class="section-label">Filters</div>', unsafe_allow_html=True)
    available_years = sorted(df_raw["Year"].dropna().unique().astype(int).tolist())
    sel_year = st.selectbox("📅 Year", ["All Years"] + [str(y) for y in available_years], index=0)
    df_year_scoped = df_raw if sel_year == "All Years" else df_raw[df_raw["Year"] == int(sel_year)].copy()
 
    MONTH_NAMES = {1:"January",2:"February",3:"March",4:"April",5:"May",6:"June",
                   7:"July",8:"August",9:"September",10:"October",11:"November",12:"December"}
    available_months = sorted(df_year_scoped["Verified Date"].dropna().dt.month.unique().astype(int).tolist())
    month_options = ["All Months"] + [MONTH_NAMES[m] for m in available_months]
    sel_month = st.selectbox("🗓 Month", month_options, index=0)
    if sel_month != "All Months":
        sel_month_num = [k for k, v in MONTH_NAMES.items() if v == sel_month][0]
        df_year_scoped = df_year_scoped[df_year_scoped["Verified Date"].dt.month == sel_month_num].copy()
 
    all_dates = sorted(df_year_scoped["Verified Date"].dropna().unique())
    if not all_dates:
        st.warning("No data for selected filters.")
        st.stop()
    date_min = pd.Timestamp(min(all_dates)); date_max = pd.Timestamp(max(all_dates))
 
    preset = st.selectbox("⏱ Timeline", [
        "Custom Range","Last 7 Days","Last 14 Days","Last 30 Days","Last 45 Days",
        "Last 60 Days","Last 3 Months","Last 6 Months","Last 12 Months","Last Quarter","All Time"
    ], index=10)
 
    offsets = {
        "Last 7 Days":6,"Last 14 Days":13,"Last 30 Days":29,"Last 45 Days":44,
        "Last 60 Days":59,"Last 3 Months":89,"Last 6 Months":179,"Last 12 Months":364,
    }
 
    def _prev_completed_quarter(ref_date):
        # Previous fully-completed calendar quarter relative to ref_date
        # Jan-Mar -> Q1, Apr-Jun -> Q2, Jul-Sep -> Q3, Oct-Dec -> Q4
        q = (ref_date.month - 1) // 3 + 1
        cur_q_start = pd.Timestamp(year=ref_date.year, month=3 * (q - 1) + 1, day=1)
        prev_q_end = cur_q_start - timedelta(days=1)
        prev_q = (prev_q_end.month - 1) // 3 + 1
        prev_q_start = pd.Timestamp(year=prev_q_end.year, month=3 * (prev_q - 1) + 1, day=1)
        return prev_q_start, prev_q_end
 
    if preset == "Last Quarter":
        preset_start, preset_end = _prev_completed_quarter(date_max)
    elif preset in offsets:
        preset_start, preset_end = (date_max - timedelta(days=offsets[preset])), date_max
    else:
        preset_start, preset_end = date_min, date_max
 
    if preset == "Custom Range":
        dr = st.date_input("Range", value=(preset_start.date(), preset_end.date()),
                           min_value=date_min.date(), max_value=date_max.date())
        d0, d1 = (pd.Timestamp(dr[0]), pd.Timestamp(dr[1])) if len(dr)==2 else (preset_start, preset_end)
    else:
        d0 = max(preset_start, date_min); d1 = min(preset_end, date_max)
        st.caption(f"📅 {d0.strftime('%d %b %Y')} → {d1.strftime('%d %b %Y')}")
 
    st.markdown('<div class="section-label">Scope</div>', unsafe_allow_html=True)
    all_tables = sorted([str(v) for v in df_year_scoped["Affected Table Name"].dropna().unique()])
    sel_tables = st.multiselect("Affected Tables", all_tables, default=all_tables)
    all_types  = sorted([str(v) for v in df_year_scoped["Validation Short"].dropna().unique()])
    sel_types  = st.multiselect("Validation Types", all_types, default=all_types)
    show_only_issues = st.toggle("Issues only", value=False)
 
    if st.session_state.popup_filter:
        st.markdown('<div class="section-label">Popup</div>', unsafe_allow_html=True)
        if st.button("✕ Close Drill-Down", use_container_width=True):
            close_popup()
 
    st.markdown("---")
    st.markdown(f'<span style="font-size:0.65rem;color:{T["text_dim"]};letter-spacing:0.1em;text-transform:uppercase">v5.6 · {"🌙 Dark" if DARK else "☀️ Light"} Mode</span>', unsafe_allow_html=True)
 
 
# ── Apply filters ──────────────────────────────────────────────────────────
df = df_year_scoped[
    (df_year_scoped["Verified Date"] >= d0) &
    (df_year_scoped["Verified Date"] <= d1) &
    (df_year_scoped["Affected Table Name"].astype(str).isin(sel_tables)) &
    (df_year_scoped["Validation Short"].isin(sel_types))
].copy()
if show_only_issues: df = df[df["Has Issue"]]
 
total       = len(df)
with_issues = int(df["Has Issue"].sum())
clean       = total - with_issues
total_recs  = int(df["Record Count"].sum())
pass_rate   = (clean / total * 100) if total else 0
 
days_sorted = sorted(df["Verified Date"].dropna().unique())
if len(days_sorted) >= 2:
    delta  = int(df[df["Verified Date"]==days_sorted[-1]]["Has Issue"].sum()) - int(df[df["Verified Date"]==days_sorted[-2]]["Has Issue"].sum())
    dlabel = f"{'▲' if delta>0 else '▼' if delta<0 else '='} {abs(delta)} vs prev"
else:
    dlabel = "—"
 
# ── Dashboard header ───────────────────────────────────────────────────────
st.markdown(f"""
<div class="dash-header">
  <div class="dash-title">Data Quality Monitor</div>
  <div class="dash-meta">
    <span class="dash-meta-chip">📅 {d0.strftime('%d %b %Y')} → {d1.strftime('%d %b %Y')}</span>
    <span class="dash-meta-chip">📋 {total:,} records</span>
    {"<span class='dash-meta-chip'>🗓 " + sel_year + "</span>" if sel_year != "All Years" else ""}
  </div>
</div>
""", unsafe_allow_html=True)
 
# ── KPI buttons ────────────────────────────────────────────────────────────
from ui.popup import open_popup
from ui.components import green_css, grey_css
 
active_kpi = st.session_state.popup_filter.get("kpi") if isinstance(st.session_state.popup_filter, dict) else None
 
kpi_labels = {
    "all":     "VALIDATION SUMMARY",
    "issues":  "ISSUE OVERVIEW",
    "clean":   f"VALIDATION SUCCESS RATE  {pass_rate:.1f}%",
    "records": "IMPACT ANALYSIS",
}
 
active_map = {
    "kpi_all":     active_kpi == "all",
    "kpi_issues":  active_kpi == "issues",
    "kpi_clean":   active_kpi == "clean",
    "kpi_records": active_kpi == "records",
}
 
base_css = f"""
<style>
div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button {{
    border-radius: 14px !important; font-family: 'Inter', sans-serif !important;
    font-size: 0.78rem !important; height: 70px !important; width: 100% !important;
    letter-spacing: 0.05em !important; transition: all 0.18s ease !important;
    cursor: pointer !important; color: {T['text_muted']} !important;
}}
"""
col_map = [("kpi_all",1),("kpi_issues",2),("kpi_clean",3),("kpi_records",4)]
for bid, nth in col_map:
    base_css += green_css(nth, T) if active_map[bid] else grey_css(nth, T)
base_css += "</style>"
st.markdown(base_css, unsafe_allow_html=True)
 
c1, c2, c3, c4 = st.columns(4)
for col, ktype, bid in zip([c1,c2,c3,c4], ["all","issues","clean","records"],
                           ["kpi_all","kpi_issues","kpi_clean","kpi_records"]):
    with col:
        if st.button(kpi_labels[ktype], key=bid, use_container_width=True):
            open_popup({"kpi": ktype}, kpi_labels[ktype])
 
st.markdown("<div style='height:6px'></div>", unsafe_allow_html=True)
 
# ── Popup ──────────────────────────────────────────────────────────────────
from ui.popup import render_popup
render_popup(df, display_labels, T, _font_css, TABLE_JS)
 
# ── Tab navigation ─────────────────────────────────────────────────────────
TAB_LABELS = ["📈  Trend Analysis", "🗂  Issue Breakdown", "📋  Raw Records"]
tab_selection = st.radio(
    "tabs", TAB_LABELS, index=st.session_state.active_tab,
    horizontal=True, label_visibility="collapsed", key="tab_radio"
)
active_tab = TAB_LABELS.index(tab_selection)
st.session_state.active_tab = active_tab
st.markdown(f'<div style="border-bottom:1px solid {T["border"]};margin:6px 0 22px"></div>', unsafe_allow_html=True)
 
# ── Tab content ────────────────────────────────────────────────────────────
if active_tab == 0:
    from charts.tab_trend import render_tab_trend
    render_tab_trend(df, T, LAYOUT, HOVER, PALETTE, PLOTLY_CONFIG, C_BLUE, C_GREEN, C_RED)
 
elif active_tab == 1:
    from charts.tab_breakdown import render_tab_breakdown
    render_tab_breakdown(df, T, LAYOUT, HOVER, PALETTE, PLOTLY_CONFIG, C_RED, C_AMBER)
 
elif active_tab == 2:
    from charts.tab_rawdata import render_tab_rawdata
    render_tab_rawdata(df, display_labels, T, _font_css, TABLE_JS)