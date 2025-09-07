from dash import Input, Output
from charts import revenue_by_category, monthly_revenue, top_customers
from data_processing import load_data


def register_callbacks(app):
    _, _, _, _, orders_df = load_data()

    @app.callback(
        Output('revenue-category-graph', 'figure'),
        Output('monthly-revenue-graph', 'figure'),
        Output('top-customers-graph', 'figure'),
        Input('category-dropdown', 'value')
    )
    def update_charts(selected_category):
        fig1 = revenue_by_category(orders_df, selected_category)
        fig2 = monthly_revenue(orders_df, selected_category)
        fig3 = top_customers(orders_df, category_filter=selected_category)
        return fig1, fig2, fig3
