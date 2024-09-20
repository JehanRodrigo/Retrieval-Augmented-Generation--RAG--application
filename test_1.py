# Define the corpus of documents
# corpus_of_documents = [
    
#     "I like reading",
#     "I enjoy swimming",
#     "I enjoy hiking",
# ]

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

def jaccard_similarity(query, document): # Jaccard similarity is a measure of how similar two sets (in this case, words in a query and a document) are based on the ratio of common words to the total unique words.
    
    query = query.lower().split(" ")  # Convert the query to lowercase and split into words using " " as the separator

    document = document.lower().split(" ")  # Does the same as above but for the document.

    intersection = set(query).intersection(set(document))  # Find common words between query and document
    # Example: If query = ['i', 'like', 'swimming'] and document = ['i', 'enjoy', 'swimming'], then the intersection is {'i', 'swimming'}.

    union = set(query).union(set(document))  # Find all unique words
    # Example: If query = ['i', 'like', 'swimming'] and document = ['i', 'enjoy', 'swimming'], then the union is {'i', 'like', 'enjoy', 'swimming'}.

    return len(intersection) / len(union)  # Return the Jaccard similarity (intersection/union)

def return_response(query, corpus): # This function determines which document in a collection (corpus) is the most similar to the user's query based on the Jaccard similarity.

    similarities = []  # Empty list to store similarity scores

    for doc in corpus:  # Loop through each document in the corpus

        similarity = jaccard_similarity(query, doc)  # Compute the similarity between query and document

        similarities.append(similarity)  # Store the similarity score
   

    return corpus[similarities.index(max(similarities))] #Finds the document in the corpus that has the highest similarity score and returns it as the response.

user_prompt = "What is a leisure activity that you like?"
user_input = "I like hiking"

# Get the response
response = return_response(user_input, corpus_of_documents) 
print(response)