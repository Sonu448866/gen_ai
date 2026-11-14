Chunking:Chunking in RAG (Retrieval-Augmented Generation) is the process of breaking a large document into smaller, meaningful pieces called chunks before converting them into embeddings and storing them in a vector database.

1. Why do we need chunking?
   Suppose you have a 100-page PDF containing information about DSA.

A user asks:

"What is the time complexity of Binary Search?"

If you convert the entire 100-page PDF into a single embedding:

- The embedding represents information from the entire document.
- It becomes difficult to retrieve the exact information about Binary Search.
- Too much unrelated information gets included in the context.
  Instead, we divide the PDF into smaller chunks.

2. What are the different chunking strategies?
   There are several approaches:
   A. Fixed-size chunking
   Divide text based on a fixed number of characters or tokens.

Example:

- Chunk 1: 500 tokens
- Chunk 2: 500 tokens
- Chunk 3: 500 tokens
  Easy to implement, but it might break sentences or concepts in the middle.

If Chunks are too small then it might not have meaning and if chunk is too large then it may have large or too many concepts info and still might loose information.

B. Recursive character chunking
Try to split text using different separators in order:

1. Paragraphs (\n\n)
2. Lines (\n)
3. Sentences
4. Words
5. Characters
   It tries to preserve meaningful boundaries while respecting the chunk size.
   The main problem in naive paragraph/sentence chunking was of variable length as some pragraph can be too small and some can be quite big.So recurssive chunking came that try to split the text using different separators .

C. Semantic chunking
Instead of splitting based on a fixed size, it identifies changes in the meaning of the text.

For example:

- One chunk about Binary Search.
- One chunk about Linear Search.
- One chunk about Merge Sort.
  This helps keep related information together.

D. Document-structure-based chunking
Split according to document structure:

- Headings
- Subheadings
- Paragraphs
- Sections
- Pages
  This is particularly useful for PDFs, documentation and textbooks.

4. What is chunk overlap?
   An important concept!

Suppose you have a document containing 1,000 tokens.

You choose:

- Chunk size = 300 tokens
- Chunk overlap = 50 tokens
  This means the last 50 tokens of one chunk are repeated in the next chunk.

Why overlap?

Imagine a sentence gets split between two chunks. The next chunk might not have enough context to understand the sentence.

Overlap helps preserve context across chunk boundaries.

Verdict: There are different chunking starategies and you may have your own too, it depends on the type of problem that you are trying to solve and based on that you can apply the best chunking strategies that gives better result.
