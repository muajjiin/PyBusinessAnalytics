from dash import html, dcc
from data_processing import load_data
from charts import revenue_by_category, monthly_revenue, top_customers


def create_layout(app):
    _, _, _, _, orders_df = load_data()

    # Dropdown options
    categories = orders_df['Category'].unique()
    dropdown_options = [{'label': cat, 'value': cat} for cat in categories]

    return html.Div([
        html.H1("Retail Dashboard", style={'text-align': 'center'}),
        html.Label("Select Product Category:"),
        dcc.Dropdown(
            id='category-dropdown',
            options=dropdown_options,
            value=None,
            multi=False,
            placeholder="All Categories"
        ),
        dcc.Graph(id='revenue-category-graph', figure=revenue_by_category(orders_df)),
        dcc.Graph(id='monthly-revenue-graph', figure=monthly_revenue(orders_df)),
        dcc.Graph(id='top-customers-graph', figure=top_customers(orders_df))
    ])
