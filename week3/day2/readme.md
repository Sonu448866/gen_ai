Embeddings – Understanding the Intuition

1. Why do we need embeddings?
   Suppose we have two sentences:

Sentence 1:
Mumbai main road par jaam laga hua hai.

Sentence 2:
Mumbai main road pe kitna traffic hai?

Notice that the words used in both sentences are not exactly the same.

However, both sentences are related to the same context: Traffic congestion on Mumbai's main road.

If we already know from Sentence 1 that there is a traffic jam on Mumbai's main road, we can use that information to answer the question in Sentence 2.

A traditional keyword-matching system might struggle because the exact words are different.

But an embedding-based system can understand that both sentences have similar semantic meanings.

This is the fundamental idea behind embeddings.

2. What exactly are embeddings?
   Computers fundamentally process numerical data. Therefore, to make text understandable to machine learning models, we convert text into numerical representations.

These numerical representations are called Embeddings.

An embedding is a vector containing multiple numerical values that represents the semantic information of a piece of text.

For example:
sentence1 = "Mumbai main road par jaam laga hua hai"embedding1 = [0.21, 0.45, 0.78, 0.12, 0.67, ...]
sentence2 = "Mumbai main road pe kitna traffic hai"embedding2 = [0.23, 0.43, 0.80, 0.15, 0.65, ...]

Note: These are illustrative numbers, not actual embedding outputs.

Each number contributes to the representation learned by the embedding model.

Together, these numbers form a vector that captures semantic information about the sentence.
Important clarification

- Embedding values are not necessarily between 0 and 10.
- They can be positive, negative, or zero, depending on the model.
- The vector contains multiple dimensions (features).
- Each dimension does not necessarily represent one understandable property such as traffic, location, or emotion.
  The model learns these numerical representations during training.

3. What is embedding dimension?
   The number of numerical values present in an embedding vector is called its embedding dimension.

For example:
embedding = [0.21, 0.45, 0.78, 0.12]
Here, the embedding dimension is 4.

Different embedding models produce vectors of different dimensions.

Embedding model Typical dimensions
all-MiniLM-L6-v2 384
all-mpnet-base-v2 768
BGE-base-en-v1.5 768
BGE-large-en-v1.5 1024
OpenAI text-embedding-3-small 1536 (default)
OpenAI text-embedding-3-large 3072 (default)

4. How do we determine similarity between embeddings?
   Now comes the interesting part.

Suppose we have generated embeddings for our two sentences.

How do we determine whether their meanings are similar?

We use similarity measurement techniques.

One of the most commonly used techniques is Cosine Similarity.

Cosine similarity measures the cosine of the angle between two vectors.

For our example, if the two sentences have similar embedding directions, their cosine similarity will be relatively high.

Important: A high cosine similarity indicates semantic closeness according to the embedding model, not necessarily that two sentences are interchangeable or that one factually answers the other.

5. How are embeddings generated?
   We use specialized models called Embedding Models.

These models are trained to convert text into meaningful numerical vectors.

Some popular embedding models and providers are:

Provider Examples
Sentence Transformers all-MiniLM-L6-v2, all-mpnet-base-v2
OpenAI text-embedding-3-small, text-embedding-3-large
BAAI BGE models
Cohere Embed models
Google Gemini embedding models
