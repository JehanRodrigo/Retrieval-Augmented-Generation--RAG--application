import requests
import json

user_input = "I like to hike"

prompt = """
You are a bot that makes recommendations for activities. You answer in very short sentences and do not include extra information.
This is the recommended activity: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended activity and the user input.
"""

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
# relevant_document = return_response(user_input, corpus_of_documents)

full_response = []

url = 'ollama pull llama2/api/generate'
data = {
    "model": "llama2",
    "prompt": prompt.format(user_input=user_input, relevant_document=corpus_of_documents)
}
headers = {'Content-Type': 'application/json'}
response = requests.post(url, data=json.dumps(data), headers=headers, stream=True)
try:
    for line in response.iter_lines():
        if line:
            decoded_line = json.loads(line.decode('utf-8'))
            
            # Check if 'response' key exists
            response_text = decoded_line.get('response')
            if response_text:  # Append only if the key is present
                full_response.append(response_text)
            else:
                print("Warning: 'response' key not found in", decoded_line)
finally:
    response.close()
print(''.join(full_response))