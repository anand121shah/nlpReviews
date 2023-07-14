# nlpReviews

📝 **Google Reviews Analysis - Restaurant Dashboard**

This repository contains code for a Google Reviews Analysis Restaurant Dashboard, built using Machine Learning and Natural Language Processing (NLP) techniques. The dashboard provides insights into restaurant reviews, including sentiment analysis and visualizations. 🍽️📊

📁 **File Structure**
- `data_collection.py`: Collects Google Reviews for restaurants using the Google Maps API and saves the data in a structured format.
- `data_preprocessing.py`: Preprocesses the raw review data by removing irrelevant information, performing text cleaning tasks, and applying tokenization and stemming/lemmatization techniques.
- `sentiment_analysis.py`: Applies sentiment analysis to classify reviews as positive, negative, or neutral and calculates sentiment scores.
- `dashboard.py`: Creates a web-based dashboard using Dash and Plotly, displaying the top 5 reviewed businesses, worst 5 reviewed businesses, and providing a search feature.
- `main.py`: Orchestrates the entire workflow, running data collection, preprocessing, sentiment analysis, and launching the dashboard application.

🔧 **Setup and Dependencies**
- Install the required dependencies by running `pip install -r requirements.txt`.
- Obtain a Google Maps API key and replace `'YOUR_API_KEY'` in `data_collection.py` with your actual key.
- Download NLTK resources by running `nltk.download('stopwords')` and `nltk.download('wordnet')` to support text preprocessing.

🚀 **Running the Application**
1. Execute `main.py` to run the data collection, preprocessing, sentiment analysis, and dashboard creation steps.
2. Access the dashboard by opening the provided URL in your web browser.
3. Interact with the dashboard to explore top and worst reviewed businesses, search for reviews, and gain insights from visualizations.

📂 **Data Files**
- `restaurant_reviews.csv`: Contains raw review data collected from Google Reviews.
- `preprocessed_reviews.csv`: Stores the preprocessed review data after cleaning and normalization.
- `sentiment_analysis_results.csv`: Stores sentiment analysis results, including sentiment labels and scores.

🌟 **Features and Functionalities**
- Top 5 Reviewed Businesses: Visualizes the top 5 restaurants based on average sentiment scores.
- Worst 5 Reviewed Businesses: Visualizes the worst 5 restaurants based on average sentiment scores.
- Search Reviews: Allows searching for reviews based on keywords such as business name or segment.

🌐 **Web Dashboard**
The dashboard provides an interactive web-based interface for exploring and analyzing Google Reviews. It includes visually appealing charts, tables, and search functionality, making it easy to derive insights from the review data.

📝 **Note**
Make sure to replace `'YOUR_PLACE_ID'` in `main.py` with the desired Google Place ID for collecting reviews from a specific restaurant.

👩‍💻 **Contributors**
Contributions to this project are welcome. Please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

📄 **License**
This project is licensed under the [MIT License](LICENSE).

🌟 **Enjoy analyzing Google Reviews with the Restaurant Dashboard!** 🍽️📊
