import plotly.express as px

def revenue_by_category(df, category_filter=None):
    if category_filter:
        df = df[df['Category'] == category_filter]
    fig = px.bar(
        df.groupby("Category")['Revenue'].sum().reset_index(),
        x="Category",
        y="Revenue",
        title="Revenue by Product Category"
    )
    return fig

def monthly_revenue(df, category_filter=None):
    if category_filter:
        df = df[df['Category'] == category_filter]
    fig = px.line(
        df.groupby('Order_Month')['Revenue'].sum().reset_index(),
        x='Order_Month',
        y='Revenue',
        title='Monthly Revenue'
    )
    return fig

def top_customers(df, top_n=10, category_filter=None):
    if category_filter:
        df = df[df['Category'] == category_filter]
    top = df.groupby('Name')['Revenue'].sum().reset_index().sort_values('Revenue', ascending=False).head(top_n)
    fig = px.bar(
        top,
        x='Name',
        y='Revenue',
        title=f'Top {top_n} Customers'
    )
    return fig
