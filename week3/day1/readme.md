RAG: Retrieval-Augmented Generation.

It is a technique in Generative AI where an LLM retrieves relevant information from an external knowledge source before generating an answer.

In simple words:

Instead of relying only on what an LLM learned during training, we provide it with relevant information from external documents or databases when answering a question.

1. Why do we need RAG?
   Suppose you ask ChatGPT:

"What is the attendance policy of my college?"

The LLM might not know your college's latest attendance policy because:

- It was not included in its training data.
- The policy might have changed recently.
- The information might be available only in your college's PDF.
  One solution is to give the LLM access to your college documents.

This is where RAG comes in.

Initially, the probelem is tried to solved using the system prompt but it has limitation as suppose some new
policy comes then the system prompt need to be updated also you can't put enormous amount of data to the system prompt.If you put all data in system prompt then at each call to LLM it goes with it.

Next solution came where all data are fed up in the pdf and that pdf goes to the LLM but it has also limitations that if pdf becomes too long.Not only that there are some many pdfs where data are there so chosing which pdf for what etc becomes a bottleneck.As in real organisation lot of data being genrated and putting all the pdf and giving it to the LLM and then LLM trying to find the relevant data from pdf are very computationally not effective and also not at all feasible.
But for small problem like 5-6 small pdf it is OK.

In early iteration of RAG , a approach was there where a software(specialized) find the relevant information from the knowledge base and based on the relevant information so genrated is then given to LLM so this helped to save some tokens.

But now way to retrieve relevant context and saving the knowledge base has drastically changed means now we use different methods to retrive context from data and there is also new way to store the knowlegebase into proper place known as vector DB.
