from data_collection import get_google_reviews, save_reviews_to_csv
from data_preprocessing import remove_irrelevant_info, text_preprocessing
from sentiment_analysis import perform_sentiment_analysis
from dashboard import app

# Data Collection
place_id = 'YOUR_PLACE_ID'  # Replace with the desired place ID
reviews = get_google_reviews(place_id)
save_reviews_to_csv(reviews, 'restaurant_reviews.csv')

# Data Preprocessing
data = pd.read_csv('restaurant_reviews.csv')  # Replace with the path to your raw review data file
data['cleaned_text'] = data['text'].apply(remove_irrelevant_info)
data['cleaned_text'] = data['cleaned_text'].apply(text_preprocessing)
data.to_csv('preprocessed_reviews.csv', index=False)

# Sentiment Analysis
data = pd.read_csv('preprocessed_reviews.csv')  # Replace with the path to your preprocessed review data file
data['sentiment'], data['sentiment_scores'] = zip(*data['cleaned_text'].map(perform_sentiment_analysis))
data.to_csv('sentiment_analysis_results.csv', index=False)

# Launch the Dashboard Application
if __name__ == '__main__':
    app.run_server(debug=True)
