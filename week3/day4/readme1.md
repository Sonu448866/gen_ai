So the flow looks like this :
Suppose you have a txt file as a knowlege base then each line of it embedded and given a id .
Qdrant stores id of each line,together with its vector and original line.

When a query comes it is converted into vector and then top-k embedding are searched based on different algorithms like cosine similarity,Dot product etc using some searching methods like HNSW.
The matched vector with the payload is sent back and then the context is given to LLM.
Qdrant stores payload so that we don't have to convert back embedding again to actual text .
