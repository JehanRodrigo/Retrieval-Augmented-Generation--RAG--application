* Ref Part 1 : https://learnbybuilding.ai/tutorials/rag-from-scratch
* Ref Part 2 : https://learnbybuilding.ai/tutorials/rag-from-scratch-part-2-semantics-and-cosine-similarity
* Retrieval Augmented Generation, or RAG, is all the rage these days because it introduces some serious capabilities to large language models like OpenAI's GPT-4 - and that's the ability to use and leverage their own data.
* This Repo will teach you the fundamental intuition behind RAG while providing a simple tutorial to help you get started.
* CLone the repo and in the test_1.py file will teach you about the Jaccard similarity.
* Then after in "test_2_Usn_LLM.py" file We will be using LLM (ollama)

## Ollama setup
* Download ollama [here](https://ollama.com/download) and install.
* Must import
  ```
  import requests
  import json
  ```
* use ``` pip install requests ```
* to pull the model ``` ollama pull lama2 ```
* to run the model ``` ollama run lama2 ```
