# # import streamlit as st


# # def build_th_html(cols_def: list) -> str:
# #     th_parts = []
# #     for lbl, idx, _ in cols_def:
# #         th_parts.append(f"""<th>
# #           <div class="th-inner">
# #             <span class="th-label" data-col="{idx}">{lbl}</span>
# #             <div class="dots-wrap" tabindex="0">
# #               <span class="dots-btn">&#8942;</span>
# #               <div class="dots-menu">
# #                 <div class="dots-menu-title">{lbl}</div>
# #                 <button class="dots-item" onclick="sortTable({idx},'asc')"><span class="dots-check sort-asc-{idx}"> </span>&#8593; Sort Ascending</button>
# #                 <button class="dots-item" onclick="sortTable({idx},'desc')"><span class="dots-check sort-desc-{idx}"> </span>&#8595; Sort Descending</button>
# #                 <button class="dots-item" onclick="sortTable({idx},'none')"><span class="dots-check sort-none-{idx}"> </span>&#8856; Clear Sort</button>
# #               </div>
# #             </div>
# #           </div>
# #         </th>""")
# #     return "".join(th_parts)


# # def year_filter_widget(key_suffix: str, dataframe, T: dict):
# #     years = sorted(dataframe["Year"].dropna().unique().astype(int).tolist())
# #     if len(years) <= 1:
# #         return dataframe
# #     c, _ = st.columns([2, 8])
# #     with c:
# #         st.markdown('<div class="year-filter-label">📅 Year Filter</div>', unsafe_allow_html=True)
# #         yr = st.selectbox("Year Filter", ["All"] + [str(y) for y in years],
# #                           key=f"yr_{key_suffix}", label_visibility="collapsed")
# #     return dataframe if yr == "All" else dataframe[dataframe["Year"] == int(yr)]


# # def chart_type_selector(key: str, options: list, T: dict) -> str:
# #     c1, c2 = st.columns([1, 3])
# #     with c1:
# #         st.markdown(f'<span style="font-size:0.7rem;color:{T["text_muted"]};text-transform:uppercase;letter-spacing:0.1em;line-height:38px;display:inline-block">Chart Type</span>', unsafe_allow_html=True)
# #     with c2:
# #         cur = st.session_state.get(key, options[0])
# #         idx = options.index(cur) if cur in options else 0
# #         chosen = st.selectbox("_", options, index=idx, key=f"dd_{key}", label_visibility="collapsed")
# #         st.session_state[key] = chosen
# #     return chosen


# # def green_css(nth: int, T: dict) -> str:
# #     return f"""
# #     div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child({nth}) button {{
# #         background: {T['green_glow']} !important; border: 2px solid {T['green']} !important;
# #         color: {T['green']} !important; font-weight: 700 !important;
# #         box-shadow: 0 0 0 3px {T['green_glow']}, 0 0 20px {T['green_glow']} !important;
# #         transform: translateY(-2px) !important;
# #     }}"""


# # def grey_css(nth: int, T: dict) -> str:
# #     return f"""
# #     div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child({nth}) button {{
# #         background: {T['bg_card']} !important; border: 1px solid {T['border']} !important;
# #         color: {T['text_muted']} !important; font-weight: 500 !important;
# #         box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important; transform: none !important;
# #     }}
# #     div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child({nth}) button:hover {{
# #         background: {T['bg_hover']} !important; border-color: {T['green']} !important;
# #         color: {T['text_primary']} !important;
# #         box-shadow: 0 0 0 2px {T['green_glow']}, 0 6px 20px rgba(0,0,0,0.1) !important;
# #         transform: translateY(-3px) !important;
# #     }}"""










# import streamlit as st


# def inject_axis_rail_arrows() -> None:
#     """
#     Injects small SVG arrow-tip markers that sit at the ends of the
#     axis drag rail tracks defined in styles.py.

#     These are purely decorative — pointer-events:none — and do NOT
#     add any new interaction logic.  They are positioned absolutely
#     inside the `div[data-testid="stPlotlyChart"]` wrapper (which has
#     position:relative set by the global CSS) to sit exactly at the
#     ends of the ::before (Y rail) and ::after (X rail) tracks.

#     ◀ / ▶  mark the left / right ends of the X-axis drag zone.
#     ▲ / ▼  mark the top  / bottom ends of the Y-axis drag zone.
#     """
#     st.markdown(
#         """
#         <style>
#         /* Ensure the Streamlit plotly wrapper is the positioning anchor */
#         div[data-testid="stPlotlyChart"] { position: relative !important; }
#         </style>
#         <script>
#         (function() {
#           function attachRailArrows() {
#             const charts = document.querySelectorAll(
#               'div[data-testid="stPlotlyChart"]'
#             );
#             charts.forEach(function(wrap) {
#               if (wrap.dataset.railInjected) return;
#               wrap.dataset.railInjected = '1';

#               const arrows = [
#                 // [className, innerText, title]
#                 ['plotly-x-rail-left',   '◀', 'Drag X-axis left'],
#                 ['plotly-x-rail-right',  '▶', 'Drag X-axis right'],
#                 ['plotly-y-rail-top',    '▲', 'Drag Y-axis up'],
#                 ['plotly-y-rail-bottom', '▼', 'Drag Y-axis down'],
#               ];

#               arrows.forEach(function([cls, txt, ttl]) {
#                 if (wrap.querySelector('.' + cls)) return;
#                 const el = document.createElement('div');
#                 el.className = cls;
#                 el.textContent = txt;
#                 el.title = ttl;
#                 wrap.appendChild(el);
#               });
#             });
#           }

#           // Run once after render, then observe for new charts
#           setTimeout(attachRailArrows, 600);
#           const obs = new MutationObserver(function() {
#             attachRailArrows();
#           });
#           obs.observe(document.body, { childList: true, subtree: true });
#         })();
#         </script>
#         """,
#         unsafe_allow_html=True,
#     )


# def build_th_html(cols_def: list) -> str:
#     th_parts = []
#     for lbl, idx, _ in cols_def:
#         th_parts.append(f"""<th>
#           <div class="th-inner">
#             <span class="th-label" data-col="{idx}">{lbl}</span>
#             <div class="dots-wrap" tabindex="0">
#               <span class="dots-btn">&#8942;</span>
#               <div class="dots-menu">
#                 <div class="dots-menu-title">{lbl}</div>
#                 <button class="dots-item" onclick="sortTable({idx},'asc')"><span class="dots-check sort-asc-{idx}"> </span>&#8593; Sort Ascending</button>
#                 <button class="dots-item" onclick="sortTable({idx},'desc')"><span class="dots-check sort-desc-{idx}"> </span>&#8595; Sort Descending</button>
#                 <button class="dots-item" onclick="sortTable({idx},'none')"><span class="dots-check sort-none-{idx}"> </span>&#8856; Clear Sort</button>
#               </div>
#             </div>
#           </div>
#         </th>""")
#     return "".join(th_parts)


# def year_filter_widget(key_suffix: str, dataframe, T: dict):
#     years = sorted(dataframe["Year"].dropna().unique().astype(int).tolist())
#     if len(years) <= 1:
#         return dataframe
#     c, _ = st.columns([2, 8])
#     with c:
#         st.markdown('<div class="year-filter-label">📅 Year Filter</div>', unsafe_allow_html=True)
#         yr = st.selectbox("Year Filter", ["All"] + [str(y) for y in years],
#                           key=f"yr_{key_suffix}", label_visibility="collapsed")
#     return dataframe if yr == "All" else dataframe[dataframe["Year"] == int(yr)]


# def chart_type_selector(key: str, options: list, T: dict) -> str:
#     c1, c2 = st.columns([1, 3])
#     with c1:
#         st.markdown(f'<span style="font-size:0.7rem;color:{T["text_muted"]};text-transform:uppercase;letter-spacing:0.1em;line-height:38px;display:inline-block">Chart Type</span>', unsafe_allow_html=True)
#     with c2:
#         cur = st.session_state.get(key, options[0])
#         idx = options.index(cur) if cur in options else 0
#         chosen = st.selectbox("_", options, index=idx, key=f"dd_{key}", label_visibility="collapsed")
#         st.session_state[key] = chosen
#     return chosen


# def green_css(nth: int, T: dict) -> str:
#     return f"""
#     div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child({nth}) button {{
#         background: {T['green_glow']} !important; border: 2px solid {T['green']} !important;
#         color: {T['green']} !important; font-weight: 700 !important;
#         box-shadow: 0 0 0 3px {T['green_glow']}, 0 0 20px {T['green_glow']} !important;
#         transform: translateY(-2px) !important;
#     }}"""


# def grey_css(nth: int, T: dict) -> str:
#     return f"""
#     div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child({nth}) button {{
#         background: {T['bg_card']} !important; border: 1px solid {T['border']} !important;
#         color: {T['text_muted']} !important; font-weight: 500 !important;
#         box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important; transform: none !important;
#     }}
#     div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child({nth}) button:hover {{
#         background: {T['bg_hover']} !important; border-color: {T['green']} !important;
#         color: {T['text_primary']} !important;
#         box-shadow: 0 0 0 2px {T['green_glow']}, 0 6px 20px rgba(0,0,0,0.1) !important;
#         transform: translateY(-3px) !important;
#     }}"""














import streamlit as st


def inject_axis_rail_arrows() -> None:
    """
    Injects small SVG arrow-tip markers that sit at the ends of the
    axis drag rail tracks defined in styles.py.

    These are purely decorative — pointer-events:none — and do NOT
    add any new interaction logic.  They are positioned absolutely
    inside the `div[data-testid="stPlotlyChart"]` wrapper (which has
    position:relative set by the global CSS) to sit exactly at the
    ends of the ::before (Y rail) and ::after (X rail) tracks.

    ◀ / ▶  mark the left / right ends of the X-axis drag zone.
    ▲ / ▼  mark the top  / bottom ends of the Y-axis drag zone.
    """
    st.markdown(
        """
        <style>
        /* Ensure the Streamlit plotly wrapper is the positioning anchor */
        div[data-testid="stPlotlyChart"] { position: relative !important; }
        </style>
        <script>
        (function() {
          function attachRailArrows() {
            const charts = document.querySelectorAll(
              'div[data-testid="stPlotlyChart"]'
            );
            charts.forEach(function(wrap) {
              if (wrap.dataset.railInjected) return;
              wrap.dataset.railInjected = '1';

              const arrows = [
                // [className, innerText, title]
                ['plotly-x-rail-left',   '◀', 'Drag X-axis left'],
                ['plotly-x-rail-right',  '▶', 'Drag X-axis right'],
                ['plotly-y-rail-top',    '▲', 'Drag Y-axis up'],
                ['plotly-y-rail-bottom', '▼', 'Drag Y-axis down'],
              ];

              arrows.forEach(function([cls, txt, ttl]) {
                if (wrap.querySelector('.' + cls)) return;
                const el = document.createElement('div');
                el.className = cls;
                el.textContent = txt;
                el.title = ttl;
                wrap.appendChild(el);
              });
            });
          }

          // Run once after render, then observe for new charts
          setTimeout(attachRailArrows, 600);
          const obs = new MutationObserver(function() {
            attachRailArrows();
          });
          obs.observe(document.body, { childList: true, subtree: true });
        })();
        </script>
        """,
        unsafe_allow_html=True,
    )


def build_th_html(cols_def: list) -> str:
    th_parts = []
    for lbl, idx, _ in cols_def:
        th_parts.append(f"""<th>
          <div class="th-inner">
            <span class="th-label" data-col="{idx}">{lbl}</span>
            <div class="dots-wrap" tabindex="0">
              <span class="dots-btn">&#8942;</span>
              <div class="dots-menu">
                <div class="dots-menu-title">{lbl}</div>
                <button class="dots-item" onclick="sortTable({idx},'asc')"><span class="dots-check sort-asc-{idx}"> </span>&#8593; Sort Ascending</button>
                <button class="dots-item" onclick="sortTable({idx},'desc')"><span class="dots-check sort-desc-{idx}"> </span>&#8595; Sort Descending</button>
                <button class="dots-item" onclick="sortTable({idx},'none')"><span class="dots-check sort-none-{idx}"> </span>&#8856; Clear Sort</button>
              </div>
            </div>
          </div>
        </th>""")
    return "".join(th_parts)


def year_filter_widget(key_suffix: str, dataframe, T: dict):
    years = sorted(dataframe["Year"].dropna().unique().astype(int).tolist())
    if len(years) <= 1:
        return dataframe
    c, _ = st.columns([2, 8])
    with c:
        st.markdown('<div class="year-filter-label">📅 Year Filter</div>', unsafe_allow_html=True)
        yr = st.selectbox("Year Filter", ["All"] + [str(y) for y in years],
                          key=f"yr_{key_suffix}", label_visibility="collapsed")
    return dataframe if yr == "All" else dataframe[dataframe["Year"] == int(yr)]


def chart_type_selector(key: str, options: list, T: dict) -> str:
    c1, c2 = st.columns([1, 3])
    with c1:
        st.markdown(f'<span style="font-size:0.7rem;color:{T["text_muted"]};text-transform:uppercase;letter-spacing:0.1em;line-height:38px;display:inline-block">Chart Type</span>', unsafe_allow_html=True)
    with c2:
        cur = st.session_state.get(key, options[0])
        idx = options.index(cur) if cur in options else 0
        chosen = st.selectbox("_", options, index=idx, key=f"dd_{key}", label_visibility="collapsed")
        st.session_state[key] = chosen
    return chosen


def green_css(nth: int, T: dict) -> str:
    return f"""
    div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child({nth}) button {{
        background: {T['green_glow']} !important; border: 2px solid {T['green']} !important;
        color: {T['green']} !important; font-weight: 700 !important;
        box-shadow: 0 0 0 3px {T['green_glow']}, 0 0 20px {T['green_glow']} !important;
        transform: translateY(-2px) !important;
    }}"""


def grey_css(nth: int, T: dict) -> str:
    return f"""
    div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child({nth}) button {{
        background: {T['bg_card']} !important; border: 1px solid {T['border']} !important;
        color: {T['text_muted']} !important; font-weight: 500 !important;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1) !important; transform: none !important;
    }}
    div[data-testid="stHorizontalBlock"] > div[data-testid="stColumn"]:nth-child({nth}) button:hover {{
        background: {T['bg_hover']} !important; border-color: {T['green']} !important;
        color: {T['text_primary']} !important;
        box-shadow: 0 0 0 2px {T['green_glow']}, 0 6px 20px rgba(0,0,0,0.1) !important;
        transform: translateY(-3px) !important;
    }}"""

