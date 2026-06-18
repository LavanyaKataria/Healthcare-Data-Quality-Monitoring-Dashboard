# import streamlit as st

# def get_theme(dark: bool) -> dict:
#     if dark:
#         return dict(
#             bg_base       = "#0B0E14",
#             bg_surface    = "#161B26",
#             bg_card       = "#161B26",
#             bg_hover      = "#202A3B",
#             bg_sidebar    = "#0F131C",
#             border        = "#242F41",
#             border_light  = "#2E3A50",
#             text_primary  = "#D9E2EC",
#             text_muted    = "#9FB3C8",
#             text_dim      = "#7C8EA3",
#             accent        = "#4D9FFF",
#             accent_glow   = "rgba(77,159,255,0.18)",
#             green         = "#22C55E",
#             green_glow    = "rgba(34,197,94,0.18)",
#             red           = "#F87171",
#             red_glow      = "rgba(248,113,113,0.18)",
#             amber         = "#FBBF24",
#             amber_glow    = "rgba(251,191,36,0.18)",
#             purple        = "#A78BFA",
#             td_color      = "#C8D8E8",
#             td_even       = "#1A2130",
#             thead_bg      = "#1C2535",
#             dots_menu_bg  = "#1C2535",
#             dots_item_col = "#C8D8E8",
#             scrollbar     = "#2E3A50",
#             plot_paper    = "#0B0E14",
#             plot_bg       = "#161B26",
#             plot_grid     = "#242F41",
#             plot_font     = "#D9E2EC",
#             legend_bg     = "rgba(22,27,38,0.97)",
#             hover_bg      = "#1C2535",
#             hover_font    = "#D9E2EC",
#             hover_border  = "#242F41",
#         )
#     else:
#         return dict(
#             bg_base       = "#F4F6FA",
#             bg_surface    = "#FFFFFF",
#             bg_card       = "#FFFFFF",
#             bg_hover      = "#EEF4FF",
#             bg_sidebar    = "#F0F2F7",
#             border        = "#E2E8F0",
#             border_light  = "#CBD5E0",
#             text_primary  = "#0E1E4D",
#             text_muted    = "#4A5568",
#             text_dim      = "#8890b0",
#             accent        = "#2563eb",
#             accent_glow   = "rgba(37,99,235,0.15)",
#             green         = "#16a34a",
#             green_glow    = "rgba(22,163,74,0.15)",
#             red           = "#dc2626",
#             red_glow      = "rgba(220,38,38,0.15)",
#             amber         = "#d97706",
#             amber_glow    = "rgba(217,119,6,0.15)",
#             purple        = "#7c3aed",
#             td_color      = "#374162",
#             td_even       = "#F8FAFC",
#             thead_bg      = "#F0F2F7",
#             dots_menu_bg  = "#FFFFFF",
#             dots_item_col = "#374162",
#             scrollbar     = "#CBD5E0",
#             plot_paper    = "rgba(0,0,0,0)",
#             plot_bg       = "rgba(0,0,0,0)",
#             plot_grid     = "#E2E8F0",
#             plot_font     = "#4A5568",
#             legend_bg     = "rgba(255,255,255,0.97)",
#             hover_bg      = "#FFFFFF",
#             hover_font    = "#0E1E4D",
#             hover_border  = "#E2E8F0",
#         )


# def build_layout(T: dict) -> dict:
#     return dict(
#         paper_bgcolor = T["plot_paper"],
#         plot_bgcolor  = T["plot_bg"],
#         font          = dict(family="Inter", color=T["plot_font"], size=11),
#         margin        = dict(l=40, r=20, t=36, b=40),
#         xaxis         = dict(gridcolor=T["plot_grid"], zerolinecolor=T["plot_grid"],
#                              showline=False, autorange=False,
#                              tickfont=dict(color=T["plot_font"])),
#         yaxis         = dict(gridcolor=T["plot_grid"], zerolinecolor=T["plot_grid"],
#                              showline=False, rangemode="tozero",
#                              tickfont=dict(color=T["plot_font"])),
#         modebar       = dict(bgcolor="rgba(0,0,0,0)", color=T["text_muted"],
#                              activecolor=T["accent"], orientation="h"),
#     )


# def build_hover(T: dict) -> dict:
#     return dict(
#         bgcolor    = T["hover_bg"],
#         bordercolor= T["hover_border"],
#         font       = dict(family="Inter", size=13, color=T["hover_font"]),
#     )


# PLOTLY_CONFIG = dict(
#     displaylogo=False, displayModeBar=True,
#     modeBarButtonsToRemove=["pan2d","select2d","lasso2d","autoScale2d",
#                             "drawline","drawopenpath","drawclosedpath","drawcircle","drawrect","eraseshape"],
#     modeBarButtonsToAdd=[],
#     toImageButtonOptions=dict(format="png", filename="chart", scale=2),
#     scrollZoom=False,
# )












import streamlit as st

def get_theme(dark: bool) -> dict:
    if dark:
        return dict(
            bg_base       = "#0B0E14",
            bg_surface    = "#161B26",
            bg_card       = "#161B26",
            bg_hover      = "#202A3B",
            bg_sidebar    = "#0F131C",
            border        = "#242F41",
            border_light  = "#2E3A50",
            text_primary  = "#D9E2EC",
            text_muted    = "#9FB3C8",
            text_dim      = "#7C8EA3",
            accent        = "#4D9FFF",
            accent_glow   = "rgba(77,159,255,0.18)",
            green         = "#22C55E",
            green_glow    = "rgba(34,197,94,0.18)",
            red           = "#F87171",
            red_glow      = "rgba(248,113,113,0.18)",
            amber         = "#FBBF24",
            amber_glow    = "rgba(251,191,36,0.18)",
            purple        = "#A78BFA",
            td_color      = "#C8D8E8",
            td_even       = "#1A2130",
            thead_bg      = "#1C2535",
            dots_menu_bg  = "#1C2535",
            dots_item_col = "#C8D8E8",
            scrollbar     = "#2E3A50",
            plot_paper    = "#0B0E14",
            plot_bg       = "#161B26",
            plot_grid     = "#242F41",
            plot_font     = "#D9E2EC",
            legend_bg     = "rgba(22,27,38,0.97)",
            hover_bg      = "#1C2535",
            hover_font    = "#D9E2EC",
            hover_border  = "#242F41",
        )
    else:
        return dict(
            bg_base       = "#F4F6FA",
            bg_surface    = "#FFFFFF",
            bg_card       = "#FFFFFF",
            bg_hover      = "#EEF4FF",
            bg_sidebar    = "#F0F2F7",
            border        = "#E2E8F0",
            border_light  = "#CBD5E0",
            text_primary  = "#0E1E4D",
            text_muted    = "#4A5568",
            text_dim      = "#8890b0",
            accent        = "#2563eb",
            accent_glow   = "rgba(37,99,235,0.15)",
            green         = "#16a34a",
            green_glow    = "rgba(22,163,74,0.15)",
            red           = "#dc2626",
            red_glow      = "rgba(220,38,38,0.15)",
            amber         = "#d97706",
            amber_glow    = "rgba(217,119,6,0.15)",
            purple        = "#7c3aed",
            td_color      = "#374162",
            td_even       = "#F8FAFC",
            thead_bg      = "#F0F2F7",
            dots_menu_bg  = "#FFFFFF",
            dots_item_col = "#374162",
            scrollbar     = "#CBD5E0",
            plot_paper    = "rgba(0,0,0,0)",
            plot_bg       = "rgba(0,0,0,0)",
            plot_grid     = "#E2E8F0",
            plot_font     = "#4A5568",
            legend_bg     = "rgba(255,255,255,0.97)",
            hover_bg      = "#FFFFFF",
            hover_font    = "#0E1E4D",
            hover_border  = "#E2E8F0",
        )


def build_layout(T: dict) -> dict:
    return dict(
        paper_bgcolor = T["plot_paper"],
        plot_bgcolor  = T["plot_bg"],
        font          = dict(family="Inter", color=T["plot_font"], size=11),
        margin        = dict(l=40, r=20, t=36, b=40),
        xaxis         = dict(gridcolor=T["plot_grid"], zerolinecolor=T["plot_grid"],
                             showline=False, autorange=False,
                             tickfont=dict(color=T["plot_font"])),
        yaxis         = dict(gridcolor=T["plot_grid"], zerolinecolor=T["plot_grid"],
                             showline=False, rangemode="tozero",
                             tickfont=dict(color=T["plot_font"])),
        modebar       = dict(bgcolor="rgba(0,0,0,0)", color=T["text_muted"],
                             activecolor=T["accent"], orientation="h"),
    )


def build_hover(T: dict) -> dict:
    return dict(
        bgcolor    = T["hover_bg"],
        bordercolor= T["hover_border"],
        font       = dict(family="Inter", size=13, color=T["hover_font"]),
    )


PLOTLY_CONFIG = dict(
    displaylogo=False, displayModeBar=True,
    modeBarButtonsToRemove=["pan2d","select2d","lasso2d","autoScale2d",
                            "drawline","drawopenpath","drawclosedpath","drawcircle","drawrect","eraseshape"],
    modeBarButtonsToAdd=[],
    toImageButtonOptions=dict(format="png", filename="chart", scale=2),
    scrollZoom=False,
)








