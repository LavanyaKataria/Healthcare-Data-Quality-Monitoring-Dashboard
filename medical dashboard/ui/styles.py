# # # import streamlit as st


# # # def inject_global_styles(T: dict, font_css: str) -> None:
# # #     """Inject the full global CSS block (fonts + CSS variables + all component styles)."""
# # #     st.markdown(f"<style>{font_css}</style>", unsafe_allow_html=True)

# # #     st.markdown(f"""
# # # <style>
# # # :root {{
# # #   --bg-base:{T['bg_base']};--bg-surface:{T['bg_surface']};--bg-card:{T['bg_card']};--bg-hover:{T['bg_hover']};
# # #   --bg-sidebar:{T['bg_sidebar']};
# # #   --border:{T['border']};--border-light:{T['border_light']};
# # #   --text-primary:{T['text_primary']};--text-muted:{T['text_muted']};--text-dim:{T['text_dim']};
# # #   --accent:{T['accent']};--accent-glow:{T['accent_glow']};
# # #   --green:{T['green']};--green-glow:{T['green_glow']};
# # #   --red:{T['red']};--red-glow:{T['red_glow']};
# # #   --amber:{T['amber']};--amber-glow:{T['amber_glow']};
# # #   --purple:{T['purple']};
# # # }}

# # # html,body,[class*="css"]{{font-family:'Inter',sans-serif;}}
# # # .stApp{{background-color:{T['bg_base']}!important;}}
# # # .main .block-container{{padding:1rem 2rem 2rem!important;max-width:1600px;background:{T['bg_base']}!important;}}
# # # ::-webkit-scrollbar{{width:5px;height:5px;}}
# # # ::-webkit-scrollbar-track{{background:{T['bg_base']};}}
# # # ::-webkit-scrollbar-thumb{{background:{T['border_light']};border-radius:99px;}}
# # # div[data-testid="stStatusWidget"]{{display:none!important;}}
# # # header[data-testid="stHeader"] [data-testid="stDecoration"]{{display:none!important;}}

# # # header[data-testid="stHeader"]{{background:{T['bg_base']}!important;border-bottom:1px solid {T['border']}!important;}}
# # # header[data-testid="stHeader"] button svg{{color:{T['text_muted']}!important;}}
# # # header[data-testid="stHeader"] [data-testid="baseButton-header"]{{color:{T['text_primary']}!important;}}

# # # section[data-testid="stSidebar"]{{background:{T['bg_sidebar']}!important;border-right:1px solid {T['border']}!important;}}
# # # section[data-testid="stSidebar"] .stMarkdown *{{color:{T['text_muted']}!important;}}
# # # section[data-testid="stSidebar"] label{{color:{T['text_muted']}!important;font-size:0.75rem!important;text-transform:uppercase;letter-spacing:0.08em;}}
# # # section[data-testid="stSidebar"] div[data-baseweb="select"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;color:{T['text_primary']}!important;border-radius:10px!important;}}
# # # section[data-testid="stSidebar"] div[data-baseweb="input"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;border-radius:10px!important;}}

# # # div[data-baseweb="select"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;border-radius:10px!important;color:{T['text_primary']}!important;}}
# # # div[data-baseweb="select"] *{{color:{T['text_primary']}!important;}}
# # # div[data-baseweb="input"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;border-radius:10px!important;}}
# # # div[data-baseweb="input"] input{{color:{T['text_primary']}!important;}}
# # # span[data-baseweb="tag"]{{background:{T['accent_glow']}!important;color:{T['accent']}!important;}}
# # # div[data-testid="stToggle"] label{{color:{T['text_muted']}!important;}}

# # # ul[data-baseweb="menu"]{{background:{T['bg_card']}!important;border:1px solid {T['border']}!important;}}
# # # ul[data-baseweb="menu"] li{{color:{T['text_primary']}!important;}}
# # # ul[data-baseweb="menu"] li:hover{{background:{T['bg_hover']}!important;}}

# # # .section-label{{font-family:'Inter',sans-serif;font-size:0.68rem;font-weight:600;letter-spacing:0.15em;text-transform:uppercase;color:{T['text_dim']};margin:28px 0 14px;display:flex;align-items:center;gap:10px;}}
# # # .section-label::after{{content:'';flex:1;height:1px;background:{T['border']};}}
# # # .year-filter-label{{font-family:'Inter',sans-serif;font-size:0.7rem;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:{T['text_muted']};margin-bottom:4px;margin-top:2px;}}
# # # .stCaption{{color:{T['text_muted']}!important;font-size:0.75rem!important;}}

# # # .dash-header{{padding:6px 0 18px;}}
# # # .dash-title{{font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:800;background:linear-gradient(135deg,{T['text_primary']} 30%,{T['accent']} 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1.1;letter-spacing:-0.02em;}}
# # # .dash-meta{{font-size:0.78rem;color:{T['text_muted']};margin-top:6px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;}}
# # # .dash-meta-chip{{display:inline-flex;align-items:center;gap:6px;background:{T['bg_card']};border:1px solid {T['border']};border-radius:99px;padding:3px 12px;font-size:0.71rem;color:{T['text_muted']};}}

# # # .sidebar-brand{{display:flex;align-items:center;gap:10px;padding:4px 0 16px;border-bottom:1px solid {T['border']};margin-bottom:20px;}}
# # # .sidebar-brand-icon{{width:34px;height:34px;background:linear-gradient(135deg,{T['accent_glow']},{T['accent_glow']});border:1px solid {T['accent']};border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;opacity:0.9;}}
# # # .sidebar-brand-text{{font-family:'Syne',sans-serif;font-size:0.95rem;font-weight:700;color:{T['text_primary']};}}
# # # .sidebar-brand-sub{{font-size:0.65rem;color:{T['text_muted']};letter-spacing:0.1em;text-transform:uppercase;}}

# # # .alert{{border-radius:10px;padding:11px 16px;font-size:0.82rem;margin:5px 0;border-left:3px solid;font-family:'Inter',sans-serif;}}
# # # .alert-critical{{background:{T['red_glow']};border-color:{T['red']};color:{T['red']};}}
# # # .alert-warn{{background:{T['amber_glow']};border-color:{T['amber']};color:{T['amber']};}}
# # # .alert-ok{{background:{T['green_glow']};border-color:{T['green']};color:{T['green']};}}

# # # .stDataFrame{{border:1px solid {T['border']}!important;border-radius:12px!important;overflow:hidden;background:{T['bg_card']}!important;}}

# # # .stDownloadButton button{{background:{T['accent_glow']}!important;border:1px solid {T['accent']}!important;color:{T['accent']}!important;border-radius:10px!important;font-size:0.78rem!important;transition:all 0.18s ease!important;}}
# # # div[data-testid="stButton"] button{{transition:all 0.2s ease!important;letter-spacing:0.01em!important;}}

# # # details{{background:{T['bg_card']}!important;border-color:{T['border']}!important;}}
# # # summary{{color:{T['text_primary']}!important;}}

# # # [data-testid="stMetricValue"]{{color:{T['text_primary']}!important;}}
# # # [data-testid="stMetricLabel"]{{color:{T['text_muted']}!important;}}

# # # .modebar-container{{opacity:1!important;position:absolute!important;top:4px!important;right:4px!important;z-index:99!important;}}
# # # .modebar{{background:{T['bg_card']}!important;border:1px solid {T['border']}!important;border-radius:5px!important;padding:2px 3px!important;box-shadow:0 1px 6px rgba(0,0,0,0.1)!important;display:flex!important;flex-direction:row!important;gap:1px!important;backdrop-filter:none!important;width:auto!important;height:auto!important;}}
# # # .modebar-group{{background:transparent!important;border:none!important;padding:0!important;margin:0!important;box-shadow:none!important;display:flex!important;flex-direction:row!important;gap:1px!important;}}
# # # .modebar-group+.modebar-group{{border:none!important;margin:0!important;padding:0!important;}}
# # # .modebar-btn{{width:22px!important;height:22px!important;min-width:22px!important;min-height:22px!important;max-width:22px!important;max-height:22px!important;border-radius:3px!important;display:flex!important;align-items:center!important;justify-content:center!important;transition:background 0.12s!important;color:{T['text_muted']}!important;background:transparent!important;padding:0!important;margin:0!important;}}
# # # .modebar-btn:hover{{background:{T['accent_glow']}!important;color:{T['accent']}!important;}}
# # # .modebar-btn.active{{background:{T['accent_glow']}!important;color:{T['accent']}!important;}}
# # # .modebar-btn svg{{width:12px!important;height:12px!important;display:block!important;}}

# # # div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button {{
# # #     border-radius:14px!important;font-family:'Inter',sans-serif!important;
# # #     font-size:0.78rem!important;height:70px!important;width:100%!important;
# # #     letter-spacing:0.05em!important;transition:all 0.18s ease!important;cursor:pointer!important;
# # #     background:{T['bg_card']}!important;border:1px solid {T['border']}!important;
# # #     color:{T['text_muted']}!important;box-shadow:0 2px 8px rgba(0,0,0,0.06)!important;
# # # }}
# # # div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button:hover {{
# # #     background:{T['bg_hover']}!important;border-color:{T['green']}!important;color:{T['text_primary']}!important;
# # #     box-shadow:0 0 0 2px {T['green_glow']},0 6px 20px rgba(0,0,0,0.08)!important;
# # #     transform:translateY(-3px)!important;
# # # }}

# # # div[data-testid="stRadio"]>label{{display:none!important;}}
# # # div[data-testid="stRadio"]>div[role="radiogroup"]{{display:flex!important;flex-direction:row!important;gap:10px!important;flex-wrap:nowrap!important;}}
# # # div[data-testid="stRadio"] div[role="radiogroup"]>label{{
# # #     display:flex!important;flex:1 1 0%!important;align-items:center!important;justify-content:center!important;
# # #     min-height:44px!important;border-radius:10px!important;cursor:pointer!important;
# # #     font-family:'Inter',sans-serif!important;font-size:0.82rem!important;font-weight:500!important;
# # #     background:{T['bg_card']}!important;color:{T['text_muted']}!important;
# # #     border:1px solid {T['border']}!important;border-bottom:3px solid transparent!important;
# # #     box-shadow:0 2px 6px rgba(0,0,0,0.06)!important;
# # #     transition:transform 0.18s cubic-bezier(0.34,1.56,0.64,1),box-shadow 0.18s ease,border-color 0.18s ease,color 0.18s ease,background 0.18s ease!important;
# # #     padding:0 14px!important;text-align:center!important;user-select:none!important;white-space:nowrap!important;
# # # }}
# # # div[data-testid="stRadio"] div[role="radiogroup"]>label:hover{{
# # #     transform:translateY(-5px)!important;background:{T['bg_hover']}!important;color:{T['text_primary']}!important;
# # #     border-color:{T['border_light']}!important;border-bottom-color:{T['accent']}!important;
# # #     box-shadow:0 10px 28px {T['accent_glow']},0 2px 8px rgba(0,0,0,0.08)!important;
# # # }}
# # # div[data-testid="stRadio"] div[role="radiogroup"]>label:has(input:checked){{
# # #     background:{T['green_glow']}!important;border:1px solid {T['green']}!important;
# # #     border-top:3px solid {T['green']}!important;color:{T['green']}!important;
# # #     font-weight:700!important;transform:translateY(-2px)!important;
# # #     box-shadow:0 0 20px {T['green_glow']},0 6px 20px {T['green_glow']}!important;
# # # }}
# # # div[data-testid="stRadio"] div[role="radiogroup"]>label input[type="radio"]{{display:none!important;}}
# # # div[data-testid="stRadio"] div[role="radiogroup"]>label>div{{font-family:'Inter',sans-serif!important;font-size:0.82rem!important;line-height:1!important;pointer-events:none!important;display:inline-flex!important;align-items:center!important;gap:6px!important;white-space:nowrap!important;}}
# # # div[data-testid="stRadio"] div[role="radiogroup"]>label>div>p{{margin:0!important;white-space:nowrap!important;display:inline!important;}}
# # # </style>
# # # """, unsafe_allow_html=True)


# # # def table_css_vars(T: dict) -> str:
# # #     return f"""
# # # :root{{
# # #   --bg:{T['bg_base']};
# # #   --bg-s:{T['bg_sidebar']};
# # #   --bg-c:{T['bg_card']};
# # #   --bg-h:{T['bg_hover']};
# # #   --bdr:{T['border']};
# # #   --bdrl:{T['border_light']};
# # #   --txt:{T['text_primary']};
# # #   --muted:{T['text_muted']};
# # #   --dim:{T['text_dim']};
# # #   --accent:{T['accent']};
# # #   --green:{T['green']};
# # #   --red:{T['red']};
# # #   --amber:{T['amber']};
# # #   --td-color:{T['td_color']};
# # #   --td-even:{T['td_even']};
# # #   --thead-bg:{T['thead_bg']};
# # #   --dots-menu-bg:{T['dots_menu_bg']};
# # #   --dots-item-color:{T['dots_item_col']};
# # #   --scrollbar:{T['scrollbar']};
# # # }}"""


# # # def table_base_css(T: dict, max_height: str = "none") -> str:
# # #     tbl_wrap_overflow = f"overflow-y:auto;max-height:{max_height};" if max_height != "none" else "overflow-y:auto;flex:1;"
# # #     return f"""
# # # *{{box-sizing:border-box;margin:0;padding:0}}
# # # {table_css_vars(T)}
# # # html,body{{background:var(--bg);color:var(--txt);font-family:'Inter',sans-serif;height:100%;overflow:hidden;}}
# # # ::-webkit-scrollbar{{width:5px;height:5px}}
# # # ::-webkit-scrollbar-track{{background:var(--bg)}}
# # # ::-webkit-scrollbar-thumb{{background:var(--scrollbar);border-radius:99px}}
# # # .box{{display:flex;flex-direction:column;height:100vh;background:var(--bg-s);border-top:3px solid var(--accent)}}
# # # .body{{overflow-y:auto;padding:16px 18px;flex:1;display:flex;flex-direction:column;gap:14px}}
# # # .stats{{display:flex;gap:10px;flex-wrap:wrap}}
# # # .stat{{background:var(--bg-c);border:1px solid var(--bdr);border-radius:10px;padding:10px 18px;flex:1;min-width:100px;text-align:center;box-shadow:0 1px 4px rgba(0,0,0,.1)}}
# # # .stat-val{{font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:700;color:var(--accent)}}
# # # .stat-lbl{{font-size:.65rem;color:var(--muted);margin-top:3px;text-transform:uppercase;letter-spacing:.07em}}
# # # .controls{{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}}
# # # .perpage{{display:flex;align-items:center;gap:7px;font-size:.78rem;color:var(--muted)}}
# # # .perpage select{{background:var(--bg-c);color:var(--txt);border:1px solid var(--bdrl);border-radius:7px;padding:4px 26px 4px 9px;font-size:.78rem;font-family:'Inter',sans-serif;cursor:pointer;outline:none;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%236b7494'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 8px center}}
# # # .srchwrap{{display:flex;align-items:center;gap:7px;font-size:.78rem;color:var(--muted)}}
# # # .srchwrap input{{background:var(--bg-c);color:var(--txt);border:1px solid var(--bdrl);border-radius:7px;padding:4px 10px;font-size:.78rem;font-family:'Inter',sans-serif;outline:none;width:155px}}
# # # .srchwrap input:focus{{border-color:var(--accent)}}.srchwrap input::placeholder{{color:var(--muted)}}
# # # .tbl-wrap{{overflow-x:auto;{tbl_wrap_overflow}}}
# # # table{{width:100%;border-collapse:collapse;font-size:.81rem;user-select:none;-webkit-user-select:none}}
# # # thead tr{{position:sticky;top:0;z-index:10}}
# # # th{{background:var(--thead-bg);color:var(--accent);font-size:.65rem;text-transform:uppercase;letter-spacing:.1em;font-weight:600;border-bottom:2px solid var(--bdrl);padding:0;white-space:nowrap}}
# # # .th-inner{{display:flex;align-items:center;justify-content:space-between;padding:9px 12px;gap:5px}}
# # # td{{padding:8px 12px;border-bottom:1px solid var(--bdr);color:var(--td-color);white-space:nowrap;cursor:default}}
# # # tr:nth-child(even) td{{background:var(--td-even)}}
# # # tr:hover td{{background:var(--bg-h)}}
# # # .dots-wrap{{position:relative;outline:none;flex-shrink:0}}
# # # .dots-btn{{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:4px;font-size:1rem;color:var(--dim);cursor:pointer;user-select:none;transition:all .15s}}
# # # .dots-btn:hover,.dots-wrap:focus-within .dots-btn{{background:var(--bg-h);color:var(--accent)}}
# # # .dots-menu{{display:none;position:absolute;top:26px;right:0;background:var(--dots-menu-bg);border:1px solid var(--bdrl);border-radius:9px;min-width:175px;box-shadow:0 12px 40px rgba(0,0,0,.25);z-index:9999;flex-direction:column;overflow:hidden}}
# # # .dots-wrap:focus-within .dots-menu{{display:flex}}
# # # .dots-menu-title{{font-size:.63rem;color:var(--accent);font-weight:700;letter-spacing:.12em;padding:9px 13px 7px;border-bottom:1px solid var(--bdr);text-transform:uppercase}}
# # # .dots-item{{display:flex;align-items:center;gap:8px;padding:7px 13px;font-size:.8rem;color:var(--dots-item-color);cursor:pointer;background:none;border:none;width:100%;text-align:left;font-family:'Inter',sans-serif;transition:background .12s}}
# # # .dots-item:hover{{background:var(--bg-h);color:var(--txt)}}
# # # .dots-check{{color:var(--green);font-size:.74rem;width:13px;flex-shrink:0}}.th-label{{cursor:pointer}}
# # # .pg-row{{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}}
# # # .pg-info{{font-size:.74rem;color:var(--muted)}}
# # # .pg-btns{{display:flex;gap:3px;flex-wrap:wrap}}
# # # .pgb{{display:inline-flex;align-items:center;justify-content:center;min-width:28px;height:28px;padding:0 7px;background:var(--bg-c);color:var(--muted);border:1px solid var(--bdr);border-radius:6px;font-size:.76rem;cursor:pointer;transition:all .15s;user-select:none}}
# # # .pgb:hover:not(.dis):not(.act){{background:var(--bg-h);border-color:var(--bdrl);color:var(--txt)}}
# # # .pgb.act{{background:var(--accent);color:#fff;border-color:var(--accent);font-weight:600}}
# # # .pgb.dis{{opacity:.3;cursor:not-allowed;pointer-events:none}}
# # # .pill-i{{display:inline-block;padding:2px 9px;border-radius:99px;font-size:.72rem;font-weight:600;background:rgba(220,38,38,.15);color:var(--red);border:1px solid rgba(220,38,38,.35)}}
# # # .pill-c{{display:inline-block;padding:2px 9px;border-radius:99px;font-size:.72rem;font-weight:600;background:rgba(22,163,74,.15);color:var(--green);border:1px solid rgba(22,163,74,.35)}}
# # # """








# # import streamlit as st


# # def inject_global_styles(T: dict, font_css: str) -> None:
# #     """Inject the full global CSS block (fonts + CSS variables + all component styles)."""
# #     st.markdown(f"<style>{font_css}</style>", unsafe_allow_html=True)

# #     st.markdown(f"""
# # <style>
# # :root {{
# #   --bg-base:{T['bg_base']};--bg-surface:{T['bg_surface']};--bg-card:{T['bg_card']};--bg-hover:{T['bg_hover']};
# #   --bg-sidebar:{T['bg_sidebar']};
# #   --border:{T['border']};--border-light:{T['border_light']};
# #   --text-primary:{T['text_primary']};--text-muted:{T['text_muted']};--text-dim:{T['text_dim']};
# #   --accent:{T['accent']};--accent-glow:{T['accent_glow']};
# #   --green:{T['green']};--green-glow:{T['green_glow']};
# #   --red:{T['red']};--red-glow:{T['red_glow']};
# #   --amber:{T['amber']};--amber-glow:{T['amber_glow']};
# #   --purple:{T['purple']};
# # }}

# # html,body,[class*="css"]{{font-family:'Inter',sans-serif;}}
# # .stApp{{background-color:{T['bg_base']}!important;}}
# # .main .block-container{{padding:1rem 2rem 2rem!important;max-width:1600px;background:{T['bg_base']}!important;}}
# # ::-webkit-scrollbar{{width:5px;height:5px;}}
# # ::-webkit-scrollbar-track{{background:{T['bg_base']};}}
# # ::-webkit-scrollbar-thumb{{background:{T['border_light']};border-radius:99px;}}
# # div[data-testid="stStatusWidget"]{{display:none!important;}}
# # header[data-testid="stHeader"] [data-testid="stDecoration"]{{display:none!important;}}

# # header[data-testid="stHeader"]{{background:{T['bg_base']}!important;border-bottom:1px solid {T['border']}!important;}}
# # header[data-testid="stHeader"] button svg{{color:{T['text_muted']}!important;}}
# # header[data-testid="stHeader"] [data-testid="baseButton-header"]{{color:{T['text_primary']}!important;}}

# # section[data-testid="stSidebar"]{{background:{T['bg_sidebar']}!important;border-right:1px solid {T['border']}!important;}}
# # section[data-testid="stSidebar"] .stMarkdown *{{color:{T['text_muted']}!important;}}
# # section[data-testid="stSidebar"] label{{color:{T['text_muted']}!important;font-size:0.75rem!important;text-transform:uppercase;letter-spacing:0.08em;}}
# # section[data-testid="stSidebar"] div[data-baseweb="select"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;color:{T['text_primary']}!important;border-radius:10px!important;}}
# # section[data-testid="stSidebar"] div[data-baseweb="input"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;border-radius:10px!important;}}

# # div[data-baseweb="select"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;border-radius:10px!important;color:{T['text_primary']}!important;}}
# # div[data-baseweb="select"] *{{color:{T['text_primary']}!important;}}
# # div[data-baseweb="input"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;border-radius:10px!important;}}
# # div[data-baseweb="input"] input{{color:{T['text_primary']}!important;}}
# # span[data-baseweb="tag"]{{background:{T['accent_glow']}!important;color:{T['accent']}!important;}}
# # div[data-testid="stToggle"] label{{color:{T['text_muted']}!important;}}

# # ul[data-baseweb="menu"]{{background:{T['bg_card']}!important;border:1px solid {T['border']}!important;}}
# # ul[data-baseweb="menu"] li{{color:{T['text_primary']}!important;}}
# # ul[data-baseweb="menu"] li:hover{{background:{T['bg_hover']}!important;}}

# # .section-label{{font-family:'Inter',sans-serif;font-size:0.68rem;font-weight:600;letter-spacing:0.15em;text-transform:uppercase;color:{T['text_dim']};margin:28px 0 14px;display:flex;align-items:center;gap:10px;}}
# # .section-label::after{{content:'';flex:1;height:1px;background:{T['border']};}}
# # .year-filter-label{{font-family:'Inter',sans-serif;font-size:0.7rem;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:{T['text_muted']};margin-bottom:4px;margin-top:2px;}}
# # .stCaption{{color:{T['text_muted']}!important;font-size:0.75rem!important;}}

# # .dash-header{{padding:6px 0 18px;}}
# # .dash-title{{font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:800;background:linear-gradient(135deg,{T['text_primary']} 30%,{T['accent']} 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1.1;letter-spacing:-0.02em;}}
# # .dash-meta{{font-size:0.78rem;color:{T['text_muted']};margin-top:6px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;}}
# # .dash-meta-chip{{display:inline-flex;align-items:center;gap:6px;background:{T['bg_card']};border:1px solid {T['border']};border-radius:99px;padding:3px 12px;font-size:0.71rem;color:{T['text_muted']};}}

# # .sidebar-brand{{display:flex;align-items:center;gap:10px;padding:4px 0 16px;border-bottom:1px solid {T['border']};margin-bottom:20px;}}
# # .sidebar-brand-icon{{width:34px;height:34px;background:linear-gradient(135deg,{T['accent_glow']},{T['accent_glow']});border:1px solid {T['accent']};border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;opacity:0.9;}}
# # .sidebar-brand-text{{font-family:'Syne',sans-serif;font-size:0.95rem;font-weight:700;color:{T['text_primary']};}}
# # .sidebar-brand-sub{{font-size:0.65rem;color:{T['text_muted']};letter-spacing:0.1em;text-transform:uppercase;}}

# # .alert{{border-radius:10px;padding:11px 16px;font-size:0.82rem;margin:5px 0;border-left:3px solid;font-family:'Inter',sans-serif;}}
# # .alert-critical{{background:{T['red_glow']};border-color:{T['red']};color:{T['red']};}}
# # .alert-warn{{background:{T['amber_glow']};border-color:{T['amber']};color:{T['amber']};}}
# # .alert-ok{{background:{T['green_glow']};border-color:{T['green']};color:{T['green']};}}

# # .stDataFrame{{border:1px solid {T['border']}!important;border-radius:12px!important;overflow:hidden;background:{T['bg_card']}!important;}}

# # .stDownloadButton button{{background:{T['accent_glow']}!important;border:1px solid {T['accent']}!important;color:{T['accent']}!important;border-radius:10px!important;font-size:0.78rem!important;transition:all 0.18s ease!important;}}
# # div[data-testid="stButton"] button{{transition:all 0.2s ease!important;letter-spacing:0.01em!important;}}

# # details{{background:{T['bg_card']}!important;border-color:{T['border']}!important;}}
# # summary{{color:{T['text_primary']}!important;}}

# # [data-testid="stMetricValue"]{{color:{T['text_primary']}!important;}}
# # [data-testid="stMetricLabel"]{{color:{T['text_muted']}!important;}}

# # .modebar-container{{opacity:1!important;position:absolute!important;top:4px!important;right:4px!important;z-index:99!important;}}
# # .modebar{{background:{T['bg_card']}!important;border:1px solid {T['border']}!important;border-radius:5px!important;padding:2px 3px!important;box-shadow:0 1px 6px rgba(0,0,0,0.1)!important;display:flex!important;flex-direction:row!important;gap:1px!important;backdrop-filter:none!important;width:auto!important;height:auto!important;}}
# # .modebar-group{{background:transparent!important;border:none!important;padding:0!important;margin:0!important;box-shadow:none!important;display:flex!important;flex-direction:row!important;gap:1px!important;}}
# # .modebar-group+.modebar-group{{border:none!important;margin:0!important;padding:0!important;}}
# # .modebar-btn{{width:22px!important;height:22px!important;min-width:22px!important;min-height:22px!important;max-width:22px!important;max-height:22px!important;border-radius:3px!important;display:flex!important;align-items:center!important;justify-content:center!important;transition:background 0.12s!important;color:{T['text_muted']}!important;background:transparent!important;padding:0!important;margin:0!important;}}
# # .modebar-btn:hover{{background:{T['accent_glow']}!important;color:{T['accent']}!important;}}
# # .modebar-btn.active{{background:{T['accent_glow']}!important;color:{T['accent']}!important;}}
# # .modebar-btn svg{{width:12px!important;height:12px!important;display:block!important;}}

# # div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button {{
# #     border-radius:14px!important;font-family:'Inter',sans-serif!important;
# #     font-size:0.78rem!important;height:70px!important;width:100%!important;
# #     letter-spacing:0.05em!important;transition:all 0.18s ease!important;cursor:pointer!important;
# #     background:{T['bg_card']}!important;border:1px solid {T['border']}!important;
# #     color:{T['text_muted']}!important;box-shadow:0 2px 8px rgba(0,0,0,0.06)!important;
# # }}
# # div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button:hover {{
# #     background:{T['bg_hover']}!important;border-color:{T['green']}!important;color:{T['text_primary']}!important;
# #     box-shadow:0 0 0 2px {T['green_glow']},0 6px 20px rgba(0,0,0,0.08)!important;
# #     transform:translateY(-3px)!important;
# # }}

# # div[data-testid="stRadio"]>label{{display:none!important;}}
# # div[data-testid="stRadio"]>div[role="radiogroup"]{{display:flex!important;flex-direction:row!important;gap:10px!important;flex-wrap:nowrap!important;}}
# # div[data-testid="stRadio"] div[role="radiogroup"]>label{{
# #     display:flex!important;flex:1 1 0%!important;align-items:center!important;justify-content:center!important;
# #     min-height:44px!important;border-radius:10px!important;cursor:pointer!important;
# #     font-family:'Inter',sans-serif!important;font-size:0.82rem!important;font-weight:500!important;
# #     background:{T['bg_card']}!important;color:{T['text_muted']}!important;
# #     border:1px solid {T['border']}!important;border-bottom:3px solid transparent!important;
# #     box-shadow:0 2px 6px rgba(0,0,0,0.06)!important;
# #     transition:transform 0.18s cubic-bezier(0.34,1.56,0.64,1),box-shadow 0.18s ease,border-color 0.18s ease,color 0.18s ease,background 0.18s ease!important;
# #     padding:0 14px!important;text-align:center!important;user-select:none!important;white-space:nowrap!important;
# # }}
# # div[data-testid="stRadio"] div[role="radiogroup"]>label:hover{{
# #     transform:translateY(-5px)!important;background:{T['bg_hover']}!important;color:{T['text_primary']}!important;
# #     border-color:{T['border_light']}!important;border-bottom-color:{T['accent']}!important;
# #     box-shadow:0 10px 28px {T['accent_glow']},0 2px 8px rgba(0,0,0,0.08)!important;
# # }}
# # div[data-testid="stRadio"] div[role="radiogroup"]>label:has(input:checked){{
# #     background:{T['green_glow']}!important;border:1px solid {T['green']}!important;
# #     border-top:3px solid {T['green']}!important;color:{T['green']}!important;
# #     font-weight:700!important;transform:translateY(-2px)!important;
# #     box-shadow:0 0 20px {T['green_glow']},0 6px 20px {T['green_glow']}!important;
# # }}
# # div[data-testid="stRadio"] div[role="radiogroup"]>label input[type="radio"]{{display:none!important;}}
# # div[data-testid="stRadio"] div[role="radiogroup"]>label>div{{font-family:'Inter',sans-serif!important;font-size:0.82rem!important;line-height:1!important;pointer-events:none!important;display:inline-flex!important;align-items:center!important;gap:6px!important;white-space:nowrap!important;}}
# # div[data-testid="stRadio"] div[role="radiogroup"]>label>div>p{{margin:0!important;white-space:nowrap!important;display:inline!important;}}

# # /* â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
# #    PLOTLY AXIS DRAG RAIL INDICATORS
# #    Exposes the existing Plotly drag zones visually.
# #    No new logic â€” purely cosmetic overlays on native Plotly
# #    SVG drag layer elements (.ewdrag = x-axis, .nsdrag = y-axis).
# #    â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• */

# # /* Container holding Plotly SVG â€” used as positioning anchor */
# # .js-plotly-plot .plotly,
# # .js-plotly-plot svg {{
# #   overflow: visible !important;
# # }}

# # /* â”€â”€ X-AXIS drag zone (bottom of chart) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# #    Plotly renders an <rect class="ewdrag drag"> at the bottom.
# #    We paint a thin rail + left/right arrow glyphs via outline
# #    and box-shadow to avoid touching layout at all.           */
# # .js-plotly-plot .ewdrag {{
# #   fill: transparent !important;
# #   stroke: none !important;
# #   cursor: ew-resize !important;
# # }}

# # /* The rail track: thin bottom border rendered as an SVG rect
# #    highlight. We achieve this via a CSS filter trick on the
# #    parent layer and a dedicated pseudo-class on the g element. */
# # .js-plotly-plot g.draglayer g.drag.ewdrag {{
# #   /* SVG rects can't have ::before/::after, so we style the
# #      containing <g> to show an underline effect via filter */
# #   filter: drop-shadow(0 3px 0 {T['border_light']}) !important;
# #   transition: filter 0.18s ease !important;
# # }}
# # .js-plotly-plot g.draglayer g.drag.ewdrag:hover {{
# #   filter: drop-shadow(0 3px 0 {T['accent']}) !important;
# # }}

# # /* â”€â”€ Y-AXIS drag zone (left side of chart) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# #    Plotly renders <rect class="nsdrag drag"> on the left edge. */
# # .js-plotly-plot .nsdrag {{
# #   fill: transparent !important;
# #   stroke: none !important;
# #   cursor: ns-resize !important;
# # }}
# # .js-plotly-plot g.draglayer g.drag.nsdrag {{
# #   filter: drop-shadow(-3px 0 0 {T['border_light']}) !important;
# #   transition: filter 0.18s ease !important;
# # }}
# # .js-plotly-plot g.draglayer g.drag.nsdrag:hover {{
# #   filter: drop-shadow(-3px 0 0 {T['accent']}) !important;
# # }}

# # /* â”€â”€ Axis rail overlay via :after on the svg container â”€â”€â”€â”€â”€
# #    Adds a thin visible track line + arrow glyphs positioned
# #    exactly over Plotly's drag zones using absolute positioning
# #    on the Streamlit plotly wrapper element.                  */
# # div[data-testid="stPlotlyChart"] {{
# #   position: relative !important;
# # }}

# # /* X-axis bottom rail track */
# # div[data-testid="stPlotlyChart"]::after {{
# #   content: 'â—€ â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ â–¶';
# #   position: absolute;
# #   bottom: 38px;
# #   left: 48px;
# #   right: 28px;
# #   height: 14px;
# #   display: flex;
# #   align-items: center;
# #   justify-content: space-between;
# #   font-size: 0.62rem;
# #   letter-spacing: 0.04em;
# #   color: {T['border_light']};
# #   pointer-events: none;
# #   user-select: none;
# #   z-index: 1;
# #   overflow: hidden;
# #   white-space: nowrap;
# #   transition: color 0.2s ease;
# #   line-height: 1;
# # }}

# # /* Replace the text approach with a cleaner SVG-compatible rail */
# # div[data-testid="stPlotlyChart"] {{
# #   isolation: isolate;
# # }}

# # /* â”€â”€ Clean rail implementation: injected via dedicated wrapper â”€
# #    We inject a thin ::before rail on the bottom (x-axis) and
# #    a ::before on a pseudo-sibling. Since a single element can
# #    only have one ::before and one ::after, we use ::before for
# #    the Y rail and ::after for the X rail.                      */

# # /* X-axis bottom rail */
# # div[data-testid="stPlotlyChart"]::after {{
# #   content: '';
# #   position: absolute;
# #   bottom: 36px;
# #   left: 52px;
# #   right: 24px;
# #   height: 2px;
# #   background: linear-gradient(
# #     to right,
# #     transparent 0px,
# #     {T['border_light']} 12px,
# #     {T['border_light']} calc(100% - 12px),
# #     transparent 100%
# #   );
# #   border-radius: 2px;
# #   pointer-events: none;
# #   z-index: 2;
# #   transition: background 0.2s ease;
# # }}

# # /* X-axis left arrow marker */
# # div[data-testid="stPlotlyChart"]::before {{
# #   content: '';
# #   position: absolute;
# #   /* Y-axis left rail */
# #   top: 36px;
# #   bottom: 50px;
# #   left: 42px;
# #   width: 2px;
# #   background: linear-gradient(
# #     to bottom,
# #     transparent 0px,
# #     {T['border_light']} 12px,
# #     {T['border_light']} calc(100% - 12px),
# #     transparent 100%
# #   );
# #   border-radius: 2px;
# #   pointer-events: none;
# #   z-index: 2;
# #   transition: background 0.2s ease;
# # }}

# # /* Hover: brighten both rails when user hovers the chart area */
# # div[data-testid="stPlotlyChart"]:hover::after {{
# #   background: linear-gradient(
# #     to right,
# #     transparent 0px,
# #     {T['border']} 12px,
# #     {T['border']} calc(100% - 12px),
# #     transparent 100%
# #   );
# # }}
# # div[data-testid="stPlotlyChart"]:hover::before {{
# #   background: linear-gradient(
# #     to bottom,
# #     transparent 0px,
# #     {T['border']} 12px,
# #     {T['border']} calc(100% - 12px),
# #     transparent 100%
# #   );
# # }}

# # /* â”€â”€ Arrow tips via injected SVG-in-HTML overlay â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
# #    Since CSS pseudo-elements can't render real arrowheads,
# #    we inject a lightweight SVG overlay via a Streamlit-safe
# #    class that wraps each chart.                              */

# # /* Arrow glyphs injected as Unicode text via data attributes,
# #    positioned over the rail ends using a label trick.       */

# # /* X-axis: left arrow cap */
# # .plotly-x-rail-left {{
# #   position: absolute;
# #   bottom: 30px;
# #   left: 44px;
# #   width: 10px;
# #   height: 14px;
# #   pointer-events: none;
# #   z-index: 3;
# #   color: {T['border_light']};
# #   font-size: 8px;
# #   display: flex;
# #   align-items: center;
# #   justify-content: center;
# #   line-height: 1;
# #   user-select: none;
# # }}

# # /* X-axis: right arrow cap */
# # .plotly-x-rail-right {{
# #   position: absolute;
# #   bottom: 30px;
# #   right: 16px;
# #   width: 10px;
# #   height: 14px;
# #   pointer-events: none;
# #   z-index: 3;
# #   color: {T['border_light']};
# #   font-size: 8px;
# #   display: flex;
# #   align-items: center;
# #   justify-content: center;
# #   line-height: 1;
# #   user-select: none;
# # }}

# # /* Y-axis: top arrow cap */
# # .plotly-y-rail-top {{
# #   position: absolute;
# #   top: 28px;
# #   left: 36px;
# #   width: 14px;
# #   height: 10px;
# #   pointer-events: none;
# #   z-index: 3;
# #   color: {T['border_light']};
# #   font-size: 8px;
# #   display: flex;
# #   align-items: center;
# #   justify-content: center;
# #   line-height: 1;
# #   user-select: none;
# # }}

# # /* Y-axis: bottom arrow cap */
# # .plotly-y-rail-bottom {{
# #   position: absolute;
# #   bottom: 44px;
# #   left: 36px;
# #   width: 14px;
# #   height: 10px;
# #   pointer-events: none;
# #   z-index: 3;
# #   color: {T['border_light']};
# #   font-size: 8px;
# #   display: flex;
# #   align-items: center;
# #   justify-content: center;
# #   line-height: 1;
# #   user-select: none;
# # }}

# # /* Hover state for arrow glyphs */
# # div[data-testid="stPlotlyChart"]:hover .plotly-x-rail-left,
# # div[data-testid="stPlotlyChart"]:hover .plotly-x-rail-right,
# # div[data-testid="stPlotlyChart"]:hover .plotly-y-rail-top,
# # div[data-testid="stPlotlyChart"]:hover .plotly-y-rail-bottom {{
# #   color: {T['accent']} !important;
# # }}

# # /* Hint label that appears on hover to guide users */
# # div[data-testid="stPlotlyChart"]:hover::after {{
# #   /* X rail already brightens; additionally pulse the rail briefly */
# #   animation: rail-pulse 0.4s ease-out 1 forwards;
# # }}
# # @keyframes rail-pulse {{
# #   0%   {{ opacity: 0.5; }}
# #   50%  {{ opacity: 1; }}
# #   100% {{ opacity: 0.85; }}
# # }}
# # </style>
# # """, unsafe_allow_html=True)


# # def table_css_vars(T: dict) -> str:
# #     return f"""
# # :root{{
# #   --bg:{T['bg_base']};
# #   --bg-s:{T['bg_sidebar']};
# #   --bg-c:{T['bg_card']};
# #   --bg-h:{T['bg_hover']};
# #   --bdr:{T['border']};
# #   --bdrl:{T['border_light']};
# #   --txt:{T['text_primary']};
# #   --muted:{T['text_muted']};
# #   --dim:{T['text_dim']};
# #   --accent:{T['accent']};
# #   --green:{T['green']};
# #   --red:{T['red']};
# #   --amber:{T['amber']};
# #   --td-color:{T['td_color']};
# #   --td-even:{T['td_even']};
# #   --thead-bg:{T['thead_bg']};
# #   --dots-menu-bg:{T['dots_menu_bg']};
# #   --dots-item-color:{T['dots_item_col']};
# #   --scrollbar:{T['scrollbar']};
# # }}"""


# # def table_base_css(T: dict, max_height: str = "none") -> str:
# #     tbl_wrap_overflow = f"overflow-y:auto;max-height:{max_height};" if max_height != "none" else "overflow-y:auto;flex:1;"
# #     return f"""
# # *{{box-sizing:border-box;margin:0;padding:0}}
# # {table_css_vars(T)}
# # html,body{{background:var(--bg);color:var(--txt);font-family:'Inter',sans-serif;height:100%;overflow:hidden;}}
# # ::-webkit-scrollbar{{width:5px;height:5px}}
# # ::-webkit-scrollbar-track{{background:var(--bg)}}
# # ::-webkit-scrollbar-thumb{{background:var(--scrollbar);border-radius:99px}}
# # .box{{display:flex;flex-direction:column;height:100vh;background:var(--bg-s);border-top:3px solid var(--accent)}}
# # .body{{overflow-y:auto;padding:16px 18px;flex:1;display:flex;flex-direction:column;gap:14px}}
# # .stats{{display:flex;gap:10px;flex-wrap:wrap}}
# # .stat{{background:var(--bg-c);border:1px solid var(--bdr);border-radius:10px;padding:10px 18px;flex:1;min-width:100px;text-align:center;box-shadow:0 1px 4px rgba(0,0,0,.1)}}
# # .stat-val{{font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:700;color:var(--accent)}}
# # .stat-lbl{{font-size:.65rem;color:var(--muted);margin-top:3px;text-transform:uppercase;letter-spacing:.07em}}
# # .controls{{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}}
# # .perpage{{display:flex;align-items:center;gap:7px;font-size:.78rem;color:var(--muted)}}
# # .perpage select{{background:var(--bg-c);color:var(--txt);border:1px solid var(--bdrl);border-radius:7px;padding:4px 26px 4px 9px;font-size:.78rem;font-family:'Inter',sans-serif;cursor:pointer;outline:none;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%236b7494'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 8px center}}
# # .srchwrap{{display:flex;align-items:center;gap:7px;font-size:.78rem;color:var(--muted)}}
# # .srchwrap input{{background:var(--bg-c);color:var(--txt);border:1px solid var(--bdrl);border-radius:7px;padding:4px 10px;font-size:.78rem;font-family:'Inter',sans-serif;outline:none;width:155px}}
# # .srchwrap input:focus{{border-color:var(--accent)}}.srchwrap input::placeholder{{color:var(--muted)}}
# # .tbl-wrap{{overflow-x:auto;{tbl_wrap_overflow}}}
# # table{{width:100%;border-collapse:collapse;font-size:.81rem;user-select:none;-webkit-user-select:none}}
# # thead tr{{position:sticky;top:0;z-index:10}}
# # th{{background:var(--thead-bg);color:var(--accent);font-size:.65rem;text-transform:uppercase;letter-spacing:.1em;font-weight:600;border-bottom:2px solid var(--bdrl);padding:0;white-space:nowrap}}
# # .th-inner{{display:flex;align-items:center;justify-content:space-between;padding:9px 12px;gap:5px}}
# # td{{padding:8px 12px;border-bottom:1px solid var(--bdr);color:var(--td-color);white-space:nowrap;cursor:default}}
# # tr:nth-child(even) td{{background:var(--td-even)}}
# # tr:hover td{{background:var(--bg-h)}}
# # .dots-wrap{{position:relative;outline:none;flex-shrink:0}}
# # .dots-btn{{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:4px;font-size:1rem;color:var(--dim);cursor:pointer;user-select:none;transition:all .15s}}
# # .dots-btn:hover,.dots-wrap:focus-within .dots-btn{{background:var(--bg-h);color:var(--accent)}}
# # .dots-menu{{display:none;position:absolute;top:26px;right:0;background:var(--dots-menu-bg);border:1px solid var(--bdrl);border-radius:9px;min-width:175px;box-shadow:0 12px 40px rgba(0,0,0,.25);z-index:9999;flex-direction:column;overflow:hidden}}
# # .dots-wrap:focus-within .dots-menu{{display:flex}}
# # .dots-menu-title{{font-size:.63rem;color:var(--accent);font-weight:700;letter-spacing:.12em;padding:9px 13px 7px;border-bottom:1px solid var(--bdr);text-transform:uppercase}}
# # .dots-item{{display:flex;align-items:center;gap:8px;padding:7px 13px;font-size:.8rem;color:var(--dots-item-color);cursor:pointer;background:none;border:none;width:100%;text-align:left;font-family:'Inter',sans-serif;transition:background .12s}}
# # .dots-item:hover{{background:var(--bg-h);color:var(--txt)}}
# # .dots-check{{color:var(--green);font-size:.74rem;width:13px;flex-shrink:0}}.th-label{{cursor:pointer}}
# # .pg-row{{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}}
# # .pg-info{{font-size:.74rem;color:var(--muted)}}
# # .pg-btns{{display:flex;gap:3px;flex-wrap:wrap}}
# # .pgb{{display:inline-flex;align-items:center;justify-content:center;min-width:28px;height:28px;padding:0 7px;background:var(--bg-c);color:var(--muted);border:1px solid var(--bdr);border-radius:6px;font-size:.76rem;cursor:pointer;transition:all .15s;user-select:none}}
# # .pgb:hover:not(.dis):not(.act){{background:var(--bg-h);border-color:var(--bdrl);color:var(--txt)}}
# # .pgb.act{{background:var(--accent);color:#fff;border-color:var(--accent);font-weight:600}}
# # .pgb.dis{{opacity:.3;cursor:not-allowed;pointer-events:none}}
# # .pill-i{{display:inline-block;padding:2px 9px;border-radius:99px;font-size:.72rem;font-weight:600;background:rgba(220,38,38,.15);color:var(--red);border:1px solid rgba(220,38,38,.35)}}
# # .pill-c{{display:inline-block;padding:2px 9px;border-radius:99px;font-size:.72rem;font-weight:600;background:rgba(22,163,74,.15);color:var(--green);border:1px solid rgba(22,163,74,.35)}}
# # """













# import streamlit as st


# def inject_global_styles(T: dict, font_css: str) -> None:
#     """Inject the full global CSS block (fonts + CSS variables + all component styles)."""
#     st.markdown(f"<style>{font_css}</style>", unsafe_allow_html=True)

#     st.markdown(f"""
# <style>
# :root {{
#   --bg-base:{T['bg_base']};--bg-surface:{T['bg_surface']};--bg-card:{T['bg_card']};--bg-hover:{T['bg_hover']};
#   --bg-sidebar:{T['bg_sidebar']};
#   --border:{T['border']};--border-light:{T['border_light']};
#   --text-primary:{T['text_primary']};--text-muted:{T['text_muted']};--text-dim:{T['text_dim']};
#   --accent:{T['accent']};--accent-glow:{T['accent_glow']};
#   --green:{T['green']};--green-glow:{T['green_glow']};
#   --red:{T['red']};--red-glow:{T['red_glow']};
#   --amber:{T['amber']};--amber-glow:{T['amber_glow']};
#   --purple:{T['purple']};
# }}

# html,body,[class*="css"]{{font-family:'Inter',sans-serif;}}
# .stApp{{background-color:{T['bg_base']}!important;}}
# .main .block-container{{padding:1rem 2rem 2rem!important;max-width:1600px;background:{T['bg_base']}!important;}}
# ::-webkit-scrollbar{{width:5px;height:5px;}}
# ::-webkit-scrollbar-track{{background:{T['bg_base']};}}
# ::-webkit-scrollbar-thumb{{background:{T['border_light']};border-radius:99px;}}
# div[data-testid="stStatusWidget"]{{display:none!important;}}
# header[data-testid="stHeader"] [data-testid="stDecoration"]{{display:none!important;}}

# header[data-testid="stHeader"]{{background:{T['bg_base']}!important;border-bottom:1px solid {T['border']}!important;}}
# header[data-testid="stHeader"] button svg{{color:{T['text_muted']}!important;}}
# header[data-testid="stHeader"] [data-testid="baseButton-header"]{{color:{T['text_primary']}!important;}}

# section[data-testid="stSidebar"]{{background:{T['bg_sidebar']}!important;border-right:1px solid {T['border']}!important;}}
# section[data-testid="stSidebar"] .stMarkdown *{{color:{T['text_muted']}!important;}}
# section[data-testid="stSidebar"] label{{color:{T['text_muted']}!important;font-size:0.75rem!important;text-transform:uppercase;letter-spacing:0.08em;}}
# section[data-testid="stSidebar"] div[data-baseweb="select"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;color:{T['text_primary']}!important;border-radius:10px!important;}}
# section[data-testid="stSidebar"] div[data-baseweb="input"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;border-radius:10px!important;}}

# div[data-baseweb="select"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;border-radius:10px!important;color:{T['text_primary']}!important;}}
# div[data-baseweb="select"] *{{color:{T['text_primary']}!important;}}
# div[data-baseweb="input"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;border-radius:10px!important;}}
# div[data-baseweb="input"] input{{color:{T['text_primary']}!important;}}
# span[data-baseweb="tag"]{{background:{T['accent_glow']}!important;color:{T['accent']}!important;}}
# div[data-testid="stToggle"] label{{color:{T['text_muted']}!important;}}

# ul[data-baseweb="menu"]{{background:{T['bg_card']}!important;border:1px solid {T['border']}!important;}}
# ul[data-baseweb="menu"] li{{color:{T['text_primary']}!important;}}
# ul[data-baseweb="menu"] li:hover{{background:{T['bg_hover']}!important;}}

# .section-label{{font-family:'Inter',sans-serif;font-size:0.68rem;font-weight:600;letter-spacing:0.15em;text-transform:uppercase;color:{T['text_dim']};margin:28px 0 14px;display:flex;align-items:center;gap:10px;}}
# .section-label::after{{content:'';flex:1;height:1px;background:{T['border']};}}
# .year-filter-label{{font-family:'Inter',sans-serif;font-size:0.7rem;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:{T['text_muted']};margin-bottom:4px;margin-top:2px;}}
# .stCaption{{color:{T['text_muted']}!important;font-size:0.75rem!important;}}

# .dash-header{{padding:6px 0 18px;}}
# .dash-title{{font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:800;background:linear-gradient(135deg,{T['text_primary']} 30%,{T['accent']} 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1.1;letter-spacing:-0.02em;}}
# .dash-meta{{font-size:0.78rem;color:{T['text_muted']};margin-top:6px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;}}
# .dash-meta-chip{{display:inline-flex;align-items:center;gap:6px;background:{T['bg_card']};border:1px solid {T['border']};border-radius:99px;padding:3px 12px;font-size:0.71rem;color:{T['text_muted']};}}

# .sidebar-brand{{display:flex;align-items:center;gap:10px;padding:4px 0 16px;border-bottom:1px solid {T['border']};margin-bottom:20px;}}
# .sidebar-brand-icon{{width:34px;height:34px;background:linear-gradient(135deg,{T['accent_glow']},{T['accent_glow']});border:1px solid {T['accent']};border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;opacity:0.9;}}
# .sidebar-brand-text{{font-family:'Syne',sans-serif;font-size:0.95rem;font-weight:700;color:{T['text_primary']};}}
# .sidebar-brand-sub{{font-size:0.65rem;color:{T['text_muted']};letter-spacing:0.1em;text-transform:uppercase;}}

# .alert{{border-radius:10px;padding:11px 16px;font-size:0.82rem;margin:5px 0;border-left:3px solid;font-family:'Inter',sans-serif;}}
# .alert-critical{{background:{T['red_glow']};border-color:{T['red']};color:{T['red']};}}
# .alert-warn{{background:{T['amber_glow']};border-color:{T['amber']};color:{T['amber']};}}
# .alert-ok{{background:{T['green_glow']};border-color:{T['green']};color:{T['green']};}}

# .stDataFrame{{border:1px solid {T['border']}!important;border-radius:12px!important;overflow:hidden;background:{T['bg_card']}!important;}}

# .stDownloadButton button{{background:{T['accent_glow']}!important;border:1px solid {T['accent']}!important;color:{T['accent']}!important;border-radius:10px!important;font-size:0.78rem!important;transition:all 0.18s ease!important;}}
# div[data-testid="stButton"] button{{transition:all 0.2s ease!important;letter-spacing:0.01em!important;}}

# details{{background:{T['bg_card']}!important;border-color:{T['border']}!important;}}
# summary{{color:{T['text_primary']}!important;}}

# [data-testid="stMetricValue"]{{color:{T['text_primary']}!important;}}
# [data-testid="stMetricLabel"]{{color:{T['text_muted']}!important;}}

# .modebar-container{{opacity:1!important;position:absolute!important;top:4px!important;right:4px!important;z-index:99!important;}}
# .modebar{{background:{T['bg_card']}!important;border:1px solid {T['border']}!important;border-radius:5px!important;padding:2px 3px!important;box-shadow:0 1px 6px rgba(0,0,0,0.1)!important;display:flex!important;flex-direction:row!important;gap:1px!important;backdrop-filter:none!important;width:auto!important;height:auto!important;}}
# .modebar-group{{background:transparent!important;border:none!important;padding:0!important;margin:0!important;box-shadow:none!important;display:flex!important;flex-direction:row!important;gap:1px!important;}}
# .modebar-group+.modebar-group{{border:none!important;margin:0!important;padding:0!important;}}
# .modebar-btn{{width:22px!important;height:22px!important;min-width:22px!important;min-height:22px!important;max-width:22px!important;max-height:22px!important;border-radius:3px!important;display:flex!important;align-items:center!important;justify-content:center!important;transition:background 0.12s!important;color:{T['text_muted']}!important;background:transparent!important;padding:0!important;margin:0!important;}}
# .modebar-btn:hover{{background:{T['accent_glow']}!important;color:{T['accent']}!important;}}
# .modebar-btn.active{{background:{T['accent_glow']}!important;color:{T['accent']}!important;}}
# .modebar-btn svg{{width:12px!important;height:12px!important;display:block!important;}}

# div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button {{
#     border-radius:14px!important;font-family:'Inter',sans-serif!important;
#     font-size:0.78rem!important;height:70px!important;width:100%!important;
#     letter-spacing:0.05em!important;transition:all 0.18s ease!important;cursor:pointer!important;
#     background:{T['bg_card']}!important;border:1px solid {T['border']}!important;
#     color:{T['text_muted']}!important;box-shadow:0 2px 8px rgba(0,0,0,0.06)!important;
# }}
# div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button:hover {{
#     background:{T['bg_hover']}!important;border-color:{T['green']}!important;color:{T['text_primary']}!important;
#     box-shadow:0 0 0 2px {T['green_glow']},0 6px 20px rgba(0,0,0,0.08)!important;
#     transform:translateY(-3px)!important;
# }}

# div[data-testid="stRadio"]>label{{display:none!important;}}
# div[data-testid="stRadio"]>div[role="radiogroup"]{{display:flex!important;flex-direction:row!important;gap:10px!important;flex-wrap:nowrap!important;}}
# div[data-testid="stRadio"] div[role="radiogroup"]>label{{
#     display:flex!important;flex:1 1 0%!important;align-items:center!important;justify-content:center!important;
#     min-height:44px!important;border-radius:10px!important;cursor:pointer!important;
#     font-family:'Inter',sans-serif!important;font-size:0.82rem!important;font-weight:500!important;
#     background:{T['bg_card']}!important;color:{T['text_muted']}!important;
#     border:1px solid {T['border']}!important;border-bottom:3px solid transparent!important;
#     box-shadow:0 2px 6px rgba(0,0,0,0.06)!important;
#     transition:transform 0.18s cubic-bezier(0.34,1.56,0.64,1),box-shadow 0.18s ease,border-color 0.18s ease,color 0.18s ease,background 0.18s ease!important;
#     padding:0 14px!important;text-align:center!important;user-select:none!important;white-space:nowrap!important;
# }}
# div[data-testid="stRadio"] div[role="radiogroup"]>label:hover{{
#     transform:translateY(-5px)!important;background:{T['bg_hover']}!important;color:{T['text_primary']}!important;
#     border-color:{T['border_light']}!important;border-bottom-color:{T['accent']}!important;
#     box-shadow:0 10px 28px {T['accent_glow']},0 2px 8px rgba(0,0,0,0.08)!important;
# }}
# div[data-testid="stRadio"] div[role="radiogroup"]>label:has(input:checked){{
#     background:{T['green_glow']}!important;border:1px solid {T['green']}!important;
#     border-top:3px solid {T['green']}!important;color:{T['green']}!important;
#     font-weight:700!important;transform:translateY(-2px)!important;
#     box-shadow:0 0 20px {T['green_glow']},0 6px 20px {T['green_glow']}!important;
# }}
# div[data-testid="stRadio"] div[role="radiogroup"]>label input[type="radio"]{{display:none!important;}}
# div[data-testid="stRadio"] div[role="radiogroup"]>label>div{{font-family:'Inter',sans-serif!important;font-size:0.82rem!important;line-height:1!important;pointer-events:none!important;display:inline-flex!important;align-items:center!important;gap:6px!important;white-space:nowrap!important;}}
# div[data-testid="stRadio"] div[role="radiogroup"]>label>div>p{{margin:0!important;white-space:nowrap!important;display:inline!important;}}

# /* â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•
#    PLOTLY AXIS DRAG RAIL INDICATORS
#    Exposes the existing Plotly drag zones visually.
#    No new logic â€” purely cosmetic overlays on native Plotly
#    SVG drag layer elements (.ewdrag = x-axis, .nsdrag = y-axis).
#    â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â•â• */

# /* Container holding Plotly SVG â€” used as positioning anchor */
# .js-plotly-plot .plotly,
# .js-plotly-plot svg {{
#   overflow: visible !important;
# }}

# /* â”€â”€ X-AXIS drag zone (bottom of chart) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#    Plotly renders an <rect class="ewdrag drag"> at the bottom.
#    We paint a thin rail + left/right arrow glyphs via outline
#    and box-shadow to avoid touching layout at all.           */
# .js-plotly-plot .ewdrag {{
#   fill: transparent !important;
#   stroke: none !important;
#   cursor: ew-resize !important;
# }}

# /* The rail track: thin bottom border rendered as an SVG rect
#    highlight. We achieve this via a CSS filter trick on the
#    parent layer and a dedicated pseudo-class on the g element. */
# .js-plotly-plot g.draglayer g.drag.ewdrag {{
#   /* SVG rects can't have ::before/::after, so we style the
#      containing <g> to show an underline effect via filter */
#   filter: drop-shadow(0 3px 0 {T['border_light']}) !important;
#   transition: filter 0.18s ease !important;
# }}
# .js-plotly-plot g.draglayer g.drag.ewdrag:hover {{
#   filter: drop-shadow(0 3px 0 {T['accent']}) !important;
# }}

# /* â”€â”€ Y-AXIS drag zone (left side of chart) â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#    Plotly renders <rect class="nsdrag drag"> on the left edge. */
# .js-plotly-plot .nsdrag {{
#   fill: transparent !important;
#   stroke: none !important;
#   cursor: ns-resize !important;
# }}
# .js-plotly-plot g.draglayer g.drag.nsdrag {{
#   filter: drop-shadow(-3px 0 0 {T['border_light']}) !important;
#   transition: filter 0.18s ease !important;
# }}
# .js-plotly-plot g.draglayer g.drag.nsdrag:hover {{
#   filter: drop-shadow(-3px 0 0 {T['accent']}) !important;
# }}

# /* â”€â”€ Axis rail overlay via :after on the svg container â”€â”€â”€â”€â”€
#    Adds a thin visible track line + arrow glyphs positioned
#    exactly over Plotly's drag zones using absolute positioning
#    on the Streamlit plotly wrapper element.                  */
# div[data-testid="stPlotlyChart"] {{
#   position: relative !important;
# }}

# /* X-axis bottom rail track */
# div[data-testid="stPlotlyChart"]::after {{
#   content: 'â—€ â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€ â–¶';
#   position: absolute;
#   bottom: 38px;
#   left: 48px;
#   right: 28px;
#   height: 14px;
#   display: flex;
#   align-items: center;
#   justify-content: space-between;
#   font-size: 0.62rem;
#   letter-spacing: 0.04em;
#   color: {T['border_light']};
#   pointer-events: none;
#   user-select: none;
#   z-index: 1;
#   overflow: hidden;
#   white-space: nowrap;
#   transition: color 0.2s ease;
#   line-height: 1;
# }}

# /* Replace the text approach with a cleaner SVG-compatible rail */
# div[data-testid="stPlotlyChart"] {{
#   isolation: isolate;
# }}

# /* â”€â”€ Clean rail implementation: injected via dedicated wrapper â”€
#    We inject a thin ::before rail on the bottom (x-axis) and
#    a ::before on a pseudo-sibling. Since a single element can
#    only have one ::before and one ::after, we use ::before for
#    the Y rail and ::after for the X rail.                      */

# /* X-axis bottom rail */
# div[data-testid="stPlotlyChart"]::after {{
#   content: '';
#   position: absolute;
#   bottom: 36px;
#   left: 52px;
#   right: 24px;
#   height: 2px;
#   background: linear-gradient(
#     to right,
#     transparent 0px,
#     {T['border_light']} 12px,
#     {T['border_light']} calc(100% - 12px),
#     transparent 100%
#   );
#   border-radius: 2px;
#   pointer-events: none;
#   z-index: 2;
#   transition: background 0.2s ease;
# }}

# /* X-axis left arrow marker */
# div[data-testid="stPlotlyChart"]::before {{
#   content: '';
#   position: absolute;
#   /* Y-axis left rail */
#   top: 36px;
#   bottom: 50px;
#   left: 42px;
#   width: 2px;
#   background: linear-gradient(
#     to bottom,
#     transparent 0px,
#     {T['border_light']} 12px,
#     {T['border_light']} calc(100% - 12px),
#     transparent 100%
#   );
#   border-radius: 2px;
#   pointer-events: none;
#   z-index: 2;
#   transition: background 0.2s ease;
# }}

# /* Hover: brighten both rails when user hovers the chart area */
# div[data-testid="stPlotlyChart"]:hover::after {{
#   background: linear-gradient(
#     to right,
#     transparent 0px,
#     {T['border']} 12px,
#     {T['border']} calc(100% - 12px),
#     transparent 100%
#   );
# }}
# div[data-testid="stPlotlyChart"]:hover::before {{
#   background: linear-gradient(
#     to bottom,
#     transparent 0px,
#     {T['border']} 12px,
#     {T['border']} calc(100% - 12px),
#     transparent 100%
#   );
# }}

# /* â”€â”€ Arrow tips via injected SVG-in-HTML overlay â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
#    Since CSS pseudo-elements can't render real arrowheads,
#    we inject a lightweight SVG overlay via a Streamlit-safe
#    class that wraps each chart.                              */

# /* Arrow glyphs injected as Unicode text via data attributes,
#    positioned over the rail ends using a label trick.       */

# /* X-axis: left arrow cap */
# .plotly-x-rail-left {{
#   position: absolute;
#   bottom: 30px;
#   left: 44px;
#   width: 10px;
#   height: 14px;
#   pointer-events: none;
#   z-index: 3;
#   color: {T['border_light']};
#   font-size: 8px;
#   display: flex;
#   align-items: center;
#   justify-content: center;
#   line-height: 1;
#   user-select: none;
# }}

# /* X-axis: right arrow cap */
# .plotly-x-rail-right {{
#   position: absolute;
#   bottom: 30px;
#   right: 16px;
#   width: 10px;
#   height: 14px;
#   pointer-events: none;
#   z-index: 3;
#   color: {T['border_light']};
#   font-size: 8px;
#   display: flex;
#   align-items: center;
#   justify-content: center;
#   line-height: 1;
#   user-select: none;
# }}

# /* Y-axis: top arrow cap */
# .plotly-y-rail-top {{
#   position: absolute;
#   top: 28px;
#   left: 36px;
#   width: 14px;
#   height: 10px;
#   pointer-events: none;
#   z-index: 3;
#   color: {T['border_light']};
#   font-size: 8px;
#   display: flex;
#   align-items: center;
#   justify-content: center;
#   line-height: 1;
#   user-select: none;
# }}

# /* Y-axis: bottom arrow cap */
# .plotly-y-rail-bottom {{
#   position: absolute;
#   bottom: 44px;
#   left: 36px;
#   width: 14px;
#   height: 10px;
#   pointer-events: none;
#   z-index: 3;
#   color: {T['border_light']};
#   font-size: 8px;
#   display: flex;
#   align-items: center;
#   justify-content: center;
#   line-height: 1;
#   user-select: none;
# }}

# /* Hover state for arrow glyphs */
# div[data-testid="stPlotlyChart"]:hover .plotly-x-rail-left,
# div[data-testid="stPlotlyChart"]:hover .plotly-x-rail-right,
# div[data-testid="stPlotlyChart"]:hover .plotly-y-rail-top,
# div[data-testid="stPlotlyChart"]:hover .plotly-y-rail-bottom {{
#   color: {T['accent']} !important;
# }}

# /* Hint label that appears on hover to guide users */
# div[data-testid="stPlotlyChart"]:hover::after {{
#   /* X rail already brightens; additionally pulse the rail briefly */
#   animation: rail-pulse 0.4s ease-out 1 forwards;
# }}
# @keyframes rail-pulse {{
#   0%   {{ opacity: 0.5; }}
#   50%  {{ opacity: 1; }}
#   100% {{ opacity: 0.85; }}
# }}
# </style>
# """, unsafe_allow_html=True)


# def table_css_vars(T: dict) -> str:
#     return f"""
# :root{{
#   --bg:{T['bg_base']};
#   --bg-s:{T['bg_sidebar']};
#   --bg-c:{T['bg_card']};
#   --bg-h:{T['bg_hover']};
#   --bdr:{T['border']};
#   --bdrl:{T['border_light']};
#   --txt:{T['text_primary']};
#   --muted:{T['text_muted']};
#   --dim:{T['text_dim']};
#   --accent:{T['accent']};
#   --green:{T['green']};
#   --red:{T['red']};
#   --amber:{T['amber']};
#   --td-color:{T['td_color']};
#   --td-even:{T['td_even']};
#   --thead-bg:{T['thead_bg']};
#   --dots-menu-bg:{T['dots_menu_bg']};
#   --dots-item-color:{T['dots_item_col']};
#   --scrollbar:{T['scrollbar']};
# }}"""


# def table_base_css(T: dict, max_height: str = "none") -> str:
#     tbl_wrap_overflow = f"overflow-y:auto;max-height:{max_height};" if max_height != "none" else "overflow-y:auto;flex:1;"
#     return f"""
# *{{box-sizing:border-box;margin:0;padding:0}}
# {table_css_vars(T)}
# html,body{{background:var(--bg);color:var(--txt);font-family:'Inter',sans-serif;height:100%;overflow:hidden;}}
# ::-webkit-scrollbar{{width:5px;height:5px}}
# ::-webkit-scrollbar-track{{background:var(--bg)}}
# ::-webkit-scrollbar-thumb{{background:var(--scrollbar);border-radius:99px}}
# .box{{display:flex;flex-direction:column;height:100vh;background:var(--bg-s);border-top:3px solid var(--accent)}}
# .body{{overflow-y:auto;padding:16px 18px;flex:1;display:flex;flex-direction:column;gap:14px}}
# .stats{{display:flex;gap:10px;flex-wrap:wrap}}
# .stat{{background:var(--bg-c);border:1px solid var(--bdr);border-radius:10px;padding:10px 18px;flex:1;min-width:100px;text-align:center;box-shadow:0 1px 4px rgba(0,0,0,.1)}}
# .stat-val{{font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:700;color:var(--accent)}}
# .stat-lbl{{font-size:.65rem;color:var(--muted);margin-top:3px;text-transform:uppercase;letter-spacing:.07em}}
# .controls{{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}}
# .perpage{{display:flex;align-items:center;gap:7px;font-size:.78rem;color:var(--muted)}}
# .perpage select{{background:var(--bg-c);color:var(--txt);border:1px solid var(--bdrl);border-radius:7px;padding:4px 26px 4px 9px;font-size:.78rem;font-family:'Inter',sans-serif;cursor:pointer;outline:none;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%236b7494'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 8px center}}
# .srchwrap{{display:flex;align-items:center;gap:7px;font-size:.78rem;color:var(--muted)}}
# .srchwrap input{{background:var(--bg-c);color:var(--txt);border:1px solid var(--bdrl);border-radius:7px;padding:4px 10px;font-size:.78rem;font-family:'Inter',sans-serif;outline:none;width:155px}}
# .srchwrap input:focus{{border-color:var(--accent)}}.srchwrap input::placeholder{{color:var(--muted)}}
# .tbl-wrap{{overflow-x:auto;{tbl_wrap_overflow}}}
# table{{width:100%;border-collapse:collapse;font-size:.81rem;user-select:none;-webkit-user-select:none}}
# thead tr{{position:sticky;top:0;z-index:10}}
# th{{background:var(--thead-bg);color:var(--accent);font-size:.65rem;text-transform:uppercase;letter-spacing:.1em;font-weight:600;border-bottom:2px solid var(--bdrl);padding:0;white-space:nowrap}}
# .th-inner{{display:flex;align-items:center;justify-content:space-between;padding:9px 12px;gap:5px}}
# td{{padding:8px 12px;border-bottom:1px solid var(--bdr);color:var(--td-color);white-space:nowrap;cursor:default}}
# tr:nth-child(even) td{{background:var(--td-even)}}
# tr:hover td{{background:var(--bg-h)}}
# .dots-wrap{{position:relative;outline:none;flex-shrink:0}}
# .dots-btn{{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:4px;font-size:1rem;color:var(--dim);cursor:pointer;user-select:none;transition:all .15s}}
# .dots-btn:hover,.dots-wrap:focus-within .dots-btn{{background:var(--bg-h);color:var(--accent)}}
# .dots-menu{{display:none;position:fixed;background:var(--dots-menu-bg);border:1px solid var(--bdrl);border-radius:9px;min-width:175px;box-shadow:0 12px 40px rgba(0,0,0,.35);z-index:99999;flex-direction:column;overflow:hidden}}
# .dots-wrap:focus-within .dots-menu{{display:flex}}
# .dots-menu-title{{font-size:.63rem;color:var(--accent);font-weight:700;letter-spacing:.12em;padding:9px 13px 7px;border-bottom:1px solid var(--bdr);text-transform:uppercase}}
# .dots-item{{display:flex;align-items:center;gap:8px;padding:7px 13px;font-size:.8rem;color:var(--dots-item-color);cursor:pointer;background:none;border:none;width:100%;text-align:left;font-family:'Inter',sans-serif;transition:background .12s}}
# .dots-item:hover{{background:var(--bg-h);color:var(--txt)}}
# .dots-check{{color:var(--green);font-size:.74rem;width:13px;flex-shrink:0}}.th-label{{cursor:pointer}}
# .pg-row{{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}}
# .pg-info{{font-size:.74rem;color:var(--muted)}}
# .pg-btns{{display:flex;gap:3px;flex-wrap:wrap}}
# .pgb{{display:inline-flex;align-items:center;justify-content:center;min-width:28px;height:28px;padding:0 7px;background:var(--bg-c);color:var(--muted);border:1px solid var(--bdr);border-radius:6px;font-size:.76rem;cursor:pointer;transition:all .15s;user-select:none}}
# .pgb:hover:not(.dis):not(.act){{background:var(--bg-h);border-color:var(--bdrl);color:var(--txt)}}
# .pgb.act{{background:var(--accent);color:#fff;border-color:var(--accent);font-weight:600}}
# .pgb.dis{{opacity:.3;cursor:not-allowed;pointer-events:none}}
# .pill-i{{display:inline-block;padding:2px 9px;border-radius:99px;font-size:.72rem;font-weight:600;background:rgba(220,38,38,.15);color:var(--red);border:1px solid rgba(220,38,38,.35)}}
# .pill-c{{display:inline-block;padding:2px 9px;border-radius:99px;font-size:.72rem;font-weight:600;background:rgba(22,163,74,.15);color:var(--green);border:1px solid rgba(22,163,74,.35)}}
# """






































import streamlit as st


def inject_global_styles(T: dict, font_css: str) -> None:
    """Inject the full global CSS block (fonts + CSS variables + all component styles)."""
    st.markdown(f"<style>{font_css}</style>", unsafe_allow_html=True)

    st.markdown(f"""
<style>
:root {{
  --bg-base:{T['bg_base']};--bg-surface:{T['bg_surface']};--bg-card:{T['bg_card']};--bg-hover:{T['bg_hover']};
  --bg-sidebar:{T['bg_sidebar']};
  --border:{T['border']};--border-light:{T['border_light']};
  --text-primary:{T['text_primary']};--text-muted:{T['text_muted']};--text-dim:{T['text_dim']};
  --accent:{T['accent']};--accent-glow:{T['accent_glow']};
  --green:{T['green']};--green-glow:{T['green_glow']};
  --red:{T['red']};--red-glow:{T['red_glow']};
  --amber:{T['amber']};--amber-glow:{T['amber_glow']};
  --purple:{T['purple']};
}}

html,body,[class*="css"]{{font-family:'Inter',sans-serif;}}
.stApp{{background-color:{T['bg_base']}!important;}}
.main .block-container{{padding:1rem 2rem 2rem!important;max-width:1600px;background:{T['bg_base']}!important;}}
::-webkit-scrollbar{{width:5px;height:5px;}}
::-webkit-scrollbar-track{{background:{T['bg_base']};}}
::-webkit-scrollbar-thumb{{background:{T['border_light']};border-radius:99px;}}
div[data-testid="stStatusWidget"]{{display:none!important;}}
header[data-testid="stHeader"] [data-testid="stDecoration"]{{display:none!important;}}

header[data-testid="stHeader"]{{background:{T['bg_base']}!important;border-bottom:1px solid {T['border']}!important;}}
header[data-testid="stHeader"] button svg{{color:{T['text_muted']}!important;}}
header[data-testid="stHeader"] [data-testid="baseButton-header"]{{color:{T['text_primary']}!important;}}

section[data-testid="stSidebar"]{{background:{T['bg_sidebar']}!important;border-right:1px solid {T['border']}!important;}}
section[data-testid="stSidebar"] .stMarkdown *{{color:{T['text_muted']}!important;}}
section[data-testid="stSidebar"] label{{color:{T['text_muted']}!important;font-size:0.75rem!important;text-transform:uppercase;letter-spacing:0.08em;}}
section[data-testid="stSidebar"] div[data-baseweb="select"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;color:{T['text_primary']}!important;border-radius:10px!important;}}
section[data-testid="stSidebar"] div[data-baseweb="input"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;border-radius:10px!important;}}

div[data-baseweb="select"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;border-radius:10px!important;color:{T['text_primary']}!important;}}
div[data-baseweb="select"] *{{color:{T['text_primary']}!important;}}
div[data-baseweb="input"]>div{{background:{T['bg_card']}!important;border-color:{T['border_light']}!important;border-radius:10px!important;}}
div[data-baseweb="input"] input{{color:{T['text_primary']}!important;}}
span[data-baseweb="tag"]{{background:{T['accent_glow']}!important;color:{T['accent']}!important;}}
div[data-testid="stToggle"] label{{color:{T['text_muted']}!important;}}

ul[data-baseweb="menu"]{{background:{T['bg_card']}!important;border:1px solid {T['border']}!important;}}
ul[data-baseweb="menu"] li{{color:{T['text_primary']}!important;}}
ul[data-baseweb="menu"] li:hover{{background:{T['bg_hover']}!important;}}

.section-label{{font-family:'Inter',sans-serif;font-size:0.68rem;font-weight:600;letter-spacing:0.15em;text-transform:uppercase;color:{T['text_dim']};margin:28px 0 14px;display:flex;align-items:center;gap:10px;}}
.section-label::after{{content:'';flex:1;height:1px;background:{T['border']};}}
.year-filter-label{{font-family:'Inter',sans-serif;font-size:0.7rem;font-weight:600;letter-spacing:0.12em;text-transform:uppercase;color:{T['text_muted']};margin-bottom:4px;margin-top:2px;}}
.stCaption{{color:{T['text_muted']}!important;font-size:0.75rem!important;}}

.dash-header{{padding:6px 0 18px;}}
.dash-title{{font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:800;background:linear-gradient(135deg,{T['text_primary']} 30%,{T['accent']} 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;line-height:1.1;letter-spacing:-0.02em;}}
.dash-meta{{font-size:0.78rem;color:{T['text_muted']};margin-top:6px;display:flex;align-items:center;gap:16px;flex-wrap:wrap;}}
.dash-meta-chip{{display:inline-flex;align-items:center;gap:6px;background:{T['bg_card']};border:1px solid {T['border']};border-radius:99px;padding:3px 12px;font-size:0.71rem;color:{T['text_muted']};}}

.sidebar-brand{{display:flex;align-items:center;gap:10px;padding:4px 0 16px;border-bottom:1px solid {T['border']};margin-bottom:20px;}}
.sidebar-brand-icon{{width:34px;height:34px;background:linear-gradient(135deg,{T['accent_glow']},{T['accent_glow']});border:1px solid {T['accent']};border-radius:9px;display:flex;align-items:center;justify-content:center;font-size:1.1rem;opacity:0.9;}}
.sidebar-brand-text{{font-family:'Syne',sans-serif;font-size:0.95rem;font-weight:700;color:{T['text_primary']};}}
.sidebar-brand-sub{{font-size:0.65rem;color:{T['text_muted']};letter-spacing:0.1em;text-transform:uppercase;}}

.alert{{border-radius:10px;padding:11px 16px;font-size:0.82rem;margin:5px 0;border-left:3px solid;font-family:'Inter',sans-serif;}}
.alert-critical{{background:{T['red_glow']};border-color:{T['red']};color:{T['red']};}}
.alert-warn{{background:{T['amber_glow']};border-color:{T['amber']};color:{T['amber']};}}
.alert-ok{{background:{T['green_glow']};border-color:{T['green']};color:{T['green']};}}

.stDataFrame{{border:1px solid {T['border']}!important;border-radius:12px!important;overflow:hidden;background:{T['bg_card']}!important;}}

.stDownloadButton button{{background:{T['accent_glow']}!important;border:1px solid {T['accent']}!important;color:{T['accent']}!important;border-radius:10px!important;font-size:0.78rem!important;transition:all 0.18s ease!important;}}
div[data-testid="stButton"] button{{transition:all 0.2s ease!important;letter-spacing:0.01em!important;}}

details{{background:{T['bg_card']}!important;border-color:{T['border']}!important;}}
summary{{color:{T['text_primary']}!important;}}

[data-testid="stMetricValue"]{{color:{T['text_primary']}!important;}}
[data-testid="stMetricLabel"]{{color:{T['text_muted']}!important;}}

.modebar-container{{opacity:1!important;position:absolute!important;top:4px!important;right:4px!important;z-index:99!important;}}
.modebar{{background:{T['bg_card']}!important;border:1px solid {T['border']}!important;border-radius:5px!important;padding:2px 3px!important;box-shadow:0 1px 6px rgba(0,0,0,0.1)!important;display:flex!important;flex-direction:row!important;gap:1px!important;backdrop-filter:none!important;width:auto!important;height:auto!important;}}
.modebar-group{{background:transparent!important;border:none!important;padding:0!important;margin:0!important;box-shadow:none!important;display:flex!important;flex-direction:row!important;gap:1px!important;}}
.modebar-group+.modebar-group{{border:none!important;margin:0!important;padding:0!important;}}
.modebar-btn{{width:22px!important;height:22px!important;min-width:22px!important;min-height:22px!important;max-width:22px!important;max-height:22px!important;border-radius:3px!important;display:flex!important;align-items:center!important;justify-content:center!important;transition:background 0.12s!important;color:{T['text_muted']}!important;background:transparent!important;padding:0!important;margin:0!important;}}
.modebar-btn:hover{{background:{T['accent_glow']}!important;color:{T['accent']}!important;}}
.modebar-btn.active{{background:{T['accent_glow']}!important;color:{T['accent']}!important;}}
.modebar-btn svg{{width:12px!important;height:12px!important;display:block!important;}}

div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button {{
    border-radius:14px!important;font-family:'Inter',sans-serif!important;
    font-size:0.78rem!important;height:70px!important;width:100%!important;
    letter-spacing:0.05em!important;transition:all 0.18s ease!important;cursor:pointer!important;
    background:{T['bg_card']}!important;border:1px solid {T['border']}!important;
    color:{T['text_muted']}!important;box-shadow:0 2px 8px rgba(0,0,0,0.06)!important;
}}
div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"] button:hover {{
    background:{T['bg_hover']}!important;border-color:{T['green']}!important;color:{T['text_primary']}!important;
    box-shadow:0 0 0 2px {T['green_glow']},0 6px 20px rgba(0,0,0,0.08)!important;
    transform:translateY(-3px)!important;
}}

div[data-testid="stRadio"]>label{{display:none!important;}}
div[data-testid="stRadio"]>div[role="radiogroup"]{{display:flex!important;flex-direction:row!important;gap:10px!important;flex-wrap:nowrap!important;}}
div[data-testid="stRadio"] div[role="radiogroup"]>label{{
    display:flex!important;flex:1 1 0%!important;align-items:center!important;justify-content:center!important;
    min-height:44px!important;border-radius:10px!important;cursor:pointer!important;
    font-family:'Inter',sans-serif!important;font-size:0.82rem!important;font-weight:500!important;
    background:{T['bg_card']}!important;color:{T['text_muted']}!important;
    border:1px solid {T['border']}!important;border-bottom:3px solid transparent!important;
    box-shadow:0 2px 6px rgba(0,0,0,0.06)!important;
    transition:transform 0.18s cubic-bezier(0.34,1.56,0.64,1),box-shadow 0.18s ease,border-color 0.18s ease,color 0.18s ease,background 0.18s ease!important;
    padding:0 14px!important;text-align:center!important;user-select:none!important;white-space:nowrap!important;
}}
div[data-testid="stRadio"] div[role="radiogroup"]>label:hover{{
    transform:translateY(-5px)!important;background:{T['bg_hover']}!important;color:{T['text_primary']}!important;
    border-color:{T['border_light']}!important;border-bottom-color:{T['accent']}!important;
    box-shadow:0 10px 28px {T['accent_glow']},0 2px 8px rgba(0,0,0,0.08)!important;
}}
div[data-testid="stRadio"] div[role="radiogroup"]>label:has(input:checked){{
    background:{T['green_glow']}!important;border:1px solid {T['green']}!important;
    border-top:3px solid {T['green']}!important;color:{T['green']}!important;
    font-weight:700!important;transform:translateY(-2px)!important;
    box-shadow:0 0 20px {T['green_glow']},0 6px 20px {T['green_glow']}!important;
}}
div[data-testid="stRadio"] div[role="radiogroup"]>label input[type="radio"]{{display:none!important;}}
div[data-testid="stRadio"] div[role="radiogroup"]>label>div{{font-family:'Inter',sans-serif!important;font-size:0.82rem!important;line-height:1!important;pointer-events:none!important;display:inline-flex!important;align-items:center!important;gap:6px!important;white-space:nowrap!important;}}
div[data-testid="stRadio"] div[role="radiogroup"]>label>div>p{{margin:0!important;white-space:nowrap!important;display:inline!important;}}

/* ═══════════════════════════════════════════════════════════
   PLOTLY AXIS DRAG RAIL INDICATORS
   Exposes the existing Plotly drag zones visually.
   No new logic — purely cosmetic overlays on native Plotly
   SVG drag layer elements (.ewdrag = x-axis, .nsdrag = y-axis).
   ═══════════════════════════════════════════════════════════ */

/* Container holding Plotly SVG — used as positioning anchor */
.js-plotly-plot .plotly,
.js-plotly-plot svg {{
  overflow: visible !important;
}}

/* ── X-AXIS drag zone (bottom of chart) ────────────────────
   Plotly renders an <rect class="ewdrag drag"> at the bottom.
   We paint a thin rail + left/right arrow glyphs via outline
   and box-shadow to avoid touching layout at all.           */
.js-plotly-plot .ewdrag {{
  fill: transparent !important;
  stroke: none !important;
  cursor: ew-resize !important;
}}

/* The rail track: thin bottom border rendered as an SVG rect
   highlight. We achieve this via a CSS filter trick on the
   parent layer and a dedicated pseudo-class on the g element. */
.js-plotly-plot g.draglayer g.drag.ewdrag {{
  /* SVG rects can't have ::before/::after, so we style the
     containing <g> to show an underline effect via filter */
  filter: drop-shadow(0 3px 0 {T['border_light']}) !important;
  transition: filter 0.18s ease !important;
}}
.js-plotly-plot g.draglayer g.drag.ewdrag:hover {{
  filter: drop-shadow(0 3px 0 {T['accent']}) !important;
}}

/* ── Y-AXIS drag zone (left side of chart) ─────────────────
   Plotly renders <rect class="nsdrag drag"> on the left edge. */
.js-plotly-plot .nsdrag {{
  fill: transparent !important;
  stroke: none !important;
  cursor: ns-resize !important;
}}
.js-plotly-plot g.draglayer g.drag.nsdrag {{
  filter: drop-shadow(-3px 0 0 {T['border_light']}) !important;
  transition: filter 0.18s ease !important;
}}
.js-plotly-plot g.draglayer g.drag.nsdrag:hover {{
  filter: drop-shadow(-3px 0 0 {T['accent']}) !important;
}}

/* ── Axis rail overlay via :after on the svg container ─────
   Adds a thin visible track line + arrow glyphs positioned
   exactly over Plotly's drag zones using absolute positioning
   on the Streamlit plotly wrapper element.                  */
div[data-testid="stPlotlyChart"] {{
  position: relative !important;
}}

/* X-axis bottom rail track */
div[data-testid="stPlotlyChart"]::after {{
  content: '◀ ─────────────────────────────────────────────── ▶';
  position: absolute;
  bottom: 38px;
  left: 48px;
  right: 28px;
  height: 14px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  font-size: 0.62rem;
  letter-spacing: 0.04em;
  color: {T['border_light']};
  pointer-events: none;
  user-select: none;
  z-index: 1;
  overflow: hidden;
  white-space: nowrap;
  transition: color 0.2s ease;
  line-height: 1;
}}

/* Replace the text approach with a cleaner SVG-compatible rail */
div[data-testid="stPlotlyChart"] {{
  isolation: isolate;
}}

/* ── Clean rail implementation: injected via dedicated wrapper ─
   We inject a thin ::before rail on the bottom (x-axis) and
   a ::before on a pseudo-sibling. Since a single element can
   only have one ::before and one ::after, we use ::before for
   the Y rail and ::after for the X rail.                      */

/* X-axis bottom rail */
div[data-testid="stPlotlyChart"]::after {{
  content: '';
  position: absolute;
  bottom: 36px;
  left: 52px;
  right: 24px;
  height: 2px;
  background: linear-gradient(
    to right,
    transparent 0px,
    {T['border_light']} 12px,
    {T['border_light']} calc(100% - 12px),
    transparent 100%
  );
  border-radius: 2px;
  pointer-events: none;
  z-index: 2;
  transition: background 0.2s ease;
}}

/* X-axis left arrow marker */
div[data-testid="stPlotlyChart"]::before {{
  content: '';
  position: absolute;
  /* Y-axis left rail */
  top: 36px;
  bottom: 50px;
  left: 42px;
  width: 2px;
  background: linear-gradient(
    to bottom,
    transparent 0px,
    {T['border_light']} 12px,
    {T['border_light']} calc(100% - 12px),
    transparent 100%
  );
  border-radius: 2px;
  pointer-events: none;
  z-index: 2;
  transition: background 0.2s ease;
}}

/* Hover: brighten both rails when user hovers the chart area */
div[data-testid="stPlotlyChart"]:hover::after {{
  background: linear-gradient(
    to right,
    transparent 0px,
    {T['border']} 12px,
    {T['border']} calc(100% - 12px),
    transparent 100%
  );
}}
div[data-testid="stPlotlyChart"]:hover::before {{
  background: linear-gradient(
    to bottom,
    transparent 0px,
    {T['border']} 12px,
    {T['border']} calc(100% - 12px),
    transparent 100%
  );
}}

/* ── Arrow tips via injected SVG-in-HTML overlay ────────────
   Since CSS pseudo-elements can't render real arrowheads,
   we inject a lightweight SVG overlay via a Streamlit-safe
   class that wraps each chart.                              */

/* Arrow glyphs injected as Unicode text via data attributes,
   positioned over the rail ends using a label trick.       */

/* X-axis: left arrow cap */
.plotly-x-rail-left {{
  position: absolute;
  bottom: 30px;
  left: 44px;
  width: 10px;
  height: 14px;
  pointer-events: none;
  z-index: 3;
  color: {T['border_light']};
  font-size: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  user-select: none;
}}

/* X-axis: right arrow cap */
.plotly-x-rail-right {{
  position: absolute;
  bottom: 30px;
  right: 16px;
  width: 10px;
  height: 14px;
  pointer-events: none;
  z-index: 3;
  color: {T['border_light']};
  font-size: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  user-select: none;
}}

/* Y-axis: top arrow cap */
.plotly-y-rail-top {{
  position: absolute;
  top: 28px;
  left: 36px;
  width: 14px;
  height: 10px;
  pointer-events: none;
  z-index: 3;
  color: {T['border_light']};
  font-size: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  user-select: none;
}}

/* Y-axis: bottom arrow cap */
.plotly-y-rail-bottom {{
  position: absolute;
  bottom: 44px;
  left: 36px;
  width: 14px;
  height: 10px;
  pointer-events: none;
  z-index: 3;
  color: {T['border_light']};
  font-size: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  line-height: 1;
  user-select: none;
}}

/* Hover state for arrow glyphs */
div[data-testid="stPlotlyChart"]:hover .plotly-x-rail-left,
div[data-testid="stPlotlyChart"]:hover .plotly-x-rail-right,
div[data-testid="stPlotlyChart"]:hover .plotly-y-rail-top,
div[data-testid="stPlotlyChart"]:hover .plotly-y-rail-bottom {{
  color: {T['accent']} !important;
}}

/* Hint label that appears on hover to guide users */
div[data-testid="stPlotlyChart"]:hover::after {{
  /* X rail already brightens; additionally pulse the rail briefly */
  animation: rail-pulse 0.4s ease-out 1 forwards;
}}
@keyframes rail-pulse {{
  0%   {{ opacity: 0.5; }}
  50%  {{ opacity: 1; }}
  100% {{ opacity: 0.85; }}
}}
</style>
""", unsafe_allow_html=True)


def table_css_vars(T: dict) -> str:
    return f"""
:root{{
  --bg:{T['bg_base']};
  --bg-s:{T['bg_sidebar']};
  --bg-c:{T['bg_card']};
  --bg-h:{T['bg_hover']};
  --bdr:{T['border']};
  --bdrl:{T['border_light']};
  --txt:{T['text_primary']};
  --muted:{T['text_muted']};
  --dim:{T['text_dim']};
  --accent:{T['accent']};
  --green:{T['green']};
  --red:{T['red']};
  --amber:{T['amber']};
  --td-color:{T['td_color']};
  --td-even:{T['td_even']};
  --thead-bg:{T['thead_bg']};
  --dots-menu-bg:{T['dots_menu_bg']};
  --dots-item-color:{T['dots_item_col']};
  --scrollbar:{T['scrollbar']};
}}"""


def table_base_css(T: dict, max_height: str = "none") -> str:
    tbl_wrap_overflow = f"overflow-y:auto;max-height:{max_height};" if max_height != "none" else "overflow-y:auto;flex:1;"
    return f"""
*{{box-sizing:border-box;margin:0;padding:0}}
{table_css_vars(T)}
html,body{{background:var(--bg);color:var(--txt);font-family:'Inter',sans-serif;height:100%;overflow:hidden;}}
::-webkit-scrollbar{{width:5px;height:5px}}
::-webkit-scrollbar-track{{background:var(--bg)}}
::-webkit-scrollbar-thumb{{background:var(--scrollbar);border-radius:99px}}
.box{{display:flex;flex-direction:column;height:100vh;background:var(--bg-s);border-top:3px solid var(--accent)}}
.body{{overflow-y:auto;padding:16px 18px;flex:1;display:flex;flex-direction:column;gap:14px}}
.stats{{display:flex;gap:10px;flex-wrap:wrap}}
.stat{{background:var(--bg-c);border:1px solid var(--bdr);border-radius:10px;padding:10px 18px;flex:1;min-width:100px;text-align:center;box-shadow:0 1px 4px rgba(0,0,0,.1)}}
.stat-val{{font-family:'Syne',sans-serif;font-size:1.5rem;font-weight:700;color:var(--accent)}}
.stat-lbl{{font-size:.65rem;color:var(--muted);margin-top:3px;text-transform:uppercase;letter-spacing:.07em}}
.controls{{display:flex;align-items:center;justify-content:space-between;gap:10px;flex-wrap:wrap}}
.perpage{{display:flex;align-items:center;gap:7px;font-size:.78rem;color:var(--muted)}}
.perpage select{{background:var(--bg-c);color:var(--txt);border:1px solid var(--bdrl);border-radius:7px;padding:4px 26px 4px 9px;font-size:.78rem;font-family:'Inter',sans-serif;cursor:pointer;outline:none;appearance:none;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='10' height='6'%3E%3Cpath d='M0 0l5 6 5-6z' fill='%236b7494'/%3E%3C/svg%3E");background-repeat:no-repeat;background-position:right 8px center}}
.srchwrap{{display:flex;align-items:center;gap:7px;font-size:.78rem;color:var(--muted)}}
.srchwrap input{{background:var(--bg-c);color:var(--txt);border:1px solid var(--bdrl);border-radius:7px;padding:4px 10px;font-size:.78rem;font-family:'Inter',sans-serif;outline:none;width:155px}}
.srchwrap input:focus{{border-color:var(--accent)}}.srchwrap input::placeholder{{color:var(--muted)}}
.tbl-wrap{{overflow-x:auto;{tbl_wrap_overflow}}}
table{{width:100%;border-collapse:collapse;font-size:.81rem;user-select:none;-webkit-user-select:none}}
thead tr{{position:sticky;top:0;z-index:10}}
th{{background:var(--thead-bg);color:var(--accent);font-size:.65rem;text-transform:uppercase;letter-spacing:.1em;font-weight:600;border-bottom:2px solid var(--bdrl);padding:0;white-space:nowrap}}
.th-inner{{display:flex;align-items:center;justify-content:space-between;padding:9px 12px;gap:5px}}
td{{padding:8px 12px;border-bottom:1px solid var(--bdr);color:var(--td-color);white-space:nowrap;cursor:default}}
tr:nth-child(even) td{{background:var(--td-even)}}
tr:hover td{{background:var(--bg-h)}}
.dots-wrap{{position:relative;outline:none;flex-shrink:0}}
.dots-btn{{display:inline-flex;align-items:center;justify-content:center;width:20px;height:20px;border-radius:4px;font-size:1rem;color:var(--dim);cursor:pointer;user-select:none;transition:all .15s}}
.dots-btn:hover,.dots-wrap:focus-within .dots-btn{{background:var(--bg-h);color:var(--accent)}}
.dots-menu{{display:none;position:absolute;top:26px;right:0;background:var(--dots-menu-bg);border:1px solid var(--bdrl);border-radius:9px;min-width:175px;box-shadow:0 12px 40px rgba(0,0,0,.25);z-index:9999;flex-direction:column;overflow:hidden}}
.dots-wrap:focus-within .dots-menu{{display:flex}}
.dots-menu-title{{font-size:.63rem;color:var(--accent);font-weight:700;letter-spacing:.12em;padding:9px 13px 7px;border-bottom:1px solid var(--bdr);text-transform:uppercase}}
.dots-item{{display:flex;align-items:center;gap:8px;padding:7px 13px;font-size:.8rem;color:var(--dots-item-color);cursor:pointer;background:none;border:none;width:100%;text-align:left;font-family:'Inter',sans-serif;transition:background .12s}}
.dots-item:hover{{background:var(--bg-h);color:var(--txt)}}
.dots-check{{color:var(--green);font-size:.74rem;width:13px;flex-shrink:0}}.th-label{{cursor:pointer}}
.pg-row{{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px}}
.pg-info{{font-size:.74rem;color:var(--muted)}}
.pg-btns{{display:flex;gap:3px;flex-wrap:wrap}}
.pgb{{display:inline-flex;align-items:center;justify-content:center;min-width:28px;height:28px;padding:0 7px;background:var(--bg-c);color:var(--muted);border:1px solid var(--bdr);border-radius:6px;font-size:.76rem;cursor:pointer;transition:all .15s;user-select:none}}
.pgb:hover:not(.dis):not(.act){{background:var(--bg-h);border-color:var(--bdrl);color:var(--txt)}}
.pgb.act{{background:var(--accent);color:#fff;border-color:var(--accent);font-weight:600}}
.pgb.dis{{opacity:.3;cursor:not-allowed;pointer-events:none}}
.pill-i{{display:inline-block;padding:2px 9px;border-radius:99px;font-size:.72rem;font-weight:600;background:rgba(220,38,38,.15);color:var(--red);border:1px solid rgba(220,38,38,.35)}}
.pill-c{{display:inline-block;padding:2px 9px;border-radius:99px;font-size:.72rem;font-weight:600;background:rgba(22,163,74,.15);color:var(--green);border:1px solid rgba(22,163,74,.35)}}
"""






