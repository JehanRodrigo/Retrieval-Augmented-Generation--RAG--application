# Define the corpus of documents
corpus_of_documents = [
    
    "I like reading books on weekends.",
    "I enjoy swimming and playing tennis.",
    "I enjoy hiking in the mountains.",
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