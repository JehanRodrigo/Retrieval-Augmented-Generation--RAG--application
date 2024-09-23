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
* now when you run ollama will run on your local machine in [http://localhost:11434](http://localhost:11434)
* to pull the model run  ``` ollama pull llama2 ``` in your powershell

### checking ollama (llama2)
* to run the model use ``` ollama run llama2 ``` in powershell and chat with it.. You can exit the prompt session using ```/bye```

## Running "test_2_Usn_LLM.py" File
* To import requests use ``` pip install requests ``` to install requests.
* Then you can run "test_2_Usn_LLM.py" File
* Learn and try editing..

# for more
## Here are ten potential areas where we could improve the current setup:
* The number of documents 👉 more documents might mean more recommendations.
* The depth/size of documents 👉 higher quality content and longer documents with more information might be better.
* The number of documents we give to the LLM 👉 Right now, we're only giving the LLM one document. We could feed in several as 'context' and allow the model to provide a more personalized recommendation based on the user input.
* The parts of documents that we give to the LLM 👉 If we have bigger or more thorough documents, we might just want to add in parts of those documents, parts of various documents, or some variation there of. In the lexicon, this is called chunking.
* Our document storage tool 👉 We might store our documents in a different way or different database. In particular, if we have a lot of documents, we might explore storing them in a data lake or a vector store.
* The similarity measure 👉 How we measure similarity is of consequence, we might need to trade off performance and thoroughness (e.g., looking at every individual document).
* The pre-processing of the documents & user input 👉 We might perform some extra preprocessing or augmentation of the user input before we pass it into the similarity measure. For instance, we might use an embedding to convert that input to a vector.
* The similarity measure 👉 We can change the similarity measure to fetch better or more relevant documents.
* The model 👉 We can change the final model that we use. We're using llama2 above, but we could just as easily use an Anthropic or Claude Model.
* The prompt 👉 We could use a different prompt into the LLM/Model and tune it according to the output we want to get the output we want.
* If you're worried about harmful or toxic output 👉 We could implement a "circuit breaker" of sorts that runs the user input to see if there's toxic, harmful, or dangerous discussions. For instance, in a healthcare context you could see if the information contained unsafe languages and respond accordingly - outside of the typical flow.


#part 2
## Running "test_3_SenTransformers.py" File
to import sentence-transformers, run ```pip install sentence-transformers```
