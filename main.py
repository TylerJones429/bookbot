def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    print(f"{num_words} words found in the document")
    print(letter_count(text))

def word_count(text):
    words = (text.split(None))
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def letter_count(text):
    letters = {}
    lowercase_text = text.lower()
    words = (lowercase_text.split(None))
    for word in words:
        for letter in word:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
    return letters
    


main()