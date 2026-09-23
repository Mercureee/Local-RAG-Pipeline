"""Phase 3 - Embedding

Loads the text chunks into a pre-trained neural network to covert the chunks into vector form.

"""
from sentence_transformers import SentenceTransformer
from load_01 import load_document
from chunk_02 import chunk_document

# Builds the model we are using to load text chunks
model = SentenceTransformer("all-MiniLM-L6-v2")

if __name__ == "__main__":
    # Gets the raw text
    raw_document = load_document()
    # Converts the text into chunks
    text_chunks = chunk_document(raw_document)
    # Prints the number of chunks
    print(f"Got {len(text_chunks)} chunks to embed")