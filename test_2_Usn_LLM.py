import requests
import json

user_input = "I don't like to hike"

prompt = """
You are a bot that makes recommendations for activities. You answer in very short sentences and do not include extra information.
This is the recommended activity: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended activity and the user input.
"""
#This is the prompt sent to the AI model. It provides a context for how the bot should behave (in this case, making short recommendations).

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

full_response = []
#This initializes an empty list to store the bot's response.

url = 'http://localhost:11434/api/generate'
#The API endpoint where the bot will send a request. In this case, it’s a local server (localhost) running on port 11434.

# the payload being sent to the API
data = {
    "model": "llama2",
    # Refers to the AI model being used.

    "prompt": prompt.format(user_input=user_input, relevant_document=corpus_of_documents)
    # This is the actual prompt being sent to the model
}

headers = {'Content-Type': 'application/json'}
# This specifies that the content type of the request being sent is JSON.

response = requests.post(url, data=json.dumps(data), headers=headers, stream=True)
"""requests.post: Sends a POST request to the given url.
data=json.dumps(data): Converts the data dictionary to a JSON string.
headers: The request includes the content-type header to let the server know it's receiving JSON data.
stream=True: Tells the server to stream the response (i.e., receive the response bit by bit instead of all at once)."""

# Processing the Response
try:
  
    for line in response.iter_lines():
      
        if line:
            decoded_line = json.loads(line.decode('utf-8'))
            
            full_response.append(decoded_line['response'])
finally:
    response.close()
"""try...finally block: Ensures that the response is closed even if an error occurs.
response.iter_lines(): Reads the streamed response line by line.
line.decode('utf-8'): Converts each line from bytes to a UTF-8 string.
json.loads(): Parses each line as JSON.
decoded_line['response']: Extracts the response from the parsed JSON and appends it to the full_response list.
response.close(): Closes the connection to the API."""

print(''.join(full_response))