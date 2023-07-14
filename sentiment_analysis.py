import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

def perform_sentiment_analysis(review):
    # Apply sentiment analysis using a pre-trained model
    # You can use a pre-trained model like VADER (included in NLTK) or train your own model
    
    sid = SentimentIntensityAnalyzer()
    sentiment_scores = sid.polarity_scores(review)
    
    # Determine the overall sentiment based on the compound score
    compound_score = sentiment_scores['compound']
    
    if compound_score >= 0.05:
        sentiment = 'Positive'
    elif compound_score <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, sentiment_scores

# Example usage
data = pd.read_csv('preprocessed_reviews.csv')  # Replace with the path to your preprocessed review data file

data['sentiment'], data['sentiment_scores'] = zip(*data['cleaned_text'].map(perform_sentiment_analysis))

# Save the results to a new file (optional)
data.to_csv('sentiment_analysis_results.csv', index=False)
