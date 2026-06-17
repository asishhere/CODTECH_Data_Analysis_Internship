# ============================================================
# CODTECH Internship - Task 3: Dashboard Development
# Website Traffic Sources Analysis
# ============================================================

import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# ── Reproducibility ──────────────────────────────────────────
np.random.seed(42)
random.seed(42)

# ── Generate synthetic website traffic dataset ────────────────
n_days = 365 * 2          # 2 years of daily data
start  = datetime(2023, 1, 1)

sources  = ['Organic Search', 'Direct', 'Social Media',
            'Paid Ads', 'Email', 'Referral']
devices  = ['Desktop', 'Mobile', 'Tablet']
pages    = ['Home', 'Product', 'Blog', 'Contact', 'Pricing']

records = []
for i in range(n_days):
    date = start + timedelta(days=i)
    for source in sources:
        # Weekend dip in traffic
        weekend_factor = 0.75 if date.weekday() >= 5 else 1.0

        # Source-specific base traffic
        base = {'Organic Search': 1200, 'Direct': 600,
                'Social Media': 900, 'Paid Ads': 750,
                'Email': 300, 'Referral': 200}[source]

        sessions    = int(base * weekend_factor * np.random.uniform(0.8, 1.2))
        bounce_rate = round(np.random.uniform(0.3, 0.75), 3)
        avg_dur     = round(np.random.uniform(60, 400), 1)   # seconds
        conv_rate   = round(np.random.uniform(0.01, 0.08), 4)
        conversions = int(sessions * conv_rate)
        device      = random.choice(devices)
        page        = random.choice(pages)

        records.append({
            'date'          : date,
            'source'        : source,
            'device'        : device,
            'landing_page'  : page,
            'sessions'      : sessions,
            'bounce_rate'   : bounce_rate,
            'avg_duration'  : avg_dur,
            'conv_rate'     : conv_rate,
            'conversions'   : conversions
        })

df = pd.DataFrame(records)
df['month'] = df['date'].dt.to_period('M').astype(str)
df['week']  = df['date'].dt.isocalendar().week.astype(int)
df['year']  = df['date'].dt.year

print(f"Dataset ready: {df.shape[0]:,} rows")

# ── Initialize Dash app with Bootstrap dark theme ─────────────
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.DARKLY]
)
app.title = "Website Traffic Dashboard"

# Color palette for sources
SOURCE_COLORS = {
    'Organic Search' : '#00C9A7',
    'Direct'         : '#4D96FF',
    'Social Media'   : '#FF6B6B',
    'Paid Ads'       : '#FFD93D',
    'Email'          : '#C77DFF',
    'Referral'       : '#FF9F43'
}

# ── Dashboard Layout ──────────────────────────────────────────
app.layout = dbc.Container([

    # ── Header ─────────────────────────────────────────────
    dbc.Row([
        dbc.Col([
            html.H1("🌐 Website Traffic Dashboard",
                    className="text-center text-white mt-3 mb-1"),
            html.P("Website Traffic Sources Analysis | CODTECH Internship Task 3",
                   className="text-center text-muted mb-3")
        ])
    ]),

    # ── Filters Row ────────────────────────────────────────
    dbc.Row([
        dbc.Col([
            html.Label("Select Traffic Source", className="text-white fw-bold"),
            dcc.Dropdown(
                id='source-filter',
                options=[{'label': 'All Sources', 'value': 'All'}] +
                        [{'label': s, 'value': s} for s in sources],
                value='All',
                clearable=False,
                style={'color': 'black'}
            )
        ], width=4),

        dbc.Col([
            html.Label("Select Device", className="text-white fw-bold"),
            dcc.Dropdown(
                id='device-filter',
                options=[{'label': 'All Devices', 'value': 'All'}] +
                        [{'label': d, 'value': d} for d in devices],
                value='All',
                clearable=False,
                style={'color': 'black'}
            )
        ], width=4),

        dbc.Col([
            html.Label("Select Year", className="text-white fw-bold"),
            dcc.Dropdown(
                id='year-filter',
                options=[{'label': str(y), 'value': y}
                         for y in sorted(df['year'].unique())],
                value=2024,
                clearable=False,
                style={'color': 'black'}
            )
        ], width=4),
    ], className="mb-4"),

    # ── KPI Cards Row ──────────────────────────────────────
    dbc.Row([
        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H6("Total Sessions", className="text-muted"),
                html.H3(id='kpi-sessions', className="text-success fw-bold")
            ])
        ], color="dark", outline=True), width=3),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H6("Total Conversions", className="text-muted"),
                html.H3(id='kpi-conversions', className="text-info fw-bold")
            ])
        ], color="dark", outline=True), width=3),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H6("Avg Bounce Rate", className="text-muted"),
                html.H3(id='kpi-bounce', className="text-warning fw-bold")
            ])
        ], color="dark", outline=True), width=3),

        dbc.Col(dbc.Card([
            dbc.CardBody([
                html.H6("Avg Session Duration", className="text-muted"),
                html.H3(id='kpi-duration', className="text-danger fw-bold")
            ])
        ], color="dark", outline=True), width=3),
    ], className="mb-4"),

    # ── Charts Row 1 ───────────────────────────────────────
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("📈 Monthly Sessions Trend",
                               className="text-white fw-bold"),
                dbc.CardBody([dcc.Graph(id='line-chart')])
            ], color="dark")
        ], width=8),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader("🍩 Traffic Source Share",
                               className="text-white fw-bold"),
                dbc.CardBody([dcc.Graph(id='pie-chart')])
            ], color="dark")
        ], width=4),
    ], className="mb-4"),

    # ── Charts Row 2 ───────────────────────────────────────
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("📊 Sessions by Source & Device",
                               className="text-white fw-bold"),
                dbc.CardBody([dcc.Graph(id='bar-chart')])
            ], color="dark")
        ], width=6),

        dbc.Col([
            dbc.Card([
                dbc.CardHeader("🎯 Conversion Rate by Source",
                               className="text-white fw-bold"),
                dbc.CardBody([dcc.Graph(id='conv-chart')])
            ], color="dark")
        ], width=6),
    ], className="mb-4"),

    # ── Charts Row 3 ───────────────────────────────────────
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader("⏱ Avg Session Duration vs Bounce Rate",
                               className="text-white fw-bold"),
                dbc.CardBody([dcc.Graph(id='scatter-chart')])
            ], color="dark")
        ], width=12),
    ], className="mb-4"),

], fluid=True, style={'backgroundColor': '#1a1a2e', 'minHeight': '100vh'})

# ── Helper: filter dataframe ──────────────────────────────────
def filter_df(source, device, year):
    filtered = df[df['year'] == year].copy()
    if source != 'All':
        filtered = filtered[filtered['source'] == source]
    if device != 'All':
        filtered = filtered[filtered['device'] == device]
    return filtered


# ── Callback: Update KPI Cards ────────────────────────────────
@app.callback(
    Output('kpi-sessions',    'children'),
    Output('kpi-conversions', 'children'),
    Output('kpi-bounce',      'children'),
    Output('kpi-duration',    'children'),
    Input('source-filter', 'value'),
    Input('device-filter', 'value'),
    Input('year-filter',   'value'),
)
def update_kpis(source, device, year):
    filtered = filter_df(source, device, year)
    sessions    = f"{filtered['sessions'].sum():,}"
    conversions = f"{filtered['conversions'].sum():,}"
    bounce      = f"{filtered['bounce_rate'].mean()*100:.1f}%"
    duration    = f"{filtered['avg_duration'].mean():.0f}s"
    return sessions, conversions, bounce, duration


# ── Callback: Line Chart — Monthly Sessions Trend ─────────────
@app.callback(
    Output('line-chart', 'figure'),
    Input('source-filter', 'value'),
    Input('device-filter', 'value'),
    Input('year-filter',   'value'),
)
def update_line(source, device, year):
    filtered = filter_df(source, device, year)
    monthly  = filtered.groupby(['month', 'source'])['sessions'].sum().reset_index()

    fig = px.line(
        monthly, x='month', y='sessions', color='source',
        color_discrete_map=SOURCE_COLORS,
        markers=True,
        title=''
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        xaxis=dict(showgrid=False, tickangle=45),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
        legend_title='Source',
        hovermode='x unified'
    )
    return fig


# ── Callback: Pie Chart — Traffic Share ───────────────────────
@app.callback(
    Output('pie-chart', 'figure'),
    Input('source-filter', 'value'),
    Input('device-filter', 'value'),
    Input('year-filter',   'value'),
)
def update_pie(source, device, year):
    filtered = filter_df(source, device, year)
    source_totals = filtered.groupby('source')['sessions'].sum().reset_index()

    fig = px.pie(
        source_totals, names='source', values='sessions',
        color='source', color_discrete_map=SOURCE_COLORS,
        hole=0.45
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=True
    )
    return fig


# ── Callback: Bar Chart — Sessions by Source & Device ─────────
@app.callback(
    Output('bar-chart', 'figure'),
    Input('source-filter', 'value'),
    Input('device-filter', 'value'),
    Input('year-filter',   'value'),
)
def update_bar(source, device, year):
    filtered = filter_df(source, device, year)
    grouped  = filtered.groupby(['source', 'device'])['sessions'].sum().reset_index()

    fig = px.bar(
        grouped, x='source', y='sessions', color='device',
        barmode='group',
        color_discrete_sequence=['#4D96FF', '#FF6B6B', '#FFD93D']
    )
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        xaxis=dict(showgrid=False, tickangle=20),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
        legend_title='Device'
    )
    return fig


# ── Callback: Conversion Rate by Source ───────────────────────
@app.callback(
    Output('conv-chart', 'figure'),
    Input('source-filter', 'value'),
    Input('device-filter', 'value'),
    Input('year-filter',   'value'),
)
def update_conv(source, device, year):
    filtered = filter_df(source, device, year)
    conv     = filtered.groupby('source')['conv_rate'].mean().reset_index()
    conv['conv_pct'] = (conv['conv_rate'] * 100).round(2)
    conv = conv.sort_values('conv_pct', ascending=True)

    fig = px.bar(
        conv, x='conv_pct', y='source', orientation='h',
        color='source', color_discrete_map=SOURCE_COLORS,
        text='conv_pct'
    )
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        showlegend=False,
        xaxis_title='Conversion Rate (%)',
        yaxis_title='',
        xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)')
    )
    return fig


# ── Callback: Scatter — Duration vs Bounce Rate ───────────────
@app.callback(
    Output('scatter-chart', 'figure'),
    Input('source-filter', 'value'),
    Input('device-filter', 'value'),
    Input('year-filter',   'value'),
)
def update_scatter(source, device, year):
    filtered = filter_df(source, device, year)
    agg = filtered.groupby('source').agg(
        avg_duration=('avg_duration', 'mean'),
        bounce_rate=('bounce_rate', 'mean'),
        sessions=('sessions', 'sum')
    ).reset_index()

    fig = px.scatter(
        agg,
        x='avg_duration', y='bounce_rate',
        size='sessions', color='source',
        color_discrete_map=SOURCE_COLORS,
        text='source',
        size_max=60
    )
    fig.update_traces(textposition='top center')
    fig.update_layout(
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color='white',
        xaxis_title='Avg Session Duration (seconds)',
        yaxis_title='Bounce Rate',
        xaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'),
        showlegend=False
    )
    return fig


# ── Run the app ───────────────────────────────────────────────
if __name__ == '__main__':
    app.run(debug=True)