# # import pandas as pd
# # from datetime import timedelta

# # SYMBOLS = ["circle","square","diamond","triangle-up","star","pentagon","hexagram","cross","bowtie","triangle-down"]


# # def apply_type_symbols(fig):
# #     for i, trace in enumerate(fig.data):
# #         sym = SYMBOLS[i % len(SYMBOLS)]
# #         try: fig.data[i].marker.symbol = sym
# #         except: pass
# #     return fig


# # def eclk(fig, h: int = 400):
# #     fig.update_layout(height=h, clickmode="event+select")
# #     return fig


# # def lock_axes(fig, date_series, value_series=None, pad_days: int = 1, y_pad_frac: float = 0.15):
# #     valid_dates = pd.to_datetime(date_series.dropna())
# #     if valid_dates.empty: return fig
# #     x_min = valid_dates.min() - timedelta(days=pad_days)
# #     x_max = valid_dates.max() + timedelta(days=pad_days)
# #     fig.update_xaxes(range=[x_min.isoformat(), x_max.isoformat()], autorange=False, fixedrange=False)
# #     if value_series is not None:
# #         vals = pd.to_numeric(value_series.dropna(), errors="coerce").dropna()
# #         if not vals.empty:
# #             y_max = float(vals.max()) * (1 + y_pad_frac)
# #             fig.update_yaxes(range=[0, y_max], autorange=False, fixedrange=False)
# #     else:
# #         fig.update_yaxes(rangemode="tozero")
# #     return fig







# import pandas as pd
# from datetime import timedelta

# SYMBOLS = ["circle","square","diamond","triangle-up","star","pentagon","hexagram","cross","bowtie","triangle-down"]


# def apply_type_symbols(fig):
#     for i, trace in enumerate(fig.data):
#         sym = SYMBOLS[i % len(SYMBOLS)]
#         try: fig.data[i].marker.symbol = sym
#         except: pass
#     return fig


# def eclk(fig, h: int = 400):
#     fig.update_layout(height=h, clickmode="event+select")
#     return fig


# def lock_axes(fig, date_series, value_series=None, pad_days: int = 1, y_pad_frac: float = 0.15,
#               window_days: int = 180):
#     """
#     Sets initial visible window for the chart instead of locking to full range.
#     - Shows the most recent `window_days` of data on load.
#     - Allows the navigator and Plotly zoom/pan to work freely.
#     - Falls back to full range if data span is shorter than window_days.
#     """
#     valid_dates = pd.to_datetime(date_series.dropna())
#     if valid_dates.empty:
#         return fig

#     x_min_full = valid_dates.min() - timedelta(days=pad_days)
#     x_max_full = valid_dates.max() + timedelta(days=pad_days)
#     total_days  = (x_max_full - x_min_full).days

#     # If total span fits within window, show everything; otherwise show last window_days
#     if total_days <= window_days:
#         x_start = x_min_full
#         x_end   = x_max_full
#     else:
#         x_end   = x_max_full
#         x_start = x_end - timedelta(days=window_days)

#     fig.update_xaxes(
#         range=[x_start.isoformat(), x_end.isoformat()],
#         autorange=False,
#         fixedrange=False   # allows zoom/pan and navigator
#     )

#     if value_series is not None:
#         vals = pd.to_numeric(value_series.dropna(), errors="coerce").dropna()
#         if not vals.empty:
#             y_max = float(vals.max()) * (1 + y_pad_frac)
#             fig.update_yaxes(range=[0, y_max], autorange=False, fixedrange=False)
#     else:
#         fig.update_yaxes(rangemode="tozero", fixedrange=False)

#     return fig













import pandas as pd
from datetime import timedelta

SYMBOLS = ["circle","square","diamond","triangle-up","star","pentagon","hexagram","cross","bowtie","triangle-down"]


def apply_type_symbols(fig):
    for i, trace in enumerate(fig.data):
        sym = SYMBOLS[i % len(SYMBOLS)]
        try: fig.data[i].marker.symbol = sym
        except: pass
    return fig


def eclk(fig, h: int = 400):
    fig.update_layout(height=h, clickmode="event+select")
    return fig


def lock_axes(fig, date_series, value_series=None, pad_days: int = 1, y_pad_frac: float = 0.15,
              window_days: int = 180):
    """
    Sets initial visible window for the chart instead of locking to full range.
    - Shows the most recent `window_days` of data on load.
    - Allows the navigator and Plotly zoom/pan to work freely.
    - Falls back to full range if data span is shorter than window_days.
    """
    valid_dates = pd.to_datetime(date_series.dropna())
    if valid_dates.empty:
        return fig

    x_min_full = valid_dates.min() - timedelta(days=pad_days)
    x_max_full = valid_dates.max() + timedelta(days=pad_days)
    total_days  = (x_max_full - x_min_full).days

    # If total span fits within window, show everything; otherwise show last window_days
    if total_days <= window_days:
        x_start = x_min_full
        x_end   = x_max_full
    else:
        x_end   = x_max_full
        x_start = x_end - timedelta(days=window_days)

    fig.update_xaxes(
        range=[x_start.isoformat(), x_end.isoformat()],
        autorange=False,
        fixedrange=False   # allows zoom/pan and navigator
    )

    if value_series is not None:
        vals = pd.to_numeric(value_series.dropna(), errors="coerce").dropna()
        if not vals.empty:
            y_max = float(vals.max()) * (1 + y_pad_frac)
            fig.update_yaxes(range=[0, y_max], autorange=False, fixedrange=False)
    else:
        fig.update_yaxes(rangemode="tozero", fixedrange=False)

    return fig

