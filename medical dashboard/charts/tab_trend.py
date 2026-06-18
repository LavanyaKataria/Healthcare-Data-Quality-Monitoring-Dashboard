import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from charts.utils import apply_type_symbols, eclk, lock_axes
from ui.components import chart_type_selector, year_filter_widget
from ui.popup import open_popup


def render_tab_trend(df, T, LAYOUT, HOVER, PALETTE, PLOTLY_CONFIG,
                     C_BLUE, C_GREEN, C_RED):
    st.markdown('<div class="section-label">Affected Record Count Over Time · by Validation Type</div>', unsafe_allow_html=True)
    ct_trend = chart_type_selector("ct_trend", ["Line","Bar","Stacked Bar","Area","Scatter"], T)
    df_trend = year_filter_widget("trend", df, T)
    df_ti    = df_trend[df_trend["Has Issue"]]
    daily    = df_ti.groupby(["Verified Date","Validation Short"])["Record Count"].sum().reset_index()
    active_types = daily.groupby("Validation Short")["Record Count"].sum()
    active_types = active_types[active_types > 0].index.tolist()
    da = daily[daily["Validation Short"].isin(active_types)]

    if da.empty:
        st.info("No issue records for the selected filters.")
    else:
        HT = "<b>%{fullData.name}</b><br>📅 <b>%{x|%d %b %Y}</b><br>RECORD_COUNT: <b>%{y:,}</b><extra></extra>"
        if ct_trend == "Line":
            fig = px.line(da, x="Verified Date", y="Record Count", color="Validation Short",
                          color_discrete_sequence=PALETTE, markers=True)
            fig.update_traces(line_width=2.5, marker_size=10, hovertemplate=HT)
            apply_type_symbols(fig)
        elif ct_trend == "Bar":
            fig = px.bar(da, x="Verified Date", y="Record Count", color="Validation Short",
                         color_discrete_sequence=PALETTE, barmode="group", text="Record Count")
            fig.update_traces(texttemplate="%{text:,}", textposition="outside", textfont=dict(size=9), hovertemplate=HT)
        elif ct_trend == "Stacked Bar":
            fig = px.bar(da, x="Verified Date", y="Record Count", color="Validation Short",
                         color_discrete_sequence=PALETTE, barmode="stack")
            fig.update_traces(hovertemplate=HT)
        elif ct_trend == "Area":
            fig = px.area(da, x="Verified Date", y="Record Count", color="Validation Short",
                          color_discrete_sequence=PALETTE, markers=True)
            fig.update_traces(hovertemplate=HT)
            apply_type_symbols(fig)
        elif ct_trend == "Scatter":
            fig = px.scatter(da, x="Verified Date", y="Record Count", color="Validation Short",
                             size="Record Count", color_discrete_sequence=PALETTE)
            fig.update_traces(hovertemplate=HT)
            apply_type_symbols(fig)

        fig.update_layout(
            **LAYOUT, hoverlabel=HOVER,
            legend=dict(bgcolor=T["legend_bg"], bordercolor=T["border"], borderwidth=1,
                        font=dict(color=T["plot_font"]))
        )
        eclk(fig, 420)
        lock_axes(fig, da["Verified Date"], da["Record Count"])
        ev = st.plotly_chart(fig, use_container_width=True, on_select="rerun", config=PLOTLY_CONFIG, key="trend_chart")
        if ev and ev.get("selection", {}).get("points"):
            pt = ev["selection"]["points"][0]; ci = pt.get("curve_number", 0)
            vt = active_types[ci] if ci < len(active_types) else None; flt = {}
            try: flt["Date"] = pd.Timestamp(pt["x"]).strftime("%Y-%m-%d")
            except: pass
            if vt: flt["Validation Type"] = vt
            if flt: open_popup(flt, f"Trend · {vt or ''} · {flt.get('Date','')}")

    ca, cb = st.columns(2)
    with ca:
        st.markdown('<div class="section-label">Daily Pass vs Issue Checks</div>', unsafe_allow_html=True)
        ct_pf = chart_type_selector("ct_passbar", ["Bar","Stacked Bar","Line","Area","Pie"], T)
        df_pf = year_filter_widget("pf", df, T)
        dpf   = df_pf.groupby(["Verified Date","Is issue found"]).size().reset_index(name="Count")
        dpf["Status"] = dpf["Is issue found"].map({"Y":"Pass ✅","N":"Issues ⚠️"})
        cm = {"Pass ✅": C_GREEN, "Issues ⚠️": C_RED}; so = ["Pass ✅","Issues ⚠️"]
        HT2 = "<b>%{fullData.name}</b><br>📅 %{x|%d %b %Y}<br>Count: <b>%{y:,}</b><extra></extra>"
        if ct_pf == "Bar":
            fp = px.bar(dpf, x="Verified Date", y="Count", color="Status", color_discrete_map=cm,
                        barmode="group", text="Count", category_orders={"Status":so})
            fp.update_traces(texttemplate="%{text:,}", textposition="outside", textfont=dict(size=9), hovertemplate=HT2)
        elif ct_pf == "Stacked Bar":
            fp = px.bar(dpf, x="Verified Date", y="Count", color="Status", color_discrete_map=cm,
                        barmode="stack", category_orders={"Status":so})
            fp.update_traces(hovertemplate=HT2)
        elif ct_pf == "Line":
            fp = px.line(dpf, x="Verified Date", y="Count", color="Status",
                         color_discrete_map=cm, markers=True)
            fp.update_traces(line_width=2.5, marker_size=10, hovertemplate=HT2)
            apply_type_symbols(fp)
        elif ct_pf == "Area":
            fp = px.area(dpf, x="Verified Date", y="Count", color="Status",
                         color_discrete_map=cm, markers=True)
            fp.update_traces(hovertemplate=HT2)
            apply_type_symbols(fp)
        elif ct_pf == "Pie":
            agg = dpf.groupby("Status")["Count"].sum().reset_index()
            fp  = go.Figure(go.Pie(labels=agg["Status"], values=agg["Count"], hole=0.42,
                marker=dict(colors=[C_GREEN, C_RED]),
                hovertemplate="<b>%{label}</b><br>Count: <b>%{value:,}</b><br>%{percent}<extra></extra>"))
        fp.update_layout(
            **LAYOUT, hoverlabel=HOVER,
            legend=dict(bgcolor=T["legend_bg"], bordercolor=T["border"], borderwidth=1,
                        font=dict(color=T["plot_font"]))
        )
        eclk(fp, 320)
        if ct_pf != "Pie":
            lock_axes(fp, dpf["Verified Date"], dpf["Count"])
        epf = st.plotly_chart(fp, use_container_width=True, on_select="rerun", config=PLOTLY_CONFIG, key="pf_chart")
        if epf and epf.get("selection", {}).get("points"):
            pt = epf["selection"]["points"][0]; flt = {}
            try: flt["Date"] = pd.Timestamp(pt["x"]).strftime("%Y-%m-%d")
            except: pass
            ci = pt.get("curve_number", -1)
            if ci == 0: flt["Status"] = "Pass"; sl = "Pass ✅"
            elif ci == 1: flt["Status"] = "Issues"; sl = "Issues ⚠️"
            else: sl = ""
            if flt: open_popup(flt, f"Daily · {sl} · {flt.get('Date','')}")

    with cb:
        st.markdown('<div class="section-label">Cumulative Affected Records Over Time</div>', unsafe_allow_html=True)
        ct_cum = chart_type_selector("ct_cumulative", ["Area","Line","Bar","Scatter","Step"], T)
        df_cs  = year_filter_widget("cum", df, T)
        cum    = df_cs[df_cs["Has Issue"]].groupby("Verified Date")["Record Count"].sum().sort_index().cumsum().reset_index()
        cum.columns = ["Date","Cumulative Records"]
        HT3 = "📅 <b>%{x|%d %b %Y}</b><br>Cumulative: <b>%{y:,}</b><extra></extra>"
        if ct_cum == "Area":
            fc = go.Figure(go.Scatter(x=cum["Date"], y=cum["Cumulative Records"], fill="tozeroy",
                line=dict(color=C_BLUE, width=2.5), fillcolor=T["accent_glow"],
                mode="lines+markers", marker=dict(size=9, color=C_BLUE, symbol="circle"),
                hovertemplate=HT3))
        elif ct_cum == "Line":
            fc = go.Figure(go.Scatter(x=cum["Date"], y=cum["Cumulative Records"],
                line=dict(color=C_BLUE, width=2.5), mode="lines+markers",
                marker=dict(size=9, symbol="diamond"), hovertemplate=HT3))
        elif ct_cum == "Bar":
            fc = go.Figure(go.Bar(x=cum["Date"], y=cum["Cumulative Records"],
                marker_color=C_BLUE, hovertemplate=HT3))
        elif ct_cum == "Scatter":
            fc = go.Figure(go.Scatter(x=cum["Date"], y=cum["Cumulative Records"], mode="markers",
                marker=dict(size=14, color=C_BLUE, opacity=0.85, symbol="star"),
                hovertemplate=HT3))
        elif ct_cum == "Step":
            fc = go.Figure(go.Scatter(x=cum["Date"], y=cum["Cumulative Records"],
                line=dict(color=C_BLUE, width=2.5, shape="hv"), fill="tozeroy",
                fillcolor=T["accent_glow"], mode="lines+markers",
                marker=dict(size=8, symbol="square"), hovertemplate=HT3))
        fc.update_layout(**LAYOUT, height=320, hoverlabel=HOVER, clickmode="event+select")
        lock_axes(fc, cum["Date"], cum["Cumulative Records"])
        ec = st.plotly_chart(fc, use_container_width=True, on_select="rerun", config=PLOTLY_CONFIG, key="cum_chart")
        if ec and ec.get("selection", {}).get("points"):
            pt = ec["selection"]["points"][0]
            try: open_popup({"Date": pd.Timestamp(pt["x"]).strftime("%Y-%m-%d"), "Status":"Issues"}, f"Cumulative · {pt['x']}")
            except: pass







# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import plotly.graph_objects as go

# from charts.utils import apply_type_symbols, eclk, lock_axes
# from ui.components import chart_type_selector, year_filter_widget
# from ui.popup import open_popup


# def render_tab_trend(df, T, LAYOUT, HOVER, PALETTE, PLOTLY_CONFIG,
#                      C_BLUE, C_GREEN, C_RED):
#     st.markdown('<div class="section-label">Affected Record Count Over Time · by Validation Type</div>', unsafe_allow_html=True)
#     ct_trend = chart_type_selector("ct_trend", ["Line","Bar","Stacked Bar","Area","Scatter"], T)
#     df_trend = year_filter_widget("trend", df, T)
#     df_ti    = df_trend[df_trend["Has Issue"]]
#     daily    = df_ti.groupby(["Verified Date","Validation Short"])["Record Count"].sum().reset_index()
#     active_types = daily.groupby("Validation Short")["Record Count"].sum()
#     active_types = active_types[active_types > 0].index.tolist()
#     da = daily[daily["Validation Short"].isin(active_types)]

#     if da.empty:
#         st.info("No issue records for the selected filters.")
#     else:
#         HT = "<b>%{fullData.name}</b><br>📅 <b>%{x|%d %b %Y}</b><br>RECORD_COUNT: <b>%{y:,}</b><extra></extra>"
#         if ct_trend == "Line":
#             fig = px.line(da, x="Verified Date", y="Record Count", color="Validation Short",
#                           color_discrete_sequence=PALETTE, markers=True)
#             fig.update_traces(line_width=2.5, marker_size=10, hovertemplate=HT)
#             apply_type_symbols(fig)
#         elif ct_trend == "Bar":
#             fig = px.bar(da, x="Verified Date", y="Record Count", color="Validation Short",
#                          color_discrete_sequence=PALETTE, barmode="group", text="Record Count")
#             fig.update_traces(texttemplate="%{text:,}", textposition="outside", textfont=dict(size=9), hovertemplate=HT)
#         elif ct_trend == "Stacked Bar":
#             fig = px.bar(da, x="Verified Date", y="Record Count", color="Validation Short",
#                          color_discrete_sequence=PALETTE, barmode="stack")
#             fig.update_traces(hovertemplate=HT)
#         elif ct_trend == "Area":
#             fig = px.area(da, x="Verified Date", y="Record Count", color="Validation Short",
#                           color_discrete_sequence=PALETTE, markers=True)
#             fig.update_traces(hovertemplate=HT)
#             apply_type_symbols(fig)
#         elif ct_trend == "Scatter":
#             fig = px.scatter(da, x="Verified Date", y="Record Count", color="Validation Short",
#                              size="Record Count", color_discrete_sequence=PALETTE)
#             fig.update_traces(hovertemplate=HT)
#             apply_type_symbols(fig)

#         fig.update_layout(
#             **LAYOUT, hoverlabel=HOVER,
#             legend=dict(bgcolor=T["legend_bg"], bordercolor=T["border"], borderwidth=1,
#                         font=dict(color=T["plot_font"]))
#         )
#         eclk(fig, 420)
#         lock_axes(fig, da["Verified Date"], da["Record Count"])
#         ev = st.plotly_chart(fig, use_container_width=True, on_select="rerun", config=PLOTLY_CONFIG, key="trend_chart")
#         if ev and ev.get("selection", {}).get("points"):
#             pt = ev["selection"]["points"][0]; ci = pt.get("curve_number", 0)
#             vt = active_types[ci] if ci < len(active_types) else None; flt = {}
#             try: flt["Date"] = pd.Timestamp(pt["x"]).strftime("%Y-%m-%d")
#             except: pass
#             if vt: flt["Validation Type"] = vt
#             if flt: open_popup(flt, f"Trend · {vt or ''} · {flt.get('Date','')}")

#     ca, cb = st.columns(2)
#     with ca:
#         st.markdown('<div class="section-label">Daily Pass vs Issue Checks</div>', unsafe_allow_html=True)
#         ct_pf = chart_type_selector("ct_passbar", ["Bar","Stacked Bar","Line","Area","Pie"], T)
#         df_pf = year_filter_widget("pf", df, T)
#         dpf   = df_pf.groupby(["Verified Date","Is issue found"]).size().reset_index(name="Count")
#         dpf["Status"] = dpf["Is issue found"].map({"Y":"Pass ✅","N":"Issues ⚠️"})
#         cm = {"Pass ✅": C_GREEN, "Issues ⚠️": C_RED}; so = ["Pass ✅","Issues ⚠️"]
#         HT2 = "<b>%{fullData.name}</b><br>📅 %{x|%d %b %Y}<br>Count: <b>%{y:,}</b><extra></extra>"
#         if ct_pf == "Bar":
#             fp = px.bar(dpf, x="Verified Date", y="Count", color="Status", color_discrete_map=cm,
#                         barmode="group", text="Count", category_orders={"Status":so})
#             fp.update_traces(texttemplate="%{text:,}", textposition="outside", textfont=dict(size=9), hovertemplate=HT2)
#         elif ct_pf == "Stacked Bar":
#             fp = px.bar(dpf, x="Verified Date", y="Count", color="Status", color_discrete_map=cm,
#                         barmode="stack", category_orders={"Status":so})
#             fp.update_traces(hovertemplate=HT2)
#         elif ct_pf == "Line":
#             fp = px.line(dpf, x="Verified Date", y="Count", color="Status",
#                          color_discrete_map=cm, markers=True)
#             fp.update_traces(line_width=2.5, marker_size=10, hovertemplate=HT2)
#             apply_type_symbols(fp)
#         elif ct_pf == "Area":
#             fp = px.area(dpf, x="Verified Date", y="Count", color="Status",
#                          color_discrete_map=cm, markers=True)
#             fp.update_traces(hovertemplate=HT2)
#             apply_type_symbols(fp)
#         elif ct_pf == "Pie":
#             agg = dpf.groupby("Status")["Count"].sum().reset_index()
#             fp  = go.Figure(go.Pie(labels=agg["Status"], values=agg["Count"], hole=0.42,
#                 marker=dict(colors=[C_GREEN, C_RED]),
#                 hovertemplate="<b>%{label}</b><br>Count: <b>%{value:,}</b><br>%{percent}<extra></extra>"))
#         fp.update_layout(
#             **LAYOUT, hoverlabel=HOVER,
#             legend=dict(bgcolor=T["legend_bg"], bordercolor=T["border"], borderwidth=1,
#                         font=dict(color=T["plot_font"]))
#         )
#         eclk(fp, 320)
#         if ct_pf != "Pie":
#             lock_axes(fp, dpf["Verified Date"], dpf["Count"])
#         epf = st.plotly_chart(fp, use_container_width=True, on_select="rerun", config=PLOTLY_CONFIG, key="pf_chart")
#         if epf and epf.get("selection", {}).get("points"):
#             pt = epf["selection"]["points"][0]; flt = {}
#             try: flt["Date"] = pd.Timestamp(pt["x"]).strftime("%Y-%m-%d")
#             except: pass
#             ci = pt.get("curve_number", -1)
#             if ci == 0: flt["Status"] = "Pass"; sl = "Pass ✅"
#             elif ci == 1: flt["Status"] = "Issues"; sl = "Issues ⚠️"
#             else: sl = ""
#             if flt: open_popup(flt, f"Daily · {sl} · {flt.get('Date','')}")

#     with cb:
#         st.markdown('<div class="section-label">Cumulative Affected Records Over Time</div>', unsafe_allow_html=True)
#         ct_cum = chart_type_selector("ct_cumulative", ["Area","Line","Bar","Scatter","Step"], T)
#         df_cs  = year_filter_widget("cum", df, T)
#         cum    = df_cs[df_cs["Has Issue"]].groupby("Verified Date")["Record Count"].sum().sort_index().cumsum().reset_index()
#         cum.columns = ["Date","Cumulative Records"]
#         HT3 = "📅 <b>%{x|%d %b %Y}</b><br>Cumulative: <b>%{y:,}</b><extra></extra>"
#         if ct_cum == "Area":
#             fc = go.Figure(go.Scatter(x=cum["Date"], y=cum["Cumulative Records"], fill="tozeroy",
#                 line=dict(color=C_BLUE, width=2.5), fillcolor=T["accent_glow"],
#                 mode="lines+markers", marker=dict(size=9, color=C_BLUE, symbol="circle"),
#                 hovertemplate=HT3))
#         elif ct_cum == "Line":
#             fc = go.Figure(go.Scatter(x=cum["Date"], y=cum["Cumulative Records"],
#                 line=dict(color=C_BLUE, width=2.5), mode="lines+markers",
#                 marker=dict(size=9, symbol="diamond"), hovertemplate=HT3))
#         elif ct_cum == "Bar":
#             fc = go.Figure(go.Bar(x=cum["Date"], y=cum["Cumulative Records"],
#                 marker_color=C_BLUE, hovertemplate=HT3))
#         elif ct_cum == "Scatter":
#             fc = go.Figure(go.Scatter(x=cum["Date"], y=cum["Cumulative Records"], mode="markers",
#                 marker=dict(size=14, color=C_BLUE, opacity=0.85, symbol="star"),
#                 hovertemplate=HT3))
#         elif ct_cum == "Step":
#             fc = go.Figure(go.Scatter(x=cum["Date"], y=cum["Cumulative Records"],
#                 line=dict(color=C_BLUE, width=2.5, shape="hv"), fill="tozeroy",
#                 fillcolor=T["accent_glow"], mode="lines+markers",
#                 marker=dict(size=8, symbol="square"), hovertemplate=HT3))
#         fc.update_layout(**LAYOUT, height=320, hoverlabel=HOVER, clickmode="event+select")
#         lock_axes(fc, cum["Date"], cum["Cumulative Records"])
#         ec = st.plotly_chart(fc, use_container_width=True, on_select="rerun", config=PLOTLY_CONFIG, key="cum_chart")
#         if ec and ec.get("selection", {}).get("points"):
#             pt = ec["selection"]["points"][0]
#             try: open_popup({"Date": pd.Timestamp(pt["x"]).strftime("%Y-%m-%d"), "Status":"Issues"}, f"Cumulative · {pt['x']}")
#             except: pass






