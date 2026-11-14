from langchain_text_splitters import (
    CharacterTextSplitter,
    RecursiveCharacterTextSplitter
)
text='''
The detective entered the abandoned house just before midnight. The rooms were silent, and the windows were covered with dust. On the table, he found a bloodstained letter opener lying beside a shattered pocket watch.

The man who did the crime was John. Nobody in the village trusted him, but he had disappeared before the murder. The detective realized that John hadn't fled out of fear, but was likely still hiding somewhere nearby.

The next morning, the detective returned to the house. Behind a loose brick, he discovered a photograph of John standing beside the victim. This finally connected the two men and revealed the hidden motive behind the crime.
'''

# FIXED SIZE CHUNKING

fixed=CharacterTextSplitter(
    separator="",
    chunk_size=100,  # It simply divides the characters into chunks of approximately 100 characters.
    chunk_overlap=0
)

print("\n======================FIXED SIZE========================")

for i,chunk in enumerate(fixed.split_text(text),1):
    print(f"\nChunk{i}:")
    print(chunk)
    print("----------------------------")



# PARAGRAPH CHUNKING

paragraph=CharacterTextSplitter(
    separator="\n\n",
    chunk_size=100,   #If paragraph is more than 100 charcters then it will me made a chunk even if \n\n doesn't come
    chunk_overlap=0

)

print("\n======================PARAGRAPH========================")

for i,chunk in enumerate(paragraph.split_text(text),1):
    print(f"\nChunk{i}:")
    print(chunk)
    print("----------------------------")


# RECURSIVE CHUNKING

recursive=RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20    # We don't pass any separator ,here it has default separator hierarchy
)

print("\n======================RECURSIVE========================")

for i,chunk in enumerate(recursive.split_text(text),1):
    print(f"\nChunk{i}:")
    print(chunk)
    print("----------------------------")


