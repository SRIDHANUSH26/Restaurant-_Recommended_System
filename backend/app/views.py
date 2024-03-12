from django.shortcuts import render
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

class app(APIView):
    def post(self, request):
        # Load the dataset

# Load the dataset
        df = pd.read_csv('E:\\sri sar project\\hotel recommender\\data\\hotel.csv')

        # Handle missing values in the 'address' column
        df['address'].fillna('', inplace=True)

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

            # Create a list of tuples containing hotel name and link
            recommendations = list(zip(df['name'].iloc[hotel_indices], hotel_links))

            return recommendations

        # Example usage
        address = request.data.get('hotel')
        recommendations = get_recommendations(address, cosine_sim)
        dict = {}
        print(f"Recommended hotels for address '{address}':")
        for hotel_name, hotel_link in recommendations:
            dict[hotel_name] = hotel_link
        print(dict)
        return Response(dict)

        