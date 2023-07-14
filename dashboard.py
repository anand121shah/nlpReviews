import pandas as pd
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Load the preprocessed data
data = pd.read_csv('sentiment_analysis_results.csv')  # Replace with the path to your sentiment analysis results file

# Create the Dash application
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1('Google Reviews Analysis Dashboard'),
    
    html.Div([
        html.H2('Top 5 Reviewed Businesses'),
        dcc.Graph(id='top-businesses')
    ]),
    
    html.Div([
        html.H2('Worst 5 Reviewed Businesses'),
        dcc.Graph(id='worst-businesses')
    ]),
    
    html.Div([
        html.H2('Search Reviews'),
        dcc.Input(id='search-input', type='text', placeholder='Enter a keyword'),
        html.Button('Search', id='search-button', n_clicks=0),
        html.Div(id='search-results')
    ])
])

# Define the callback for displaying top 5 reviewed businesses
@app.callback(
    Output('top-businesses', 'figure'),
    Input('search-button', 'n_clicks')
)
def display_top_businesses(n_clicks):
    # Calculate the average sentiment scores for each business
    avg_sentiment = data.groupby('business_name')['sentiment_scores'].mean().reset_index()
    top_businesses = avg_sentiment.nlargest(5, 'sentiment_scores')
    
    # Create a bar chart to visualize the top businesses
    fig = px.bar(top_businesses, x='business_name', y='sentiment_scores',
                 labels={'business_name': 'Business Name', 'sentiment_scores': 'Sentiment Score'},
                 title='Top 5 Reviewed Businesses')
    
    return fig

# Define the callback for displaying worst 5 reviewed businesses
@app.callback(
    Output('worst-businesses', 'figure'),
    Input('search-button', 'n_clicks')
)
def display_worst_businesses(n_clicks):
    # Calculate the average sentiment scores for each business
    avg_sentiment = data.groupby('business_name')['sentiment_scores'].mean().reset_index()
    worst_businesses = avg_sentiment.nsmallest(5, 'sentiment_scores')
    
    # Create a bar chart to visualize the worst businesses
    fig = px.bar(worst_businesses, x='business_name', y='sentiment_scores',
                 labels={'business_name': 'Business Name', 'sentiment_scores': 'Sentiment Score'},
                 title='Worst 5 Reviewed Businesses')
    
    return fig

# Define the callback for search functionality
@app.callback(
    Output('search-results', 'children'),
    Input('search-button', 'n_clicks'),
    Input('search-input', 'value')
)
def search_reviews(n_clicks, keyword):
    if keyword:
        filtered_data = data[data['cleaned_text'].str.contains(keyword, case=False)]
        search_results = filtered_data[['business_name', 'cleaned_text']].head(10)
        return html.Table([
            html.Thead(html.Tr([html.Th('Business Name'), html.Th('Review Text')])),
            html.Tbody([
                html.Tr([
                    html.Td(row['business_name']),
                    html.Td(row['cleaned_text'])
                ]) for _, row in search_results.iterrows()
            ])
        ])
    else:
        return ''

if __name__ == '__main__':
    app.run_server(debug=True)
