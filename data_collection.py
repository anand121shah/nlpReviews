import requests
import csv

API_KEY = 'YOUR_API_KEY'  # Replace with your Google Maps API key

def get_google_reviews(place_id):
    url = f'https://maps.googleapis.com/maps/api/place/details/json?place_id={place_id}&fields=reviews&key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return data['result']['reviews']

def save_reviews_to_csv(reviews, file_name):
    fieldnames = ['author_name', 'rating', 'text']
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for review in reviews:
            writer.writerow({
                'author_name': review['author_name'],
                'rating': review['rating'],
                'text': review['text']
            })

# Example usage
place_id = 'YOUR_PLACE_ID'  # Replace with the desired place ID
reviews = get_google_reviews(place_id)
save_reviews_to_csv(reviews, 'restaurant_reviews.csv')
