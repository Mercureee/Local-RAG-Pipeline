"""Phase 2 - Chunking

Splits the text file into text chunks and returns it as a list of text chunks to be converted into vectors.
"""
from load_01 import load_document 
def chunk_document(document, chunk_size = 500, overlap = 50):
    """ Slices the text with overlap allowing it to read all of the document text with full context.

    args


    Returns:
        list[str]: A list containing chunks of the document
    """
    chunks = []
    current_position = 0

    while current_position < len(document):
        
        current_slice = document[current_position : current_position + chunk_size] 
        
        chunks.append(current_slice)
        
        current_position += chunk_size - overlap

    return chunks
if __name__ == "__main__":
    raw_document = load_document()
    text_chunks = chunk_document(raw_document)
    print(text_chunks)