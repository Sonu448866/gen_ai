HNSW: Hierarchial Navigable Small World

It is a graph-based indexing algorithm used by Qdrant to perform fast similarity searches on vector embeddings.

In simple words, suppose you have stored 10 lakh vectors in Qdrant. When a user asks a question, Qdrant needs to find the vectors most similar to the query vector.

Instead of comparing the query vector with all 10 lakh vectors one by one, HNSW helps Qdrant navigate through a graph and find the nearest vectors much faster.

2. How does HNSW work?
   The important concept is that HNSW creates multiple layers of graphs.

Think of it as navigating through Google Maps:

- Higher layers: Give you a broad overview and help you jump quickly towards the target.
- Lower layers: Help you navigate more precisely.
- Bottom layer: Contains all the vectors.

Let's break it down.
Layer 2 – Top layer
Contains very few nodes.

It helps you make large jumps towards the approximate location of the target vector.
Layer 1 – Middle layer
Contains more nodes.

You move closer to the target by exploring nearby connections.
Layer 0 – Bottom layer
Contains all the vectors.

You perform a more detailed search here to identify the nearest neighbors.

The key idea: HNSW starts at the top layer and gradually moves towards the bottom layer, improving the search location at each level.

There are three important parameters you should understand.

Parameter Meaning Effect of increasing
m Maximum graph connections per node More connections, higher memory usage
ef_construct Candidates explored while building the graph Better graph quality, slower indexing
hnsw_ef Candidates explored during searching Better recall, slower search

Filters:
Filters in Qdrant allow you to retrieve vectors based on specific conditions on their metadata (payload), rather than relying only on vector similarity.
It makes index of that filter.

In simple words, filters help you tell Qdrant:

"Search only within these particular documents, topics, categories, or conditions."

1. First, understand Payload
   When you store a vector in Qdrant, you can also store additional information with it. This additional information is called Payload.
   For example:
   {
   "id": 1,
   "vector": [0.12, 0.45, 0.67],
   "payload": {
   "topic": "Binary Search",
   "language": "C++",
   "video_name": "Binary Search Explained",
   "timestamp": 325,
   "difficulty": "Easy"
   }
   }

Here:

- vector contains the embedding.
- payload contains metadata associated with that embedding.
  Payload is useful because you can filter your search using these metadata fields.

2. Why do we need filters?
   Suppose your Qdrant database contains 50,000 transcript chunks.

A user asks:

"Explain binary search in C++."

Without filters:

- Qdrant searches for semantically similar vectors.
- It might retrieve binary search explanations in Java, Python, and C++.
  With filters:
- You can restrict the search to language = C++.
- Qdrant searches only within the matching records.

3. Types of filters in Qdrant
   Qdrant provides several filtering conditions.

A. Match filter
Checks whether a payload field matches a particular value.

Example: Retrieve only C++ videos.

from qdrant_client.models import Filter, FieldCondition, MatchValue

query_filter = Filter(
must=[
FieldCondition(
key="language",
match=MatchValue(value="C++")
)
]
)

B. Range filter
Used when you want to filter numerical values.

Example: Retrieve transcript chunks between 5 and 10 minutes.

from qdrant_client.models import Range

query_filter = Filter(
must=[
FieldCondition(
key="timestamp",
range=Range(
gte=300,
lte=600
)
)
]
)

Here:

- gte = Greater than or equal to.
- lte = Less than or equal to.
- gt = Greater than.
- lt = Less than.

C. Match Any
Used when a field can match any one of multiple values.

Example: Retrieve C++ or Java videos.

from qdrant_client.models import MatchAny

query_filter = Filter(
must=[
FieldCondition(
key="language",
match=MatchAny(any=["C++", "Java"])
)
]
)

D. Must, Should and Must Not
These are three important logical conditions in Qdrant.

Condition Meaning Logical equivalent
must All conditions must match AND
should At least one should match OR
must_not Conditions must not match NOT

Example:
query_filter = Filter(
must=[
FieldCondition(
key="language",
match=MatchValue(value="C++")
)
],
must_not=[
FieldCondition(
key="difficulty",
match=MatchValue(value="Hard")
)
]
)
