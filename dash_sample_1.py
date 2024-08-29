import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Sample DataFrame
data = {
    "Country": ["United States", "China", "India", "Germany", "United Kingdom"],
    "GDP (in Trillions)": [21.43, 14.34, 2.87, 3.84, 2.83],
}

df = pd.DataFrame(data)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("GDP of Countries"),
    
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in df['Country']],
        value='United States'  # Default value
    ),
    
    dcc.Graph(id='gdp-graph')
])

# Define the callback to update the graph
@app.callback(
    Output('gdp-graph', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    filtered_df = df[df['Country'] == selected_country]
    fig = px.bar(filtered_df, x='Country', y='GDP (in Trillions)', title=f"GDP of {selected_country}")
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
