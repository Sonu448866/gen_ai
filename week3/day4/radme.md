Why we need vector database?

Your program can store small knowlegebase but for storing large data , you need some storage.
For each query the knowlegebase gets converted into embeddings(makes slow) and then similarity happens sequentailly to retrieve relevant context means we can say that there is no persistance of the embeddings when it gets generated once.
Also to generate embedding and then similarity search over it is time consuming process.

So there was mainly three issues: Time constraint,persistence,Memory
However there are also other like concurrency etc.

There are multiple different vector database like:Weaviate,ChromaDB,Qdrant,FAISS,PineCone,PgVector

We will be using Qdrant as it give some free space upto 1GB.

Qdrant is a Vector Database it has collection just like tables which is there in RDBMS.
Collction stores vectors just like in RDBMS tables has rows and columns.
In collection there are points and each point has ID,actual vector and payload.
Qdrant stores data in structures called Points.

For example, a complete Qdrant point could look like this:
{
"id": 101,

    "vector": [
        0.21, 0.45, 0.78, 0.12
    ],

    "payload": {
        "text": "Mumbai main road has heavy traffic",
        "city": "Mumbai",
        "category": "traffic"
    }

}

Qdrant does not necessarily generate the embeddings itself.

You generally use an embedding model such as Sentence Transformers or OpenAI to generate vectors and then store them in Qdrant.

A Collection is a named group of points in Qdrant.

Think of a collection like a table in a traditional database.

For example, suppose you are building a college-document chatbot.

You might create:

Qdrant Database
│
├── college_documents
│ ├── Point 1: Attendance policy
│ ├── Point 2: Examination policy
│ └── Point 3: Admission policy
│
├── placement_documents
│ ├── Point 1: Java interview questions
│ ├── Point 2: Company information
│ └── Point 3: Placement guidelines
│
└── research_papers
├── Point 1: Paper about RAG
├── Point 2: Paper about embeddings
└── Point 3: Paper about LLMs

Collection vs Point vs Vector vs Payload

Term Meaning
Collection Group of related records
Point Individual record
Vector Numerical embedding
Payload Original text and metadata
ID Unique identifier of a point

Term Meaning
Collection Group of related records
Point Individual record
Vector Numerical embedding
Payload Original text and metadata
ID Unique identifier of a point

4. How does Qdrant actually perform vector search?
   This is probably the most important technical concept.

Suppose you have 10 lakh (1 million) vectors in your collection.

A user submits a query, and you want the 5 most similar vectors.

One approach would be:

1. Compare the query vector with the first stored vector.
2. Calculate its similarity.
3. Compare with the second vector.
4. Continue until all 1 million vectors are checked.
5. Sort the results and return the top 5.
   This is called Brute Force Search.

It can be expensive for large datasets.

Qdrant uses a vector indexing technique called HNSW (Hierarchical Navigable Small World) for dense vector search.

Understanding HNSW
HNSW is a graph-based approximate nearest-neighbor search algorithm.

Instead of comparing the query with every single vector, it creates a graph where vectors are connected to other nearby vectors.

Think of it like navigating a city.

Suppose you want to reach a particular destination:

- At the beginning, you take larger roads to reach the general area.
- Then you take smaller roads.
- Finally, you reach the exact destination through nearby streets.
  HNSW follows a similar concept.

It has multiple graph layers:

Upper layers

- Have fewer nodes.
- Have longer-distance connections.
- Help navigate quickly across the vector space.
  Lower layers
- Have more nodes.
- Have more local connections.
- Help locate nearby vectors accurately.
  The search starts from an entry point in an upper layer and gradually moves towards more promising neighboring vectors.

This avoids checking every vector in many cases.

Technical note: HNSW is approximate nearest-neighbor search, so it may not always return the mathematically exact nearest neighbors. You can request exact search when needed, trading speed for computation.

Important HNSW parameters

Parameter Purpose
m Controls the number of graph connections per node
ef_construct Controls the search breadth while constructing the graph
ef Controls the search breadth during querying

Generally:

- Increasing m can improve search quality but requires more memory.
- Increasing ef_construct can improve graph quality but makes indexing slower.
- Increasing ef can improve search recall but makes queries slower.
  Qdrant's dense-vector indexing documentation explains its HNSW implementation and these configuration options.

5. What are Distance Metrics in Qdrant?
   When creating a collection, you must specify how vector similarity or distance should be measured.

Qdrant supports three primary distance metrics for dense vectors.
A. Cosine Similarity: Measures the angle between two vectors.Useful when you want to compare semantic similarity while largely ignoring vector magnitude.

B. Dot Product: Multiplies corresponding vector components and sums the results.Useful when the embedding model is trained for dot-product similarity. It is also closely related to cosine similarity when vectors are normalized.

C. Euclidean Distance: Measures the straight-line distance between two vectors.For Euclidean distance, smaller values indicate closer vectors.

Metric What it measures Better result
Cosine Angular similarity Higher
Dot Vector dot product Higher
Euclidean Straight-line distance Lower
