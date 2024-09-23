from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

corpus_of_documents = [
    "Take a leisurely walk in the park and enjoy the fresh air.",
    "Visit a local museum and discover something new.",
    "Attend a live music concert and feel the rhythm.",
    "Go for a hike and admire the natural scenery.",
    "Have a picnic with friends and share some laughs.",
    "Explore a new cuisine by dining at an ethnic restaurant.",
    "Take a yoga class and stretch your body and mind.",
    "Join a local sports league and enjoy some friendly competition.",
    "Attend a workshop or lecture on a topic you're interested in.",
    "Visit an amusement park and ride the roller coasters."
]
model = SentenceTransformer('all-MiniLM-L6-v2')
doc_embeddings = model.encode(corpus_of_documents)

query = "What's the best outside activity?"
query_embedding = model.encode([query])
similarities = cosine_similarity(query_embedding, doc_embeddings)


indexed = list(enumerate(similarities[0]))
sorted_index = sorted(indexed, key=lambda x: x[1], reverse=True)

recommended_documents = []
for value, score in sorted_index:
    formatted_score = "{:.2f}".format(score)
    print(f"{formatted_score} => {corpus_of_documents[value]}")
    
    
    if score > 0.3:
        recommended_documents.append(corpus_of_documents[value])
        