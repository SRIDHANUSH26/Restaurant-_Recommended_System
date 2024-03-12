import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json

# Load the dataset
df = pd.read_csv('E:\\sri sar project\\hotel recommender\\data\\hotel.csv')

# Create a TF-IDF vectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Apply TF-IDF vectorization to the addresses
tfidf_matrix = tfidf.fit_transform(df['address'])

# Compute the cosine similarity matrix
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to get recommendations based on address
def get_recommendations(address, cosine_sim):
    try:
        # Get the index of the address
        index = df[df['address'] == address].index[0]
    except IndexError:
        print(f"No matching address found for '{address}'.")
        return []

    # Get the similarity scores of all addresses with the given address
    similarity_scores = list(enumerate(cosine_sim[index]))

    # Sort the addresses based on similarity scores
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    # Get the top 5 most similar addresses
    top_addresses = similarity_scores[1:9]

    # Get the hotel indices and corresponding links
    hotel_indices = [address[0] for address in top_addresses]
    hotel_links = df['hotel_link'].iloc[hotel_indices]

    # Create a list of dictionaries containing hotel name and link
    recommendations = [{'name': name, 'link': link} for name, link in zip(df['name'].iloc[hotel_indices], hotel_links)]

    return recommendations

# Example usage
address = 'Karunyanagar'
recommendations = get_recommendations(address, cosine_sim)
print(f"Recommended hotels for address '{address}':")

# Convert recommendations to JSON
json_recommendations = json.dumps(recommendations, indent=4)
print(json_recommendations)