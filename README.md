# Retrieval-Augmented-Generation--RAG--application
* Ref Part 1 : https://learnbybuilding.ai/tutorials/rag-from-scratch
* Ref Part 2 : https://learnbybuilding.ai/tutorials/rag-from-scratch-part-2-semantics-and-cosine-similarity
* Retrieval Augmented Generation, or RAG, is all the rage these days because it introduces some serious capabilities to large language models like OpenAI's GPT-4 - and that's the ability to use and leverage their own data.
* This Repo will teach you the fundamental intuition behind RAG while providing a simple tutorial to help you get started.
* CLone the repo and in the test_1.py file will teach you about the Jaccard similarity.
* Then after in "test_2_Usn_LLM.py" file We will be using LLM (ollama)

## Ollama setup
* Ref 1: https://dev.to/jayantaadhikary/installing-llms-locally-using-ollama-beginners-guide-4gbi
* Download ollama [here](https://ollama.com/download) and install. {you can browse other ollama models in here https://ollama.com/library}
* * now when you run ollama will run on your local machine in [http://localhost:11434](http://localhost:11434)
* to pull the model run  ``` ollama pull llama2 ``` in your powershell

### checking ollama (llama2)
* to run the model use ``` ollama run llama2 ``` in powershell and chat with it.. You can exit the prompt session using ```/bye```

## Running "test_2_Usn_LLM.py" File
* Must import
  ```
  import requests
  import json
  ```
* use ``` pip install requests ``` to install requests.
* Then Learn and try editing..
