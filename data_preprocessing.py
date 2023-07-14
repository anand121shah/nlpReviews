import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

def remove_irrelevant_info(review):
    # Remove timestamps, usernames, or any other irrelevant information from the review text
    # Modify this function based on your specific requirements
    # For example, you can use regular expressions to remove patterns or substrings
    return review

def text_preprocessing(review):
    # Convert the text to lowercase
    review = review.lower()
    
    # Remove punctuation
    review = review.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenization
    tokens = word_tokenize(review)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    
    # Stemming
    stemmer = PorterStemmer()
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in stemmed_tokens]
    
    # Join the tokens back into a single string
    preprocessed_text = ' '.join(lemmatized_tokens)
    
    return preprocessed_text

# Example usage
data = pd.read_csv('restaurant_reviews.csv')  # Replace with the path to your raw review data file
data['cleaned_text'] = data['text'].apply(remove_irrelevant_info)
data['cleaned_text'] = data['cleaned_text'].apply(text_preprocessing)

# Save the preprocessed data to a new file (optional)
data.to_csv('preprocessed_reviews.csv', index=False)
