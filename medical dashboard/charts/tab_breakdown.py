import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

from charts.utils import apply_type_symbols, eclk
from ui.components import chart_type_selector, year_filter_widget
from ui.popup import open_popup


def render_tab_breakdown(df, T: dict, LAYOUT: dict, HOVER: dict, PALETTE: list,
                         PLOTLY_CONFIG: dict, C_RED: str, C_AMBER: str) -> None:
    df_bd = year_filter_widget("breakdown", df, T)
    cx, cy = st.columns(2)

    with cx:
        st.markdown('<div class="section-label">Affected Records by Validation Type</div>', unsafe_allow_html=True)
        ct_bt = chart_type_selector("ct_bytype", ["Horizontal Bar","Bar","Line","Pie","Scatter"], T)
        byt = (df_bd.groupby("Validation Short").agg(
            Total_Checks=("Unique Key","count"),
            Checks_With_Issues=("Has Issue","sum"),
            Total_Records=("Record Count","sum")
        ).reset_index().sort_values("Total_Records", ascending=(ct_bt=="Horizontal Bar")))

        if ct_bt == "Horizontal Bar":
            fb = go.Figure()
            fb.add_trace(go.Bar(y=byt["Validation Short"], x=byt["Total_Records"], orientation="h",
                marker_color=C_RED, name="Affected Records",
                text=byt["Total_Records"].apply(lambda v:f"{int(v):,}"),
                textposition="outside", textfont=dict(size=9, color=T["plot_font"]),
                hovertemplate="<b>%{y}</b><br>Affected Records: <b>%{x:,}</b><extra></extra>"))
            fb.add_trace(go.Bar(y=byt["Validation Short"], x=byt["Checks_With_Issues"], orientation="h",
                marker_color=C_AMBER, name="Checks w/ Issues",
                text=byt["Checks_With_Issues"].apply(lambda v:f"{int(v):,}"),
                textposition="outside", textfont=dict(size=9, color=T["plot_font"]),
                hovertemplate="<b>%{y}</b><br>Checks w/ Issues: <b>%{x:,}</b><extra></extra>"))
            fb.update_layout(**LAYOUT, barmode="group")
        elif ct_bt == "Bar":
            fb = go.Figure()
            fb.add_trace(go.Bar(x=byt["Validation Short"], y=byt["Total_Records"], marker_color=C_RED,
                name="Affected Records", text=byt["Total_Records"].apply(lambda v:f"{int(v):,}"),
                textposition="outside", textfont=dict(size=9, color=T["plot_font"])))
            fb.add_trace(go.Bar(x=byt["Validation Short"], y=byt["Checks_With_Issues"], marker_color=C_AMBER,
                name="Checks w/ Issues", text=byt["Checks_With_Issues"].apply(lambda v:f"{int(v):,}"),
                textposition="outside", textfont=dict(size=9, color=T["plot_font"])))
            fb.update_layout(**LAYOUT, barmode="group")
        elif ct_bt == "Line":
            fb = go.Figure()
            fb.add_trace(go.Scatter(x=byt["Validation Short"], y=byt["Total_Records"],
                mode="lines+markers", name="Affected Records",
                line=dict(color=C_RED, width=2.5), marker=dict(size=10, symbol="circle")))
            fb.add_trace(go.Scatter(x=byt["Validation Short"], y=byt["Checks_With_Issues"],
                mode="lines+markers", name="Checks w/ Issues",
                line=dict(color=C_AMBER, width=2.5), marker=dict(size=10, symbol="diamond")))
            fb.update_layout(**LAYOUT)
        elif ct_bt == "Pie":
            fb = go.Figure(go.Pie(labels=byt["Validation Short"], values=byt["Total_Records"], hole=0.45,
                marker=dict(colors=PALETTE), textinfo="percent+label",
                hovertemplate="<b>%{label}</b><br>Records: <b>%{value:,}</b><extra></extra>"))
            fb.update_layout(**LAYOUT, showlegend=False)
        elif ct_bt == "Scatter":
            fb = px.scatter(byt, x="Total_Records", y="Checks_With_Issues", size="Total_Records",
                color="Validation Short", color_discrete_sequence=PALETTE, text="Validation Short")
            fb.update_traces(textposition="top center", textfont=dict(size=9, color=T["plot_font"]))
            apply_type_symbols(fb)
            fb.update_layout(**LAYOUT)

        fb.update_layout(
            hoverlabel=HOVER,
            legend=dict(bgcolor=T["legend_bg"], bordercolor=T["border"], borderwidth=1,
                        font=dict(color=T["plot_font"]))
        )
        eclk(fb, 380)
        ebe = st.plotly_chart(fb, use_container_width=True, on_select="rerun", config=PLOTLY_CONFIG, key="bytype_chart")
        if ebe and ebe.get("selection", {}).get("points"):
            pt = ebe["selection"]["points"][0]
            vt = pt.get("x") or pt.get("y") or pt.get("label")
            if vt and vt in byt["Validation Short"].values:
                open_popup({"Validation Type": vt}, f"VALIDATION_TYPE: {vt}")

    with cy:
        st.markdown('<div class="section-label">Issue Distribution by Table</div>', unsafe_allow_html=True)
        ct_tbl = chart_type_selector("ct_bytable", ["Donut","Pie","Bar","Horizontal Bar","Treemap"], T)
        btbl   = (df_bd[df_bd["Has Issue"]].groupby("Affected Table Name")["Record Count"].sum()
                  .reset_index().sort_values("Record Count", ascending=False))
        if btbl.empty or btbl["Record Count"].sum() == 0:
            st.info("No affected records.")
        else:
            if ct_tbl == "Donut":
                fp2 = go.Figure(go.Pie(labels=btbl["Affected Table Name"], values=btbl["Record Count"], hole=0.55,
                    marker=dict(colors=PALETTE), textinfo="percent+label", textfont=dict(size=10, color=T["plot_font"]),
                    hovertemplate="<b>%{label}</b><br>Records: <b>%{value:,}</b><br>%{percent}<extra></extra>"))
                fp2.update_layout(**LAYOUT, height=380, showlegend=False, clickmode="event+select")
            elif ct_tbl == "Pie":
                fp2 = go.Figure(go.Pie(labels=btbl["Affected Table Name"], values=btbl["Record Count"], hole=0,
                    marker=dict(colors=PALETTE), textinfo="percent+label",
                    hovertemplate="<b>%{label}</b><br>Records: <b>%{value:,}</b><br>%{percent}<extra></extra>"))
                fp2.update_layout(**LAYOUT, height=380, showlegend=False, clickmode="event+select")
            elif ct_tbl == "Bar":
                fp2 = px.bar(btbl, x="Affected Table Name", y="Record Count",
                    color_discrete_sequence=PALETTE, text="Record Count")
                fp2.update_traces(texttemplate="%{text:,}", textposition="outside",
                                  textfont=dict(size=9, color=T["plot_font"]))
                fp2.update_layout(**LAYOUT, height=380, showlegend=False)
            elif ct_tbl == "Horizontal Bar":
                fp2 = px.bar(btbl, y="Affected Table Name", x="Record Count", orientation="h",
                    color_discrete_sequence=PALETTE, text="Record Count")
                fp2.update_traces(texttemplate="%{text:,}", textposition="outside",
                                  textfont=dict(size=9, color=T["plot_font"]))
                fp2.update_layout(**LAYOUT, height=380, showlegend=False)
            elif ct_tbl == "Treemap":
                fp2 = px.treemap(btbl, path=["Affected Table Name"], values="Record Count",
                    color="Record Count",
                    color_continuous_scale=[T["bg_surface"], T["accent"], T["red"]])
                fp2.update_traces(textinfo="label+value+percent root",
                                  textfont=dict(color=T["plot_font"]))
                fp2.update_layout(**LAYOUT, height=380)
            eclk(fp2, 380)
            ep2 = st.plotly_chart(fp2, use_container_width=True, on_select="rerun", config=PLOTLY_CONFIG, key="pie_chart")
            if ep2 and ep2.get("selection", {}).get("points"):
                pt = ep2["selection"]["points"][0]
                tn = pt.get("label") or pt.get("x") or pt.get("y")
                if tn: open_popup({"Table": tn, "Status":"Issues"}, f"AFFTECTED_TABLE_NAME: {tn}")

    st.markdown('<div class="section-label">Validation Type Summary</div>', unsafe_allow_html=True)
    summary = (df_bd.groupby("Validation Short").agg(
        Total_Checks=("Unique Key","count"),
        Checks_With_Issues=("Has Issue","sum"),
        Total_Records=("Record Count","sum"),
        Max_Records=("Record Count","max"),
        Avg_Records=("Record Count","mean")
    ).reset_index())
    summary["Issue Rate"]   = (summary["Checks_With_Issues"] / summary["Total_Checks"] * 100).round(1).astype(str) + "%"
    summary["Avg_Records"]  = summary["Avg_Records"].round(2)
    st.dataframe(summary.rename(columns={
        "Validation Short":"VALIDATION_TYPE","Total_Checks":"Total Checks","Checks_With_Issues":"Checks w/ Issues",
        "Total_Records":"Affected Records","Max_Records":"Max Records","Avg_Records":"Avg Records"
    }), use_container_width=True, hide_index=True)

    if len(summary) > 0:
        st.markdown('<div class="section-label">⚡ Alerts</div>', unsafe_allow_html=True)
        worst = summary.sort_values("Total_Records", ascending=False).iloc[0]
        st.markdown(f'<div class="alert alert-critical">🔴 <b>{worst["Validation Short"]}</b> has the highest affected records: <b>{int(worst["Total_Records"]):,}</b></div>', unsafe_allow_html=True)
        wr = summary.sort_values("Checks_With_Issues", ascending=False).iloc[0]
        if wr["Total_Checks"] > 0:
            st.markdown(f'<div class="alert alert-warn">🟡 <b>{wr["Validation Short"]}</b> flags issues on <b>{wr["Checks_With_Issues"]/wr["Total_Checks"]*100:.0f}%</b> of its checks</div>', unsafe_allow_html=True)
        ct0 = summary[summary["Checks_With_Issues"] == 0]
        if len(ct0):
            st.markdown(f'<div class="alert alert-ok">🟢 Zero issues: <b>{", ".join(ct0["Validation Short"].tolist())}</b></div>', unsafe_allow_html=True)
        ai = summary[(summary["Checks_With_Issues"] == summary["Total_Checks"]) & (summary["Total_Checks"] > 0)]
        if len(ai):
            st.markdown(f'<div class="alert alert-critical">🔴 Always flagging (100%): <b>{", ".join(ai["Validation Short"].tolist())}</b></div>', unsafe_allow_html=True)























































# import streamlit as st
# import plotly.express as px
# import plotly.graph_objects as go

# from charts.utils import apply_type_symbols, eclk
# from ui.components import chart_type_selector, year_filter_widget
# from ui.popup import open_popup



# def render_tab_breakdown(df, T: dict, LAYOUT: dict, HOVER: dict, PALETTE: list,
#                          PLOTLY_CONFIG: dict, C_RED: str, C_AMBER: str) -> None:
#     df_bd = year_filter_widget("breakdown", df, T)
#     cx, cy = st.columns(2)

#     with cx:
#         st.markdown('<div class="section-label">Affected Records by Validation Type</div>', unsafe_allow_html=True)
#         ct_bt = chart_type_selector("ct_bytype", ["Horizontal Bar","Bar","Line","Pie","Scatter"], T)
#         byt = (df_bd.groupby("Validation Short").agg(
#             Total_Checks=("Unique Key","count"),
#             Checks_With_Issues=("Has Issue","sum"),
#             Total_Records=("Record Count","sum")
#         ).reset_index().sort_values("Total_Records", ascending=(ct_bt=="Horizontal Bar")))

#         if ct_bt == "Horizontal Bar":
#             fb = go.Figure()
#             fb.add_trace(go.Bar(y=byt["Validation Short"], x=byt["Total_Records"], orientation="h",
#                 marker_color=C_RED, name="Affected Records",
#                 text=byt["Total_Records"].apply(lambda v:f"{int(v):,}"),
#                 textposition="outside", textfont=dict(size=9, color=T["plot_font"]),
#                 hovertemplate="<b>%{y}</b><br>Affected Records: <b>%{x:,}</b><extra></extra>"))
#             fb.add_trace(go.Bar(y=byt["Validation Short"], x=byt["Checks_With_Issues"], orientation="h",
#                 marker_color=C_AMBER, name="Checks w/ Issues",
#                 text=byt["Checks_With_Issues"].apply(lambda v:f"{int(v):,}"),
#                 textposition="outside", textfont=dict(size=9, color=T["plot_font"]),
#                 hovertemplate="<b>%{y}</b><br>Checks w/ Issues: <b>%{x:,}</b><extra></extra>"))
#             fb.update_layout(**LAYOUT, barmode="group")
#         elif ct_bt == "Bar":
#             fb = go.Figure()
#             fb.add_trace(go.Bar(x=byt["Validation Short"], y=byt["Total_Records"], marker_color=C_RED,
#                 name="Affected Records", text=byt["Total_Records"].apply(lambda v:f"{int(v):,}"),
#                 textposition="outside", textfont=dict(size=9, color=T["plot_font"])))
#             fb.add_trace(go.Bar(x=byt["Validation Short"], y=byt["Checks_With_Issues"], marker_color=C_AMBER,
#                 name="Checks w/ Issues", text=byt["Checks_With_Issues"].apply(lambda v:f"{int(v):,}"),
#                 textposition="outside", textfont=dict(size=9, color=T["plot_font"])))
#             fb.update_layout(**LAYOUT, barmode="group")
#         elif ct_bt == "Line":
#             fb = go.Figure()
#             fb.add_trace(go.Scatter(x=byt["Validation Short"], y=byt["Total_Records"],
#                 mode="lines+markers", name="Affected Records",
#                 line=dict(color=C_RED, width=2.5), marker=dict(size=10, symbol="circle")))
#             fb.add_trace(go.Scatter(x=byt["Validation Short"], y=byt["Checks_With_Issues"],
#                 mode="lines+markers", name="Checks w/ Issues",
#                 line=dict(color=C_AMBER, width=2.5), marker=dict(size=10, symbol="diamond")))
#             fb.update_layout(**LAYOUT)
#         elif ct_bt == "Pie":
#             fb = go.Figure(go.Pie(labels=byt["Validation Short"], values=byt["Total_Records"], hole=0.45,
#                 marker=dict(colors=PALETTE), textinfo="percent+label",
#                 automargin=True, textposition="outside",
#                 hovertemplate="<b>%{label}</b><br>Records: <b>%{value:,}</b><extra></extra>"))
#             fb.update_layout(**LAYOUT, showlegend=False, margin=dict(l=80, r=80, t=50, b=80))
#         elif ct_bt == "Scatter":
#             fb = px.scatter(byt, x="Total_Records", y="Checks_With_Issues", size="Total_Records",
#                 color="Validation Short", color_discrete_sequence=PALETTE, text="Validation Short")
#             fb.update_traces(textposition="top center", textfont=dict(size=9, color=T["plot_font"]))
#             apply_type_symbols(fb)
#             fb.update_layout(**LAYOUT)

#         fb.update_layout(
#             hoverlabel=HOVER,
#             legend=dict(bgcolor=T["legend_bg"], bordercolor=T["border"], borderwidth=1,
#                         font=dict(color=T["plot_font"]))
#         )
#         eclk(fb, 380)
#         ebe = st.plotly_chart(fb, use_container_width=True, on_select="rerun", config=PLOTLY_CONFIG, key="bytype_chart")
#         if ebe and ebe.get("selection", {}).get("points"):
#             pt = ebe["selection"]["points"][0]
#             vt = pt.get("x") or pt.get("y") or pt.get("label")
#             if vt and vt in byt["Validation Short"].values:
#                 open_popup({"Validation Type": vt}, f"VALIDATION_TYPE: {vt}")

#     with cy:
#         st.markdown('<div class="section-label">Issue Distribution by Table</div>', unsafe_allow_html=True)
#         ct_tbl = chart_type_selector("ct_bytable", ["Donut","Pie","Bar","Horizontal Bar","Treemap"], T)
#         btbl   = (df_bd[df_bd["Has Issue"]].groupby("Affected Table Name")["Record Count"].sum()
#                   .reset_index().sort_values("Record Count", ascending=False))
#         if btbl.empty or btbl["Record Count"].sum() == 0:
#             st.info("No affected records.")
#         else:
#             if ct_tbl == "Donut":
#                 fp2 = go.Figure(go.Pie(labels=btbl["Affected Table Name"], values=btbl["Record Count"], hole=0.55,
#                     marker=dict(colors=PALETTE), textinfo="percent+label", textfont=dict(size=10, color=T["plot_font"]),
#                     automargin=True, textposition="outside",
#                     hovertemplate="<b>%{label}</b><br>Records: <b>%{value:,}</b><br>%{percent}<extra></extra>"))
#                 fp2.update_layout(**LAYOUT, height=420, showlegend=False, clickmode="event+select",
#                                   margin=dict(l=80, r=80, t=50, b=80))
#             elif ct_tbl == "Pie":
#                 fp2 = go.Figure(go.Pie(labels=btbl["Affected Table Name"], values=btbl["Record Count"], hole=0,
#                     marker=dict(colors=PALETTE), textinfo="percent+label",
#                     automargin=True, textposition="outside",
#                     hovertemplate="<b>%{label}</b><br>Records: <b>%{value:,}</b><br>%{percent}<extra></extra>"))
#                 fp2.update_layout(**LAYOUT, height=420, showlegend=False, clickmode="event+select",
#                                   margin=dict(l=80, r=80, t=50, b=80))
#             elif ct_tbl == "Bar":
#                 fp2 = px.bar(btbl, x="Affected Table Name", y="Record Count",
#                     color_discrete_sequence=PALETTE, text="Record Count")
#                 fp2.update_traces(texttemplate="%{text:,}", textposition="outside",
#                                   textfont=dict(size=9, color=T["plot_font"]))
#                 fp2.update_layout(**LAYOUT, height=380, showlegend=False)
#             elif ct_tbl == "Horizontal Bar":
#                 fp2 = px.bar(btbl, y="Affected Table Name", x="Record Count", orientation="h",
#                     color_discrete_sequence=PALETTE, text="Record Count")
#                 fp2.update_traces(texttemplate="%{text:,}", textposition="outside",
#                                   textfont=dict(size=9, color=T["plot_font"]))
#                 fp2.update_layout(**LAYOUT, height=380, showlegend=False)
#             elif ct_tbl == "Treemap":
#                 fp2 = px.treemap(btbl, path=["Affected Table Name"], values="Record Count",
#                     color="Record Count",
#                     color_continuous_scale=[T["bg_surface"], T["accent"], T["red"]])
#                 fp2.update_traces(textinfo="label+value+percent root",
#                                   textfont=dict(color=T["plot_font"]))
#                 fp2.update_layout(**LAYOUT, height=380)
#             eclk(fp2, 420)
#             ep2 = st.plotly_chart(fp2, use_container_width=True, on_select="rerun", config=PLOTLY_CONFIG, key="pie_chart")
#             if ep2 and ep2.get("selection", {}).get("points"):
#                 pt = ep2["selection"]["points"][0]
#                 tn = pt.get("label") or pt.get("x") or pt.get("y")
#                 if tn: open_popup({"Table": tn, "Status":"Issues"}, f"AFFTECTED_TABLE_NAME: {tn}")

#     st.markdown('<div class="section-label">Validation Type Summary</div>', unsafe_allow_html=True)
#     summary = (df_bd.groupby("Validation Short").agg(
#         Total_Checks=("Unique Key","count"),
#         Checks_With_Issues=("Has Issue","sum"),
#         Total_Records=("Record Count","sum"),
#         Max_Records=("Record Count","max"),
#         Avg_Records=("Record Count","mean")
#     ).reset_index())
#     summary["Issue Rate"]  = (summary["Checks_With_Issues"] / summary["Total_Checks"] * 100).round(1).astype(str) + "%"
#     summary["Avg_Records"] = summary["Avg_Records"].round(2)
#     st.dataframe(summary.rename(columns={
#         "Validation Short":"VALIDATION_TYPE","Total_Checks":"Total Checks","Checks_With_Issues":"Checks w/ Issues",
#         "Total_Records":"Affected Records","Max_Records":"Max Records","Avg_Records":"Avg Records"
#     }), use_container_width=True, hide_index=True)

#     if len(summary) > 0:
#         st.markdown('<div class="section-label">⚡ Alerts</div>', unsafe_allow_html=True)
#         worst = summary.sort_values("Total_Records", ascending=False).iloc[0]
#         st.markdown(f'<div class="alert alert-critical">🔴 <b>{worst["Validation Short"]}</b> has the highest affected records: <b>{int(worst["Total_Records"]):,}</b></div>', unsafe_allow_html=True)
#         wr = summary.sort_values("Checks_With_Issues", ascending=False).iloc[0]
#         if wr["Total_Checks"] > 0:
#             st.markdown(f'<div class="alert alert-warn">🟡 <b>{wr["Validation Short"]}</b> flags issues on <b>{wr["Checks_With_Issues"]/wr["Total_Checks"]*100:.0f}%</b> of its checks</div>', unsafe_allow_html=True)
#         ct0 = summary[summary["Checks_With_Issues"] == 0]
#         if len(ct0):
#             st.markdown(f'<div class="alert alert-ok">🟢 Zero issues: <b>{", ".join(ct0["Validation Short"].tolist())}</b></div>', unsafe_allow_html=True)
#         ai = summary[(summary["Checks_With_Issues"] == summary["Total_Checks"]) & (summary["Total_Checks"] > 0)]
#         if len(ai):
#             st.markdown(f'<div class="alert alert-critical">🔴 Always flagging (100%): <b>{", ".join(ai["Validation Short"].tolist())}</b></div>', unsafe_allow_html=True)
