import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("dataset.csv")

# Convert text data into vectors
vectorizer = CountVectorizer()
vectors = vectorizer.fit_transform(data["Genre"])

# Compute similarity
similarity = cosine_similarity(vectors)

# Recommendation function

def recommend(movie_name):
 movie_name = movie_name.lower()

    # Find movie index
    matches = data[data['Title'].str.lower() == movie_name]
    if matches.empty:
        print("Movie not found in dataset.")
        return

    idx = matches.index[0]
    scores = list(enumerate(similarity[idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    print("\nRecommended Movies:")
    count = 0
    for i in scores[1:]:
        print("-", data.iloc[i[0]].Title)
        count += 1
        if count == 5:
            break

# User input
movie = input("Enter your favourite movie: ")
recommend(movie)
