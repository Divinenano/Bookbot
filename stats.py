def get_num_words(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        words = str.split(file_contents)
        word_count = len(words)
    return (f"{word_count} words found in the document")

def stats():
    path = "books/frankenstein.txt"
    text = get_num_words(path)
    print(text)

stats()
