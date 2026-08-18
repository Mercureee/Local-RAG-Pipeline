"""
Phase 1 - Document loading.

Read a raw UTF-8 text file and returns its contents as one string for chunking.
"""
def load_document():
    """ Read the text file and return its contents.

    Returns:
        str: The document contents
    """
    with open("sample.txt", "r", encoding = "utf-8") as f:
        document = f.read()
    return document
if __name__ == "__main__":
    text_data = load_document()
    print(text_data)